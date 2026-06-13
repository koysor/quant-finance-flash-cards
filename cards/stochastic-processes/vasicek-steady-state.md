# Vasicek Steady-State Distribution

**Topic:** Stochastic Processes
**Tags:** Vasicek, steady state, Fokker-Planck, normal distribution, negative rates, long-run distribution
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **Vasicek steady-state distribution** is the long-run (stationary) probability density of the spot rate under the Vasicek model. As $t \to \infty$, the spot rate converges in distribution to a **Normal distribution**, centred on the long-run mean with a variance that balances the mean-reversion speed against the diffusion intensity.

## Key Formula

The steady-state PDF $P_\infty(r)$ satisfies the stationary Fokker–Planck equation and is:

$$P_\infty(r) = \sqrt{\frac{\gamma}{\pi\beta}}\,\exp\!\left(-\frac{\gamma}{\beta}\!\left(r - \frac{\eta}{\gamma}\right)^{\!2}\right)$$

This is a Normal distribution:

$$r \xrightarrow{t \to \infty} \mathcal{N}\!\left(\frac{\eta}{\gamma},\; \frac{\beta}{2\gamma}\right)$$

| Parameter | Steady-state mean | Steady-state variance |
|---|---|---|
| Vasicek | $\eta/\gamma$ | $\beta/(2\gamma)$ |
| CIR | $\eta/\gamma$ | $\alpha\eta/(2\gamma^2)$ (Gamma distribution) |

**Negative rates:** because the Vasicek steady state is Normal (supported on $(-\infty, +\infty)$), the short rate can go negative with probability $\Phi\!\left(-\frac{\eta/\gamma}{\sqrt{\beta/(2\gamma)}}\right)$.

## Example

With $\gamma = 0.5$, $\eta = 0.02$, $\beta = 0.0004$, the long-run mean is $0.02/0.5 = 4\%$ and the long-run standard deviation is $\sqrt{0.0004/(2 \times 0.5)} = 2\%$. The probability of a negative rate is $\Phi(-4/2) = \Phi(-2) \approx 2.3\%$ — small but non-zero.

## Remember

The Gaussian steady state of Vasicek is analytically convenient — it makes bond prices exponential-affine — but economically problematic because negative interest rates are an implication of the model. The CIR model replaces the Normal steady state with a Gamma distribution by changing the diffusion coefficient from $\sqrt{\beta}$ to $\sqrt{\alpha r}$. This single change prevents negative rates (provided the Feller condition $\eta > \alpha/2$ holds) at the cost of slightly less tractable closed-form formulas.
