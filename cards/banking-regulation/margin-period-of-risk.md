# Margin Period of Risk

**Topic:** Banking Regulation
**Tags:** margin period of risk, initial margin, counterparty risk, close-out, clearing
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Margin Period of Risk (MPoR) is the regulatory time horizon over which a bank remains exposed to adverse price moves after a counterparty has defaulted but before it can fully close out and re-hedge the position. During this window, variation margin ceases to flow, so the bank bears all mark-to-market risk without collateral protection.

## Key Formula

Initial Margin must cover the potential loss over the MPoR at the required confidence level:

$$IM = \text{ES}_{97.5\%}(\Delta V_{\text{MPoR}}) \quad \text{or} \quad \text{VaR}_{99\%}(\Delta V_{\text{MPoR}})$$

where $\Delta V_{\text{MPoR}}$ is the portfolio value change over the MPoR horizon. For a position with daily volatility $\sigma_1$:

$$\sigma_{\text{MPoR}} = \sigma_1 \times \sqrt{\text{MPoR}}$$

Regulatory MPoR standards:

| Setting | MPoR |
|---|---|
| CCP-cleared (liquid markets) | 2–5 business days |
| Bilateral OTC (UMR-in-scope) | 10 business days |
| Bilateral with large netting set or illiquid | up to 20 business days |

## Example

A bilateral FX swap with 1-day 99% VaR of £500,000 and a 10-day MPoR requires:

$$IM = £500{,}000 \times \sqrt{10} \approx £1.58\text{m}$$

If the same trade were centrally cleared with a 3-day MPoR, IM would be only $£500{,}000 \times \sqrt{3} \approx £866{,}000$ — 45% less, directly incentivising central clearing.

## Remember

The gap between bilateral (10-day) and centrally-cleared (2–5-day) MPoR is a deliberate regulatory incentive to push standardised derivatives onto CCPs: shorter MPoR means smaller IM, reducing the cost of clearing and making CCPs more attractive than bilateral OTC trading. For quants sizing IM models, the MPoR horizon is often the most sensitive parameter — lengthening it by one day increases IM by approximately $\sqrt{(N+1)/N} - 1$ percent, which for a large portfolio can be tens of millions of pounds.
