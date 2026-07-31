# OTM-Splice Skew Construction

**Topic:** Volatility
**Tags:** volatility smile, out-of-the-money, put-call parity, skew, interpolation, liquidity filtering
**Created:** 2026-07-07
**Author:** Claude Sonnet 5

---

## Definition

The **OTM-splice** is a practical rule for building one clean implied volatility smile at each expiry from noisy option quotes: use only out-of-the-money puts for strikes below the forward and out-of-the-money calls for strikes above it, joining the two halves at the forward. Deep in-the-money options trade rarely and carry wide bid-ask spreads, so any smile built including them inherits that noise; OTM options on both wings are the liquid, tightly-quoted side of the market for their respective strikes.

## Key Formula

At log-moneyness $y = \ln(K/F_T)$, the spliced implied volatility is:

$$\sigma_{\text{imp}}^{\text{spliced}}(y) = \begin{cases} \sigma_{\text{imp}}^{\text{put}}(y) & y \le 0 \\ \sigma_{\text{imp}}^{\text{call}}(y) & y > 0 \end{cases}$$

Equivalently, restrict to calls only and recover put implied volatilities via put-call parity, $C(K) - P(K) = D_T(F_T - K)$, since a European call and put at the same strike and expiry imply identical volatility under Black-Scholes — the choice of which side to quote from is a liquidity decision, not a modelling one.

## Example

At one expiry, the $y = -0.15$ (OTM put) strike quotes a tight 0.30-vol-point bid-ask spread on the put, but the ITM call at the same strike quotes a 2.5-vol-point spread — ten times wider, because few traders buy deep ITM calls when a synthetic long (long call, short put, or simply the underlying) is cheaper to trade. Building the $y=-0.15$ point of the smile from the put's 0.30-point spread rather than the call's 2.5-point spread gives a materially more reliable input to the curvature calculation used two steps later in a local volatility pipeline.

## Remember

The OTM-splice matters most for exactly the calculation that comes right after it: the curvature $\partial_{KK}$ of the reconstructed price surface, which feeds both the Breeden-Litzenberger risk-neutral density check and the Dupire local variance formula. Second derivatives amplify noise quadratically, so feeding them the widest-spread, most stale quotes on the surface — deep ITM options — is the single easiest way to manufacture a spurious butterfly arbitrage violation that has nothing to do with the market and everything to do with data quality. The OTM-splice is a cheap, model-free liquidity filter applied before any interpolation or differentiation begins, in the same spirit as the Box Rate method's use of put-call parity to keep inputs internally consistent.
