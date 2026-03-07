# Equivalent Probability Measures

**Topic:** Stochastic Processes
**Tags:** measure theory, risk-neutral, absolute continuity, no-arbitrage, probability
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Two probability measures $\mathbb{P}$ and $\mathbb{Q}$ on the same sample space are **equivalent** (written $\mathbb{P} \sim \mathbb{Q}$) if they agree on which events are possible and which are impossible, even though they may assign different probabilities. Formally, $\mathbb{P}(A) = 0 \Leftrightarrow \mathbb{Q}(A) = 0$ for all events $A$.

## Key Formula

**Absolute continuity:** $\mathbb{Q} \ll \mathbb{P}$ means $\mathbb{P}(A) = 0 \implies \mathbb{Q}(A) = 0$.

**Equivalence:** $\mathbb{P} \sim \mathbb{Q}$ means $\mathbb{Q} \ll \mathbb{P}$ and $\mathbb{P} \ll \mathbb{Q}$.

Expectations convert between measures via the Radon–Nikodým derivative $\Lambda$:

$$E^{\mathbb{Q}}[Y] = E^{\mathbb{P}}[\Lambda \cdot Y], \qquad \Lambda = \frac{d\mathbb{Q}}{d\mathbb{P}}$$

## Example

Consider a stock that can go up to £120 or down to £80 from £100. Under $\mathbb{P}$: $P(\text{up}) = 0.6$, $P(\text{down}) = 0.4$. Under $\mathbb{Q}$: $Q(\text{up}) = 0.5$, $Q(\text{down}) = 0.5$.

Both measures assign non-zero probability to both outcomes, so $\mathbb{P} \sim \mathbb{Q}$. The Radon–Nikodým derivative is $\Lambda(\text{up}) = 0.5/0.6 = 5/6$ and $\Lambda(\text{down}) = 0.5/0.4 = 5/4$.

## Remember

The equivalence of the physical measure $\mathbb{P}$ and the risk-neutral measure $\mathbb{Q}$ is the mathematical expression of no-arbitrage. If the measures were not equivalent, some event possible under $\mathbb{P}$ would be impossible under $\mathbb{Q}$ (or vice versa), creating an arbitrage opportunity — a trade that is costless but has a positive probability of profit. The First Fundamental Theorem of Asset Pricing formalises this: a market is arbitrage-free if and only if there exists an equivalent martingale measure $\mathbb{Q}$ under which discounted prices are martingales.
