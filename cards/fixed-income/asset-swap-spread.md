# Asset Swap Spread

**Topic:** Fixed Income
**Tags:** asset swap, credit spread, swap curve, fixed income, bond pricing, interbank market
**Created:** 2026-03-11
**Author:** claude-sonnet-4-6

---

## Definition

The **asset swap spread (ASW)** is the spread above (or below) the floating swap rate that a protection buyer receives when a bond's fixed cash flows are exchanged for floating via an interest rate swap. It measures how much a bond yields in excess of the interbank swap curve, stripping out the risk-free rate component and isolating the bond's credit and liquidity premium in floating-rate terms.

## Key Formula

In a par asset swap, the bond is purchased at par and its fixed coupons are swapped to LIBOR (or SOFR) flat plus a spread $s$:

$$\text{ASW} = c - r_{\text{swap}} + \frac{P_{\text{market}} - P_{\text{par}}}{A}$$

where $c$ is the bond coupon, $r_{\text{swap}}$ is the swap rate of matching maturity, $P_{\text{market}}$ is the bond's dirty price, $P_{\text{par}}$ is par (100), and $A$ is the swap's annuity (present value of £1 per period). More intuitively, the spread satisfies:

$$\text{Bond Price} = \text{PV of coupons discounted at swap rate} + \text{PV of } s \text{ on notional}$$

## Example

A 5-year gilt-edged corporate bond has a coupon of 5.50% and trades at a clean price of 98.50 (dirty price ≈ 98.75). The 5-year GBP swap rate is 4.80%. The annuity factor is 4.32.

$$\text{ASW} \approx (5.50\% - 4.80\%) + \frac{98.75 - 100}{4.32} = 0.70\% - 0.029\% \approx 67 \text{ bps}$$

An investor who enters an asset swap on this bond receives SONIA + 67 bps on the floating leg, earning 67 basis points above the risk-free swap curve as compensation for the bond's credit and liquidity risk.

## Remember

The asset swap spread is the fixed income market's native language for relative value: traders compare ASW across bonds of the same issuer to find mispricings, and across issuers to gauge relative credit cheapness. Because the ASW is expressed as a spread over the swap curve rather than gilts or Treasuries, it directly ties bond valuation to the interbank funding market — the same market used to hedge and finance the position. A tightening ASW (spread falling) indicates a bond is becoming more expensive; a widening ASW signals either credit deterioration or a buying opportunity. During the 2008 crisis, investment-grade corporate ASWs widened from 50–100 bps to over 500 bps, quantifying the cost of credit risk in the swaps market.
