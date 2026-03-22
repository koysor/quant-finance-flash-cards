# Optionality Risk

**Topic:** Banking Regulation
**Tags:** optionality risk, IRRBB, prepayment, embedded options, behavioural modelling
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Optionality risk** is the IRRBB sub-risk arising from options embedded in banking book products — both explicit (e.g. callable bonds, caps on variable-rate loans) and behavioural (e.g. mortgage prepayment, early deposit withdrawal). When interest rates change, customers exercise these options in ways that are adverse for the bank: borrowers prepay when rates fall (shortening asset duration) and depositors withdraw when rates rise (shortening liability duration). This asymmetric behaviour amplifies the bank's interest rate exposure.

## Key Formula

The **conditional prepayment rate** (CPR) for mortgages is often modelled as a function of the rate incentive:

$$\text{CPR}(r) = \text{CPR}_{\text{base}} + \beta \times \max(c - r, \; 0)$$

where $c$ is the coupon rate, $r$ is the current market rate, and $\beta$ is a sensitivity parameter.

The **option-adjusted duration** of a mortgage portfolio:

$$D_{\text{OA}} = -\frac{1}{P}\frac{\Delta P}{\Delta r}\bigg|_{\text{with prepayment}}$$

This is shorter than the contractual duration because prepayments shorten the expected cash-flow horizon when rates fall.

## Example

A bank holds £5bn of fixed-rate mortgages with a contractual maturity of 25 years and a coupon of 4.5%. Market rates fall from 4.5% to 3.0%.

- **Without prepayment:** modified duration ≈ 8.5 years
- **With prepayment:** the CPR doubles as borrowers refinance, shortening expected duration to ≈ 4.2 years

The bank expected to earn 4.5% for 8.5 years of duration but must now reinvest the prepaid principal at 3.0%. The duration shortening also reduces the EVE gain the bank would have received from the rate fall.

## Remember

Optionality risk is the most challenging IRRBB component to model because it depends on customer behaviour, not just market rates. Mortgage prepayment models, deposit decay functions, and loan drawdown assumptions all require behavioural calibration from historical data — and the behaviour can shift in unprecedented rate environments, as seen during the 2020–2023 rate cycle. Basel requires banks to stress-test embedded options under each of the six prescribed rate scenarios and to include behavioural assumptions in their EVE and NII calculations. The asymmetry is key: customers exercise options when it hurts the bank (prepay when rates fall, withdraw deposits when rates rise), creating a negative convexity exposure that simple duration measures cannot capture.
