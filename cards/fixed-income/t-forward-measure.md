# T-Forward Measure

**Topic:** Fixed Income
**Tags:** T-forward measure, forward measure, numeraire, zero-coupon bond, martingale, caplet pricing
**Created:** 2026-06-12
**Author:** Claude Sonnet 4.6

---

## Definition

The **$T$-forward measure** $\mathbb{Q}^T$ is the probability measure obtained by choosing the zero-coupon bond $P(t,T)$ as the numéraire. Under this measure, the price of any claim paid at time $T$ equals its $\mathbb{Q}^T$-expectation, with no stochastic discounting inside the expectation. The $T$-forward measure is the natural pricing measure for any product whose payoff and payment occur at the same date $T$.

## Key Formula

Pricing under $\mathbb{Q}^T$: for any claim with payoff $H$ paid at $T$:

$$V_0 = P(0,T)\,\mathbb{E}^{\mathbb{Q}^T}[H]$$

**Radon–Nikodým derivative** from risk-neutral to $T$-forward measure:

$$\frac{d\mathbb{Q}^T}{d\mathbb{Q}}\bigg|_t = \frac{P(t,T)}{P(0,T)\,B_t}$$

where $B_t = e^{\int_0^t r_s\,ds}$ is the money-market account.

**Key martingale property:** the simply-compounded forward LIBOR/SOFR rate for $[T_1, T_2]$:

$$F(t;\,T_1,T_2) = \frac{1}{\delta}\!\left(\frac{P(t,T_1)}{P(t,T_2)} - 1\right)$$

is a martingale under $\mathbb{Q}^{T_2}$ (the measure associated with the payment date $T_2$).

## Example

Caplet paying $\delta(L_{T_1} - K)^+$ at $T_2 = T_1 + \delta$.

Under the risk-neutral measure $\mathbb{Q}$: $L_{T_1}$ is correlated with the discount factor $P(T_1,T_2)$ — a product of two stochastic processes, hard to integrate.

Under $\mathbb{Q}^{T_2}$ (the $T_2$-forward measure): the forward LIBOR $F(t;T_1,T_2)$ is a martingale, so $\mathbb{E}^{\mathbb{Q}^{T_2}}[L_{T_1}] = F(0;T_1,T_2)$. If $L_{T_1}$ is assumed lognormal under $\mathbb{Q}^{T_2}$, the caplet formula reduces directly to Black's formula with $P(0,T_2)$ as the discount factor — no stochastic integral needed.

## Remember

The $T$-forward measure is the reason why Black's caplet formula **works**: the trick is not assuming lognormal rates under the risk-neutral measure (which is wrong), but recognising that the forward rate is a martingale under the forward measure and then making the lognormal assumption there. This distinction matters because the risk-neutral dynamics of LIBOR include a drift term (due to convexity) that complicates pricing, whereas under $\mathbb{Q}^T$ the forward rate drifts exactly to zero. The LIBOR market model is built on exactly this: each forward rate is lognormal under its own payment-date forward measure, and changes of measure between different dates are handled via the Girsanov drift adjustment.
