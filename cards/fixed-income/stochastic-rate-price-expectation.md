# Price–Expectation with Stochastic Rates

**Topic:** Fixed Income
**Tags:** risk-neutral pricing, stochastic discount factor, expectation, bond pricing, Q-measure
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

When interest rates are stochastic, the discount factor is a random variable correlated with the payoff. The bond price is then the **risk-neutral expectation of the discounted payoff**, where the stochastic discount factor $e^{-\int_t^T r(\tau)\,d\tau}$ must remain inside the expectation — it cannot be factored out.

## Key Formula

$$V(r,t) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(\tau)\,d\tau}\,\cdot\,\text{Payoff}(T)\,\middle|\,\mathcal{F}_t\right]$$

| Case | Formula | When valid |
|---|---|---|
| Constant rate $r$ | $V = e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}[\text{Payoff}]$ | Deterministic $r$ |
| Deterministic $r(t)$ | $V = e^{-\int_t^T r(\tau)d\tau}\,\mathbb{E}^{\mathbb{Q}}[\text{Payoff}]$ | Rate known in advance |
| Stochastic $r$ | $V = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r\,d\tau}\cdot\text{Payoff}\right]$ | General case |

For a **zero-coupon bond** (Payoff $= 1$):

$$V(r,t;T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(\tau)\,d\tau}\,\middle|\,r(t) = r\right]$$

## Example

Under Vasicek with risk-neutral parameters $\eta = 0.025$, $\gamma = 0.4$, $\beta = 0.0001$, and current rate $r = 3\%$, a 5-year zero-coupon bond is priced by simulating 10,000 risk-neutral paths of $r(\tau)$ over $[0, 5]$, computing $e^{-\int_0^5 r\,d\tau}$ on each path, and averaging. The closed-form Vasicek formula gives the same answer: $V = e^{A - Br}$ where $B = (1 - e^{-5\gamma})/\gamma$.

## Remember

The stochastic discount factor $e^{-\int_t^T r\,d\tau}$ is the key difference between fixed-income and equity pricing. In equity derivatives the discount rate is the constant risk-free rate and factors out. In interest rate models the discount rate is itself stochastic, so it is **correlated** with the payoff — a rise in rates simultaneously reduces the discount factor and changes payoff expectations. Separating them would be a mathematical error.
