# Fundamental Theorems of Asset Pricing

**Topic:** Derivatives
**Tags:** no-arbitrage, equivalent martingale measure, complete market, asset pricing, FTAP
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The **Fundamental Theorems of Asset Pricing** (FTAP) are two results that connect the economic concepts of no-arbitrage and market completeness to the mathematical existence and uniqueness of an equivalent martingale measure. Together they provide the rigorous foundation for all derivative pricing.

## Key Formula

**First Fundamental Theorem:**

$$\text{No arbitrage} \iff \exists\;\text{equivalent martingale measure } \mathbb{Q}$$

Under $\mathbb{Q}$, discounted asset prices are martingales:

$$E^{\mathbb{Q}}\!\left[e^{-rT}S_T \mid \mathcal{F}_0\right] = S_0$$

**Second Fundamental Theorem:**

$$\text{Market is complete} \iff \mathbb{Q} \text{ is unique}$$

| Condition | Equivalent Martingale Measure |
|---|---|
| Arbitrage-free, complete | Exactly one $\mathbb{Q}$ — unique prices |
| Arbitrage-free, incomplete | Many $\mathbb{Q}$'s — a range of no-arbitrage prices |
| Arbitrage exists | No $\mathbb{Q}$ exists |

## Example

In the Black–Scholes model (one stock, one Brownian motion), the risk-neutral measure is uniquely determined by setting $\theta = (\mu - r)/\sigma$. The market is complete: every contingent claim can be replicated, and every derivative has a unique no-arbitrage price.

Add stochastic volatility (a second source of randomness $dW_t^{(2)}$ with no traded asset to hedge it): now infinitely many equivalent martingale measures exist, each assigning a different price to volatility risk. The market is incomplete — option prices are no longer unique, and the trader must choose a measure (equivalently, a volatility risk premium) based on calibration or preferences.

## Remember

The FTAP tells you precisely when derivative pricing "works." The first theorem justifies the entire risk-neutral pricing programme: if there is no arbitrage, then prices can be computed as discounted $\mathbb{Q}$-expectations. The second theorem explains why Black–Scholes gives a single price (complete market, unique $\mathbb{Q}$) while stochastic volatility models produce a family of prices that must be pinned down by market calibration (incomplete market, multiple $\mathbb{Q}$'s). In practice, every time a quant calibrates a model to market prices of vanilla options, they are implicitly selecting one $\mathbb{Q}$ from the many that are consistent with no-arbitrage — the second theorem is why calibration is necessary.
