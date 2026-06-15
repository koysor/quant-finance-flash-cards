# Yield Curve Theories

**Topic:** Fixed Income
**Tags:** yield curve, expectations hypothesis, liquidity preference, market segmentation, term premium, term structure
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

Three classical theories explain why the yield curve has the shape it does. They differ in whether investors are willing to substitute freely across maturities and whether a maturity-specific risk premium exists.

## Key Formula

All three can be expressed through the **yield decomposition**:

$$y(t, T) = \underbrace{\frac{1}{T-t}\int_t^T E_t^{\mathbb{P}}[r_s]\,ds}_{\text{expected future short rates}} + \underbrace{\text{TP}(t,T)}_{\text{term premium}}$$

| Theory | Term Premium | Substitution across maturities |
|--------|-------------|-------------------------------|
| **Pure Expectations** | $\text{TP} = 0$ | Perfect |
| **Liquidity Preference** | $\text{TP} > 0$, rising with $T-t$ | Partial |
| **Market Segmentation** | Arbitrary, segment-specific | None |

Under pure expectations, a normal (upward-sloping) curve means the market expects short rates to rise. Under liquidity preference, the curve can slope upward even when short rates are expected to remain flat.

## Example

The 2-year yield is 3.80% and the 10-year yield is 4.30%. The 50 bp spread can be decomposed as:

- **Pure expectations view:** markets expect rates to rise ~50 bp over the decade
- **Liquidity preference view:** markets may expect flat rates, but 10-year buyers require ~50 bp extra for duration risk
- **Segmentation view:** 10-year buyers (pension funds) and 2-year buyers (money market funds) are separate pools, and supply/demand in each determines rates independently

## Remember

The term premium decomposition matters for central bank communication: when the Fed says "monetary policy is tight," they mean real short rates are elevated, not that yields are high. A steep yield curve with flat expected short rates means the term premium has risen — often a sign of fiscal uncertainty or inflation risk, not expected monetary tightening. The ACM model (Adrian-Crump-Moench) is the most cited decomposition of US Treasury yields into expected rate and term premium components, published by the New York Fed.
