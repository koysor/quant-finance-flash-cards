# Ambiguity Aversion (Ellsberg Paradox)

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** ambiguity aversion, ellsberg paradox, knightian uncertainty, behavioural finance, equity risk premium, robust portfolio
**Created:** 2026-04-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Ambiguity aversion** is the preference for known risks over unknown risks, even when the expected values are identical. The **Ellsberg paradox** (1961) demonstrates this: most people prefer to bet on an urn with a known 50/50 composition over one with an unknown composition, violating expected utility theory, which predicts indifference.

## Key Formula

In the maxmin expected utility framework (Gilboa–Schmeidler), an ambiguity-averse agent maximises utility under the worst-case probability measure from an ambiguity set $\mathcal{P}$:

$$\max_{\mathbf{w}}\; \min_{P \in \mathcal{P}}\; \mathbb{E}_P[U(\mathbf{w}^\top \mathbf{r})]$$

The agent acts as if nature picks the worst distribution within the plausible set.

## Example

A sovereign wealth fund considering an allocation to emerging market equities knows the historical mean return is 8% and volatility is 25%. However, the return distribution is itself uncertain — political risk, currency regime change, and thin liquidity make the true distribution unknown. Ambiguity aversion causes the fund to underweight EM equities relative to the mean-variance efficient weight, demanding an **ambiguity premium** on top of the standard risk premium.

## Remember

Ambiguity aversion provides a behavioural explanation for several puzzles in asset pricing that rational expected utility cannot explain. The **equity risk premium puzzle** — why historical equity returns are so much higher than theory predicts — is partly attributable to investors demanding compensation for Knightian uncertainty about the true equity return distribution, not just for measurable volatility. Similarly, the **home bias** (investors overweighting domestic equities) reflects lower ambiguity about familiar markets. Robust portfolio construction explicitly models ambiguity aversion by solving the maxmin problem, producing more diversified allocations than mean-variance optimisation.
