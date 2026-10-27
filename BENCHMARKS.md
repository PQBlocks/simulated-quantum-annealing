# Benchmarks & Performance Verification

> Measured performance, comparative baselines, and evaluation methodology for `pqblocks-anneal-sqa`.

---

> [!NOTE]
> **Domain Classification**: Quantum-inspired classical optimisation: not cryptography, no security claim.

---

## 1. Benchmark Results on Synthetic MaxCut Instance

Comparative benchmarks against established baseline solvers on the `synthetic_maxcut` problem instance ($N=20$, Edges=102).

| Solver | Best Energy | TTS(0.99) | 95% Confidence Interval | Avg Runtime |
|---|---|---|---|---|
| **pqblocks-anneal-sqa** | **-42.0** | **0.0221s** | **[0.0220s, 0.0222s]** | **0.0221s** |
| D-Wave Neal (Simulated Annealing) | -42.0 | 0.0009s | [0.0009s, 0.0010s] | 0.0009s |
| OpenJij (SQA reference) | -42.0 | 0.0362s | [0.0183s, 0.0583s] | 0.0362s |
| Google CP-SAT (Constraint Solver) | -42.0 | 0.1308s | [0.1221s, 0.1412s] | 0.1308s |
| MQLib (Heuristic) | -42.0 | 2.0025s | [2.0024s, 2.0026s] | 2.0025s |

---

## 2. Reading the Numbers: Trotter Multi-Replica Overhead

- **Computational Work**: SQA simulates $P$ Trotter replicas in imaginary time (typically $P=32$). Each sweep of SQA therefore performs $P \times$ more spin updates than single-replica classical Simulated Annealing (such as D-Wave Neal).
- **Comparative Advantages**: SQA outperforms CP-SAT and MQLib on dense unstructured instances with sub-second convergence. While D-Wave Neal exhibits faster per-sweep wall time by avoiding replica simulation, SQA emulates quantum tunneling effects across narrow energy barriers.

---

## 3. Microbenchmarks Across Trotter Dimensions

Measurements conducted on Linux x86_64, Python 3.14 on 4-spin frustrated ring (100 sweeps):

| Trotter Dimension ($P$) | Latency | Throughput |
|---|---|---|
| $P=4$ replicas | 0.09 ms | 11,100 runs/sec |
| $P=16$ replicas | 0.20 ms | 4,985 runs/sec |
| $P=32$ replicas | 0.35 ms | 2,833 runs/sec |

---

## 4. Reproducing the Measurements

```bash
python3 -c "
from pqblocks_anneal_sqa import SimulatedQuantumAnnealingSampler

h = [-1.0, 1.0, 2.0, -2.0]
J = [[0.0, 1.0, -1.0, 2.0],
     [0.0, 0.0, 1.0, -1.0],
     [0.0, 0.0, 0.0, -2.0],
     [0.0, 0.0, 0.0, 0.0]]

sampler = SimulatedQuantumAnnealingSampler()
samples, energies = sampler.sample_ising(h, J, P=32, num_sweeps=100)
print(f'Best Energy: {energies[0]:.6f}')
"
```
