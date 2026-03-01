# Fat-Tailed Distributions

**Topic:** Probability
**Tags:** distributions, fat tails, kurtosis, tail risk, extreme events

---

## Definition

A fat-tailed distribution is one whose tails decay more slowly than those of the normal distribution, meaning extreme values occur with substantially higher probability. Formally, a distribution has fat tails if its tail probability $P(X > x)$ decreases as a power law $x^{-\alpha}$ rather than exponentially, or more generally if its kurtosis exceeds the normal value of 3 (excess kurtosis > 0).

## Key Formula

The kurtosis of a distribution measures how heavy its tails are relative to the normal:

$$\kappa = \frac{E\left[(X - \mu)^4\right]}{\left(E\left[(X - \mu)^2\right]\right)^2}$$

A normal distribution has $\kappa = 3$. Fat-tailed distributions have $\kappa > 3$, so the **excess kurtosis** is:

$$\kappa_{\text{excess}} = \kappa - 3 > 0$$

For a Student's $t$-distribution with $\nu > 4$ degrees of freedom, the kurtosis is:

$$\kappa = 3 + \frac{6}{\nu - 4}$$

## Example

Suppose daily equity returns have sample mean $\mu = 0$ and standard deviation $\sigma = 1\%$. Under the normal distribution, a $-4\sigma$ move (a daily loss of 4%) has probability:

$$P(X < -4\sigma) = \Phi(-4) \approx 0.0032\% \quad (\text{about 1 in 31{,}574 days, or once every 125 years})$$

Now model the same returns with a $t$-distribution with $\nu = 5$ degrees of freedom (scaled to the same standard deviation). The probability of a $-4\sigma$ move becomes approximately:

$$P(X < -4\sigma) \approx 0.51\% \quad (\text{about 1 in 196 days, or roughly once a year})$$

The fat-tailed model predicts extreme losses roughly **160 times more often** than the normal.

## Remember

Real financial returns are fat-tailed: events like the 1987 crash ($-22\sigma$ under the normal model) or the 2008 crisis occur far more frequently than Gaussian assumptions permit. Any risk model built on the normal distribution -- parametric VaR, Black-Scholes, mean-variance optimisation -- systematically underestimates tail risk. Recognising fat tails is the first step toward using heavier-tailed models (Student's $t$, stable distributions) or non-parametric methods (historical simulation, extreme value theory) that give more realistic estimates of catastrophic loss.
