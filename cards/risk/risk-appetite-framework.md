# Risk Appetite Framework

**Topic:** Risk
**Tags:** risk appetite, risk tolerance, risk capacity, governance, var limit, desk limits
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

A Risk Appetite Framework (RAF) is the formal governance structure that translates a board's high-level willingness to accept risk into quantitative limits at every level of the organisation — from the firm as a whole down to individual trading desks. It distinguishes three related but distinct concepts: risk capacity (the maximum risk the firm can absorb without breaching regulatory or solvency constraints), risk appetite (the amount of risk the board actively chooses to accept in pursuit of strategic objectives), and risk tolerance (the acceptable deviation around appetite before an escalation is triggered).

## Key Formula

The cascade from board to desk can be represented as a hierarchy of binding constraints:

| Level | Metric | Typical Limit |
|---|---|---|
| Board / firm | 1-day 99% VaR | ≤ 1–2% of Tier 1 capital |
| Business line | 1-day 99% VaR | ≤ 30–40% of firm limit |
| Trading desk | 1-day 99% VaR | ≤ 5–10% of business-line limit |
| Individual trader | Notional / DV01 / delta | Hard stop, no override |

Breach thresholds define the escalation ladder:

$$\text{Utilisation} = \frac{\text{Current VaR}}{\text{Approved VaR Limit}}$$

- $\text{Utilisation} > 75\%$ — yellow flag: desk head notified, review required  
- $\text{Utilisation} > 100\%$ — breach: CRO informed, position reduction mandatory within one business day  
- Drawdown $>$ stop-loss trigger — trading suspended pending risk committee sign-off

Expected Shortfall (ES) limits are set alongside VaR to capture tail risk:

$$\text{ES limit} = k \times \text{VaR limit}, \quad k \approx 1.3\text{–}1.6 \text{ (calibrated to loss distribution)}$$

## Example

A bank has Tier 1 capital of £4 bn. The board sets firm-wide 1-day 99% VaR appetite at 1% of capital = £40 m. The Rates desk receives a sub-limit of 20% = £8 m. A junior trader runs a position with DV01 of £500 k per bp. At end of day the desk's VaR reads £6.4 m (80% utilisation) — a yellow flag is raised. After a further £2 m increase the limit is breached; the CRO is alerted and the position must be reduced by the following morning. If losses subsequently exceed the desk's £15 m monthly stop-loss, all new risk-taking ceases until the risk committee reconvenes.

## Remember

A RAF is not just a spreadsheet of numbers — it is the governance chain that makes risk-taking deliberate. In practice, the VaR and ES limits derived from the board's appetite statement feed directly into daily P&L attribution reports and drive margin calls, hedge triggers, and capital allocation across desks. Without the framework, a single trader's outsized position (as in the 2012 London Whale episode) can consume risk budget invisibly until losses breach regulatory capital thresholds.
