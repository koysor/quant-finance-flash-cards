# CDS Index (CDX / iTraxx)

**Topic:** Derivatives
**Tags:** CDS index, CDX, iTraxx, credit derivatives, index spread, macro hedge, standardised CDS
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A CDS index is a standardised, liquid credit derivative referencing a basket of equal-weighted single-name CDS; CDX covers North American names, iTraxx covers European and Asian names. The index protection buyer pays a fixed spread on all names in return for credit protection.

## Key Formula

Index spread $\approx \frac{1}{N}\sum_{i=1}^N s_i$ (equal-weighted average of constituent single-name spreads).

On default of name $i$: buyer receives $(1 - R_i) \times \frac{\text{Notional}}{N}$; index notional reduces by $\frac{1}{N}$.

Index–intrinsic basis $= s_{\text{index}} - \frac{1}{N}\sum s_i$: positive in stress (demand for macro protection), negative otherwise.

## Example

CDX Investment Grade (Series 43, 125 names): spread $= 75$bps. Protection buyer on \$125m notional pays $0.75\% \times \$125\text{m} = \$937{,}500$ p.a. If one name defaults with $R = 40\%$: buyer receives $0.60 \times \$1\text{m} = \$600{,}000$; notional falls to \$124m.

## Remember

CDS indices are the standard vehicle for macro credit hedges — far more liquid than single-name CDS. During the London Whale episode (2013), JPMorgan accumulated a massive long position in iTraxx Series 9 (credit protection seller) that distorted the index basis and ultimately led to \$6bn in trading losses when the position was forcibly reduced.
