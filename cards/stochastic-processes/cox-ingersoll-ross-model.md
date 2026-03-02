# Cox-Ingersoll-Ross Model

**Topic:** Stochastic Processes
**Tags:** CIR, short-rate model, mean reversion, interest rates, square-root diffusion, non-negative
**Author:** Claude Opus 4.6

---

## Definition

The **Cox-Ingersoll-Ross (CIR) model** is a short-rate model in which the interest rate is mean-reverting and the volatility scales with $\sqrt{r}$. This square-root diffusion ensures that interest rates remain **non-negative**, addressing the main limitation of the Vasicek model.

## Key Formula

The CIR SDE is:

$$dr = \gamma(\bar{r} - r) \, dt + \sigma \sqrt{r} \, dW$$

| Parameter | Meaning |
|---|---|
| $\gamma$ | Speed of mean reversion |
| $\bar{r}$ | Long-run equilibrium rate |
| $\sigma$ | Volatility parameter |
| $\sqrt{r}$ | Diffusion scales with level — noise vanishes at $r = 0$ |

**Feller condition** for strict positivity:

$$2\gamma\bar{r} \geq \sigma^2$$

When this holds, the drift at $r = 0$ is strong enough to push the rate away from zero before the diffusion can pull it negative.

| Property | Vasicek | CIR |
|---|---|---|
| Drift | $\gamma(\bar{r} - r)$ | $\gamma(\bar{r} - r)$ |
| Diffusion | $\sigma$ (constant) | $\sigma\sqrt{r}$ (level-dependent) |
| Negative rates? | Yes | No (if Feller condition met) |
| Steady-state distribution | Normal | Non-central chi-squared |
| Analytical tractability | High | High |

## Example

With $\gamma = 0.5$, $\bar{r} = 4\%$, $\sigma = 0.10$, the Feller condition requires $2 \times 0.5 \times 0.04 = 0.04 \geq 0.01 = \sigma^2$. This is satisfied, so rates stay strictly positive. As $r$ falls towards zero, $\sigma\sqrt{r}$ shrinks, reducing the random fluctuations and preventing the rate from reaching zero.

## Remember

The CIR model fixes the Vasicek model's negative-rate problem by making volatility proportional to $\sqrt{r}$. As $r$ approaches zero the noise dies away, creating a natural floor. The Feller condition $2\gamma\bar{r} \geq \sigma^2$ is the precise criterion for this floor to hold. The CIR model is widely used for modelling interest rates and default intensities in credit risk, and its analytical tractability makes it a workhorse in fixed-income quantitative finance.
