# CIR Bond Price Formula

**Topic:** Fixed Income
**Tags:** CIR, bond pricing, closed form, affine model, interest rates, term structure
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **CIR bond price formula** is the closed-form solution for a zero-coupon bond price under the Cox-Ingersoll-Ross short-rate model. Like the Vasicek formula, it is exponential-affine in the current short rate, but the A and B functions differ to reflect the square-root diffusion that keeps rates non-negative.

## Key Formula

$$P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}, \qquad \tau = T - t$$

$$B(\tau) = \frac{2\!\left(e^{h\tau} - 1\right)}{(h + \kappa)\!\left(e^{h\tau} - 1\right) + 2h}$$

$$A(\tau) = \left[\frac{2h\,e^{(\kappa + h)\tau/2}}{(h + \kappa)\!\left(e^{h\tau} - 1\right) + 2h}\right]^{\!2\kappa\theta/\sigma^2}$$

where $h = \sqrt{\kappa^2 + 2\sigma^2}$, $\kappa$ is the mean-reversion speed, $\theta$ is the long-run mean, and $\sigma$ is the volatility.

The CIR yield is $y(t,T) = -\ln P / \tau = -(\ln A - Br)/\tau$, which is again affine in $r_t$.

## Example

Parameters: $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.08$, $r_t = 0.03$, $\tau = 2$.

$$h = \sqrt{0.25 + 2 \times 0.0064} = \sqrt{0.2628} \approx 0.5126$$

$$B(2) = \frac{2(e^{1.025} - 1)}{(0.5 + 0.5126)(e^{1.025} - 1) + 2 \times 0.5126} \approx \frac{2 \times 1.787}{1.013 \times 1.787 + 1.025} \approx 1.375$$

$$P \approx A(2)\,e^{-1.375 \times 0.03}$$

The resulting bond price is around 0.93–0.94 for these parameters, implying a 2-year yield near 3–4%.

## Remember

The CIR formula and the Vasicek $A/B$ formula look similar — both are exponential-affine — but the CIR functions are more complicated because the variance of $r$ depends on $r$ itself (the $\sqrt{r}$ diffusion). This structural difference ensures CIR rates cannot go negative, which matters for calibrating to low-rate environments. In practice, CIR is often preferred when rates are near zero; Vasicek is preferred for analytical tractability in multi-factor extensions.
