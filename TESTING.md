# Testing & Test Suite Documentation

> Test suite coverage, execution procedures, and verification breakdown for `pqblocks-anneal-sqa`.

---

## 1. Test Suite Summary

The test suite contains **18 comprehensive tests** covering the Suzuki-Trotter Hamiltonian, Path-Integral Monte Carlo updates, statistical equivalence against reference calculations, and benchmark wrapper integration.

- **Status**: 18 passed, 0 failed, 1 warning (numba compiler informational warning)
- **Runtime**: ~18.0 seconds (includes stochastic integration distributions over 200 runs)
- **Statement Coverage**: 59% across 115 statements
- **Python Matrix**: Fully verified on Python 3.11, 3.12, 3.13, and 3.14

---

## 2. Test File Breakdown

| Test File | Tests | Focus Area |
|---|---|---|
| `test_sqa_benchmark_wrapper.py` | 3 | Benchmark wrapper contract, parameter serialization, and dimod BQM integration |
| `test_sqa_integration.py` | 4 | Stochastic two-tier equivalence, Kolmogorov-Smirnov test, z-test, and golden instance verification |
| `test_sqa_reference.py` | 2 | 4-spin worked example flip evaluation and inner loop energy verification |
| `test_sqa_sampler.py` | 9 | Input boundary conditions (empty input, dimension mismatches, symmetric requirements, negative sweeps) |

---

## 3. Running the Tests

To run the complete test suite:

```bash
pytest -v
```

To run with coverage reporting:

```bash
pytest --cov=pqblocks_anneal_sqa --cov-report=term
```
