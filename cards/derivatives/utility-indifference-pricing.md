# Utility Indifference Pricing

**Topic:** Derivatives
**Tags:** incomplete markets, utility theory, indifference price, risk aversion, exponential utility
**Created:** 2026-06-03
**Author:** Gemini CLI

---

## Definition

**Utility Indifference Pricing** is a framework for valuing financial claims in **incomplete markets**, where perfect replication (hedging) is impossible. The indifference price $p_0$ is the amount of money that leaves an investor equally happy (in terms of expected utility) whether they sell the claim and hedge it optimally, or do nothing. It represents the minimum compensation a risk-averse agent requires to take on the risk of an unhedgeable claim.

## Key Formula

For an agent with utility function $U(x)$, the indifference price $p_0$ of a claim $Z$ is the value that satisfies:

$$\sup_{\delta} \mathbb{E}[U(\Pi_T(0, 0, \delta))] = \sup_{\delta} \mathbb{E}[U(\Pi_T(Z, p_0, \delta))]$$

where $\Pi_T$ is the terminal wealth of a portfolio with hedge $\delta$. For an **exponential utility** $U(x) = -\frac{1}{\lambda} e^{-\lambda x}$ with risk aversion $\lambda$:

$$p_0 = \frac{1}{\lambda} \log \frac{\mathbb{E}[e^{\lambda Z^*}]}{\mathbb{E}[e^{\lambda \Pi^*}]}$$

In complete markets, $p_0$ collapses to the standard risk-neutral price, regardless of the utility function $U$.

## Example

A bank wants to price a bespoke insurance derivative against a "flash crash" in an illiquid emerging market index. Because the index is illiquid, the bank cannot perfectly delta-hedge. Using a risk aversion $\lambda = 0.1$, the bank calculates that the expected loss and volatility of the unhedged residual risk require a "risk premium" of £5M over the expected payoff. The utility indifference price is thus £55M, whereas a naive risk-neutral model (ignoring incompleteness) might have suggested £50M.

## Remember

Utility indifference pricing is the "gold standard" for pricing in **incomplete markets**—those with transaction costs, liquidity gaps, or non-tradable risk factors. It replaces the "no-arbitrage" requirement of complete markets with a "no-utility-loss" requirement. In modern quantitative finance, it is the theoretical foundation for **Deep Hedging**, where neural networks are trained to find the hedge $\delta$ that achieves this utility equilibrium.
