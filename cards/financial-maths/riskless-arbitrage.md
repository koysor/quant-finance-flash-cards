# Riskless Arbitrage

**Topic:** Financial Mathematics
**Tags:** arbitrage, no-arbitrage, risk-free profit, law of one price, mispricing
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A **riskless arbitrage** is a self-financing trading strategy that requires zero net investment, has no possibility of loss in any state of the world, and has a strictly positive probability of profit. It exploits a mispricing between related instruments: if two portfolios have identical future payoffs but different current prices, buying the cheaper and selling the dearer locks in a guaranteed profit.

## Key Formula

If portfolio $A$ and portfolio $B$ have identical payoffs at time $T$ in every state, then to prevent arbitrage:

$$V_A(0) = V_B(0)$$

This is the **law of one price**. A violation creates a riskless arbitrage with profit:

$$\pi = |V_A(0) - V_B(0)| \cdot e^{rT}$$

**Cash-and-carry arbitrage** for a forward contract: the forward price must satisfy

$$F_0 = S_0\,e^{rT}$$

If $F_0 > S_0\,e^{rT}$: borrow $S_0$, buy the asset, sell the forward — profit $= F_0 - S_0\,e^{rT}$.

If $F_0 < S_0\,e^{rT}$: short the asset, invest $S_0$, buy the forward — profit $= S_0\,e^{rT} - F_0$.

## Example

Gold trades at $S_0 = \text{£}1{,}800$ per ounce and the 1-year risk-free rate is $r = 5\%$. The fair forward price is:

$$F_0 = 1{,}800 \times e^{0.05} = 1{,}800 \times 1.05127 = \text{£}1{,}892.29$$

A dealer quotes a 1-year gold forward at £1,920. To arbitrage:

1. Borrow £1,800 at 5%
2. Buy 1 oz of gold at £1,800
3. Enter a forward to sell at £1,920

At expiry: deliver the gold, receive £1,920, repay £1,892.29. Riskless profit = **£27.71** per ounce.

## Remember

Riskless arbitrage is the enforcement mechanism behind every pricing relationship in quantitative finance. The forward pricing formula $F = Se^{rT}$, put–call parity $C - P = S - Ke^{-rT}$, and covered interest rate parity all hold *because* any deviation would create a riskless arbitrage that market participants would immediately exploit. In practice, pure riskless arbitrage is rare — transaction costs, borrowing constraints, and execution risk create a **no-arbitrage band** around theoretical prices. When apparent arbitrages do appear (e.g. the cash–CDS basis during the 2008 crisis), they often reflect hidden risks such as counterparty exposure, funding costs, or liquidity constraints rather than genuine free money.
