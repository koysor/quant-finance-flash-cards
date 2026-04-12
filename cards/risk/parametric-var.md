# Parametric (Delta-Normal) VaR

**Topic:** Risk
**Tags:** var, parametric, normal distribution, z-score, volatility, delta-normal
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

**Parametric VaR** (also called Delta-Normal VaR) estimates Value at Risk analytically by assuming asset returns are normally distributed. Because the normal distribution is fully described by its mean $\mu$ and standard deviation $\sigma$, no simulation or historical data is needed — VaR is computed directly from these two parameters.

This makes parametric VaR fast and transparent, but the normality assumption is its fundamental weakness: real asset returns have fat tails and skewness that the normal distribution cannot capture.

## Key Formula

**General form** — for a portfolio with normally distributed P&L:

$$\text{VaR}_c = -\left(\mu + \Phi^{-1}(1 - c)\,\sigma\right)$$

where $\Phi^{-1}$ is the inverse standard normal CDF and $c$ is the confidence level.

**Practical dollar formula** (zero-mean daily return assumption):

$$\text{VaR} = \text{Vol} \times \sqrt{T} \times z_c \times N$$

| Symbol | Meaning |
|--------|---------|
| $\text{Vol}$ | Daily volatility (as a decimal) |
| $T$ | Holding period in trading days |
| $z_c$ | Standard normal z-score at confidence $c$ |
| $N$ | Notional value (£ or \$) |

**Key z-scores:**

| Confidence level | $z_c$ |
|-----------------|-------|
| 95% | 1.645 |
| 99% | 2.326 |
| 99.5% | 2.576 |

## Example

**QQQ (Nasdaq 100 ETF)** — position of \$100,000 with daily volatility of 2.21%, 99% confidence.

**1-day VaR:**

$$\text{VaR}_{1d} = 2.21\% \times \sqrt{1} \times 2.326 \times \$100{,}000 = \$5{,}141$$

**10-day VaR** (scaling via the square-root rule):

$$\text{VaR}_{10d} = 2.21\% \times \sqrt{10} \times 2.326 \times \$100{,}000 \approx \$16{,}252$$

There is a 1% chance of losing more than \$5,141 in a single day on this position. Scaling to 10 days assumes returns are independent and identically distributed.

## Remember

Parametric VaR is elegant but rests on a fragile assumption: that returns are normally distributed. In reality, equity and credit returns exhibit **fat tails** — extreme losses occur far more frequently than the normal distribution predicts. The 2008 financial crisis produced daily losses that a normal model would have assigned probabilities of less than 1 in a trillion.

This is precisely why regulators moved away from VaR towards **Expected Shortfall (ES)** under **FRTB (Fundamental Review of the Trading Book)**: ES measures the *expected* loss in the tail beyond the VaR threshold, penalising fat-tailed distributions more heavily. Parametric VaR ignores what happens when the normality assumption breaks — ES does not.
