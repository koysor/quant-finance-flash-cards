# Brownian Bridge

**Topic:** Stochastic Processes
**Tags:** brownian bridge, conditional distribution, barrier monitoring, Monte Carlo, interpolation, Gaussian process
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **Brownian bridge** is a Brownian motion $W_t$ conditioned on its terminal value $W_T = b$. It is a Gaussian process that starts at 0, is pinned at $b$ at time $T$, and evolves stochastically in between. In quantitative finance it solves the **barrier-monitoring problem**: given only the simulated values of $S_{t_k}$ and $S_{t_{k+1}}$ at two discrete time steps, the Brownian bridge gives the exact probability that the continuous path crossed a barrier somewhere between those steps.

## Key Formula

**Conditional distribution** at time $t \in [0, T]$, given $W_T = b$:

$$W_t \mid W_T = b \;\sim\; N\!\left(\frac{b\,t}{T},\; \frac{t(T - t)}{T}\right)$$

**Barrier-crossing probability** between two steps. For a GBM path with $S_{t_k}$ and $S_{t_{k+1}}$ both above a lower barrier $B$, the probability that the path touched $B$ at some point in $(t_k, t_{k+1})$ is:

$$\Pr\!\left(\min_{t_k \leq s \leq t_{k+1}} S_s < B \;\middle|\; S_{t_k},\, S_{t_{k+1}}\right) = \exp\!\left(-\frac{2\ln(S_{t_k}/B)\,\ln(S_{t_{k+1}}/B)}{\sigma^2\,(t_{k+1} - t_k)}\right)$$

This follows from the reflection principle applied to the Brownian bridge. If either endpoint is below $B$, the option has already knocked out.

## Example

Daily Monte Carlo for a down-and-out call, barrier $B = 90$. At close of day 47: $S_{47} = 95$. At close of day 48: $S_{48} = 97$. Both are above the barrier, but did the intraday path dip below 90?

$$\Pr(\text{knocked out intraday}) = \exp\!\left(-\frac{2\ln(95/90)\,\ln(97/90)}{(0.25)^2 \times (1/252)}\right)$$

$$= \exp\!\left(-\frac{2 \times 0.0541 \times 0.0755}{0.0000992}\right) = \exp(-82.3) \approx 0\%$$

With both endpoints well above the barrier and $\sigma = 25\%$ over one day, the probability of an intraday breach is negligible. Repeat for a closer call: $S_{47} = 91$, $S_{48} = 93$:

$$\Pr = \exp\!\left(-\frac{2\ln(91/90)\ln(93/90)}{0.0000992}\right) = \exp\!\left(-\frac{2(0.0111)(0.0328)}{0.0000992}\right) \approx \exp(-7.35) \approx 0.064\%$$

Still small, but $6.4$ times out of $10{,}000$ steps — enough to matter for a large barrier book.

## Remember

Without the Brownian bridge correction, a daily Monte Carlo for a barrier option uses only end-of-day prices and systematically underestimates the probability of barrier breach: the true option value is lower (for knock-outs) than the discretely monitored price implies. The correction factor — multiplying each step's survival probability by $1 - \exp(-2 \ln(S_k/B)\ln(S_{k+1}/B)/(\sigma^2 \Delta t))$ — is exact under GBM and adds negligible computational cost. In practice, risk managers call this the **barrier monitoring adjustment**, and it is particularly important for options near the barrier and for products where the barrier is monitored continuously in the term sheet but priced with weekly or monthly Monte Carlo steps.
