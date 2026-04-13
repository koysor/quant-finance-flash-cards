# Funding Valuation Adjustment (FVA)

**Topic:** Banking Regulation
**Tags:** fva, xva, funding cost, uncollateralised, hull-white
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Funding Valuation Adjustment (FVA) is the adjustment to a derivative's value to account for the cost (or benefit) of funding the cash flows on uncollateralised or partially collateralised positions. When a bank enters an uncollateralised derivative, it cannot offset the funding cost of posting variation margin on the hedge — this funding cost must be recovered in the price. FVA decomposes into a Funding Cost Adjustment (FCA) for funding costs and a Funding Benefit Adjustment (FBA) for funding benefits.

## Key Formula

FVA is approximately the present value of the funding spread applied to the derivative's exposure profile:

$$\text{FVA} = -\int_0^T s_f \cdot \mathbb{E}[V_t^+] \, dt + \int_0^T s_f \cdot \mathbb{E}[V_t^-] \, dt$$

$$= \text{FCA} + \text{FBA}$$

where $s_f$ is the firm's funding spread (cost above risk-free), $\mathbb{E}[V_t^+]$ is the expected positive exposure (bank funds the hedge), and $\mathbb{E}[V_t^-]$ is the expected negative exposure (bank receives funding benefit). In practice:

$$\text{FVA} \approx -s_f \cdot \text{EPE} \cdot T + s_f \cdot \text{ENE} \cdot T$$

## Example

A bank enters a 5-year uncollateralised interest rate swap with a corporate client. The swap is worth +£5 m to the bank. The bank hedges with a collateralised swap in the interbank market, so it must post variation margin to the interbank counterparty but cannot collect collateral from the corporate. If the bank's funding spread is 80 bps and the average positive exposure over 5 years is £5 m, the FCA ≈ $0.008 \times £5\text{m} \times 5 = £200{,}000$ — a cost that should be charged upfront to the corporate client.

## Remember

FVA sparked one of quantitative finance's most public academic debates: Hull and White (2012) argued FVA should not be included in derivative pricing because it represents a funding choice that is already captured in the firm's cost of capital — including it double-counts. Practitioners largely disagreed, arguing that treasury's funding charge to trading desks is real and must be recovered in trade pricing. The debate matters for quant developers because whether FVA is included in the pricing model affects the P&L of every uncollateralised trade: banks that include FVA charge more to corporate clients, those that do not are cheaper but bear hidden funding risk on their balance sheet.

