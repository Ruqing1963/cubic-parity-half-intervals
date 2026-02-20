#!/usr/bin/env python3
"""
cubic_parity_verifier.py
========================
Verify the Cubic Parity Constraint Theorem: in the right half
of the Legendre interval, every cubic phase count is even.
Also verify the quartic complementary pairing for p ≡ 5 (mod 8).

Titan Project -- Paper XIII, February 2026
Author: Ruqing Chen, GUT Geoservice Inc.
"""

import sympy
import argparse


def verify_cubic_parity(limit_n):
    total = 0
    even_holds = 0
    zero_skew = 0

    print("=" * 60)
    print(f"Cubic Parity Constraint (n=2 to {limit_n})")
    print("=" * 60)

    for n in range(2, limit_n + 1):
        p = 2 * n - 1
        if not sympy.isprime(p) or p % 3 != 1:
            continue

        mid = n * (n - 1)
        counts = {}
        for x in range(mid + 1, n ** 2):
            res = x % p
            if res == 0:
                continue
            c = pow(res, (p - 1) // 3, p)
            counts[c] = counts.get(c, 0) + 1

        vals = sorted(counts.values())
        if len(vals) < 3:
            continue

        total += 1
        ae = all(v % 2 == 0 for v in vals)
        eq = (vals[0] == vals[1] == vals[2])
        if ae:
            even_holds += 1
        if eq:
            zero_skew += 1

    print(f"Qualifying primes: {total}")
    print(f"All phases even:   {even_holds}/{total} "
          f"({100 * even_holds / total:.2f}%)")
    print(f"Zero skew:         {zero_skew}/{total} "
          f"({100 * zero_skew / total:.1f}%)")
    print("=" * 60)


def verify_quartic_pairing(limit_n):
    total = 0
    holds = 0

    print(f"\nQuartic Pairing for p ≡ 5 (mod 8), n ≤ {limit_n}")
    print("=" * 60)

    for n in range(2, limit_n + 1):
        p = 2 * n - 1
        if not sympy.isprime(p):
            continue
        if (p - 1) % 4 != 0 or p % 8 != 5:
            continue
        if (p - 1) // 4 < 2:
            continue

        total += 1
        mid = n * (n - 1)
        counts = {}
        for x in range(mid + 1, n ** 2):
            res = x % p
            if res == 0:
                continue
            c = pow(res, (p - 1) // 4, p)
            counts[c] = counts.get(c, 0) + 1

        phi0 = counts.get(1, 0)
        phi2 = counts.get(p - 1, 0)
        others = sorted(v for k, v in counts.items()
                        if k not in [1, p - 1])

        paired = (phi0 == phi2
                  and len(others) == 2
                  and others[0] == others[1])
        if paired:
            holds += 1

    print(f"Qualifying primes: {total}")
    print(f"Pairing holds:     {holds}/{total} "
          f"({100 * holds / total:.1f}%)")
    print("=" * 60)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Verify cubic parity and quartic pairing."
    )
    parser.add_argument("--limit", type=int, default=1000)
    args = parser.parse_args()
    verify_cubic_parity(args.limit)
    verify_quartic_pairing(args.limit)
