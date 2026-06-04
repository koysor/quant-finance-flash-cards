# Utility Indifference Pricing

**Topic:** Derivatives
**Tags:** utility indifference, incomplete markets, risk aversion, exponential utility, reservation price
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Utility indifference pricing** (also called reservation pricing) values a derivative in an incomplete market by finding the price $p$ at which an agent is indifferent between (a) trading optimally without the derivative, and (b) selling the derivative at price $p$ and then trading optimally with the resulting position. It is the subjective price at which selling the derivative neither improves nor worsens the agent's expected utility.

## Key Formula

For an agent with exponential utility $U(W) = -e^{-\gamma W}$ (risk aversion $\gamma > 0$), the indifference price $p$ of a claim $H$ satisfies:

$$V(w) = V^H(w + p)$$

where $V(w) = \sup_\pi \mathbb{E}[-e^{-\gamma W_T^\pi}]$ is the value function without the claim, and $V^H(w+p) = \sup_\pi \mathbb{E}[-e^{-\gamma(W_T^\pi - H)}]$ is the value function after selling $H$ for $p$.

This yields the **indifference price**:

$$p = \frac{1}{\gamma}\left[\inf_{\mathbb{Q}}\left(\mathbb{E}^{\mathbb{Q}}[H] + \frac{1}{\gamma} H(\mathbb{Q} \| \mathbb{P})\right) - \inf_{\mathbb{Q}} \frac{1}{\gamma} H(\mathbb{Q} \| \mathbb{P})\right]$$

where the infimum is over equivalent martingale measures $\mathbb{Q}$, and $H(\mathbb{Q} \| \mathbb{P})$ is the relative entropy of $\mathbb{Q}$ with respect to the physical measure $\mathbb{P}$. As $\gamma \to 0$ (risk-neutral limit), $p \to \mathbb{E}^{\mathbb{Q}^*}[H]$ — the standard risk-neutral price under the minimal entropy martingale measure.

## Example

A natural gas producer holds unhedgeable weather risk and sells a temperature-indexed weather call option paying $\max(T_{\text{avg}} - 20, 0) \times \text{\textsterling}1{,}000$ per degree. Standard risk-neutral pricing fails — temperature is not a traded asset, so the market is incomplete. With risk aversion $\gamma = 0.01$ and the distribution of $T_{\text{avg}}$ estimated from historical data, the utility indifference price is \$3{,}200, reflecting both the expected payoff and a risk premium for the unhedgeable residual exposure. A risk-neutral model using an arbitrary pricing measure might give \$2{,}500 — the difference is the agent's personal risk premium, and it shrinks as $\gamma \to 0$.

## Remember

Utility indifference pricing is the theoretically correct approach to valuation in **incomplete markets** — markets where the underlying risk cannot be fully replicated by traded assets. This covers weather and catastrophe derivatives, executive stock options (employees cannot short their own company), insurance liabilities, and credit derivatives with jump-to-default risk. In contrast to Black-Scholes (which assumes a complete market with perfect replication), indifference prices depend on the agent's risk aversion $\gamma$: as $\gamma \to 0$ the agent becomes risk neutral and the indifference price converges to the standard risk-neutral expectation. This makes utility indifference pricing the theoretical bridge between subjective personal valuation and objective market pricing.
