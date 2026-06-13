# Multi-Step TD Learning (TD(λ))

**Topic:** Machine Learning
**Tags:** td lambda, eligibility traces, multi-step returns, bias-variance, reinforcement learning, temporal difference
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**TD(λ)** interpolates between one-step TD learning ($\lambda = 0$) and full Monte Carlo returns ($\lambda = 1$) by forming a geometrically weighted average of $n$-step returns. The parameter $\lambda \in [0,1]$ controls the bias-variance trade-off: low $\lambda$ gives low variance but high bias (relies on potentially inaccurate bootstrap estimates); high $\lambda$ gives low bias but high variance (depends on long, noisy trajectories).

## Key Formula

The **$n$-step return** from time $t$:

$$G_t^{(n)} = \sum_{k=1}^{n} \gamma^{k-1} R_{t+k} + \gamma^n V(S_{t+n})$$

The **$\lambda$-return** is the geometric mixture:

$$G_t^\lambda = (1 - \lambda)\sum_{n=1}^{\infty} \lambda^{n-1}\,G_t^{(n)}$$

When $\lambda = 0$: $G_t^0 = R_{t+1} + \gamma V(S_{t+1})$ — pure TD(0) bootstrap.
When $\lambda = 1$: $G_t^1 = \sum_{k=1}^{T-t} \gamma^{k-1} R_{t+k}$ — pure Monte Carlo.

**Eligibility traces** provide an online implementation: $e_t(s) \leftarrow \gamma\lambda\,e_{t-1}(s) + \mathbf{1}[S_t = s]$, so each state's trace decays geometrically unless revisited.

## Example

Pricing a 30-day option using TDBP with different $\lambda$ values. Each "reward" is zero except at maturity where $R_T = \text{payoff}(S_T)$. With $\lambda = 0$ (pure TD): the day-29 network bootstraps from the day-30 payoff only — low variance but the day-28 network depends on how good day-29 is. With $\lambda = 0.9$: the day-27 network blends bootstraps from days 28–30 with partial path payoffs, improving accuracy when early time-step networks are still inaccurate. Setting $\lambda = 1$ recovers plain Monte Carlo pricing.

## Remember

TDBP uses $\lambda = 0$ implicitly — each time-step network is trained against only the immediately adjacent next-step network. Increasing $\lambda$ would allow earlier time-step networks to see longer-horizon payoff information, potentially speeding convergence for options with long maturities or complex path-dependent payoffs (barriers, Asians) where the one-step bootstrap is a poor proxy for the terminal payoff. The practical reason TDBP uses $\lambda = 0$ is architectural simplicity: the backward-induction structure trains one network at a time, making multi-step targets difficult to compute without running full trajectories — exactly the computational burden that TD learning was designed to avoid.
