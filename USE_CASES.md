# Use Cases & Integration Patterns

> Practical applications and integration scenarios for `pqblocks-anneal-sqa`.

---

## 1. Escaping Deep Local Minima via Simulated Quantum Tunneling

In classical Simulated Annealing, the probability of traversing a barrier of height $\Delta E$ is proportional to $\exp(-\beta \Delta E)$. On energy landscapes characterized by tall, thin potential barriers (such as heavily frustrated spin glasses or planted solution instances), thermal fluctuations frequently become trapped in suboptimal local minima.

Simulated Quantum Annealing introduces a transverse magnetic field $\Gamma(t)$ that drives quantum tunneling between states:

```python
from pqblocks_anneal_sqa import SimulatedQuantumAnnealingSampler

# Solve frustrated spin glass with SQA
sampler = SimulatedQuantumAnnealingSampler()
samples, energies = sampler.sample_ising(h, J, P=32, num_sweeps=1000)
print(f"Optimal energy found: {energies[0]:.4f}")
```

---

## 2. Parameterizing Transverse Field Schedules

Users can customize the transverse field schedule from initial quantum fluctuations ($\Gamma_0$) to final classical freezing ($\Gamma_f \approx 0$):

```python
# Anneal with custom transverse field boundaries
samples, energies = sampler.sample_ising(
    h=h,
    J=J,
    beta=10.0,
    gamma_0=2.0,   # Strong initial transverse field (quantum exploration)
    gamma_f=0.01,  # Near-zero final transverse field (classical localization)
    num_sweeps=500
)
```

---

## 3. Integration with Dimod Benchmark Pipelines

`pqblocks_anneal_sqa.sqa_benchmark_wrapper.SQABenchmarkWrapper` conforms directly to `dimod.BinaryQuadraticModel`, allowing straightforward inclusion into evaluation harnesses like `pqblocks-qubo-bench`:

```python
import dimod
from pqblocks_anneal_sqa import SQABenchmarkWrapper

bqm = dimod.BinaryQuadraticModel({0: -1.0, 1: 1.0}, {(0, 1): 2.0}, 0.0, dimod.SPIN)
wrapper = SQABenchmarkWrapper(num_sweeps=500, beta=5.0, P=16)
sampleset = wrapper.sample(bqm)
print("Best energy from wrapper:", sampleset.first.energy)
```
