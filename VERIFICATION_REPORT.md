# Verification Report: pqblocks-anneal-sqa

> Formal release verification report for `pqblocks-anneal-sqa`.

---

## 1. Executive Summary

| Attribute | Value |
|---|---|
| **Product** | `pqblocks-anneal-sqa` |
| **Package Name** | `pqblocks_anneal_sqa` |
| **Version** | `0.1.0` |
| **Classification** | Quantum-inspired classical optimisation: not cryptography, no security claim |
| **Verification Status** | **PASSED** |
| **Test Matrix** | Python 3.11, 3.12, 3.13, 3.14 |
| **Test Results** | 18 passed, 0 failed across all supported versions |
| **Leak Gate** | 0 hits (19 files scanned) |

---

## 2. Verification Gate Results

| Check ID | Verification Item | Target | Result | Status |
|---|---|---|---|---|
| **CHK-01** | Test Suite Completeness | 18 passing tests | 18 passed, 0 failed | **PASS** |
| **CHK-02** | Python Compatibility | Python 3.11–3.14 | Clean execution on all 4 versions | **PASS** |
| **CHK-03** | Source & Wheel Build | PEP 517 / PEP 621 | Valid sdist and wheel generated | **PASS** |
| **CHK-04** | Package Integrity | `twine check --strict` | Passed without warnings | **PASS** |
| **CHK-05** | Public Leak Gate | 0 internal leaks | 0 hits across all files | **PASS** |
| **CHK-06** | Example Verification | $\ge 2$ functioning examples | `quickstart.py` & `02_trotter_monte_carlo_annealing.py` passed | **PASS** |
| **CHK-07** | Statistical Equivalence | Two-tier KS / z-test | Passed with $p > 0.05$ | **PASS** |

---

## 3. Mathematical & Algorithmic Verification

- **Suzuki-Trotter Hamiltonian**: Validated against analytical reference calculations:
  $$H_{\text{eff}} = \frac{1}{P} \sum_{k=1}^P \left( \sum_{i} h_i s_{i,k} + \sum_{i < j} J_{ij} s_{i,k} s_{j,k} \right) - J_{\perp} \sum_{k=1}^P \sum_i s_{i,k} s_{i, k+1}$$
  Where $J_{\perp} = -\frac{1}{2\beta} \ln \tanh(\beta \Gamma / P)$.
- **Statistical Equivalence**: Verified via two-sample Kolmogorov-Smirnov test and two-proportion z-tests comparing reference and optimized sampling distributions.

---

## 4. Conclusion

The package `pqblocks-anneal-sqa` has satisfied all release verification requirements and is verified for release.
