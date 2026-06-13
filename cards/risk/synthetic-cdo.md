# Synthetic CDO

**Topic:** Risk
**Tags:** synthetic CDO, credit derivatives, CDS, super-senior, correlation trading, structured credit
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A synthetic CDO gains exposure to a reference portfolio of credit names not by owning the underlying bonds but by selling credit protection via CDS; unlike a cash CDO, no assets are purchased — the vehicle collects CDS premiums and pays out on credit events.

## Key Formula

Tranche mechanics are identical to a cash CDO:

$$\ell_{\text{tranche}}(L) = \frac{\max(0,\;\min(L - A,\;B-A))}{B - A}$$

where $L$ = portfolio loss rate, $[A, B]$ = attachment/detachment.

**Key difference from cash CDO:** the portfolio loss $L = \frac{1}{N}\sum_i \mathbf{1}_{\{\text{default}_i\}}(1-R_i)$ is funded by CDS premia rather than coupon income. Unfunded super-senior tranche (above $[15\%,\,30\%]$) pays very low spread for negligible expected loss.

## Example

\$1bn synthetic CDO on 125 investment-grade names (similar to CDX IG). Equity $[0\%,3\%]$: receives spread $500$bps p.a., bears first \$30m of losses. Super-senior $[15\%,30\%]$: receives $2$bps p.a., only loses if 15%+ of names default (implying $\ge 18–19$ defaults at 40% recovery).

## Remember

Synthetic CDOs were at the centre of the 2008 financial crisis: by referencing the same pool of mortgage-related names multiple times across different deals, the system created synthetic exposure far exceeding the underlying bond supply. Banks retained super-senior tranches believing them to be near-riskless — until correlation spiked and housing defaults moved together, wiping out tranches whose models had assigned them near-zero expected loss.
