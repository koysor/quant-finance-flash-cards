# Swap Spread

**Topic:** Fixed Income
**Tags:** swap spread, interest rate swap, government bonds, credit risk, fixed income, term structure
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **swap spread** is the difference between the fixed rate on an interest rate swap and the yield of a government bond of the same maturity. It represents the extra return the fixed-rate payer demands above the risk-free sovereign yield, compensating for the bank credit risk and funding costs embedded in the interbank swap market.

## Key Formula

$$\text{Swap Spread}(T) = r_{\text{swap}}(T) - r_{\text{govt}}(T)$$

where $r_{\text{swap}}(T)$ is the par fixed rate on a $T$-maturity interest rate swap and $r_{\text{govt}}(T)$ is the yield on the on-the-run government bond of the same maturity. The spread is quoted in **basis points** (bps), where 1 bps = 0.01%.

At each maturity $T$, the swap rate can be decomposed as:

$$r_{\text{swap}}(T) = r_{\text{govt}}(T) + \text{Swap Spread}(T)$$

## Example

On a given date, the 10-year UK gilt yields 4.20% and the 10-year GBP interest rate swap fixed rate is 4.55%.

$$\text{10Y Swap Spread} = 4.55\% - 4.20\% = 0.35\% = 35 \text{ bps}$$

If the gilt yield rises to 4.40% but the swap rate rises only to 4.65%, the spread narrows to 25 bps — indicating reduced demand for fixed-rate protection or improved bank credit quality relative to sovereigns.

## Remember

The swap spread is one of the most closely watched indicators of bank credit risk and systemic stress in fixed-income markets. A widening swap spread signals that investors perceive increased risk in lending to banks at term (since the floating leg of a swap is linked to the interbank rate), or that there is surging demand for fixed-rate protection. During the 2008 financial crisis, 10-year USD swap spreads briefly turned **negative** — meaning swap fixed rates fell below Treasury yields — a highly unusual event driven by massive demand for Treasuries as a safe haven and technical constraints on arbitrageurs. At each tenor, the swap spread is the single most liquid point on the spread curve between the swap curve and the sovereign curve, making it a key input for pricing corporate bonds, mortgage-backed securities, and interest rate derivatives on a spread basis.
