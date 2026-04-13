# Credit Value Adjustment (CVA)

**Topic:** Banking Regulation
**Tags:** cva, counterparty risk, expected exposure, credit default swap, derivative pricing
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

CVA is the market-value adjustment applied to a derivative portfolio to reflect the risk that the counterparty defaults before the contract matures. It is the expected present value of the loss from counterparty default — equivalently, the price of a contingent credit protection that would eliminate counterparty risk entirely. Basel III introduced an explicit CVA capital charge after the 2008 crisis revealed that most counterparty-related losses came from CVA mark-to-market moves, not from actual defaults.

## Key Formula

$$\text{CVA} \approx (1 - R) \sum_{i=1}^{n} \text{EE}(t_i) \cdot \text{PD}(t_{i-1},\, t_i) \cdot D(t_i)$$

where:
- $R$ = recovery rate (typically 40%)
- $\text{EE}(t_i)$ = expected exposure at time $t_i$ (the average positive mark-to-market across scenarios)
- $\text{PD}(t_{i-1}, t_i)$ = marginal probability of default in interval $[t_{i-1}, t_i]$, derived from CDS spreads
- $D(t_i)$ = risk-free discount factor

## Example

A 5-year interest rate swap with a counterparty has an average expected exposure of £10 m across the life of the trade. The counterparty's CDS spread implies an annual default probability of 1% and a recovery rate of 40%.

$$\text{CVA} \approx (1 - 0.40) \times £10\text{m} \times 5 \times 1\% = £0.30\text{m}$$

The bank writes down the derivative's fair value by £300,000 on day one, reflecting the cost of bearing counterparty risk.

## Remember

CVA transformed counterparty credit risk from a back-office concern into a front-office pricing input: every OTC derivative now has a CVA desk that charges the trading desk for the cost of hedging counterparty exposure using CDS. Banks that failed to price CVA before 2008 — treating derivatives as risk-free — suffered billions in write-downs when counterparty credit quality deteriorated. For quants, the key modelling challenge is computing EE across thousands of scenarios and netting sets, which requires a full Monte Carlo simulation of the underlying risk factors through time.
