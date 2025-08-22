# Prime Polarity — Z(p)/Z(o)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A framework for empirically scoring the **prime-signal polarity** of number-theoretic generators, with formal polarity measurement and amplification transforms.

## 🎯 Goal

Formalize the intuition ("does this generator *see* primes?") into a measurable, reproducible **Polarity Index (PI)**:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Ctext%7BPI%7D%20%3D%202%5Ccdot%5Ctext%7BAUC%7D%20-%201%20%5Cin%20%5B-1%2C1%5D" alt="PI = 2*AUC - 1" />
</p>

## 📦 Installation

```bash
pip install prime-polarity
```

## 🔬 What It Does

Computes generators like:
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?Z(n)%20%3D%20%5Cexp%5Cleft(%5Cfrac%7B%5Cpi%5C%2C%5Czeta(n-1)%7D%7Bn%7D%5Cright)%20%2B%201" alt="Z(n) = exp(πζ(n-1)/n) + 1" />
</p>

Applies five polarity amplifiers:

1. **Möbius Twist**
   <p align="center">
     <img src="https://latex.codecogs.com/svg.latex?M%5BG%5D(n)%20%3D%20%5Csum_%7Bd%7Cn%7D%20%5Cmu(d)%20%5Ccdot%20G%5Cleft(%5Cfrac%7Bn%7D%7Bd%7D%5Cright)" alt="Möbius Transform" />
   </p>

2. **Fractional-part Proximity**  
   `s(n) = min({G(n)}, 1 - {G(n)})`

3. **Forward Difference**  
   `ΔG(n) = G(n+1) - G(n)`

4. **Log-Mellin Slope**  
   `Δ_log G(n) = n * (G(n+1) - G(n))`

5. **Dirichlet-character Projection**  
   (Uses small moduli by default)

Labels primes vs. composites using a sieve and computes AUC-derived Polarity Index for each feature.

## 🚀 Quickstart

```bash
prime-polarity score --start 100000 --end 120000 --windows 3 --window-size 5000
```

## 📊 Polarity Scale

| Level | Rating | AUC Range | PI Range | Description |
|:---:|:---:|:---:|:---:|:---|
| **+2** | Perfect Direct | 1.00 | +1.00 | Perfect separation (deterministic tests) |
| **+1** | Strong Signal | 0.75-0.95 | +0.50-0.90 | Highly informative (probabilistic tests) |
| **0** | Neutral | ~0.50 | ~0.00 | No predictive power (smooth functions) |
| **-1** | Reverse Signal | 0.05-0.25 | -0.90-0.50 | Strong compositeness signal |
| **-2** | Perfect Reverse | 0.00 | -1.00 | Perfect inverted separation |

## 🧠 Theoretical Background

### Irrationality & Transcendence Heuristics
- Generators of form `G(n) = exp(F(n))` where `F(n)` takes algebraically independent values
- Lindemann–Weierstrass phenomena suggest transcendental outputs
- For `Z(n) = exp(π * ζ(n-1) / n) + 1`: as `n → ∞`, `Z(n) → 2`

### Generator Family
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?G_%7Ba%2Cb%7D(n)%20%3D%20%5Cexp%5Cleft(a%5C%2C%5Czeta(b(n))%5Cright)" alt="Generator Family" />
</p>

### Research Directions
- Irrationality on density-1 subsequences
- Transcendence under Schanuel's conjecture
- Linear independence of ζ(1 + iθₙ) values

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Please review our [Code of Conduct](CODE_OF_CONDUCT.md).

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<p align="center">
  <em>Empirical number theory meets measurable signal detection</em>
</p>
