# Tower Property

**Topic:** Stochastic Processes
**Tags:** conditional expectation, martingale, iterated expectations, filtration, measure theory
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **tower property** (law of iterated expectations) states that nesting conditional expectations collapses to the outermost (coarsest) conditioning. If $\mathcal{F}_s \subseteq \mathcal{F}_t$ (i.e. $s \leq t$), then conditioning on the finer information $\mathcal{F}_t$ first and then on the coarser $\mathcal{F}_s$ yields the same result as conditioning on $\mathcal{F}_s$ directly.

## Key Formula

$$E\!\big[E[X \mid \mathcal{F}_t] \mid \mathcal{F}_s\big] = E[X \mid \mathcal{F}_s], \qquad s \leq t$$

As a special case, setting $s = 0$ so that $\mathcal{F}_0$ is trivial:

$$E\!\big[E[X \mid \mathcal{F}_t]\big] = E[X]$$

## Example

A stock price $S_t$ follows geometric Brownian motion. A trader wants $E[S_2 \mid \mathcal{F}_0]$.

Using the tower property through an intermediate time:

$$E[S_2 \mid \mathcal{F}_0] = E\!\big[E[S_2 \mid \mathcal{F}_1] \mid \mathcal{F}_0\big]$$

Under the risk-neutral measure, $E^{\mathbb{Q}}[S_2 \mid \mathcal{F}_1] = S_1 e^{r}$, so:

$$E^{\mathbb{Q}}[S_2 \mid \mathcal{F}_0] = E^{\mathbb{Q}}[S_1 e^{r} \mid \mathcal{F}_0] = e^{r} \cdot E^{\mathbb{Q}}[S_1 \mid \mathcal{F}_0] = e^{r} \cdot S_0 e^{r} = S_0 e^{2r}$$

The two one-step expectations compose consistently into one two-step expectation.

## Remember

The tower property is why martingale-based pricing works across arbitrary time horizons. It guarantees that multi-step discounted expectations are self-consistent: pricing a derivative to maturity $T$ by first pricing to an intermediate date $t$ and then from $t$ to $T$ gives the same answer as pricing directly to $T$. This consistency underpins backward induction in binomial trees, the recursive structure of American option pricing, and the fundamental theorem that connects no-arbitrage to the existence of a martingale measure.
