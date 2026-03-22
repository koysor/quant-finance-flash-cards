# Net Stable Funding Ratio

**Topic:** Banking Regulation
**Tags:** NSFR, liquidity risk, Basel III, funding stability, banking regulation, structural liquidity
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **Net Stable Funding Ratio (NSFR)** is a Basel III regulatory standard requiring banks to maintain a stable funding profile over a one-year horizon. While the LCR addresses short-term (30-day) liquidity stress, the NSFR ensures that long-term assets are funded by appropriately stable sources, discouraging excessive reliance on short-term wholesale funding to finance illiquid, long-dated assets.

## Key Formula

$$\text{NSFR} = \frac{\text{Available Stable Funding (ASF)}}{\text{Required Stable Funding (RSF)}} \times 100\% \geq 100\%$$

Each liability and equity item receives an **ASF factor** (0–100%) reflecting its stability:
- Tier 1 capital and long-term debt (>1 year): 100%
- Stable retail deposits: 95%
- Less stable retail deposits: 90%
- Wholesale funding (<6 months): 0–50%

Each asset receives an **RSF factor** (0–100%) reflecting its liquidity:
- Cash and central bank reserves: 0%
- Unencumbered government bonds: 5%
- Performing corporate loans (≥1 year): 65–85%
- Residential mortgages: 65%

## Example

A bank reports:

| Item | Amount | Factor | Weighted |
|---|---|---|---|
| **ASF:** Tier 1 capital | £8bn | 100% | £8.0bn |
| Stable retail deposits | £30bn | 95% | £28.5bn |
| Wholesale funding (>1yr) | £10bn | 100% | £10.0bn |
| **Total ASF** | | | **£46.5bn** |
| **RSF:** Cash & reserves | £5bn | 0% | £0.0bn |
| Government bonds | £12bn | 5% | £0.6bn |
| Residential mortgages | £35bn | 65% | £22.75bn |
| Corporate loans | £15bn | 85% | £12.75bn |
| **Total RSF** | | | **£36.1bn** |

$$\text{NSFR} = \frac{£46.5\text{bn}}{£36.1\text{bn}} \times 100\% = 128.8\%$$

The bank comfortably exceeds the 100% minimum, holding £10.4bn of surplus stable funding.

## Remember

The NSFR complements the LCR by addressing structural funding mismatches rather than short-term liquidity stress. Before 2008, many banks funded long-term mortgage books with short-term commercial paper and overnight repos — a strategy that appeared profitable until wholesale markets froze. Northern Rock's 2007 collapse was a textbook NSFR failure: its mortgage assets required stable funding, but its liabilities were dominated by short-term securitisation and wholesale borrowing that evaporated in the crisis. The NSFR forces banks to align funding tenor with asset tenor, reducing the maturity transformation that is profitable in normal times but catastrophic in stress. For ALM teams, the NSFR creates a binding constraint on the funding mix, often requiring more expensive long-term debt or retail deposit gathering.
