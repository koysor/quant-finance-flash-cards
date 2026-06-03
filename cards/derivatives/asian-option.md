# Asian Option

**Topic:** Derivatives
**Tags:** asian option, arithmetic average, path-dependent, exotic option, commodity, state augmentation
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

An **Asian option** has a payoff that depends on the average of the underlying price over the option's life rather than its terminal value. The **arithmetic average** form is the most common in practice (energy, FX, equity) because it reduces the impact of spot manipulation near expiry. The averaging makes the payoff path-dependent: two price paths ending at the same spot can yield different payoffs depending on the path taken.

## Key Formula

**Arithmetic average call** (fixed strike):

$$C_\text{Asian} = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}\!\left[\max\!\left(\frac{1}{N}\sum_{i=1}^{N} S_{t_i} - K,\; 0\right)\right]$$

No closed-form solution exists for the arithmetic average because the sum of log-normal random variables is not log-normal. The **geometric average** is the tractable alternative (Kemna-Vorst, 1990):

$$C_\text{Geo} = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}\!\left[\max\!\left(\left(\prod_{i=1}^{N} S_{t_i}\right)^{1/N} - K,\; 0\right)\right]$$

which does admit a closed form and serves as a **control variate** for Monte Carlo pricing of the arithmetic version.

## Example

A 6-month Asian call on Brent crude, monthly averaging ($N = 6$), strike $K = \$80$. Path A: prices $\{85, 90, 88, 92, 86, 89\}$, average = \$88.33, payoff = \$8.33. Path B: same endpoint $S_{T} = 89$ but prices $\{79, 78, 77, 80, 84, 89\}$, average = \$81.17, payoff = \$1.17. Both paths end at \$89 but the Asian payoffs differ by \$7.16 — a vanilla call would price them identically.

## Remember

Asian options are cheaper than vanilla options for the same strike because averaging reduces the effective volatility of the payoff — a single bad day near expiry cannot crater the payout. For RL pricing, the running average $\bar{S}_t = \frac{1}{n}\sum_{k=1}^{n} S_{t_k}$ must be included as a state variable to restore the Markov property: the correct state is $(S_t, \bar{S}_t, \tau)$ rather than $(S_t, \tau)$ alone. The geometric Asian option serves a dual purpose in RL — as a closed-form benchmark for validating the RL pricer on a related instrument, and as a control variate in the Monte Carlo training paths that reduces the variance of the Bellman residual estimate.
