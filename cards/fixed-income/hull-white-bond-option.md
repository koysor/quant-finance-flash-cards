# Hull–White Bond Option Pricing

**Topic:** Fixed Income
**Tags:** Hull-White, bond option, caplet, closed form, calibration, swaption, Black formula
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Under the Hull–White one-factor model, European options on zero-coupon bonds have a Black-type closed-form price; because a caplet is a put option on a zero-coupon bond, this formula prices caps and floors analytically and drives the standard calibration to cap vol quotes.

## Key Formula

Zero-coupon bond: $P(t,T) = A(t,T)\,e^{-B(t,T)\,r_t}$, where $B(t,T) = (1-e^{-a(T-t)})/a$.

**Bond call** (option to buy $P(T_0, T_1)$ at time $T_0$ for strike $X$):

$$C_0 = P(0,T_1)\,N(h) - X\,P(0,T_0)\,N(h - \sigma_P)$$

$$\sigma_P = \sigma\,B(T_0,T_1)\sqrt{\frac{1-e^{-2aT_0}}{2a}}, \qquad h = \frac{1}{\sigma_P}\ln\frac{P(0,T_1)}{X\,P(0,T_0)} + \frac{\sigma_P}{2}$$

**Caplet** on LIBOR $L(T_0, T_1)$ with day-count $\delta$ and strike $K_L$: the caplet pays $\delta\max(L - K_L, 0)$ at $T_1$, which equals $\frac{1+\delta K_L}{\delta}$ put options on $P(T_0, T_1)$ struck at $X = 1/(1+\delta K_L)$.

**Vol of vol** $\sigma_P$ encodes how uncertain the $T_1$-bond price is at $T_0$: longer accrual periods ($T_1 - T_0$) and slower mean reversion ($a \to 0$) both increase $\sigma_P$.

## Example

$T_0 = 1$ yr, $T_1 = 1.5$ yr ($\delta = 0.5$), $K_L = 4\%$, so $X = 1/1.02 = 0.9804$. Hull–White parameters $a = 0.1$, $\sigma = 0.01$. Current ZCB prices $P(0,1) = 0.960$, $P(0,1.5) = 0.934$.

$B(T_0, T_1) = (1-e^{-0.1\times0.5})/0.1 = 0.4877$

$\sigma_P = 0.01 \times 0.4877 \times \sqrt{(1-e^{-0.2})/0.2} = 0.01 \times 0.4877 \times 0.9516 \approx 0.464\%$

$h = \ln(0.934/(0.9804\times0.960))/0.00464 + 0.00464/2 \approx 0.47$ → caplet price $\approx 13$ bp of notional.

## Remember

The Hull–White bond-option formula is the engine behind cap calibration: swap desks strip the cap vol surface into individual caplet vols, then fit $a$ and $\sigma$ to minimise pricing errors across the strip. The mean-reversion speed $a$ controls how fast $B(T_0, T_1)$ saturates — high $a$ compresses longer caplet vols toward zero, creating a falling term structure of caplet vol. This is why $a$ is read off the slope of the cap vol curve rather than from bond prices: it is fundamentally a vol parameter, not just a rate-dynamics parameter.
