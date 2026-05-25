# Transfer Entropy

**Topic:** Computational Finance
**Tags:** transfer entropy, information flow, lead-lag, causality, granger causality, time series
**Created:** 2026-05-25
**Author:** Claude Sonnet 4.6

---

## Definition

**Transfer entropy** $T_{X \to Y}$ measures the directed flow of information from process $X$ to process $Y$ — specifically, how much knowing the past of $X$ reduces uncertainty about the next value of $Y$ beyond what $Y$'s own past already provides. Unlike correlation or mutual information, transfer entropy is asymmetric and captures the direction of statistical influence.

## Key Formula

$$T_{X \to Y} = H(Y_t \mid Y_{t-1}) - H(Y_t \mid Y_{t-1}, X_{t-1})$$

Equivalently as a KL divergence:

$$T_{X \to Y} = \sum_{y_t, y_{t-1}, x_{t-1}} p(y_t, y_{t-1}, x_{t-1}) \log \frac{p(y_t \mid y_{t-1}, x_{t-1})}{p(y_t \mid y_{t-1})}$$

**Key properties:**
- $T_{X \to Y} \geq 0$, equal to zero iff $X_{t-1} \perp Y_t \mid Y_{t-1}$
- $T_{X \to Y} \neq T_{Y \to X}$ in general — asymmetry reveals directionality
- Reduces to Granger causality in the Gaussian case

## Example

Testing whether US equity order flow $X$ leads European equity returns $Y$. Using 1-minute bins over 60 trading days:

$$T_{X \to Y} = 0.043 \text{ bits}, \qquad T_{Y \to X} = 0.009 \text{ bits}$$

The asymmetry ($T_{X \to Y} \gg T_{Y \to X}$) confirms that US order flow contains predictive information about European returns beyond what European returns themselves reveal — consistent with the US market being the price-discovery leader for global equity risk. A symmetric result would indicate bidirectional coupling with no clear leader.

## Remember

Transfer entropy is the information-theoretic generalisation of Granger causality: where Granger causality tests for linear predictive improvement in a VAR framework, transfer entropy detects any statistical dependence (linear or non-linear) between the pasts of two processes. In quantitative finance, transfer entropy is used to map information flow across assets — for instance, identifying which equity index leads credit spreads, which currency pair leads commodity prices, or which order book variable leads the mid-price. It is also used to study contagion: during crises, transfer entropy from distressed assets to previously unrelated assets increases sharply, revealing channels of propagation that correlation matrices miss because they are symmetric and lag-blind. The main practical challenge is estimation: transfer entropy requires joint density estimation in high dimensions, and insufficient data leads to biased estimates that statistical tests (permutation testing or bootstrap) must correct for.
