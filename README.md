# Prime Polarity — Z(p)/Z(o)
<summary>
A tiny, empirical framework to **score the prime-signal polarity** of number-theoretic generators such as:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?Z(n)%20%3D%20%5Cexp%5Cleft(%5Cfrac%7B%5Cpi%5C%2C%5Czeta(n-1)%7D%7Bn%7D%5Cright)%20%2B%201" alt="Z(n) = exp(πζ(n-1)/n) + 1" />
</p>

and an odd-character variant `Z(o)`.

---

**Goal:**  
Formalize the intuition (“does this generator *see* primes?”) into a **measurable, reproducible Polarity Index (PI):**

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ctext%7BPI%7D%20%3D%202%5Ccdot%5Ctext%7BAUC%7D%20-%201%20%5Cin%20%5B-1%2C1%5D" alt="PI = 2*AUC - 1" />
</p>

---


- Python $\geq$ 3.9
- pip

Install the package with development dependencies:


---

## What it does

- Computes `Z(n)` and an optional odd-character variant `Z(o)`.
- Applies **five polarity amplifiers (transforms)** to the generator's output `G(n)`:

  1.  **Möbius twist**
      <p align="center">
        <img src="https://latex.codecogs.com/svg.latex?M%5BG%5D(n)%20%3D%20%5Csum_%7Bd%7Cn%7D%20%5Cmu(d)%20%5Ccdot%20G%5Cleft(%5Cfrac%7Bn%7D%7Bd%7D%5Cright)" alt="MG = Sum_{d|n} μ(d) * G(n/d)" />
      </p>

  2.  **Fractional-part proximity**  
      — `s(n) = min({G(n)}, 1 - {G(n)})`, where `{x}` is the fractional part of `x`.

  3.  **Forward difference**  
      — `ΔG(n) = G(n+1) - G(n)`

  4.  **Log-Mellin slope**  
      — `Δ_log G(n) = n * (G(n+1) - G(n))`

  5.  **Dirichlet-character projection**  
      (Uses a few small moduli by default).

- Labels **primes vs. composites** with a sieve.
- Scores each feature by **AUC** and converts it to **Polarity Index (PI)**.
- Reports per-window stability.

**Expectation:**  
A raw generator like `Z(n)` is typically **neutral** (PI ≈ 0). If any true prime signal exists, some of these transforms should amplify it, pushing the PI into the **0.2–0.6** territory.
</summary>
---
## Quickstart

Compute polarity for default transforms on `n` in the range `[100000, 120000]`, analyzed over three sliding windows:

```bash
prime-polarity score --start 100000 --end 120000 --windows 3 --window-size 5000

### 1) Irrationality & Transcendence Heuristics

- If a generator has the form `G(n) = exp(F(n))` where `F(n)` takes algebraically independent values at infinitely many `n`, **Lindemann–Weierstrass**-type phenomena suggest that “many” outputs are transcendental.
- For `Z(n) = exp(π * ζ(n-1) / n) + 1`: as `n → ∞`, `ζ(n-1) → 1`, so `Z(n) → 2`. This near-constancy makes the prime signal weak, but it does not by itself decide the irrationality or transcendence of individual values.

### 2) A “Generator Family” to Study

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?G_%7Ba%2Cb%7D(n)%20%3D%20%5Cexp%5Cleft(a%5C%2C%5Czeta(b(n))%5Cright)" alt="G_{a,b}(n) = exp(a * ζ(b(n)))" />
</p>
...with a slowly-varying function `b(n)` (e.g., `1 + (i*c) / log(n)`) and arithmetic couplings (Dirichlet `L`-values, characters). The goal is to empirically test polarity and heuristics for irrationality/transcendence.

- When can one show **infinitely many values are irrational**?
- Under extra hypotheses (e.g., **Schanuel’s conjecture**), which subfamilies would be **transcendental** infinitely often?

### 3) Minimal “Proof Sketch” Targets Collaborators Could Tackle

- **Irrationality on a density-1 subsequence:**  
  Show that if `b(n) → 1` with a controlled imaginary part and `a` is not a rational multiple of `π`, then `{Re(ζ(b(n)))}` (the fractional part of the real part) avoids rational numbers on a set of density 1.
- **Transcendence under conditional axioms:**  
  With Schanuel's conjecture or related axioms, the `exp` of linearly independent complex numbers is algebraically independent. The task is to seek linear independence for `ζ(1 + iθ_n)` vs. `ζ(1 + iθ_m)`.

---

### Polarity Scale (−2 … +2)

> 💡 **Note:** The measurable **Polarity Index (PI)** in this repo is always in **[−1, 1]** with \( \mathrm{PI} = 2\cdot\mathrm{AUC} - 1 \). The **polarity levels −2…+2** below are **conceptual bins**.

| Polarity | Rating | AUC | PI | Description | Example generators / methods | What to do |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **+2** 🚀 | **Perfect direct signal** | **1.00** | **+1.00** | Output separates primes from composites **perfectly**. | Deterministic primality (AKS, ECPP), ground-truth labels. | Nothing—this is the ideal ceiling. |
| **+1** ✅ | **Strong direct signal** | ~0.75–0.95 | ~+0.50–+0.90 | Output is **highly** informative for primality. | High-confidence probabilistic tests (Miller–Rabin, Baillie–PSW). | Use as primary feature; verify **window stability** and add null baselines. |
| **0** ⚖️ | **Neutral signal** | ~0.50 | ~0.00 | Output is **independent** of primality (no ranking power). | Smooth analytic forms (e.g., raw \( Z(n) \)); random noise. | Apply **amplifiers/transforms** (Möbius twist, fractional-part, etc.). |
| **−1** ⚠️ | **Reverse signal** | ~0.05–0.25 | ~−0.90–−0.50 | Output is strongly tied to **compositeness** or ranks primes **worst**. | Compositeness witnesses/factor-finding scores; mis-signed but informative transforms. | **Negate or invert** the feature; it can become a high-value positive signal. |
| **−2** ↩️ | **Perfect reverse signal** | **0.00** | **−1.00** | Output separates **composites** from primes perfectly (but **inverted**). | An oracle that always exposes a factor for composites. | Flip sign (or swap labels) to obtain **+2** behavior. |

<br/>
<details>
<summary><b>Quick mapping reminder</b></summary>
<br/>

- \( \mathrm{AUC} = 0.5 \Rightarrow \mathrm{PI} = 0 \) (neutral)
- \( \mathrm{AUC} = 1.0 \Rightarrow \mathrm{PI} = +1 \) (perfect direct)
- \( \mathrm{AUC} = 0.0 \Rightarrow \mathrm{PI} = -1 \) (perfect reverse)

</details>
## Contributing

See [CONTRIBUTING](CONTRIBUTING.md). Be kind: [CODE OF CONDUCT](CODE_OF_CONDUCT.md).

---

## License

MIT
