# Martingales

**Topic:** Stochastic Processes
**Level:** A Level Mathematics
**Tags:** martingale, conditional expectation, fair game, risk-neutral, no-arbitrage
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

A **martingale** is a stochastic process whose conditional expected future value, given all information available now, equals its current value. Informally, a martingale is a "fair game" — on average, you neither win nor lose from this point forward.

A process $M_t$ is a martingale with respect to a filtration $\{\mathcal{F}_t\}$ if for every $s < t$:

$$\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$$

## Key Formula

The defining property in discrete time: if $M_0, M_1, M_2, \ldots$ is a martingale, then

$$\mathbb{E}[M_{n+1} \mid M_0, M_1, \ldots, M_n] = M_n$$

Equivalently, the expected change is zero:

$$\mathbb{E}[M_{n+1} - M_n \mid \mathcal{F}_n] = 0$$

Standard Brownian motion $W_t$ is the most important continuous-time martingale:

$$\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s \quad \text{for } s < t$$

## Example

A fair coin is flipped repeatedly. You win £1 for heads and lose £1 for tails. Starting with £10, your wealth after $n$ flips is $M_n$.

After 3 flips you have £11. What is your expected wealth after 5 flips?

$$\mathbb{E}[M_5 \mid M_3 = 11] = 11$$

No matter how many more flips remain, your expected future wealth equals your current wealth — this is the martingale property.

## Remember

In quantitative finance, the martingale concept is the theoretical backbone of **risk-neutral pricing**. Under the risk-neutral measure $\mathbb{Q}$, the discounted price of any traded asset is a martingale: $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T \mid \mathcal{F}_0] = S_0$. This single property — that discounted prices are fair games under $\mathbb{Q}$ — is what guarantees no-arbitrage and allows every derivative to be priced as a discounted expected payoff.
