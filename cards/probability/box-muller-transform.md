# Box–Muller Transform

**Topic:** Probability
**Tags:** simulation, random number generation, normal distribution, Monte Carlo, sampling
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The **Box–Muller transform** is an algorithm that converts two independent uniform random variables $U_1, U_2 \sim \text{Uniform}(0, 1)$ into two independent standard normal variables $Z_1, Z_2 \sim N(0, 1)$. It exploits the polar symmetry of the bivariate normal distribution to avoid evaluating the inverse CDF $\Phi^{-1}$, making it both exact and computationally efficient.

## Key Formula

**Basic form:**

$$Z_1 = \sqrt{-2 \ln U_1}\;\cos(2\pi U_2)$$
$$Z_2 = \sqrt{-2 \ln U_1}\;\sin(2\pi U_2)$$

The term $R = \sqrt{-2 \ln U_1}$ generates the radial component (a Rayleigh-distributed radius), and $\theta = 2\pi U_2$ generates a uniform angle. Together they produce a point $(Z_1, Z_2)$ drawn from the standard bivariate normal.

| Input | Output | Distribution |
|---|---|---|
| $U_1 \sim U(0,1)$ | $Z_1 \sim N(0,1)$ | Standard normal |
| $U_2 \sim U(0,1)$ | $Z_2 \sim N(0,1)$ | Standard normal |

## Example

Draw $U_1 = 0.25$ and $U_2 = 0.80$:

$$R = \sqrt{-2 \ln 0.25} = \sqrt{-2 \times (-1.3863)} = \sqrt{2.7726} = 1.6651$$

$$\theta = 2\pi \times 0.80 = 5.0265 \text{ radians}$$

$$Z_1 = 1.6651 \times \cos(5.0265) = 1.6651 \times 0.3090 = 0.5145$$

$$Z_2 = 1.6651 \times \sin(5.0265) = 1.6651 \times (-0.9511) = -1.5837$$

From two uniform draws we have generated two independent standard normal samples: $Z_1 \approx 0.51$ and $Z_2 \approx -1.58$.

## Remember

The Box–Muller transform is the workhorse behind normal random number generation in Monte Carlo engines. Every time a quant simulates a stock price path via $S_T = S_0 \exp((\mu - \tfrac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z)$, the $Z$ value is typically produced by Box–Muller or its polar variant (Marsaglia's method). It generates two normals per call with only a logarithm and trigonometric functions — no iterative root-finding for $\Phi^{-1}$. For pricing path-dependent derivatives like Asian or barrier options via Monte Carlo, millions of $Z$ draws are needed per simulation run, so the speed and exactness of Box–Muller directly affect both the accuracy and the wall-clock time of the pricing engine.
