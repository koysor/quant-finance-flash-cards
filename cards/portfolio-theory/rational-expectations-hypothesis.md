# Rational Expectations Hypothesis

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** rational expectations, market efficiency, asset pricing, equilibrium, forecasting
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

The Rational Expectations Hypothesis (REH) states that economic agents form expectations about future variables using all available information and the correct model of the economy. Agents do not make systematic forecasting errors — their expectations equal the true expected value plus a random, unpredictable error.

## Key Formula

An agent's expectation of a variable $X_{t+1}$ formed at time $t$ satisfies:

$$\mathbb{E}_t[X_{t+1}] = \mathbb{E}[X_{t+1} \mid \mathcal{I}_t]$$

Where $\mathcal{I}_t$ is the full information set available at time $t$, including the correct model structure. The forecast error is:

$$X_{t+1} - \mathbb{E}_t[X_{t+1}] = \varepsilon_{t+1}, \qquad \mathbb{E}_t[\varepsilon_{t+1}] = 0$$

The error $\varepsilon_{t+1}$ is **mean-zero and uncorrelated** with any information available at time $t$ — if it were not, agents would use that information to improve their forecasts.

## Example

Under REH, the current forward rate $F_t$ for a currency should be an unbiased predictor of the future spot rate $S_{t+1}$:

$$F_t = \mathbb{E}_t[S_{t+1}]$$

A regression of $S_{t+1}$ on $F_t$ should yield a slope of 1 and a mean-zero residual. In practice, the **forward premium puzzle** — a slope significantly less than 1 — is one of the most persistent violations of REH in foreign exchange markets.

## Remember

REH is the macro foundation of the Efficient Markets Hypothesis: if agents are rational and use all available information, then asset prices — which aggregate those expectations — should fully reflect all information. The forward premium puzzle and the equity premium puzzle are both empirical rejections of REH, suggesting that risk premia, behavioural biases, or model uncertainty (ambiguity aversion) drive a wedge between rational expectations and observed prices.
