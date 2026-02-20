# The Parity of Cubic Phases in Legendre Half-Intervals

**Titan Project — Paper XIII**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

For primes p = 2n−1 with p ≡ 1 (mod 6), the negation involution x ↦ p−x preserves the cubic residue character (since χ₃(−1) = 1). This yields:

- **Right half**: every cubic phase count is even (perfect orbit pairing).
- **Left half**: exactly one phase count is odd — the phase of the midpoint m = n(n−1) ≡ p−r (mod p), whose involution partner is the puncture r = 4⁻¹.

This answers **Open Question 1** from [Paper XII](https://zenodo.org/records/18714643): cubic zero-skew is **not** an algebraic necessity.

Also proved: for k = 4, p ≡ 5 (mod 8), the involution forces complementary pairing Φ₀ = Φ₂ and Φ₁ = Φ₃ (78/78 verified).

## Repository Structure

```
├── paper/
│   ├── Cubic_Parity.tex
│   └── Cubic_Parity.pdf
├── scripts/
│   └── cubic_parity_verifier.py
├── LICENSE
└── README.md
```

## Quick Start

```bash
pip install sympy
python scripts/cubic_parity_verifier.py --limit 1000
```

## Companion Papers

| # | Title | Link |
|---|-------|------|
| IX | Quadratic Residue Asymmetry | [Zenodo:18706876](https://zenodo.org/records/18706876) |
| X | Oppermann's Parity Law | [Zenodo:18707265](https://zenodo.org/records/18707265) |
| XII | Higher-Order Residue Deficits | [Zenodo:18714643](https://zenodo.org/records/18714643) |
| **XIII** | **Cubic Parity (this repo)** | Zenodo (forthcoming) |

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
