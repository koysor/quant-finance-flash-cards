# Lognormal Steady-State Rate Distribution

**Topic:** Fixed Income
**Tags:** lognormal, steady state, interest rate, Fokker-Planck, empirical, drift estimation
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **lognormal steady-state distribution** is the empirical fit to the long-run histogram of spot interest rates: the probability density is lognormal with a median rate $\bar{r}$ and log-standard deviation $a$. Substituting this fitted density into the Fokker–Planck inversion formula produces the nonlinear mean-reverting drift consistent with the data.

## Key Formula

The lognormal steady-state PDF:

$$p_\infty(r) = \frac{1}{a r\sqrt{2\pi}}\exp\!\left(-\frac{(\log(r/\bar{r}))^2}{2a^2}\right)$$

From US 1-month LIBOR (1985–1997): $\bar{r} = 0.08$ (8%), $a = 0.40$.

The implied real-world drift via Fokker–Planck inversion (with volatility $w = \nu r^\beta$):

$$u(r) = \nu^2 r^{2\beta-1}\!\left(\beta - \tfrac{1}{2} - \frac{\log(r/\bar{r})}{2a^2}\right)$$

When $r < \bar{r}$: $\log(r/\bar{r}) < 0 \Rightarrow u(r) > 0$ (upward pull). When $r > \bar{r}$: drift is negative (downward pull). The strength of the pull increases with log-distance from $\bar{r}$.

## Example

At $r = 4\%$ with $\bar{r} = 8\%$: $\log(0.04/0.08) = \log(0.5) = -0.693$. With $a = 0.4$, $\beta = 1.13$, $\nu = 0.126$: the drift term $-\log(r/\bar{r})/(2a^2) = 0.693/0.32 = 2.17$, giving a strong upward pull. At $r = 15\%$: $\log(0.15/0.08) = 0.629$, drift contribution $= -0.629/0.32 = -1.97$, giving a downward pull. The pull is nonlinear and asymmetric.

## Remember

Using a lognormal rather than a normal steady-state distribution has two practical advantages: it assigns zero probability to negative rates (consistent with pre-2015 rate regimes) and it produces nonlinear mean reversion rather than the linear Ornstein–Uhlenbeck drift of the Vasicek model. The log-distance pull $\log(r/\bar{r})$ means that rates at extreme levels (very high or very low) experience stronger mean reversion than rates near the long-run median, matching empirical behaviour more closely than any linear model.
