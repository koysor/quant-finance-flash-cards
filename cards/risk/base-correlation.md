# Base Correlation

**Topic:** Risk
**Tags:** cdo tranche, implied correlation, correlation skew, gaussian copula, equity tranche, structured credit
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

Base correlation is the single Gaussian-copula correlation that reprices a hypothetical **equity tranche** running from 0% up to a given detachment point. Quoting correlation this way rather than tranche by tranche removes the ambiguity and non-existence problems that afflict compound correlation.

## Key Formula

A tranche spanning attachment $a$ to detachment $d$ is decomposed into the difference of two base tranches:

$$V_{[a,d]} = V_{[0,d]}(\rho_d) - V_{[0,a]}(\rho_a)$$

Each base tranche $[0,x]$ is priced under the one-factor Gaussian copula with its own correlation $\rho_x$, extracted by bootstrapping upwards from the equity tranche. The market's quoted correlations form a rising curve in $d$ — the **correlation skew**:

$$\rho_{3\%} < \rho_{7\%} < \rho_{10\%} < \rho_{15\%}$$

Compound correlation, which solves for one $\rho$ per tranche directly, can have two roots or none for mezzanine tranches, because their value is not monotone in correlation. Base correlation is monotone by construction, so the bootstrap always has a unique solution.

## Example

An iTraxx portfolio quotes base correlations of 20% at the 3% detachment point and 32% at 7%.

The 3–7% mezzanine tranche is then priced as the 0–7% base tranche at $\rho = 32\%$ minus the 0–3% base tranche at $\rho = 20\%$. Using one blended correlation of, say, 26% for both legs would misprice it, because each leg must be valued at the correlation the market actually assigns to its own detachment point.

The upward slope says the market pays more for senior protection than a single-correlation model implies — it prices in more systemic, everything-fails-together risk than the Gaussian copula generates on its own.

## Remember

Base correlation is best understood as the credit market's analogue of the implied volatility smile: it is not a belief about how correlated defaults truly are, but the adjustment that forces an acknowledged-wrong model to match traded prices. The correlation skew exists because the Gaussian copula has no tail dependence, so it systematically understates the probability of many names defaulting together, and senior tranches — which only pay out in exactly that scenario — must therefore be repriced upward through a higher correlation input. That is the same deficiency a Student's t copula addresses structurally rather than by parameter adjustment. The practical warning is that interpolating base correlation between quoted detachment points can produce **negative implied tranche losses**, an arbitrage that signals the interpolation rather than the market is at fault.
