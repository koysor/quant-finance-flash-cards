# Partially Observable MDP (POMDP)

**Topic:** Computational Finance
**Tags:** pomdp, belief state, hidden state, reinforcement learning, regime switching, observation model
**Created:** 2026-06-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **Partially Observable MDP (POMDP)** extends the standard MDP to settings where the agent cannot observe the full state $s_t$ directly, but instead receives an observation $o_t$ that is a noisy or incomplete signal of the hidden state. The agent maintains a **belief state** $b_t$ — a probability distribution over all possible hidden states — and updates it via Bayes' rule after each observation. Optimal POMDP policies are functions of the belief state rather than the true state.

## Key Formula

A POMDP is defined by the 7-tuple $(S, A, P, R, \Omega, O, \gamma)$ where $\Omega$ is the observation space and $O(o \mid s', a)$ is the observation model.

**Belief update** (after taking action $a$, observing $o$):

$$b'(s') = \frac{O(o \mid s', a)\,\sum_s P(s' \mid s, a)\,b(s)}{P(o \mid b, a)}$$

where the denominator $P(o \mid b, a) = \sum_{s'} O(o \mid s', a)\sum_s P(s' \mid s, a)\,b(s)$ normalises the distribution.

**Value function** over belief states (piecewise linear and convex for finite $S$):

$$V(b) = \max_{\alpha \in \Gamma} \sum_s \alpha(s)\,b(s)$$

where $\Gamma$ is a set of $\alpha$-vectors (linear value functions over states).

**Optimal action** at belief $b$:

$$\pi^*(b) = \arg\max_a \left[ \sum_s R(s,a)\,b(s) + \gamma \sum_o P(o \mid b,a)\,V(b'_{a,o}) \right]$$

## Example

**Hidden volatility regime trading:** Two hidden states $S = \{\text{low vol}, \text{high vol}\}$. The agent observes daily VIX changes $o_t$ (noisy) but not the true regime. Transition: $P(\text{high} \mid \text{low}) = 0.05$ (regime rarely switches), $P(\text{low} \mid \text{high}) = 0.15$ (high vol reverts faster).

Observation model: in low-vol regime, $|\Delta\text{VIX}| < 1$ with probability 0.80; in high-vol regime, with probability 0.35.

Starting belief $b_0 = (0.7, 0.3)$ (70% low vol). After observing $|\Delta\text{VIX}| = 2.1$:

$$b_1(\text{high vol}) = \frac{0.65 \times 0.3}{0.65 \times 0.3 + 0.20 \times 0.7} = \frac{0.195}{0.335} \approx 0.582$$

The agent updates to 58% high-vol probability and reduces its delta exposure accordingly — a Bayesian volatility regime filter implemented as a POMDP belief update.

## Remember

In finance, the **hidden state is almost always the market regime**: high/low volatility, trending/mean-reverting, risk-on/risk-off. A standard MDP assumes the agent knows the regime, which is unrealistic — traders must infer the regime from noisy price data. The POMDP framework makes this inference explicit via the belief state $b_t$, which is exactly the regime probability output of a **hidden Markov model (HMM)**. The key insight is that the POMDP belief update is identical to the HMM filter: both apply Bayes' rule using the transition matrix and the observation likelihood. In practice, POMDP solutions are computationally intractable for large state spaces, so practitioners approximate with particle filters (sequential Monte Carlo) or recurrent neural networks that maintain an implicit belief state in their hidden activations — the latter is how LSTM-based trading agents handle partial observability without explicitly solving the POMDP.
