# Gaussian Copula in Credit Portfolio Modelling

**Topic:** Risk
**Tags:** Gaussian copula, credit correlation, CDO, default correlation, Li model, structured products
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **Gaussian copula** model for credit portfolios (Li, 2000) links individual obligors' default times through a common multivariate normal distribution. Each obligor $i$ is assigned a latent variable $X_i = \sqrt{\rho}\,Z + \sqrt{1-\rho}\,\varepsilon_i$, where $Z$ is a shared **systemic factor** and $\varepsilon_i$ is an idiosyncratic shock, both standard normal. Obligor $i$ defaults by time $T$ if $X_i$ falls below the threshold $\Phi^{-1}(\text{PD}_i)$. The single parameter $\rho$ — the pairwise asset correlation — controls how clustered defaults are across the portfolio.

## Key Formula

**Conditional default probability** given the systemic factor $Z = z$:

$$\text{PD}_i(z) = \Phi\!\left(\frac{\Phi^{-1}(\text{PD}_i) - \sqrt{\rho}\,z}{\sqrt{1 - \rho}}\right)$$

**Unconditional joint default probability** (integrate out $Z$):

$$\Pr(\tau_i \leq T,\; \tau_j \leq T) = \Phi_2\!\left(\Phi^{-1}(\text{PD}_i),\; \Phi^{-1}(\text{PD}_j);\; \rho\right)$$

where $\Phi_2(\cdot,\cdot;\rho)$ is the bivariate normal CDF with correlation $\rho$.

**Large homogeneous portfolio (LHP) loss distribution** (Vasicek, 1987) — portfolio loss fraction $L$ given $\rho$ and uniform $\text{PD}$:

$$\Pr(L \leq x) = \Phi\!\left(\frac{\sqrt{1-\rho}\,\Phi^{-1}(x) - \Phi^{-1}(\text{PD})}{\sqrt{\rho}}\right)$$

CDO tranche losses are then priced by integrating this distribution over the attachment and detachment points of each tranche.

## Example

Portfolio of 100 investment-grade bonds, each with $\text{PD} = 2\%$, $\text{LGD} = 60\%$, asset correlation $\rho = 0.20$.

**Conditional PD** given a severe systemic shock $Z = -2$ (a 2-standard-deviation bad year):

$$\text{PD}(z{=}{-2}) = \Phi\!\left(\frac{\Phi^{-1}(0.02) + 2\sqrt{0.20}}{\sqrt{0.80}}\right) = \Phi\!\left(\frac{-2.054 + 0.894}{0.894}\right) = \Phi(-1.297) \approx 9.7\%$$

Under stress, individual 2% obligors behave as if they each have a 9.7% default rate — nearly 5× higher — because the systemic shock affects all of them simultaneously. The equity tranche (absorbs first losses) is devastated; the senior tranche (above 10% losses) is hit far harder than the independent-default model would predict.

At $\rho = 0$: defaults are independent, portfolio loss is tightly concentrated near $100 \times 2\% \times 60\% = £1.2\%$ of notional. Senior tranches are virtually risk-free.

At $\rho \to 1$: either nobody defaults or everybody defaults. The senior tranche is now nearly as risky as the equity tranche — the correlation "transfers" risk from equity to senior.

## Remember

The Gaussian copula model became the dominant CDO pricing tool in 2004–2007 because it collapsed all default correlation into a single tradeable parameter: **implied correlation**, analogous to implied volatility. Traders quoted CDO tranches in correlation space, just as option traders quote in vol space. The model's fatal flaw was that the Gaussian distribution has **thin tails**: in the copula, very bad systemic outcomes (extreme left tail of $Z$) are underweighted relative to empirical experience. When US house prices fell simultaneously across all states in 2007 — a correlation event far in the tail — the senior AAA tranches that the model priced as near-risk-free suffered catastrophic losses. The **correlation smile** (different implied correlations for different tranches from the same CDO) is the direct analogue of the volatility smile: it reveals that the market does not believe the Gaussian copula's single-$\rho$ assumption.
