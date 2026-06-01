# Probability of Backtest Overfitting

**Topic:** Statistics
**Tags:** backtesting, overfitting, sharpe ratio, combinatorial cross-validation, multiple testing, strategy validation
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

The **Probability of Backtest Overfitting (PBO)** is the fraction of combinatorial out-of-sample paths from CPCV on which the selected strategy (the one with the highest in-sample Sharpe ratio) achieves a non-positive out-of-sample Sharpe ratio, providing a data-driven probability that a strategy's backtest performance is the result of overfitting rather than genuine skill.

## Key Formula

From $\binom{N}{k}$ CPCV paths, select the strategy $s^*$ that maximises in-sample Sharpe on each path. PBO is the proportion of paths where $s^*$ underperforms:

$$\text{PBO} = \frac{1}{\binom{N}{k}} \sum_{i=1}^{\binom{N}{k}} \mathbf{1}\!\left[SR^{(i)}_{\text{OOS}}(s^*) \leq 0\right]$$

The **logit** of the distribution of relative OOS performance $\lambda^{(i)} = SR^{(i)}_{\text{OOS}}(s^*) - \bar{SR}^{(i)}_{\text{OOS}}$ is plotted as a histogram; PBO equals the mass of this distribution at $\lambda \leq 0$:

$$\text{PBO} = \Pr\!\left(\lambda \leq 0\right)$$

## Example

A systematic equity strategy is tested via CPCV with $N = 12$ monthly folds and $k = 2$ test folds per path, yielding $\binom{12}{2} = 66$ paths. The strategy with the highest in-sample Sharpe is selected from each path's training set. On 20 of 66 paths, this selected strategy has OOS Sharpe $\leq 0$, giving $\text{PBO} = 20/66 \approx 30\%$. A PBO of 30\% means the strategy fails roughly one-third of the time on unseen data — a warning sign that the selection process was over-tuned.

## Remember

PBO is one of the few strategy validation metrics that directly penalises the selection process rather than the strategy itself. A strategy tested once on the full history may look excellent; the same strategy selected from 50 variants tested on the same data almost certainly has an inflated Sharpe. PBO captures this: it asks not "did this strategy do well out-of-sample?" but "did the *best-in-sample* strategy do well out-of-sample?" — a subtler and more realistic question that matches how strategies are actually chosen in practice. A PBO above 50\% means the selection process is essentially a coin flip, and the strategy should be rejected regardless of its reported headline Sharpe.
