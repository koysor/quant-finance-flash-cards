# Knightian Uncertainty

**Topic:** Risk
**Tags:** knightian uncertainty, model uncertainty, ambiguity, risk, robust portfolio, tail risk
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Knightian uncertainty** (also called **ambiguity** or **deep uncertainty**) is the condition where probabilities themselves cannot be reliably assigned to outcomes — as distinct from risk, where probabilities are known or estimable. Introduced by Frank Knight in *Risk, Uncertainty and Profit* (1921).

## Key Formula

In robust decision theory, an agent facing Knightian uncertainty maximises utility under the worst-case probability measure from an ambiguity set $\mathcal{P}$:

$$\max_{\mathbf{w}} \min_{P \in \mathcal{P}} \mathbb{E}_P[U(\mathbf{w}^\top \mathbf{r})]$$

The ambiguity set $\mathcal{P}$ is typically a ball of probability measures within a given statistical distance (e.g. KL divergence) of a reference model.

## Example

A portfolio manager is asked to optimise weights using expected returns estimated from 5 years of data. For most stocks, standard errors on the mean return are larger than the mean return itself — meaning the true expected return could plausibly be positive or negative. This is Knightian uncertainty: not just noisy estimates (risk), but fundamental ignorance of the return distribution. A robust portfolio responds by diversifying aggressively across assets and strategies, reducing sensitivity to any single model's output.

## Remember

The Knight risk/uncertainty distinction maps directly onto two types of financial loss that require different responses. **Risk** (known probabilities) is managed with standard VaR, CVaR, and hedging. **Knightian uncertainty** (unknown probabilities) demands robustness: diversification that does not depend on precise return estimates, stress tests that do not assume a specific probability distribution, and portfolio construction methods (such as maximum diversification or risk parity) that are relatively insensitive to return forecasts. The 2008 crisis is the canonical case — models priced CDO tranches with high confidence, but the true probability of correlated mortgage defaults was Knightian: the historical data simply did not exist.
