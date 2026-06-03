# Lookback Option

**Topic:** Derivatives
**Tags:** lookback option, path-dependent, running maximum, running minimum, exotic option, state augmentation
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

A **lookback option** has a payoff that depends on the extremum of the underlying price over the option's life. A **floating-strike lookback call** pays $S_T - \min_{u \le T} S_u$ (buy at the lowest price in hindsight); a **fixed-strike lookback call** pays $\max(\max_{u \le T} S_u - K, 0)$ (profit from the highest price reached). They are the most path-dependent vanilla-style instruments and the natural stress test for RL state design.

## Key Formula

For a **fixed-strike lookback call** under GBM, the closed-form price involves the running maximum $M_T = \max_{u \le T} S_u$:

$$C_\text{LB} = S_0\,N(d_1) - Ke^{-rT}N(d_2) + S_0 e^{-rT}\frac{\sigma^2}{2r}\!\left[N(d_1) - e^{rT}\!\left(\frac{S_0}{K}\right)^{-2r/\sigma^2}\!N(d_3)\right]$$

For RL pricing, the running maximum $M_t = \max_{u \le t} S_u$ must be tracked as a state variable. The Markov-sufficient state is:

$$s_t = (S_t,\; M_t,\; \tau) \quad \text{(lookback call)} \qquad \text{or} \qquad s_t = (S_t,\; m_t,\; \tau) \quad \text{(lookback put)}$$

where $m_t = \min_{u \le t} S_u$.

## Example

A 3-month floating-strike lookback call with $S_0 = 100$, $\sigma = 20\%$, $r = 5\%$. At day 45, $S_{45} = 95$ and $m_{45} = 91$ (running minimum so far). The RL agent with state $(95, 91, 0.58\,\text{yr})$ estimates the remaining option value accounting for the locked-in floor of 91. If the price later rises to 110, the payoff is $110 - 91 = 19$; if it falls back to 92 and then recovers to 98, the payoff is $98 - 91 = 7$. A vanilla call with strike 91 prices differently in each scenario — only the lookback correctly values the path history.

## Remember

Lookback options are the definitive test of whether an RL pricer correctly augments its state: an agent with state $(S_t, \tau)$ only will systematically underprice floating-strike lookbacks because it cannot distinguish a stock at 95 that bottomed at 91 from one that bottomed at 75 — the two have very different remaining option values. Adding the running extremum as a state variable increases the TDBP input dimension by one, which is the entire cost of handling this extreme path dependence. This illustrates the RL pricing paradigm's key advantage over PDE methods: the PDE for a 2D state space $(S, M)$ requires a 2D grid with absorbing boundary conditions at the diagonal, while TDBP simply adds one more neuron to the input layer.
