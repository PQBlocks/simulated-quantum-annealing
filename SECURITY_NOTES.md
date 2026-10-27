# Security Notes & Posture

> Security scope, numerical safeguards, and execution boundaries for `pqblocks-anneal-sqa`.

---

## 1. Non-Cryptographic Classification

> [!NOTE]
> **Domain Classification**: Quantum-inspired classical optimisation: not cryptography, no security claim.

`pqblocks-anneal-sqa` is a heuristic numerical solver implementing Path-Integral Monte Carlo for combinatorial optimization. It does not implement, expose, or validate cryptographic primitives, key encapsulation mechanisms, digital signatures, or confidential data handling.

---

## 2. Numerical Safeguards & Trotter Stability

- **$J_{\perp}$ Log-Tanh Underflow Guarding**:
  The imaginary-time coupling between adjacent Trotter replicas is given by:
  $$J_{\perp} = -\frac{1}{2\beta} \ln \tanh\left(\frac{\beta \Gamma}{P}\right)$$
  When $\beta \Gamma / P$ becomes extremely small, $\tanh(x) \to 0$ and $\ln(\tanh(x)) \to -\infty$. The kernel incorporates analytical clamping to ensure $J_{\perp}$ remains finite and numerically stable throughout the annealing schedule.
- **Metropolis Ratio Clamping**: Transition acceptance probabilities $\exp(-\Delta E \cdot \beta)$ are bounded to prevent IEEE 754 floating-point overflow.
- **Matrix Consistency**: Input matrices are verified for dimension agreement, absence of NaN/inf values, and symmetry.
