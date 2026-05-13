# A Priori vs A Posteriori

**Topic:** Statistics
**Tags:** a priori, a posteriori, Bayesian, prior, posterior, epistemology
**Author:** Claude Sonnet 4.6

---

## Definition

*A priori* knowledge is derived from reasoning, theory, or assumptions before observing data. *A posteriori* knowledge is derived from observed evidence. In statistics, the prior distribution is an a priori belief about a parameter; the posterior distribution is the a posteriori belief after incorporating data.

## Key Formula

Bayes' theorem is the formal bridge between the two:

$$\underbrace{p(\theta \mid \text{data})}_{\text{a posteriori}} \;\propto\; \underbrace{p(\text{data} \mid \theta)}_{\text{likelihood}} \times \underbrace{p(\theta)}_{\text{a priori}}$$

The prior $p(\theta)$ encodes what is assumed before evidence; the posterior $p(\theta \mid \text{data})$ encodes what is inferred after.

## Example

An analyst wants to estimate the equity risk premium (ERP). Two approaches:

- **A priori**: CAPM theory implies $\text{ERP} = \beta \times (\bar{r}_M - r_f)$. Using a long-run market return of 7% and risk-free rate of 2%, the a priori ERP is 5% — derived from a theoretical model, no new data required.
- **A posteriori**: OLS regression of last 36 months of excess returns gives $\hat{\text{ERP}} = 3.8\%$ — a purely data-driven estimate.

A Bayesian analyst blends the two: the Black–Litterman model uses the CAPM equilibrium returns as the a priori prior and investor views as the a posteriori update, producing a posterior estimate of ~4.5%.

## Remember

The a priori / a posteriori distinction maps directly onto the two sides of quantitative finance. **Model-based pricing** (Black–Scholes, CAPM, risk-neutral discounting) is a priori: conclusions follow from theoretical assumptions before a single data point is observed. **Empirical estimation** (historical volatility, OLS betas, implied parameters) is a posteriori: conclusions follow from fitting models to observed returns. The Black–Litterman model is the clearest practical example of formally combining both — a priori equilibrium weights are updated by a posteriori investor views using Bayes' theorem, producing portfolio allocations that neither ignores theory nor blindly follows data.
