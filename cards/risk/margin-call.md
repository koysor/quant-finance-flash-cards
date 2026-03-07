# Margin Call

**Topic:** Risk
**Tags:** margin, leverage, collateral, liquidation, risk management
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A margin call is a demand from a broker or exchange for an investor to deposit additional funds or securities when the equity in a leveraged account falls below the required maintenance margin. If the investor cannot meet the call, the broker may forcibly liquidate positions.

## Key Formula

A margin call is triggered when the **equity ratio** drops to or below the maintenance margin $m$:

$$\frac{\text{Equity}}{\text{Position Value}} \leq m$$

For a long position bought at price $P_0$ with initial equity $E_0$, the **margin call price** is:

$$P_{\text{call}} = P_0 \times \frac{1 - \frac{E_0}{P_0 \times Q}}{1 - m}$$

which simplifies to:

$$P_{\text{call}} = \frac{P_0 \times Q - E_0}{Q \times (1 - m)}$$

where $Q$ is the number of shares and $m$ is the maintenance margin fraction.

## Example

A trader buys 200 shares at £50 each (position value £10,000), putting up £6,000 of equity and borrowing £4,000. The maintenance margin is 25%.

The margin call triggers when:

$$\frac{\text{Equity}}{\text{Position Value}} = \frac{200P - 4{,}000}{200P} \leq 0.25$$

Solving: $200P - 4{,}000 = 0.25 \times 200P$, so $150P = 4{,}000$, giving $P_{\text{call}} = £26.67$.

If the share price falls to £26.67, the position is worth £5,334 and equity is just £1,334 — exactly 25%. Any further decline forces a margin call.

## Remember

Margin calls create a dangerous feedback loop in financial markets. When prices fall, leveraged investors receive margin calls and are forced to sell assets, which pushes prices down further, triggering more margin calls. This **margin spiral** was a key amplifier of the 2008 crisis and the 1998 LTCM collapse. In quantitative risk management, stress tests must model this procyclical liquidation effect — a portfolio's VaR in isolation understates the true risk because it ignores the market impact of forced selling by similarly positioned funds.
