# Hansen–Jagannathan Bound

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** hansen jagannathan, sharpe ratio, stochastic discount factor, equity premium puzzle, asset pricing, volatility bound
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **Hansen–Jagannathan (HJ) bound** is a necessary condition that any valid stochastic discount factor must satisfy: the ratio of the SDF's standard deviation to its mean must be at least as large as the maximum Sharpe ratio achievable by any portfolio. It is a model-free test of asset pricing theories.

## Key Formula

For any SDF $M$ that prices assets correctly:

$$\frac{\text{std}(M)}{E[M]} \geq \max_i \left|\frac{E[R^i] - R_f}{\text{std}(R^i)}\right| = \text{SR}_{\max}$$

Equivalently, the **HJ volatility bound** says the SDF must be at least as volatile (relative to its mean) as the maximum observed Sharpe ratio in the market:

$$\text{std}(M) \geq E[M] \cdot \text{SR}_{\max} = \frac{\text{SR}_{\max}}{R_f}$$

The bound is **tight**: the minimum-variance SDF that prices a given set of assets exactly meets it with equality.

## Example

Empirically, the US equity market has had a Sharpe ratio of approximately $0.40$ annually, with $E[M] \approx 1/(1+R_f) \approx 0.97$.

The HJ bound requires: $\text{std}(M) \geq 0.97 \times 0.40 \approx 0.39$.

Under the standard CRRA consumption CAPM with risk aversion $\gamma = 2$ and annual consumption growth volatility $\sigma_c = 1\%$, the implied $\text{std}(M) \approx \gamma \sigma_c = 0.02$ — far below the required 0.39. Matching the bound requires $\gamma \approx 39$, implying implausible risk aversion.

## Remember

The HJ bound is the most concise statement of the **equity premium puzzle**: observed Sharpe ratios are too high to be explained by an SDF implied by reasonable investor preferences over aggregate consumption. This has driven 30 years of theoretical innovation — habit formation (Campbell-Cochrane), rare disaster models (Barro, Rietz), long-run risk (Bansal-Yaron), and ambiguity aversion — all designed to make the SDF volatile enough to clear the HJ hurdle without requiring unreasonably high risk aversion.
