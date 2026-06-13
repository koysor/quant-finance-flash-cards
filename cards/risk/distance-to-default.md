# Distance to Default

**Topic:** Risk
**Tags:** distance to default, KMV, Moody's analytics, EDF, credit risk, Merton model
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **distance to default (DD)** is the number of standard deviations that a firm's asset value stands above its default threshold, measured in one year's time under the risk-neutral (or real-world) distribution of log-asset returns. It is the key output of the KMV/Moody's Analytics implementation of the Merton structural model and feeds directly into the **Expected Default Frequency (EDF)** — the probability that the firm defaults within the next twelve months.

## Key Formula

Under GBM with asset drift $\mu_V$ and asset volatility $\sigma_V$, the log-asset value in one year is:

$$\ln V_1 \sim N\!\left(\ln V_0 + \left(\mu_V - \tfrac{1}{2}\sigma_V^2\right),\; \sigma_V^2\right)$$

**Distance to default** to a default point $D_P$ (typically short-term debt plus half long-term debt):

$$\text{DD} = \frac{\ln(V_0/D_P) + (\mu_V - \tfrac{1}{2}\sigma_V^2)}{\sigma_V}$$

**Expected Default Frequency** (real-world, using drift $\mu_V$):

$$\text{EDF} = N(-\text{DD}) = \Pr(V_1 < D_P)$$

In practice, KMV maps DD to EDF using an **empirical default database** rather than the normal CDF: the theoretical $N(-\text{DD})$ understates EDF for investment-grade firms at short horizons because the normal distribution has thin tails relative to observed defaults. The Merton risk-neutral version uses $r$ instead of $\mu_V$, giving $d_2$ from the Black-Scholes formula.

**Calibration** — $V_0$ and $\sigma_V$ are unobservable but determined from two simultaneous equations using observed equity price $E_0$ and equity volatility $\sigma_E$:

$$E_0 = V_0 N(d_1) - D_P e^{-r} N(d_2), \qquad \sigma_E E_0 = \sigma_V V_0 N(d_1)$$

## Example

Firm: equity market cap $E_0 = £50\text{m}$, $\sigma_E = 40\%$, short-term debt £30m, half of long-term debt £20m → $D_P = £50\text{m}$. Solving the two equations gives $V_0 \approx £95\text{m}$, $\sigma_V \approx 22\%$, $\mu_V = 8\%$.

$$\text{DD} = \frac{\ln(95/50) + (0.08 - 0.024)}{0.22} = \frac{0.641 + 0.056}{0.22} \approx 3.17$$

$$\text{EDF}_{\text{theoretical}} = N(-3.17) \approx 0.08\%$$

A DD of 3.17 means the firm's assets must fall by more than 3 standard deviations to hit the default point — considered safe by KMV standards (DD > 4 is "very safe"; DD < 1 is "distressed"). After mapping through the empirical database, the actual EDF might be 0.15–0.30%, reflecting fat-tailed empirical default rates.

## Remember

Distance to default is the dominant early-warning credit signal used by banks and rating agencies because it combines **balance sheet information** (the default point $D_P$) with **market information** (implied $V_0$ and $\sigma_V$ from equity). A falling DD preceded the failures of Bear Stearns and Lehman Brothers by months, dropping below 2.0 well before ratings agencies downgraded them. The key limitation is the reliance on equity market data: for private firms, $\sigma_E$ is unobservable, requiring proxy estimation from comparable public firms. For this reason, KMV scores are most reliable for large-cap public companies and lose accuracy for small or thinly traded firms.
