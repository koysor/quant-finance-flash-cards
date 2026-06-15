# CRRA Utility

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** crra, constant relative risk aversion, utility function, risk aversion, power utility, consumption
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Constant Relative Risk Aversion (CRRA)** utility is the power-law family of utility functions in which the investor's risk aversion, measured relative to their wealth, is constant. It is the standard utility specification in macro-finance models because it is the only family consistent with balanced growth and with the observed stability of portfolio shares across wealth levels.

## Key Formula

$$U(C) = \begin{cases} \dfrac{C^{1-\gamma}}{1-\gamma} & \gamma \neq 1 \\[6pt] \ln C & \gamma = 1 \end{cases}$$

The **coefficient of relative risk aversion** $\gamma$ is constant:

$$\text{RRA}(C) = -\frac{C\,U''(C)}{U'(C)} = \gamma$$

The **stochastic discount factor** under CRRA with time-discount $\beta \in (0,1)$:

$$M_{t+1} = \beta\left(\frac{C_{t+1}}{C_t}\right)^{-\gamma}$$

Higher $\gamma$ means more curvature — the investor is more averse to consumption fluctuations and demands a larger risk premium for bearing them.

## Example

Consider two consumption paths for an investor with $\gamma = 3$, $\beta = 0.98$:

- **Path A:** $C_t = 1$, $C_{t+1} = 1.10$ (10% growth). $M_{t+1} = 0.98 \times (1.10)^{-3} \approx 0.98 \times 0.751 = 0.736$
- **Path B:** $C_t = 1$, $C_{t+1} = 0.90$ (10% fall). $M_{t+1} = 0.98 \times (0.90)^{-3} \approx 0.98 \times 1.372 = 1.344$

The SDF is much higher in the bad state — assets that pay off in recessions have a high SDF covariance and thus command a lower risk premium (investors are happy to overpay for insurance).

## Remember

CRRA utility underlies the CCAPM, Merton's continuous-time portfolio problem, and the Hansen–Jagannathan bound tests. The log-utility case ($\gamma = 1$) has the special property that the optimal portfolio share in risky assets is independent of wealth and horizon — the Kelly criterion. For $\gamma > 1$, investors reduce risky exposure as risk aversion rises; for $\gamma < 1$, they increase it. Empirical estimates of $\gamma$ from financial data tend to be 10–50, far higher than the values of 1–3 implied by experimental evidence — the source of the equity premium puzzle.
