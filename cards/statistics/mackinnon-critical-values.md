# MacKinnon Critical Values

**Topic:** Statistics
**Tags:** unit root, dickey-fuller, critical values, cointegration testing, sample size, hypothesis testing
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

MacKinnon critical values are response-surface estimates of the cut-off points for Dickey-Fuller and cointegration tests. Because the test statistic does not follow a standard distribution under the null of a unit root, its critical values must be simulated, and MacKinnon's tables express them as a function of sample size rather than as fixed numbers.

## Key Formula

The critical value for a given significance level is fitted as a response surface in the number of observations:

$$CV(N_{obs}) = \beta_\infty + \frac{\beta_1}{N_{obs}} + \frac{\beta_2}{N_{obs}^2}$$

The $\beta_\infty$ term is the asymptotic value; the correction terms matter in small samples. Separate coefficient sets apply for each deterministic specification (no constant, constant, constant plus trend) and, for cointegration tests, for each number of variables in the system.

Critically, the values are **more negative** than standard normal or $t$ cut-offs — around $-3.4$ at 5% for a constant-only ADF regression, against $-1.65$ for a one-sided normal test.

## Example

For an ADF test with a constant, 5% level, with $\beta_\infty = -2.861$, $\beta_1 = -2.738$, $\beta_2 = -8.36$:

At $N_{obs} = 100$:

$$CV = -2.861 - \frac{2.738}{100} - \frac{8.36}{10{,}000} = -2.861 - 0.0274 - 0.0008 = -2.889$$

At $N_{obs} = 500$ it tightens to $-2.867$. A test statistic of $-2.88$ therefore rejects the unit root at 100 observations but *fails* to reject at 500 — the same number, opposite conclusions.

## Remember

Using the wrong critical values is the most common way a pairs-trading study reaches a false conclusion, and it has a specific history: Python's Dickey-Fuller values were simply wrong until 2017, when they were corrected to MacKinnon's 2010 table. Two traps persist. Testing a residual that was itself estimated by regression requires **cointegration** critical values, not plain ADF ones — the residual has been chosen to look as stationary as possible, so the null is easier to reject by construction and the cut-off must be more demanding. And the Engle-Granger and Phillips-Ouliaris implementations in some packages still rest on tables simulated in the 1990s on only a few hundred replications. The deeper lesson is Fischer Black's: a single stationarity test never establishes a tradeable spread, so vary the sample period and form your own view of what economically drives the relationship.
