# Time Decay

**Topic:** Derivatives
**Tags:** options, time decay, theta, time value, expiry
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Time decay** is the erosion of an option's time value as expiry approaches. Measured by the Greek **theta** ($\Theta$), it reflects the diminishing probability that a favourable move in the underlying will occur before the option expires. All else being equal, an option is worth less today than it was yesterday.

## Key Formula

For a European ATM call under Black–Scholes:

$$\Theta_{\text{call}} = -\frac{S_0 \, N'(d_1) \, \sigma}{2\sqrt{T}} - r K e^{-rT} N(d_2)$$

where $N'(d_1) = \frac{1}{\sqrt{2\pi}} e^{-d_1^2/2}$ is the standard normal PDF.

The time value component of any option satisfies:

$$\text{Time value} = V - \max(\text{intrinsic value}, \; 0)$$

and decays to zero at expiry: $\text{Time value}\big|_{T=0} = 0$.

For an ATM option, time value scales approximately as:

$$\text{Time value} \approx 0.4 \, \sigma \, S \, \sqrt{T}$$

showing the characteristic **square-root decay** — half the time remaining does not halve the time value, it reduces it by a factor of $1/\sqrt{2} \approx 0.71$.

## Example

An ATM call has $S_0 = K = £100$, $\sigma = 25\%$, $T = 0.25$ years, $\Theta = -£0.05$ per day.

- Today's time value $\approx 0.4 \times 0.25 \times 100 \times \sqrt{0.25} = £5.00$
- Tomorrow (all else equal): time value falls by roughly £0.05 to £4.95
- With 1 week left ($T \approx 0.02$): time value $\approx 0.4 \times 0.25 \times 100 \times \sqrt{0.02} \approx £1.41$

The decay accelerates sharply in the final weeks — this is why short-dated options lose value so rapidly.

## Remember

Time decay is the option seller's edge and the buyer's cost of carrying optionality. In quantitative finance, the non-linear acceleration of theta near expiry is critical for strategy selection: sellers of options (e.g. covered calls, iron condors) harvest theta most efficiently in the final 30–45 days, while buyers prefer longer-dated options where theta burn is slower per day. The square-root relationship means that doubling the time to expiry only increases the option price by about 41%, not 100%.
