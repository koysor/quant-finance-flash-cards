# Essential Supremum Notation

**Topic:** Mathematical Notation
**Tags:** notation, essential supremum, risk measures, almost sure, measure theory, var
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **essential supremum** of a random variable $X$, written $\operatorname{ess\,sup} X$ or $\operatorname{esssup} X$, is the smallest constant $c$ such that $P(X > c) = 0$ — the "almost-sure upper bound." It differs from the ordinary supremum $\sup X$ in that it ignores events of probability zero: if $X$ takes the value $10^6$ with probability zero, the essential supremum is unaffected while the ordinary supremum is $10^6$.

## Key Formula

$$\operatorname{ess\,sup} X = \inf\{\,c \in \mathbb{R} : P(X > c) = 0\,\}$$

Equivalently, $\operatorname{ess\,sup} X$ is the smallest $c$ such that $X \leq c$ **almost surely** ($P$-a.s.).

The dual concept, the **essential infimum**:

$$\operatorname{ess\,inf} X = \sup\{\,c \in \mathbb{R} : P(X < c) = 0\,\} = -\operatorname{ess\,sup}(-X)$$

**Value-at-Risk** expressed using essential infimum — the tightest loss level not exceeded with probability $1 - \alpha$:

$$\operatorname{VaR}_\alpha(L) = \operatorname{ess\,inf}\{\,l \in \mathbb{R} : P(L > l) \leq 1 - \alpha\,\}$$

This is the measure-theoretic definition that handles continuous and discrete loss distributions uniformly, without edge cases at discontinuities.

**Coherent risk measures** are defined via a worst-case expected loss:

$$\rho(X) = \operatorname{ess\,sup}_{Q \in \mathcal{Q}}\, E^Q[-X]$$

where $\mathcal{Q}$ is a set of "stress" probability measures — making coherent risk measures suprema over a family of scenarios.

## Example

A loss variable $L$ is 0 with probability 99%, exactly 50 with probability 0.9%, and exactly 1,000,000 with probability 0.1% (a tail scenario).

- **Ordinary supremum:** $\sup L = 1{,}000{,}000$
- **$\operatorname{ess\,sup} L$:** The smallest $c$ with $P(L > c) = 0$ is $1{,}000{,}000$ — here both agree because the tail event has positive probability.
- **$\operatorname{VaR}_{99\%}$** $= \operatorname{ess\,inf}\{l : P(L > l) \leq 0.01\} = 50$ — the loss level not exceeded with 99% probability.
- **$\operatorname{VaR}_{99.9\%}$** $= 1{,}000{,}000$ — the ess inf now hits the tail scenario.

If instead $L = 1{,}000{,}000$ on a single probability-zero set: $\operatorname{ess\,sup} L = 0$ but $\sup L = 1{,}000{,}000$ — they diverge.

## Remember

The essential supremum arises in finance wherever **probability-zero events must not distort a bound**. In coherent risk measure theory (Artzner et al. 1999), the axiom of **monotonicity** ($X \leq Y$ a.s. implies $\rho(X) \leq \rho(Y)$) and the dual representation as an ess sup over stress measures require the "almost sure" qualifier — a loss that occurs with probability zero should not drive the risk measure. Practically, this distinction matters in **regulatory VaR**: a loss model with a probability-zero spike at $10^{10}$ should not show an infinite 99.9% VaR. The ess inf formulation of VaR handles this cleanly. Whenever you see "a.s." (almost surely) or "P-a.s." in a bound, the essential supremum or infimum is the correct mathematical notion, not the ordinary sup/inf.
