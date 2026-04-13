# Funding Liquidity Risk

**Topic:** Risk
**Tags:** funding liquidity, lcr, repo market, solvency, systemic risk, basel iii
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Funding liquidity risk is the danger that a firm cannot roll over its short-term borrowing — repos, commercial paper, or interbank loans — or meet margin calls as they fall due, even if it remains solvent. It is distinct from market liquidity risk (the cost of exiting a position due to wide bid-ask spreads or thin order books): a firm can be solvent on paper yet collapse purely because it cannot refinance maturing debt in time.

## Key Formula

The **Liquidity Coverage Ratio (LCR)**, introduced under Basel III, is the primary regulatory measure of 30-day funding resilience:

$$\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Net cash outflows over 30 days}} \geq 100\%$$

where HQLA (High Quality Liquid Assets) are assets that can be converted to cash rapidly without significant price loss, and net cash outflows are stressed outflows minus the smaller of stressed inflows and 75% of stressed outflows:

$$\text{Net outflows} = \text{Outflows} - \min\!\left(\text{Inflows},\; 0.75 \times \text{Outflows}\right)$$

## Example

A bank has HQLA of £40bn (government bonds and central bank reserves). Under a 30-day stress scenario it faces:
- Retail deposit run-off: £6bn
- Wholesale funding not rolled over: £28bn
- Derivatives margin calls: £10bn
- Contractual loan repayments received: £12bn

$$\text{Net outflows} = £44\text{bn} - \min(£12\text{bn},\; 0.75 \times £44\text{bn}) = £44\text{bn} - £12\text{bn} = £32\text{bn}$$

$$\text{LCR} = \frac{£40\text{bn}}{£32\text{bn}} = 125\%$$

The bank is compliant. If wholesale funding seizure worsened to £40bn, net outflows would rise to £44bn and LCR would fall below 100%, signalling a funding crisis.

## Remember

The 2008 crisis illustrated why solvency does not equal liquidity: Lehman Brothers was technically solvent at the moment it filed for bankruptcy, but the repo market froze — counterparties stopped rolling over overnight repos and demanded higher haircuts — leaving Lehman unable to finance its long-dated asset positions. This is the classic funding liquidity crisis mechanism: short-term liabilities mature faster than long-dated assets can be sold. The LCR was designed precisely to break this dynamic by requiring banks to hold pre-positioned liquid assets so they can survive 30 days without market access. Risk managers should stress-test rollover assumptions and haircut schedules, not just mark-to-market P&L — a position that looks profitable on paper can destroy a firm if the funding that supports it evaporates overnight.
