# Monte Carlo Standard Error

**Topic:** Computational Finance
**Tags:** monte carlo, standard error, confidence interval, discretisation bias, convergence
**Created:** 2026-11-19
**Author:** Claude Opus 5.5

---

## Definition

A Monte Carlo price is a sample average, so it carries statistical error. Its standard error is the sample standard deviation of the discounted payoffs divided by the square root of the number of paths, and it gives a confidence interval for the true price. When paths come from a discretised SDE there is also a bias from the time step, which more paths do not remove. The total error is the two combined.

## Key Formula

With $N$ discounted payoffs of sample mean $\hat{V}$ and sample standard deviation $s$:

$$\text{SE} = \frac{s}{\sqrt{N}}, \qquad \text{95\% CI} = \hat{V} \pm 1.96\,\frac{s}{\sqrt{N}}$$

With a scheme of weak order 1 and $M$ time steps, the root-mean-square error is

$$\text{RMSE} = \sqrt{\text{bias}^2 + \text{SE}^2} \approx \sqrt{\left(\frac{c}{M}\right)^2 + \frac{s^2}{N}}$$

## Example

10,000 paths give a mean discounted payoff of $£10.48$ with sample standard deviation $£14.70$:

$$\text{SE} = \frac{14.70}{\sqrt{10{,}000}} = £0.147, \qquad \text{95\% CI} = 10.48 \pm 0.288 = [£10.19,\ £10.77]$$

Halving the standard error to $£0.074$ needs four times as many paths, 40,000. For a fixed budget of $N \times M$ path-steps, the two error terms balance when $N$ grows like $M^2$: doubling the number of time steps calls for four times as many paths.

## Remember

A Monte Carlo price without its standard error is not a result: two runs that differ by less than two standard errors agree. The $1/\sqrt{N}$ rate holds in any dimension, which is why Monte Carlo wins for baskets and path-dependent products where grids are hopeless, but it is slow. Every extra decimal place costs a hundred times more paths. That is the case for variance reduction and quasi-random numbers. And because more paths cannot fix a biased time step, a desk sizing a simulation must budget for both errors, not just the one the confidence interval shows.
