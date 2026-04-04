# Convergence Trading

**Topic:** Fixed Income
**Tags:** convergence trading, on-the-run, off-the-run, spread, relative value, liquidity premium
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Convergence trading is a relative value strategy that profits from the expected narrowing of a spread between two related instruments. The classic example is the on-the-run/off-the-run Treasury trade: the most recently issued Treasury bond (on-the-run) trades at a premium due to its superior liquidity, while the previously issued bond of similar maturity (off-the-run) trades at a discount. A convergence trader buys the cheap off-the-run bond and shorts the expensive on-the-run bond, then waits for the spread to narrow as the on-the-run bond ages and loses its liquidity premium.

## Key Formula

The **yield spread** between the on-the-run and off-the-run bonds:

$$\text{Spread}_t = y_{\text{off}} - y_{\text{on}}$$

Since higher yield means lower price, the spread is positive when the off-the-run bond is cheaper. The **expected P&L** from convergence:

$$E[\text{P\&L}] \approx \text{DV01} \times \Delta\text{Spread} \times \text{Notional}$$

where DV01 is the dollar value of a basis point. The trade is typically leveraged via repo financing, so the **net carry** is:

$$\text{Carry} = (y_{\text{off}} - y_{\text{on}}) - (r_{\text{repo,off}} - r_{\text{repo,on}})$$

The first term is the yield pickup; the second is the financing cost differential (off-the-run bonds typically have slightly higher repo rates).

## Example

A 10-year on-the-run gilt yields 4.20% and the off-the-run gilt (issued 6 months earlier, same maturity) yields 4.28%. The DV01 of each bond is £850 per £1 million notional. The trader buys £10 million of the off-the-run bond and shorts £10 million of the on-the-run bond.

Over the next 3 months, as a new gilt is issued and the previously on-the-run bond loses its liquidity premium, the spread narrows from 8 basis points to 3 basis points:

$$\text{P\&L} = £850 \times 10 \times (8 - 3) \times \frac{1}{100} = £850 \times 10 \times 0.05 = £425$$

Wait — more carefully: $\text{P\&L} = \text{DV01} \times \text{Notional multiplier} \times \Delta\text{Spread}$:

$$\text{P\&L} = £850 \times 10 \times 5 = £42{,}500$$

on £10 million notional. With 10x repo leverage (posting £1 million of capital), the return on equity is 4.25% over 3 months.

## Remember

Convergence trading is the archetypal fixed-income relative value strategy and the trade that famously destroyed Long-Term Capital Management in 1998. The mathematics of the trade is straightforward — the spread should converge as the liquidity premium dissipates — but the risk comes from the leverage required to make small basis-point spreads profitable. LTCM held convergence trades at 25x leverage; when spreads widened during the Russian crisis instead of narrowing, margin calls forced liquidation at the worst possible time. For quant risk managers, the lesson is that convergence trades are right on average but can diverge catastrophically before they converge, making position sizing and liquidity management more important than the spread forecast itself.
