# Combinatorial Purged Cross-Validation

**Topic:** Computational Finance
**Tags:** cross-validation, backtesting, overfitting, financial machine learning, sharpe ratio, model selection
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Combinatorial Purged Cross-Validation (CPCV)** extends purged cross-validation by generating all $\binom{N}{k}$ combinations of $k$ test folds from $N$ total folds rather than a single sequential test path, producing a distribution of out-of-sample performance estimates rather than a single number.

## Key Formula

Divide $T$ observations into $N$ folds. Choose $k$ folds as the test set in each combination:

$$\text{Number of paths} = \binom{N}{k} = \frac{N!}{k!\,(N-k)!}$$

Each path produces an out-of-sample Sharpe ratio estimate $SR^{(i)}_\text{OOS}$. The full set $\{SR^{(i)}_\text{OOS}\}_{i=1}^{\binom{N}{k}}$ forms a distribution. Purging and an embargo period are applied to each train/test split before fitting.

The **probability of backtest overfitting (PBO)** is the fraction of paths with non-positive OOS Sharpe:

$$\text{PBO} = \frac{1}{\binom{N}{k}}\sum_{i=1}^{\binom{N}{k}} \mathbf{1}\!\left[SR^{(i)}_\text{OOS} \leq 0\right]$$

## Example

A momentum strategy is evaluated on 10 years of daily data divided into $N = 10$ annual folds, with $k = 2$ test folds per path. This gives $\binom{10}{2} = 45$ test paths. The strategy achieves $SR > 0$ in 38 of 45 paths, giving $\text{PBO} = 7/45 \approx 16\%$ — reasonably convincing. A rival strategy where only 20 of 45 paths are profitable has $\text{PBO} = 56\%$, effectively a coin toss, and should be rejected regardless of its headline Sharpe.

## Remember

Walk-forward validation produces a single OOS Sharpe ratio that can be lucky or unlucky depending on which test window falls in a bull or bear market. CPCV produces a full distribution: if the strategy is genuine, most of the $\binom{N}{k}$ paths should be profitable; if it is overfit, the distribution straddles zero. A PBO above 50% means the strategy fails on more test windows than it passes — a statistically grounded rejection criterion that is far harder to game than a single backtest Sharpe ratio. CPCV was introduced by Lopez de Prado and Lewis in *Journal of Financial Economics* (2019).
