# Stochastic Integral Notation

**Topic:** Mathematical Notation
**Tags:** stochastic integral, Itô integral, Stratonovich, adapted process, Brownian motion
**Created:** 2026-03-09
**Author:** Claude Sonnet 4.6

---

## Definition

The **Itô stochastic integral** $\int_0^t H_s \, dW_s$ accumulates the gains from a trading strategy $H_s$ driven by a Brownian motion $W_s$. It differs from the ordinary Riemann integral because $W_s$ has infinite variation — it cannot be defined path-by-path and requires $H_s$ to be **adapted** (non-anticipating).

| Symbol | Read as | Meaning |
|---|---|---|
| $\int_0^t H_s \, dW_s$ | "integral of H dW" | Itô integral — gains from holding $H_s$ units over Brownian increments |
| $\int_0^t H_s \, dS_s$ | "integral of H dS" | Gains process from holding $H_s$ units of asset $S$ |
| $H_s \in \mathcal{F}_s$ | "H adapted" | $H_s$ depends only on information available at $s$, not the future |
| $\int_0^t H_s \circ dW_s$ | "Stratonovich integral" | Alternative convention; satisfies ordinary chain rule but is anticipating |
| $[W, W]_t = t$ | "quadratic variation of W" | The key property distinguishing stochastic from ordinary calculus |

## Key Formula

The **Itô isometry** (expected squared gain equals expected squared position):

$$E\!\left[\left(\int_0^t H_s \, dW_s\right)^{\!2}\right] = E\!\left[\int_0^t H_s^2 \, ds\right]$$

Relationship between Itô ($\int H \, dW$) and Stratonovich ($\int H \circ dW$):

$$\int_0^t H_s \circ dW_s = \int_0^t H_s \, dW_s + \tfrac{1}{2}[H, W]_t$$

## Example

A trader holds $\Delta_t$ shares of a stock driven by $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$. The cumulative profit and loss (P&L) from time 0 to $T$ is:

$$\text{P\&L} = \int_0^T \Delta_t \, dS_t$$

With $\Delta_t = 0.5$ (constant half-share position) and $\sigma = 0.2$, the P&L variance over one year is $0.5^2 \times 0.04 \times S_0^2 \times 1 = 0.01 S_0^2$ by the Itô isometry. The P&L is itself a stochastic integral — an Itô integral because $\Delta_t$ must be determined from current prices, not tomorrow's.

## Remember

The requirement that $H_s$ be **adapted** is the mathematical statement that a hedging strategy cannot use future price information. In the Black-Scholes delta-hedging argument, the replicating portfolio $\int_0^t \Delta_s \, dS_s$ is an Itô integral precisely because $\Delta_s$ depends only on $S_s$ (the current price), not on $S_T$ (the future payoff). The Itô convention — not Stratonovich — is standard in finance because it preserves the martingale (no-arbitrage) property of price processes.
