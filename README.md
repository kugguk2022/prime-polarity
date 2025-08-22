# Prime Polarity $$\frac{Z(p)}{Z(o)}$$

A tiny, empirical framework to **score the prime-signal polarity** of number-theoretic generators such as our

$$
Z(n) = \exp\^\left(\frac{\pi\,\zeta(n-1)}{n}\right) + 1
$$

and an odd-character variant $Z(o)$.

**Goal:** turn informal intuition (“does this generator *see* primes?(does it generate irrationals and/or transcendentals instead”) into a **measurable, reproducible Polarity Index (PI)** based on ROC AUC.

---

## What it does

- Computes **$Z(n)$** and optional **$Z(o)$** placeholders.
- Applies **five polarity amplifiers** (transforms):
  1. Möbius twist  $$M[G](n) = ∑_{d|n} μ(d) · G(n/d)$$
  2. Fractional-part proximity  $$\,s(n)=\min(\{G(n)\},1-\{G(n)\})$$
  3. Forward difference  $$\,\Delta G(n)=G(n+1)-G(n)$$
  4. Log-Mellin slope  $$\,\Delta_{\log}G(n)=n\big(G(n+1)-G(n)\big)$$
  5. Dirichlet-character projection (few small moduli by default)
- Labels **primes vs. composites** with a sieve.
- Scores each feature by **AUC** and converts it to **Polarity Index**  
  **PI** $$= 2\cdot\text{AUC}-1 \in [-1,1]$$.
- Reports per-window stability.

**Expectation:** raw $$Z(n)$$ is typically **neutral** (PI≈0). If any true signal exists, some transforms should push PI into **0.2–0.6** territory.

---

## Install

```bash
pip install .[dev]
```

Python ≥ 3.9 is recommended.

---

## Quickstart

Compute polarity for default transforms on $n\in[100000, 120000]$ in three sliding windows:

```bash
prime-polarity score --start 100000 --end 120000 --windows 3 --window-size 5000
```

---

## Development

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .[dev]
pytest -q
```

---

## Appendix: Irrational/Transcendental Generator Notes

This project is **empirical**; it doesn’t claim proofs. Still, here is a concise map for collaborators.

### 1) Irrationality & transcendence heuristics
- If a generator has the form $G(n)=\exp(F(n))$ where $F(n)$ takes algebraically independent values at infinitely many $n$, **Lindemann–Weierstrass**-type phenomena suggest “many” outputs are transcendental. Proving this for specific $F(n)$ is typically very hard.
- For $Z(n)=\exp(\pi\,\zeta(n-1)/n)+1$: as $n\to\infty$, $\zeta(n-1)\to 1$, so $Z(n)\to 2$. Near-constancy makes prime-signal weak, but does not by itself decide irrationality/transcendence of individual values.

### 2) A “generator family” to study
Consider $ G_{a,b}(n) = \exp\!\big(a\,\zeta(b(n))\big) $ with slowly-varying $b(n)$ (e.g., $1+\tfrac{i\,c}{\log n}$) and arithmetic couplings (Dirichlet $L$-values, characters). Empirically test polarity; theoretically, ask:
- When can one show **infinitely many values are irrational**?
- Under extra hypotheses (e.g., **Schanuel’s conjecture**), which subfamilies would be **transcendental** infinitely often?

### 3) Minimal “proof sketch” targets collaborators could tackle
- **Irrationality on a density-1 subsequence:** Show that if $b(n)\to 1$ with controlled imaginary part and $a\notin \pi\mathbb{Q}$, then $\{\Re \zeta(b(n))\}$ avoids rationals on a set of density 1. (Diophantine approximation + equidistribution tools.)
- **Transcendence under conditional axioms:** With Schanuel or related, $\exp$ of linearly independent complex numbers is algebraically independent. Seek linear independence for $\zeta(1+i\theta_n)$ via mean-value theorems and zero-density estimates.

---

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) and [CODE OF CONDUCT](CODE_OF_CONDUCT.md).

---

## License

MIT
