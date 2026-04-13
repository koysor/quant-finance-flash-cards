# Economic Capital

**Topic:** Risk
**Tags:** economic capital, unexpected loss, RAROC, solvency, capital allocation, VaR
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Economic capital (EC) is the amount of capital a bank estimates it needs to remain solvent at a chosen confidence level (typically 99.9%) over a one-year horizon, covering unexpected losses that exceed the expected loss already priced into the business. Unlike regulatory capital, which is set by rulebooks such as Basel III, economic capital is an internal risk-management metric calibrated to the bank's own loss distribution.

## Key Formula

Let $EL$ be the expected loss and $\text{VaR}_{99.9\%}$ be the 99.9th percentile of the one-year loss distribution. Then:

$$EC = \text{UL} = \text{VaR}_{99.9\%} - EL$$

Risk-Adjusted Return on Capital (RAROC) measures the profitability of a business line relative to its economic capital:

$$\text{RAROC} = \frac{\text{Net Revenue} - EL}{\text{Economic Capital}}$$

A desk is economically viable if $\text{RAROC} \geq \text{hurdle rate}$ (the firm's cost of equity, typically 10–15%).

## Example

A credit desk has a one-year loss distribution with:
- $EL = £2\text{m}$ (average annual losses, already charged in loan pricing)
- $\text{VaR}_{99.9\%} = £12\text{m}$

$$EC = £12\text{m} - £2\text{m} = £10\text{m}$$

If the desk earns net revenue of £3.5m after provisioning for expected losses:

$$\text{RAROC} = \frac{£3.5\text{m}}{£10\text{m}} = 35\%$$

With a hurdle rate of 12%, this desk creates shareholder value. A desk with RAROC below the hurdle rate destroys value and should be restructured or downsized.

## Remember

Economic capital converts abstract loss distributions into a concrete performance metric for bank management. RAROC lets a head of trading compare the profitability of a rates desk, a credit desk, and an equity desk on equal footing — each charged only for the unexpected loss it contributes to the firm. This is how banks allocate scarce capital to maximise risk-adjusted returns, and why a desk showing positive accounting profit can still be shut down if its RAROC fails to cover the firm's cost of equity.
