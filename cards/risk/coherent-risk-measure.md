# Coherent Risk Measure

**Topic:** Risk
**Level:** A Level Mathematics
**Tags:** risk, coherent, subadditivity, expected shortfall, risk measure, regulation
**Created:** 2026-02-28
**Author:** Claude Opus 4.6

---

## Definition

A **coherent risk measure** is a function $\rho$ that maps a portfolio's loss distribution to a single number, satisfying four axioms that ensure the measure behaves sensibly for risk management. The axioms were introduced by Artzner, Delbaen, Eber, and Heath (1999) and are now a cornerstone of modern risk theory.

## Key Formula

A risk measure $\rho$ is coherent if it satisfies all four axioms for any loss random variables $X$ and $Y$:

$$\text{1. Subadditivity: } \rho(X + Y) \leq \rho(X) + \rho(Y)$$

$$\text{2. Positive homogeneity: } \rho(\lambda X) = \lambda \, \rho(X) \quad \text{for } \lambda > 0$$

$$\text{3. Monotonicity: if } X \leq Y \text{ then } \rho(X) \leq \rho(Y)$$

$$\text{4. Translation invariance: } \rho(X + c) = \rho(X) + c \quad \text{for constant } c$$

## Example

Two trading desks each have a standalone 95% VaR of £10 million. Their combined portfolio has 95% VaR of £22 million because, on the worst days, their losses happen to coincide.

**Subadditivity check:**

VaR: $\rho(A + B) = 22 > 10 + 10 = 20$ — **violates** subadditivity. VaR is not coherent.

Expected Shortfall (ES): if the standalone ES of each desk is £12 million and the combined ES is £21 million, then $\rho(A + B) = 21 \leq 12 + 12 = 24$ — **satisfies** subadditivity. ES is coherent.

## Remember

VaR fails subadditivity, meaning that merging two portfolios can appear riskier than holding them separately — this penalises diversification, which is economically nonsensical. **Expected Shortfall** (also called CVaR) is the standard coherent alternative and has replaced VaR as the primary risk measure in the Basel III Fundamental Review of the Trading Book (FRTB). When a regulator or risk committee asks for a "coherent" number, they are asking for ES, not VaR.
