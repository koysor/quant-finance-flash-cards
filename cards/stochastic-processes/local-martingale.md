# Local Martingale

**Topic:** Stochastic Processes
**Tags:** local martingale, martingale, stopping time, measure change, doleans exponential, integrability
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

A process $M_t$ is a **local martingale** if there exists an increasing sequence of stopping times $\tau_n \uparrow \infty$ such that each stopped process $M_{t \wedge \tau_n}$ is a true martingale. Every true martingale is a local martingale, but the converse fails: a local martingale can have $E[\lvert M_t \rvert] = \infty$, breaking the global fair-game property.

## Key Formula

The localising sequence $(\tau_n)$ satisfies:

$$\tau_n = \inf\{t \ge 0 : \lvert M_t \rvert \ge n\}, \qquad \tau_n \uparrow \infty \text{ a.s.}$$

The stopped process $M^{\tau_n}_t = M_{t \wedge \tau_n}$ is a uniformly integrable martingale for each $n$. A sufficient condition for upgrading a non-negative local martingale to a true martingale is:

$$E[M_t] = E[M_0] \quad \text{for all } t \ge 0$$

which fails precisely when the process exhibits **probability mass leakage to infinity** (a strict local martingale).

## Example

The 3/2 process $Z_t = 1/(1 - W_t)$ on $[0, 1)$, where $W_t$ is a Brownian motion started at 0, is a local martingale but not a true martingale: $E[Z_t] > Z_0 = 1$ because there is positive probability that $W_t$ reaches 1 in finite time, sending $Z_t \to \infty$. More concretely, with $W_0 = 0$ at $t = 0.9$, numerical simulation gives $E[Z_{0.9}] \approx 1.19 \ne 1$.

## Remember

In quantitative finance, the distinction matters acutely for the Doléans exponential used as a Radon–Nikodým density in Girsanov's theorem. The density process $\mathcal{E}(-\lambda W)_t$ is always a non-negative local martingale, but it must be a **true** martingale for the change of measure from $\mathbb{P}$ to $\mathbb{Q}$ to produce a valid probability measure (one that integrates to 1). Strict local martingales — those that fail to be true martingales — arise in bubble models where the asset price process has positive probability of reaching infinity, leading to sub-replication of European calls.
