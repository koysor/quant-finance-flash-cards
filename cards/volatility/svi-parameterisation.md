# SVI Parameterisation

**Topic:** Volatility
**Tags:** svi, implied volatility, smile, gatheral, parameterisation, calibration, vol surface
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The **Stochastic Volatility Inspired (SVI)** parameterisation (Gatheral, 2004) fits the implied volatility smile at a single maturity with five parameters using a hyperbola-shaped total implied variance curve. It is the most widely used practitioner tool for interpolating and extrapolating the implied vol smile, because it is both flexible enough to match observed market smiles and constrained enough to avoid introducing spurious butterfly arbitrage at a single maturity.

## Key Formula

SVI parameterises the **total implied variance** $w(k) = \hat{\sigma}^2(k)\cdot T$ as a function of log-moneyness $k = \ln(K/F)$:

$$w(k) = a + b\!\left\{\rho(k - m) + \sqrt{(k-m)^2 + \sigma^2}\right\}$$

where the five parameters are:
- $a \in \mathbb{R}$: overall variance level
- $b \ge 0$: slope of the wings (ATM vol sensitivity)
- $\rho \in (-1, 1)$: skew — asymmetry between put and call wings
- $m \in \mathbb{R}$: ATM shift (horizontal translation)
- $\sigma > 0$: curvature (ATM smoothness)

Butterfly no-arbitrage at this maturity requires $b(1 + |\rho|) \le 2/T$.

## Example

SPX 3-month smile: ATM vol = 18%, 25-delta put vol = 21%, 25-delta call vol = 16.5%. SVI fit with $a = 0.030$, $b = 0.140$, $\rho = -0.70$, $m = 0.00$, $\sigma = 0.20$ gives total variance $w(0) = 0.0324$ ($\approx 18\%$ vol), steeply negative $\rho$ producing the observed left skew. The fit residual is $< 0.2$ vol points across all strikes — better than Heston (which must simultaneously fit the term structure) but applicable only at the single 3-month slice.

## Remember

SVI is a **single-maturity** tool — it fits one smile slice perfectly but says nothing about the term structure of volatility. To build a full arbitrage-free surface, SVI is applied independently at each maturity and then the resulting slices must satisfy additional **calendar spread conditions** (variance must be non-decreasing in maturity at each strike). The **Surface SVI (SSVI)** extension by Gatheral and Jacquier (2014) parameterises all maturities jointly to ensure calendar spread arbitrage is automatically excluded. For RL pricing and normalising flow vol surface generation, SVI and SSVI provide the parameterised representation to which the model output is compared during validation.
