# Kazamaki Condition

**Topic:** Stochastic Processes
**Tags:** kazamaki condition, local martingale, true martingale, measure change, girsanov, integrability
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

The **Kazamaki condition** is a sufficient criterion to guarantee that the Doléans exponential $\mathcal{E}(M)$ of a continuous local martingale $M$ is a uniformly integrable martingale (and hence a valid probability density). It is strictly weaker than the Novikov condition, meaning it applies in more cases, but is also harder to verify in practice.

## Key Formula

Let $M$ be a continuous local martingale. The Kazamaki condition states:

$$\sup_{T} E\!\left[e^{M_T / 2}\right] < \infty$$

where the supremum is taken over all bounded stopping times $T$. If this holds, then $\mathcal{E}(M)_t = e^{M_t - \frac{1}{2}[M,M]_t}$ is a uniformly integrable martingale.

Compare with the **Novikov condition**, which requires the stronger:

$$E\!\left[\exp\!\left(\tfrac{1}{2}[M,M]_\infty\right)\right] < \infty$$

Kazamaki $\subsetneq$ Novikov in terms of which processes satisfy it: every process satisfying Novikov also satisfies Kazamaki, but not vice versa.

## Example

Let $M_t = \int_0^t \theta_s\,dW_s$ where $\theta_s$ is a stochastic process (not necessarily bounded). Novikov requires $E[\exp(\frac{1}{2}\int_0^T \theta_s^2\,ds)] < \infty$. If $\theta_s$ grows fast enough that this expectation is infinite yet $\sup_T E[e^{M_T/2}] < \infty$ still holds, Kazamaki applies but Novikov fails. A concrete instance arises with $\theta_s = \sqrt{2/(T-s)}$ near the terminal time $T$: the quadratic variation $\int_0^T \theta_s^2\,ds$ diverges, violating Novikov, but the exponential half-martingale condition can still be finite.

## Remember

Both Kazamaki and Novikov are used in quantitative finance to validate Girsanov changes of measure — that is, to confirm the market-price-of-risk process $\lambda_t$ produces a genuine risk-neutral measure $\mathbb{Q}$. In practice, Novikov is the standard tool because its condition ($E[e^{\frac{1}{2}\int \lambda^2 dt}] < \infty$) is directly checkable from the model parameters. Kazamaki matters theoretically when the market price of risk is large or path-dependent and Novikov fails — for example, in certain stochastic volatility models where $\lambda_t$ depends on the variance process and can grow rapidly.
