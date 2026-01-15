#!/usr/bin/env python3
"""
Token Estimator for Gemini Handoff
Estimates token cost before delegating tasks to Gemini.
"""

import sys
import os
from pathlib import Path


def estimate_tokens_from_file(filepath):
    """
    Estimate tokens for a single file.
    Rule of thumb: ~0.75 tokens per word, ~4 characters per token.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Rough estimate: 4 chars ≈ 1 token
            estimated_tokens = len(content) // 4
            return estimated_tokens
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
        return 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python token_estimator.py file1.md file2.md ...")
        print("   or: python token_estimator.py --glob '*.md'")
        sys.exit(1)

    files = sys.argv[1:]

    # Handle glob patterns if needed
    if files[0] == '--glob' and len(files) > 1:
        import glob
        pattern = files[1]
        files = glob.glob(pattern, recursive=True)

    total_tokens = 0
    file_details = []

    for filepath in files:
        if not os.path.exists(filepath):
            print(f"Warning: File not found: {filepath}", file=sys.stderr)
            continue

        tokens = estimate_tokens_from_file(filepath)
        total_tokens += tokens
        file_details.append((filepath, tokens))

    # Output results
    print(f"\n{'='*60}")
    print(f"TOKEN ESTIMATION REPORT")
    print(f"{'='*60}\n")

    print(f"Files analyzed: {len(file_details)}")
    print(f"\nPer-file breakdown:")
    for filepath, tokens in sorted(file_details, key=lambda x: x[1], reverse=True):
        print(f"  {tokens:>8,} tokens - {filepath}")

    print(f"\n{'='*60}")
    print(f"TOTAL ESTIMATED TOKENS: {total_tokens:,}")
    print(f"{'='*60}\n")

    # Recommendation
    if total_tokens > 50000:
        print("✅ RECOMMENDATION: DELEGATE to Gemini (>50k tokens)")
        print(f"   Estimated savings: ~{total_tokens:,} tokens")
    elif total_tokens > 20000:
        print("⚠️  RECOMMENDATION: CONSIDER delegating (>20k tokens)")
        print(f"   Borderline case - evaluate task complexity")
    else:
        print("❌ RECOMMENDATION: Claude can handle this (<20k tokens)")
        print(f"   Delegation overhead not worth it")

    print()
    return 0 if total_tokens > 50000 else 1


if __name__ == "__main__":
    sys.exit(main())
