#!/usr/bin/env python3
"""
Audit Validator for Gemini Output
Validates Gemini's work against standards and source of truth.
"""

import argparse
import sys
import os
import re
from pathlib import Path
from datetime import datetime


def check_frontmatter(filepath):
    """Check if file has complete frontmatter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for frontmatter
        if not content.startswith('---'):
            return False, "Missing frontmatter"

        # Extract frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False, "Incomplete frontmatter"

        frontmatter = parts[1]

        # Check required fields
        required = ['criado', 'atualizado']
        for field in required:
            if f'{field}:' not in frontmatter:
                return False, f"Missing field: {field}"

        return True, "Complete frontmatter"

    except Exception as e:
        return False, f"Error reading file: {e}"


def check_nomenclature(filepath):
    """Check if filename follows nomenclature standards."""
    filename = os.path.basename(filepath)

    # Known prefixes
    valid_prefixes = [
        'RESUMO_', 'PROJETO_', 'BRIEFING_', 'PLANILHA_', 'STATUS_',
        'CHECKLIST_', 'TEMPLATE_', 'PROTOCOLO_', 'PLANO_', 'TODO_',
        'DASHBOARD_', 'MOC_', '_MOC_', 'VALORES_', 'CHECKPOINT_'
    ]

    # Check if starts with valid prefix or is README/STATUS
    if filename in ['README.md', 'STATUS_ATUAL.md']:
        return True, "Standard filename"

    for prefix in valid_prefixes:
        if filename.startswith(prefix):
            # Check for proper format (no spaces)
            if ' ' in filename:
                return False, "Filename contains spaces"
            return True, f"Valid prefix: {prefix}"

    # Could be a content file (Category_Sub_Topic.md)
    if filename.replace('.md', '').replace('_', '').isalnum():
        return True, "Content file (no prefix needed)"

    return False, "Unknown nomenclature pattern"


def extract_values(content, patterns):
    """Extract critical values from content based on patterns."""
    found_values = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            found_values[name] = matches
    return found_values


def validate_against_source_of_truth(filepath, source_of_truth_path, critical_patterns):
    """Validate critical values against source of truth."""
    issues = []

    if not os.path.exists(source_of_truth_path):
        return issues, "Source of truth not found - skipping validation"

    try:
        # Read both files
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(source_of_truth_path, 'r', encoding='utf-8') as f:
            source_content = f.read()

        # Extract values
        file_values = extract_values(content, critical_patterns)
        source_values = extract_values(source_content, critical_patterns)

        # Compare
        for key in file_values:
            if key in source_values:
                if file_values[key] != source_values[key]:
                    issues.append(f"{key}: {file_values[key]} != {source_values[key]} (source)")

        return issues, f"Checked {len(file_values)} value types"

    except Exception as e:
        return issues, f"Error validating: {e}"


def audit_file(filepath, source_of_truth=None):
    """Audit a single file."""
    result = {
        'file': filepath,
        'exists': os.path.exists(filepath),
        'frontmatter': None,
        'nomenclature': None,
        'values': None,
        'issues': []
    }

    if not result['exists']:
        result['issues'].append("File does not exist")
        return result

    # Check frontmatter
    fm_ok, fm_msg = check_frontmatter(filepath)
    result['frontmatter'] = {'ok': fm_ok, 'msg': fm_msg}
    if not fm_ok:
        result['issues'].append(f"Frontmatter: {fm_msg}")

    # Check nomenclature
    nom_ok, nom_msg = check_nomenclature(filepath)
    result['nomenclature'] = {'ok': nom_ok, 'msg': nom_msg}
    if not nom_ok:
        result['issues'].append(f"Nomenclature: {nom_msg}")

    # Validate values if source of truth provided
    if source_of_truth:
        # Define critical patterns (financial values, ROI, etc.)
        patterns = {
            'investment': r'R\$ ([\d.,]+)',
            'roi': r'ROI[:\s]+([\d]+)%',
            'margin': r'[Mm]argem[:\s]+([\d.,]+)%'
        }
        value_issues, value_msg = validate_against_source_of_truth(
            filepath, source_of_truth, patterns
        )
        result['values'] = {'issues': value_issues, 'msg': value_msg}
        if value_issues:
            result['issues'].extend([f"Value: {issue}" for issue in value_issues])

    return result


def generate_report(results, output_file="AUDIT_REPORT.md"):
    """Generate audit report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    total_files = len(results)
    total_issues = sum(len(r['issues']) for r in results)
    files_with_issues = sum(1 for r in results if r['issues'])

    approval_pct = ((total_files - files_with_issues) / total_files * 100) if total_files > 0 else 0

    report = f"""# AUDIT REPORT - Gemini Work Validation

**Date:** {timestamp}
**Auditor:** Claude Code (audit_validator.py)

---

## ✅ APPROVAL: {approval_pct:.0f}%

---

## 📊 METRICS

- **Files audited:** {total_files}
- **Files with issues:** {files_with_issues}
- **Files correct:** {total_files - files_with_issues}
- **Total issues found:** {total_issues}

---

## 📋 DETAILED RESULTS

"""

    # Files with issues
    if files_with_issues > 0:
        report += "### ⚠️ Files with Issues\n\n"
        for r in results:
            if r['issues']:
                report += f"**{r['file']}** ({len(r['issues'])} issues):\n"
                for issue in r['issues']:
                    report += f"  - {issue}\n"
                report += "\n"
    else:
        report += "### ✅ All Files Passed\n\nNo issues found!\n\n"

    # Files correct
    correct_files = [r for r in results if not r['issues']]
    if correct_files:
        report += "### ✅ Files Correct\n\n"
        for r in correct_files:
            report += f"- {r['file']}\n"
        report += "\n"

    report += "---\n\n"

    # Recommendations
    if approval_pct >= 90:
        report += "## 🎯 RECOMMENDATION: **APPROVE**\n\n"
        report += "Quality is excellent (≥90%). Minor issues can be fixed quickly.\n"
    elif approval_pct >= 70:
        report += "## ⚠️  RECOMMENDATION: **APPROVE WITH CORRECTIONS**\n\n"
        report += "Quality is acceptable (70-90%). Fix issues listed above.\n"
    else:
        report += "## ❌ RECOMMENDATION: **NEEDS REWORK**\n\n"
        report += "Quality is below threshold (<70%). Significant issues found.\n"

    report += f"\n---\n\n**Generated:** {timestamp}\n"

    # Write report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    return report, approval_pct


def main():
    parser = argparse.ArgumentParser(
        description="Audit Gemini's output against standards"
    )
    parser.add_argument(
        "--files",
        required=True,
        help="Comma-separated list of files to audit"
    )
    parser.add_argument(
        "--source-of-truth",
        default=None,
        help="Path to source of truth document (e.g., VALORES_OFICIAIS.md)"
    )
    parser.add_argument(
        "--output",
        default="AUDIT_REPORT.md",
        help="Output report file (default: AUDIT_REPORT.md)"
    )

    args = parser.parse_args()

    files = [f.strip() for f in args.files.split(',')]

    print(f"\n{'='*60}")
    print(f"AUDITING {len(files)} FILES")
    print(f"{'='*60}\n")

    results = []
    for filepath in files:
        print(f"Auditing: {filepath}...", end=" ")
        result = audit_file(filepath, args.source_of_truth)
        results.append(result)

        if result['issues']:
            print(f"⚠️  {len(result['issues'])} issues")
        else:
            print("✅ OK")

    print(f"\n{'='*60}")
    report, approval = generate_report(results, args.output)
    print(f"AUDIT COMPLETE: {approval:.0f}% approval")
    print(f"{'='*60}\n")
    print(f"Report saved to: {args.output}\n")

    # Return exit code based on approval
    return 0 if approval >= 70 else 1


if __name__ == "__main__":
    sys.exit(main())
