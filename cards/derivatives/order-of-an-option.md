# Order of an Option

**Topic:** Derivatives
**Tags:** compound option, order, call on call, geske formula, bivariate normal, exotic options
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **order** of an option is the number of layers of contingency in its payoff. A standard call or put is a **first-order** option; a **compound option** — an option whose underlying is itself an option — is **second-order**; an option on a compound option is **third-order**. Each additional order introduces a new critical asset price and replaces the univariate normal distribution $N(\cdot)$ in the pricing formula with the next-higher multivariate normal.

## Key Formula

A **call-on-call** (second-order) with outer strike $X$, outer expiry $T_1$, inner call strike $K$, inner expiry $T_2 > T_1$ is priced by the **Geske (1979) formula**:

$$C_{\text{CoC}} = S_0\, N_2(a_1,\, b_1;\, \sqrt{T_1/T_2}) - Ke^{-rT_2}\, N_2(a_2,\, b_2;\, \sqrt{T_1/T_2}) - Xe^{-rT_1}\, N(a_2)$$

where $N_2(\cdot,\cdot;\rho)$ is the bivariate normal CDF, $\rho = \sqrt{T_1/T_2}$, and $a_i$, $b_i$ are Black–Scholes $d_1$, $d_2$ arguments evaluated at the critical stock price $S^*$ satisfying $C_{\text{BS}}(S^*, K, T_2-T_1) = X$.

## Example

A company's stock trades at $S_0 = 100$. An investor buys a call on a call: inner call ($K = 100$, $T_2 = 1$ year), outer call ($X = 8$, $T_1 = 3$ months). At $T_1 = 0.25$: if $S_{T_1} = 115$, the inner call is worth about $\$18$ (in-the-money), so the outer call pays $18 - 8 = \$10$. If $S_{T_1} = 95$, the inner call is worth about $\$5 < \$8$, so the outer call expires worthless — the investor loses only the compound option premium, not the full vanilla call premium.

## Remember

The order of an option has practical relevance far beyond exotic derivatives desks. In the **Merton structural model**, equity is a first-order call on the firm's assets; a convertible bond embeds an option to convert into equity, making it effectively second-order. In **real options analysis**, a multi-stage investment project (invest now to gain the right to invest further later) has order equal to the number of sequential decision gates — each gate is an outer option on the value of exercising all subsequent gates. Higher-order options are cheaper than vanilla calls at the same moneyness because the outer option only pays when both the outer and inner exercise conditions are met simultaneously, reducing the probability of payoff.
