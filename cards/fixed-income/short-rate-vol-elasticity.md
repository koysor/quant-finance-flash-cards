# Short-Rate Volatility Elasticity

**Topic:** Fixed Income
**Tags:** volatility elasticity, beta, power law, CEV, empirical, Vasicek, CIR, LIBOR
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **volatility elasticity** $\beta$ parametrises how fast interest rate volatility grows with the rate level in the power-law model $dr = u(r)\,dt + \nu r^\beta\,dW_t$. It governs the model's distributional properties: $\beta = 0$ gives Gaussian rates (Vasicek), $\beta = \frac{1}{2}$ gives non-negative CIR rates, and $\beta = 1$ gives log-normal rates.

## Key Formula

The quadratic variation identity:

$$\mathbb{E}\!\left[(\delta r)^2\right] = \nu^2 r^{2\beta}\,\delta t$$

implies that the **conditional standard deviation** of $\delta r$ scales as $\nu r^\beta \sqrt{\delta t}$.

| $\beta$ | Model | Volatility grows as | Negative rates? |
|---|---|---|---|
| 0 | Vasicek / Ho–Lee | Constant $\nu$ | Possible |
| 0.5 | CIR / Hull–White II | $\nu\sqrt{r}$ | No (Feller) |
| 1 | Lognormal / BGDM | $\nu r$ | No |
| 1.13 | Empirical (US LIBOR) | $\nu r^{1.13}$ | No |

## Example

Comparing the volatility of a 2% rate versus a 6% rate under three models:

- Vasicek ($\beta = 0$): both have the same absolute volatility $\nu$.
- CIR ($\beta = 0.5$): the 6% rate is $\sqrt{6/2} = 1.73\times$ more volatile.
- $\beta = 1.13$: the 6% rate is $(6/2)^{1.13} = 3^{1.13} \approx 3.45\times$ more volatile.

US data firmly favours $\beta \approx 1.13$, making rates behave more like equities than like the Vasicek model's constant-volatility Brownian motion.

## Remember

The empirical finding $\beta \approx 1.13$ has practical consequences: a model calibrated with $\beta = 0$ (Vasicek) systematically underestimates the volatility of high-rate environments and overestimates it when rates are low. This matters for pricing caps and floors, which are more valuable when volatility is higher. The US data suggests that a constant-volatility model systematically misprices these instruments when the yield curve is steep.
