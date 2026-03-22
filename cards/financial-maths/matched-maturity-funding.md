# Matched-Maturity Funding

**Topic:** Financial Mathematics
**Tags:** matched maturity, funding, ALM, FTP, duration gap, interest rate risk
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Matched-maturity funding** is the principle that each asset on a bank's balance sheet should be funded by a liability of equivalent maturity or repricing tenor. Under perfect maturity matching, a 5-year fixed-rate loan would be funded by a 5-year fixed-rate bond, eliminating interest rate risk entirely. In practice, perfect matching is neither possible nor desirable — banks earn a term premium by deliberately mismatching maturities — but the concept provides the theoretical benchmark against which funds transfer pricing and ALM decisions are measured.

## Key Formula

Under matched-maturity funding, the duration gap is zero:

$$D_{\text{gap}} = D_A - \frac{PV_L}{PV_A} \times D_L = 0$$

The **net interest margin** under matched funding equals the pure credit spread:

$$\text{NIM}_{\text{matched}} = r_{\text{loan}} - r_{\text{matched-funding}} = \text{credit spread only}$$

Any NIM above this level represents compensation for deliberate maturity mismatch:

$$\text{NIM}_{\text{actual}} - \text{NIM}_{\text{matched}} = \text{term premium earned}$$

## Example

A bank originates a £100m 5-year fixed mortgage at 5.00%.

**Matched funding:** issue a 5-year fixed bond at 3.80%. NIM = 5.00% − 3.80% = **1.20%** (pure credit spread, no rate risk).

**Mismatched funding:** fund with 3-month deposits at 2.50%. NIM = 5.00% − 2.50% = **2.50%**, which is 1.30% higher — but the bank is exposed to deposit rates rising over the next 5 years.

The extra 1.30% is the **term premium** the bank earns for bearing interest rate risk. If 3-month rates rise to 5.50% within two years, the NIM collapses to −0.50%, turning the position unprofitable.

## Remember

Matched-maturity funding is the intellectual foundation of funds transfer pricing — the FTP rate for any product is the rate at which the bank could fund that product on a matched-maturity basis. By pricing internal transfers at the matched-maturity rate, FTP ensures that business units earn credit margins while treasury explicitly manages the maturity transformation decision. The 2007–2008 crisis demonstrated the danger of extreme maturity mismatching: institutions like Northern Rock funded 25-year mortgages with short-term securitisation, earning wide NIMs until the wholesale funding market froze. Modern ALM accepts some deliberate mismatch as a source of earnings but measures and limits it through duration gap targets, EVE limits, and NII sensitivity bounds.
