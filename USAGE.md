# Usage examples and expected results

## Install
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Build a dataset
```bash
python scripts/make_dataset.py --start 100000 --end 120000 --out data/polarity_100k_120k.csv
```

**What to expect**
- `Z_raw` will be nearly constant (tends to 2).
- Most transforms will yield small but non-zero variation.
- Any genuine lift should be modest and unstable until you add masks/nulls and widen ranges.

## Evaluate features
```bash
python scripts/eval.py --data data/polarity_100k_120k.csv --format md --out results.md
```

This produces a Markdown table with AUC and PI (PI = 2*AUC - 1).

**Typical qualitative outcome**
- `Z_raw`: PI ~ 0 (neutral).
- `ForwardDiff`, `LogMellinSlope`: small |PI|, noisy across ranges.
- `MobiusFast`, `Dirichlet_q*`: can show weak signal, but verify with masks/nulls.
- `K3`: speculative; expect near-neutral unless a real effect exists.

> Treat any PI < 0.2 as neutral unless it is stable across disjoint windows and beats a null.
