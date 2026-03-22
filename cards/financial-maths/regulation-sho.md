# Regulation SHO

**Topic:** Financial Mathematics
**Tags:** regulation sho, short selling, locate requirement, close-out, SEC, compliance
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Regulation SHO is the US Securities and Exchange Commission's (SEC) primary regulatory framework governing short selling, enacted in 2005. It establishes three key requirements: the **locate rule** (broker-dealers must have reasonable grounds to believe the security can be borrowed before accepting a short sale order), the **close-out requirement** (failures to deliver must be closed out within specified timeframes), and the **alternative uptick rule** (Rule 201, a circuit breaker that restricts short selling when a stock drops 10% or more in a single day).

## Key Formula

The **close-out threshold** under Regulation SHO:

$$\text{Threshold Security} \iff \text{FTDs} \geq 10{,}000 \text{ shares} \;\wedge\; \text{FTDs} \geq 0.5\% \times \text{Shares Outstanding}$$

for 5 consecutive settlement days.

The **alternative uptick rule** (Rule 201) triggers when:

$$\frac{P_{\text{current}} - P_{\text{prev close}}}{P_{\text{prev close}}} \leq -10\%$$

Once triggered, short sales may only be executed at a price above the current national best bid for the remainder of the day and the following day.

## Example

A stock has 20 million shares outstanding. Over 5 consecutive settlement days, failures to deliver average 120,000 shares:

$$0.5\% \times 20{,}000{,}000 = 100{,}000$$

Since $120{,}000 \geq 10{,}000$ and $120{,}000 \geq 100{,}000$, the stock is designated a **threshold security**. Broker-dealers with open fail-to-deliver positions must close them out by purchasing shares within 13 consecutive settlement days.

If the stock closed yesterday at £40 and today drops to £35.50:

$$\frac{£35.50 - £40.00}{£40.00} = -11.25\%$$

The alternative uptick rule activates, restricting short sales to prices above the national best bid.

## Remember

Regulation SHO is the practical embodiment of short-sale constraints that quantitative models must account for. The locate requirement adds friction and cost to short selling (especially for hard-to-borrow stocks), the close-out rules create forced buying demand when fails accumulate, and the alternative uptick rule restricts execution during steep declines. For systematic trading strategies, these constraints mean that the theoretical short-selling payoff differs from the realised payoff — models that ignore Reg SHO frictions will overestimate the profitability of short-side signals.
