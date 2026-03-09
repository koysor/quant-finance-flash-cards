# Snell Envelope

**Topic:** Derivatives
**Tags:** american option, optimal stopping, supermartingale, early exercise, backward induction
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **Snell envelope** of a process $Z_t$ is the smallest supermartingale that dominates $Z_t$ at every time $t$. In American option pricing, $Z_t = e^{-rt}\,\text{payoff}(S_t)$ is the discounted intrinsic value, and the Snell envelope gives the fair price of the American option at every point in time. The optimal exercise time is the first moment the Snell envelope touches the payoff process.

## Key Formula

The Snell envelope $U_t$ is constructed by **backward induction**:

$$U_T = Z_T$$

$$U_t = \max\!\left(Z_t,\; E^{\mathbb{Q}}[U_{t+1} \mid \mathcal{F}_t]\right) \qquad t = T-1, T-2, \ldots, 0$$

At each step: compare the immediate exercise value $Z_t$ with the continuation value $E^{\mathbb{Q}}[U_{t+1} \mid \mathcal{F}_t]$, and take the larger.

The **optimal stopping time** is:

$$\tau^* = \inf\{t \geq 0 : U_t = Z_t\}$$

The American option price is $V_0 = U_0 = \sup_\tau E^{\mathbb{Q}}[Z_\tau]$.

## Example

A two-step binomial tree for an American put with $S_0 = £100$, $K = £105$, $u = 1.10$, $d = 0.90$, $r = 2\%$ per step.

Stock prices: $S_{uu} = 121$, $S_{ud} = 99$, $S_{dd} = 81$. Risk-neutral probability: $p = (1.02 - 0.90)/(1.10 - 0.90) = 0.60$.

**At $T = 2$:** $Z_{uu} = 0$, $Z_{ud} = 6$, $Z_{dd} = 24$.

**At $t = 1$:**
- Up node ($S = 110$): continuation $= (0.60 \times 0 + 0.40 \times 6)/1.02 = 2.35$; exercise $= \max(105 - 110, 0) = 0$. $U = 2.35$.
- Down node ($S = 90$): continuation $= (0.60 \times 6 + 0.40 \times 24)/1.02 = 12.94$; exercise $= 15$. $U = \mathbf{15}$ (exercise early).

**At $t = 0$:** continuation $= (0.60 \times 2.35 + 0.40 \times 15)/1.02 = 7.26$; exercise $= 5$. $U_0 = \mathbf{£7.26}$.

Optimal strategy: exercise early at the down node at $t = 1$ (where exercise value 15 > continuation value 12.94).

## Remember

The Snell envelope is the mathematical engine behind American option pricing on every trading desk. Backward induction through a binomial tree — comparing exercise value with continuation value at each node — is precisely the construction of the Snell envelope. In continuous time, the American option price is the value of the Snell envelope at time zero, and the **optimal exercise boundary** is the surface where it touches the intrinsic value. For Monte Carlo pricing of American options, algorithms like Longstaff–Schwartz approximate the Snell envelope by regressing continuation values on basis functions of the state variables. The supermartingale property of the Snell envelope has a financial interpretation: the American option price can only decrease in expected discounted terms because the option to exercise early is being consumed as time passes.
