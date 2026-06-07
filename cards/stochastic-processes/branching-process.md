# Branching Process

**Topic:** Stochastic Processes
**Tags:** branching process, galton-watson, extinction probability, offspring distribution, population dynamics
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **Galton–Watson branching process** is a discrete-time stochastic model in which each individual in generation $n$ independently produces a random number of offspring according to a common offspring distribution $p_k = P(Z = k)$. The population size $Z_n$ evolves from generation to generation, and the key question is whether the population survives indefinitely or eventually goes extinct. Branching processes appear in finance wherever a "success" event triggers further cascading events: credit contagion, order-book self-excitation, and bank run dynamics all share this branching structure.

## Key Formula

Let $Z_n$ be the population at generation $n$, with $Z_0 = 1$ (one ancestor). The offspring distribution has mean $\mu = E[Z]$ and generating function $G(s) = E[s^Z] = \sum_{k=0}^\infty p_k s^k$.

**Evolution equation:**

$$Z_{n+1} = \sum_{i=1}^{Z_n} X_i, \qquad X_i \overset{\text{i.i.d.}}{\sim} p_k$$

**Mean population:**

$$E[Z_n] = \mu^n$$

**Extinction probability** $q = P(\text{population eventually dies out})$ is the smallest non-negative root of:

$$q = G(q) \quad \Longleftrightarrow \quad q = \sum_{k=0}^\infty p_k\, q^k$$

**Criticality classification:**

| Regime | Condition | Long-run behaviour |
|---|---|---|
| Subcritical | $\mu < 1$ | Certain extinction ($q = 1$) |
| Critical | $\mu = 1$ | Certain extinction ($q = 1$) |
| Supercritical | $\mu > 1$ | Survives with probability $1 - q > 0$ |

## Example

A bank contagion model: each defaulting bank triggers defaults at $k$ other banks with probabilities $p_0 = 0.4$, $p_1 = 0.3$, $p_2 = 0.2$, $p_3 = 0.1$.

**Mean offspring:** $\mu = 0(0.4) + 1(0.3) + 2(0.2) + 3(0.1) = 1.0$ — critical regime.

**Generating function:** $G(s) = 0.4 + 0.3s + 0.2s^2 + 0.1s^3$

**Extinction probability:** solve $q = G(q)$ → $q = 1$ (critical process, certain extinction eventually, but expected cascade size is infinite: $E[Z_n] = 1^n = 1$ for all $n$, yet extinction is sure).

Increasing contagion to $\mu = 1.2$ (supercritical) by shifting weight to $p_2$ and $p_3$: $G(q) = q$ has a root at $q \approx 0.62$, so a contagion cascade survives indefinitely with probability $\approx 38\%$.

## Remember

The branching process extinction criterion — survive if and only if $\mu > 1$ — is exactly the **Hawkes process stationarity condition** $n^* = \alpha/\beta < 1$. In a Hawkes process, each event triggers on average $n^*$ offspring events; if $n^* > 1$ the process is supercritical and event rates explode to infinity (a model for flash crashes). The branching process framework also underlies **network contagion models** in systemic risk: each failing counterparty "infects" others with mean $\mu$ failures, and regulators use the extinction condition $\mu < 1$ as the criterion for a cascade to be self-limiting rather than systemic. The key insight is that criticality ($\mu = 1$) is deceptive — extinction is certain, but the *expected* time to extinction is infinite, meaning the system lingers near collapse for very long periods.
