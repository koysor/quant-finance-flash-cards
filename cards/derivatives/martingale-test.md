# Martingale Test

**Topic:** Derivatives
**Tags:** martingale, validation, monte carlo, discounted price, model checking, numerical methods
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **martingale test** is a diagnostic check that verifies whether a numerical pricing implementation correctly produces risk-neutral dynamics. Under the risk-neutral measure $\mathbb{Q}$, the discounted asset price must be a martingale, so the sample average of discounted terminal prices across simulated paths should approximately equal the initial price. A failure indicates a bug in the simulation, discretisation error, or an incorrect model specification.

## Key Formula

The test checks whether:

$$\frac{1}{N}\sum_{i=1}^{N} e^{-rT} S_T^{(i)} \approx S_0$$

where $S_T^{(i)}$ is the terminal stock price on simulated path $i$, $r$ is the risk-free rate, $T$ is the time horizon, and $N$ is the number of paths.

The test statistic under the null hypothesis (correct implementation) is:

$$z = \frac{\bar{S}_{\text{disc}} - S_0}{s / \sqrt{N}}$$

where $\bar{S}_{\text{disc}}$ is the sample mean of discounted terminal prices and $s$ is the sample standard deviation. Reject correctness if $|z| > 1.96$ at the 5% level.

## Example

A quant simulates $N = 100{,}000$ paths of GBM with $S_0 = £100$, $r = 5\%$, $\sigma = 20\%$, $T = 1$ year.

The sample mean of $e^{-0.05}S_T$ across all paths is £100.03, with sample standard deviation $s = £20.10$.

$$z = \frac{100.03 - 100.00}{20.10 / \sqrt{100{,}000}} = \frac{0.03}{0.0636} = 0.47$$

Since $|0.47| < 1.96$, the test passes — the simulation correctly produces martingale discounted prices.

If instead the quant had accidentally used $\mu = 10\%$ instead of $r = 5\%$ as the drift, the mean would be approximately $£100 \times e^{(0.10 - 0.05)} \approx £105.13$, giving $z \approx 80.7$ — an immediate failure flagging the error.

## Remember

The martingale test is the first quality check that every quantitative developer runs after implementing a pricing engine. Before trusting any option price from a Monte Carlo simulation, finite difference solver, or tree model, the quant verifies that the underlying asset satisfies the martingale condition. On trading desks, this test catches common implementation errors: using the wrong drift, incorrect time stepping, errors in the discretisation scheme (e.g. Euler vs Milstein), or accidentally correlating the discount factor with the asset price. It is computationally cheap (it reuses the simulated paths) and provides immediate, unambiguous feedback — making it the standard "smoke test" in quantitative finance software development.
