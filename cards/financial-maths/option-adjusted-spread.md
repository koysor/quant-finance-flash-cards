# Option-Adjusted Spread

**Topic:** Financial Mathematics
**Tags:** option-adjusted spread, oas, z-spread, embedded options, callable bonds, fixed income, credit spread
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **option-adjusted spread (OAS)** is the constant spread added to the benchmark zero rate curve such that the model price of a bond — after explicitly accounting for the value of any embedded option (call, put, or prepayment right) — equals the observed market price. It represents the pure credit and liquidity premium the investor earns, stripped of any compensation for bearing option risk.

$$\text{OAS} = \text{Z-spread} - \text{Option value (in spread terms)}$$

For a **callable bond**, the issuer holds the right to redeem early, which benefits the issuer and harms the investor; this embedded call has positive value, so OAS < Z-spread. For a **putable bond**, the investor holds the right to sell back the bond early; the embedded put benefits the investor, so OAS > Z-spread.

## Key Formula

OAS is computed via a **term-structure model** (e.g. Hull–White or Black–Derman–Toy). The bond is valued across an interest rate lattice and the spread $s$ that equates model price to market price is solved numerically:

$$P_{\text{market}} = \mathbb{E}^Q\!\left[\sum_{i=1}^{n} \frac{C_i \cdot \mathbf{1}_{\{\text{not called at } t_i\}}}{e^{(r(t_i) + s)\, t_i}}\right]$$

where the expectation is taken over simulated short-rate paths under the risk-neutral measure $Q$, and the indicator $\mathbf{1}_{\{\text{not called}\}}$ reflects that cash flows cease if the issuer exercises the call. The option value in spread terms is:

$$\text{Option value} = \text{Z-spread} - \text{OAS}$$

## Example

A callable corporate bond trades at £96. The Z-spread (treating it as option-free) is computed as 180 bps. An interest rate model values the embedded call option at 50 bps in spread terms (i.e. the call option lowers the bond's fair spread by 50 bps from the investor's perspective).

$$\text{OAS} = 180\,\text{bps} - 50\,\text{bps} = 130\,\text{bps}$$

The investor earns only 130 bps for credit and liquidity risk; the remaining 50 bps compensates for the reinvestment/call risk. A non-callable bond from the same issuer trading at a Z-spread of 130 bps would be fairly valued relative to this callable bond.

## Remember

OAS is the industry standard for comparing bonds with different embedded options on a like-for-like basis: a callable corporate bond with OAS = 130 bps and a bullet bond with Z-spread = 130 bps offer the same pure credit premium, making OAS the correct metric for relative-value analysis in credit markets. OAS is also central to mortgage-backed securities (MBS) analysis, where prepayment optionality varies with interest rates — a wider OAS on an MBS versus a comparable corporate bond signals either extra credit risk or model error in the prepayment assumption.
