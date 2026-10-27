# Verification Evidence & Traceability

> Detailed execution evidence, command outputs, and reproducibility artifacts for `pqblocks-anneal-sqa`.

---

## 1. Clean-Room Test Execution Evidence

Full test execution output in a clean virtual environment running Python 3.14.8:

```text
============================= test session starts ==============================
platform linux -- Python 3.14.8, pytest-9.1.1, pluggy-1.6.0
rootdir: /tmp/pqblocks-gate-sqa/tests
configfile: pyproject.toml
testpaths: tests
plugins: hypothesis-6.168.0, cov-7.1.0, anyio-4.15.1
collected 18 items

tests/test_sqa_benchmark_wrapper.py ...                                  [ 16%]
tests/test_sqa_integration.py ....                                       [ 38%]
tests/test_sqa_reference.py ..                                           [ 50%]
tests/test_sqa_sampler.py .........                                      [100%]

======================== 18 passed, 1 warning in 18.11s ========================
```

---

## 2. Example Execution Evidence

### Quickstart Execution:

```bash
$ python3 examples/quickstart.py
Best Spin State: [1, -1, -1, -1]
Best Energy: -6.000000
```

### Multi-Replica Trotter Evaluation:

```bash
$ python3 examples/02_trotter_monte_carlo_annealing.py
--- SQA Multi-Replica Transverse-Field Annealing ---
Trotter replicas (P= 4): Best Energy = -6.000000, Config = [-1, 1, -1, 1]
Trotter replicas (P= 8): Best Energy = -6.000000, Config = [-1, 1, -1, 1]
Trotter replicas (P=16): Best Energy = -6.000000, Config = [-1, 1, -1, 1]

Trotter replica evaluation completed successfully.
```
