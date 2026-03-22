# Option Premium Decomposition

**Topic:** Derivatives
**Tags:** options, premium, intrinsic value, extrinsic value, time value
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Option premium decomposition** splits the market price of an option into two components: **intrinsic value** (the payoff if exercised immediately) and **extrinsic value** (also called time value — the additional amount reflecting the probability of further favourable moves before expiry). Every factor that affects option pricing maps onto one of these two components.

## Key Formula

$$\text{Premium} = \underbrace{\max(S - K, \; 0)}_{\text{intrinsic (call)}} \;+\; \underbrace{\text{Extrinsic value}}_{\text{time value}}$$

$$\text{Premium} = \underbrace{\max(K - S, \; 0)}_{\text{intrinsic (put)}} \;+\; \underbrace{\text{Extrinsic value}}_{\text{time value}}$$

Extrinsic value depends on:

- **Time to expiry** $T$ — more time means more chance of a favourable move
- **Volatility** $\sigma$ — higher volatility widens the distribution of $S_T$
- **Interest rates** $r$ — affect the present value of the strike

At expiry, extrinsic value is always zero: $\text{Premium}\big|_{T=0} = \text{Intrinsic value}$.

## Example

A stock trades at £108. A European call with $K = £100$ is priced at £12.

- **Intrinsic value** = $\max(108 - 100, 0) = £8$
- **Extrinsic value** = £12 − £8 = **£4**

A European put with $K = £100$ on the same stock is priced at £2.50.

- **Intrinsic value** = $\max(100 - 108, 0) = £0$ (out of the money)
- **Extrinsic value** = £2.50 − £0 = **£2.50** (the entire premium is extrinsic)

## Remember

The decomposition explains why OTM options still have value despite zero intrinsic value — their entire premium is extrinsic, reflecting the market's probabilistic assessment of finishing in the money. In quantitative finance, this decomposition is essential for understanding theta (extrinsic value decays to zero), vega (volatility inflates extrinsic value), and the early exercise decision for American options — early exercise is only rational when the interest earned on intrinsic value exceeds the extrinsic value sacrificed.
