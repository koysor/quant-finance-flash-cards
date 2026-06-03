# Digital Bond and Digital Share

**Topic:** Computational Finance
**Tags:** digital bond, digital share, option decomposition, call option, tdbp, risk-neutral pricing
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A European call option can be decomposed into two binary instruments: the **digital share** $D_S$, which pays the stock price $S_T$ if the option expires in the money (and zero otherwise), and the **digital bond** $D_B$, which pays £1 if the option expires in the money. TDBP models often predict these two components separately, improving training stability over direct payoff learning.

## Key Formula

$$C = D_S - K \cdot D_B$$

where $K$ is the strike, and under the risk-neutral measure $\mathbb{Q}$:

$$D_B = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}\!\left[\mathbf{1}_{\{S_T \ge K\}}\right], \qquad D_S = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}\!\left[S_T\,\mathbf{1}_{\{S_T \ge K\}}\right]$$

Under log-normal dynamics, $D_B = e^{-rT}N(d_2)$ and $D_S = S_0 N(d_1)$, recovering the Black-Scholes formula $C = S_0 N(d_1) - K e^{-rT} N(d_2)$.

## Example

An RL model predicts $D_B = 0.55$ (discounted probability of exercise) and $D_S = 62$ (discounted conditional expected stock value). The call price is $62 - 100 \times 0.55 = 7$. The delta is approximately $N(d_1) \approx D_S / S_0$, giving a direct interpretation of the hedge ratio from the decomposition outputs.

## Remember

Decomposing into digital bond and digital share separates two distinct learning tasks: the **probability of exercise** ($D_B$, monotone in $S$) and the **conditional expected value** ($D_S$, smooth in $S$). Neural networks learn these smoother targets more reliably than the kinked payoff $\max(S_T - K, 0)$ directly. The decomposition also makes Greeks natural outputs — the delta of the call equals $\partial D_S / \partial S_0 - K \cdot \partial D_B / \partial S_0$.
