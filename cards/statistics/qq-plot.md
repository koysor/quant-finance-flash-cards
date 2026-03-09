# Quantile–Quantile Plot

**Topic:** Statistics
**Tags:** Q-Q plot, normal distribution, goodness of fit, diagnostics, fat tails
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

A **quantile–quantile (Q-Q) plot** is a graphical tool that compares the quantiles of a data sample against the theoretical quantiles of a reference distribution (usually the standard normal). If the data follow the reference distribution, the points lie on a straight line. Deviations from the line reveal skewness, fat tails, or other departures from normality.

## Key Formula

For $n$ sorted observations $x_{(1)} \leq x_{(2)} \leq \cdots \leq x_{(n)}$, each point on the Q-Q plot is:

$$\left(\Phi^{-1}\!\left(\frac{i - 0.5}{n}\right),\; x_{(i)}\right) \quad \text{for } i = 1, 2, \ldots, n$$

If the data are truly $N(\mu, \sigma^2)$, the points lie on the line:

$$x = \mu + \sigma z$$

| Pattern | Interpretation |
|---|---|
| Points on straight line | Data match the reference distribution |
| S-shaped curve | Fat tails (heavy-tailed distribution) |
| Concave upward | Right skew |
| Concave downward | Left skew |
| Flattened ends | Thin tails (light-tailed distribution) |

## Example

A risk analyst collects 100 daily log-returns for an equity index. The sorted 5th-smallest return is $x_{(5)} = -3.8\%$. The theoretical quantile is:

$$z_5 = \Phi^{-1}\!\left(\frac{5 - 0.5}{100}\right) = \Phi^{-1}(0.045) = -1.695$$

If returns were normal with $\mu = 0.05\%$ and $\sigma = 1.2\%$, the expected value at this quantile would be $0.05 + 1.2 \times (-1.695) = -1.98\%$.

The actual $-3.8\%$ is far below $-1.98\%$ — this point sits well below the reference line, indicating a fatter left tail than the normal distribution predicts.

## Remember

The Q-Q plot is the first diagnostic tool a quant reaches for when validating distributional assumptions. If a VaR model assumes normality but the Q-Q plot shows an S-shaped departure, the model is systematically underestimating tail risk — exactly the scenario that produced losses in the 2008 financial crisis. Regulatory frameworks (Basel III) require banks to backtest their VaR models, and Q-Q plots provide immediate visual evidence of model misspecification. They also guide model selection: an S-shaped Q-Q plot suggests switching to a Student's $t$ distribution or using the Cornish–Fisher correction, while a straight-line Q-Q plot confirms that the normal assumption is adequate for the data at hand.
