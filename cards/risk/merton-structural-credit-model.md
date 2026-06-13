# Merton Structural Credit Model

**Topic:** Risk
**Tags:** Merton model, structural credit, default probability, credit spread, equity as call option, firm value
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Merton (1974) structural credit model** treats a firm's equity as a **call option** on the firm's asset value $V_t$, with strike equal to the face value $D$ of outstanding debt maturing at $T$. At maturity, shareholders receive $\max(V_T - D, 0)$ (they exercise the call if the firm is solvent) while bondholders receive $\min(V_T, D)$. Default occurs if and only if $V_T < D$, giving an explicit, risk-neutral default probability derived from the lognormal distribution of $V_T$.

## Key Formula

Firm asset value follows GBM: $dV_t = \mu V_t\,dt + \sigma_V V_t\,dW_t$.

**Equity** (call on firm value at maturity $T$):

$$E_0 = V_0 N(d_1) - D e^{-rT} N(d_2)$$

**Risky zero-coupon bond value** (by put-call parity, $E_0 + B_0 = V_0 + \text{put}$ gives):

$$B_0 = V_0 N(-d_1) + D e^{-rT} N(d_2)$$

where:

$$d_1 = \frac{\ln(V_0/D) + (r + \tfrac{1}{2}\sigma_V^2)T}{\sigma_V \sqrt{T}}, \qquad d_2 = d_1 - \sigma_V\sqrt{T}$$

**Risk-neutral default probability:** $\Pr^{\mathbb{Q}}(V_T < D) = N(-d_2)$

**Credit spread** on the bond ($y$ solves $B_0 = De^{-yT}$):

$$s = y - r = -\frac{1}{T}\ln\!\left(N(d_2) + \frac{V_0}{De^{-rT}} N(-d_1)\right)$$

## Example

Firm: $V_0 = £120\text{m}$, $D = £100\text{m}$ (face, 5-year maturity), $\sigma_V = 30\%$, $r = 4\%$.

$$d_1 = \frac{\ln(1.2) + (0.04 + 0.045)(5)}{0.30\sqrt{5}} = \frac{0.182 + 0.425}{0.671} = 0.904$$

$$d_2 = 0.904 - 0.671 = 0.233$$

$$\Pr^{\mathbb{Q}}(\text{default}) = N(-0.233) \approx 40.8\%$$

$$B_0 = 120 \times N(-0.904) + 100 e^{-0.20} \times N(0.233) \approx 120(0.183) + 81.87(0.592) \approx \pounds70.4\text{m}$$

$$s = -\frac{1}{5}\ln(70.4/81.87) \approx 0.030 = 300\,\text{bps}$$

## Remember

Merton's insight is that **capital structure is just option decomposition**: holding debt in a levered firm is equivalent to holding a risk-free bond and selling a put option on the firm's assets to the shareholders. Credit spread therefore equals the fair value of this put, divided by the bond's duration. In practice, the model is used in **KMV/Moody's Analytics** form: observed equity price and equity volatility are used to back out implied $V_0$ and $\sigma_V$ via two simultaneous equations ($E_0 = V_0N(d_1) - De^{-rT}N(d_2)$ and $\sigma_E E_0 = \sigma_V V_0 N(d_1)$), then $N(-d_2)$ gives the **Expected Default Frequency** (EDF). The model struggles with short maturities (observed spreads exceed model spreads for investment-grade firms) because it predicts zero default probability for firms with low leverage — the Black-Cox extension fixes this by allowing default before maturity if firm value hits a time-varying barrier.
