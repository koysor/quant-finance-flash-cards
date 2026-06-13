# Compound Option

**Topic:** Derivatives
**Tags:** compound option, call on call, put on call, geske formula, second-order, staged decisions
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **compound option** is an option whose underlying is itself an option: the outer option gives the right to buy or sell an inner option at a specified price $X$ on a specified date $T_1 < T_2$, where $T_2$ is the inner option's expiry. There are four types — call-on-call (CoC), call-on-put (CoP), put-on-call (PoC), put-on-put (PoP) — and the payoff materialises only when both exercise conditions are simultaneously met.

## Key Formula

The four payoffs at outer expiry $T_1$ (inner strike $K$, inner expiry $T_2$):

| Type | Payoff at $T_1$ |
|------|-----------------|
| Call-on-call | $\max\bigl(C(S_{T_1}, K, T_2\!-\!T_1) - X,\; 0\bigr)$ |
| Call-on-put | $\max\bigl(P(S_{T_1}, K, T_2\!-\!T_1) - X,\; 0\bigr)$ |
| Put-on-call | $\max\bigl(X - C(S_{T_1}, K, T_2\!-\!T_1),\; 0\bigr)$ |
| Put-on-put | $\max\bigl(X - P(S_{T_1}, K, T_2\!-\!T_1),\; 0\bigr)$ |

The **Geske (1979)** closed-form for a call-on-call uses the bivariate normal CDF $N_2$:

$$C_{\text{CoC}} = S_0 N_2(a_1, b_1;\, \rho) - Ke^{-rT_2} N_2(a_2, b_2;\, \rho) - Xe^{-rT_1} N(a_2)$$

where $\rho = \sqrt{T_1/T_2}$, and $a_i$, $b_i$ are Black–Scholes arguments evaluated at the critical stock price $S^*$ satisfying $C_{\text{BS}}(S^*, K, T_2 - T_1) = X$.

## Example

A pharmaceutical company in Phase 2 trials ($T_1 = 3$ months) plans to raise capital via a convertible bond if Phase 3 succeeds ($T_2 = 9$ months). It buys a **call-on-call**: pay £1.20 today for the right to buy a 6-month call with $K = \pounds100$ for outer strike $X = \pounds4$.

At $T_1$: Phase 3 succeeds, stock at £115, inner call worth £16 → compound call pays £16 − £4 = **£12** (10× leverage on the £1.20 premium). Phase 3 fails, stock at £75, inner call worth £1 → compound call expires worthless, losing only £1.20 (not the full call premium of £4+).

## Remember

Compound options are the natural instrument for staged decision processes — wherever one event must occur before a second decision becomes relevant. In **corporate finance**, a firm bidding for a target might buy a put-on-call: if the bid succeeds and equity markets subsequently fall, the put-on-call pays out, hedging the M&A currency risk. In **real options**, a company cannot invest in a factory until it wins a government contract — the contract win is the outer trigger, the investment NPV is the inner option. The compound structure means premium is only spent when the outer gate is passed, making it more capital-efficient than buying the inner option outright before knowing whether the outer condition will be met.
