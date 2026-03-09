# Ornstein–Uhlenbeck Process

**Topic:** Stochastic Processes
**Tags:** mean reversion, sde, gaussian, interest rates, vasicek
**Created:** 2026-03-08
**Author:** Claude Sonnet 4.6

---

## Definition

The **Ornstein–Uhlenbeck (OU) process** is a mean-reverting stochastic process defined by the SDE $dX = \theta(\mu - X)\,dt + \sigma\,dW$, where $\theta > 0$ is the speed of reversion, $\mu$ is the long-run mean, and $\sigma$ is the volatility. It is the only continuous-time process that is simultaneously Gaussian, Markov, and stationary.

## Key Formula

The SDE and its exact solution are:

$$dX_t = \theta(\mu - X_t)\,dt + \sigma\,dW_t$$

$$X_t = \mu + (X_0 - \mu)e^{-\theta t} + \sigma\int_0^t e^{-\theta(t-s)}\,dW_s$$

The conditional distribution is Gaussian with:

$$\mathbb{E}[X_t \mid X_0] = \mu + (X_0 - \mu)e^{-\theta t}, \qquad \operatorname{Var}(X_t \mid X_0) = \frac{\sigma^2}{2\theta}\bigl(1 - e^{-2\theta t}\bigr)$$

## Example

Suppose an interest rate follows an OU process with $\mu = 0.05$, $\theta = 2$, $\sigma = 0.01$, and current rate $X_0 = 0.08$. After one year:

$$\mathbb{E}[X_1] = 0.05 + (0.08 - 0.05)e^{-2} \approx 0.05 + 0.03 \times 0.135 = 0.054$$

The rate is pulled 86.5% of the way back towards 5% within a year. The standard deviation at $t = 1$ is $\frac{0.01}{\sqrt{4}}\sqrt{1 - e^{-4}} \approx 0.0049$, so the 95% confidence interval is roughly $[4.5\%,\, 6.3\%]$.

## Remember

The **Vasicek model** is precisely an OU process applied to the short rate. The mean-reversion speed $\theta$ governs how quickly rates return to their long-run level $\mu$ after a shock — a large $\theta$ (fast reversion) flattens the term structure because long rates are anchored close to $\mu$, whilst a small $\theta$ allows short-rate deviations to persist and produces a more steeply sloped yield curve.
