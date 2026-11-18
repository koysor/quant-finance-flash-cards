# abcd Volatility Parametrisation

**Topic:** Fixed Income
**Tags:** abcd, instantaneous volatility, libor market model, caplet calibration, humped volatility
**Created:** 2026-11-18
**Author:** Claude Opus 5.5

---

## Definition

The abcd form (popularised by Rebonato) gives the instantaneous volatility of each forward rate in a LIBOR market model as a function of its time to expiry $\tau = T_i - t$ alone, with four parameters. It produces the humped shape seen in the market, where forwards expiring in one to two years are the most volatile, and because it depends only on $\tau$ the volatility structure looks the same tomorrow as today (time-homogeneous). A scaling factor $k_i$ per forward then matches each caplet price exactly.

## Key Formula

$$\sigma_i(t) = k_i\Big[(a + b\,\tau)\,e^{-c\,\tau} + d\Big], \qquad \tau = T_i - t$$

Short end $a + d$, long end $d$, hump at $\tau^* = \dfrac{1}{c} - \dfrac{a}{b}$ (with $a + d > 0$, $c > 0$, $d > 0$). Calibrating to the Black caplet volatility $\sigma_i^{\text{Black}}$:

$$k_i^2 = \frac{\left(\sigma_i^{\text{Black}}\right)^2 T_i}{\displaystyle\int_0^{T_i}\Big[(a + b(T_i - s))\,e^{-c(T_i - s)} + d\Big]^2 ds}$$

## Example

With $a = 0.05$, $b = 0.5$, $c = 1.5$, $d = 0.12$:

- at $\tau = 0$: $0.05 + 0.12 = 17.0\%$
- hump at $\tau^* = 1/1.5 - 0.05/0.5 = 0.567$ years: $(0.05 + 0.5 \times 0.567)e^{-0.85} + 0.12 = 26.2\%$
- at $\tau = 10$: about $12.0\%$

For a caplet expiring at $T = 2$, the root-mean-square of this curve over its life is $22.7\%$. If the market quotes $20\%$, then $k = 0.20 / 0.227 = 0.88$.

## Remember

The abcd form keeps an interest-rate model's future volatility realistic. Fitting each caplet with an arbitrary time-dependent volatility can match today's prices while implying a smile and term structure tomorrow that look nothing like the market's, which mis-prices anything that depends on future volatility, such as Bermudan swaptions. If the fitted $k_i$ stay close to 1, the four parameters explain the market well. If they swing widely, the model is being forced.
