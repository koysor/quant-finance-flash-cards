# Overnight Index Swap

**Topic:** Financial Mathematics
**Tags:** overnight index swap, ois, risk-free rate, sonia, sofr, discounting
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

An overnight index swap (OIS) is an interest rate swap in which one party pays a fixed rate and receives the geometric compounding of an overnight reference rate (such as SONIA in the UK or SOFR in the US) over the swap's term. The OIS rate is considered the best market proxy for the risk-free rate because overnight lending carries minimal credit risk.

## Key Formula

The **compounded overnight leg** over $n$ business days:

$$\text{Floating Leg} = N \times \left[\prod_{i=1}^{n}\left(1 + r_i \times \frac{d_i}{360}\right) - 1\right]$$

where $N$ is the notional, $r_i$ is the overnight rate on day $i$, and $d_i$ is the day count (usually 1, but 3 over weekends).

At maturity, the net payment is:

$$\text{Net} = N \times \left[\prod_{i=1}^{n}\left(1 + r_i \times \frac{d_i}{360}\right) - 1 - r_{\text{fixed}} \times \frac{T}{360}\right]$$

where $r_{\text{fixed}}$ is the agreed OIS rate and $T$ is the total day count.

## Example

A 30-day OIS on £10 million notional at a fixed rate of 4.50%. Over the 30 days, the compounded SONIA rate averages 4.55%.

Floating leg:

$$\text{Floating} = £10{,}000{,}000 \times \left(1.0455^{30/365} - 1\right) \approx £10{,}000{,}000 \times 0.003655 = £36{,}550$$

Fixed leg:

$$\text{Fixed} = £10{,}000{,}000 \times 0.045 \times \frac{30}{360} = £37{,}500$$

Net payment from fixed payer to floating payer: $£37{,}500 - £36{,}550 = £950$.

The fixed payer overpaid because SONIA came in slightly below the locked-in OIS rate.

## Remember

The OIS rate has replaced LIBOR as the standard risk-free rate for discounting derivatives and valuing collateralised positions. After the LIBOR manipulation scandal, regulators mandated the transition to overnight rates (SONIA, SOFR, €STR) that are based on actual transactions rather than bank submissions. In quantitative finance, the OIS curve is now used for discounting cash flows on collateralised derivatives (OIS discounting), while the spread between OIS and term lending rates measures bank credit risk and funding stress. During the 2008 crisis, the LIBOR-OIS spread widened from 10 basis points to over 350 basis points, making it one of the most-watched indicators of systemic stress.
