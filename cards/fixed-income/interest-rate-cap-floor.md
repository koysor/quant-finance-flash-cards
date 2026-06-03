# Interest Rate Cap and Floor

**Topic:** Fixed Income
**Tags:** cap, floor, caplet, floorlet, interest rate options, black model, libor
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

An **interest rate cap** is a series of European call options (caplets) on a floating reference rate — it pays the holder when the rate exceeds a strike level, protecting a floating-rate borrower from rising rates. A **floor** is the corresponding series of put options (floorlets), protecting a fixed-rate lender from falling rates. Caps and floors are the most liquid interest rate options and the primary calibration instruments for Hull-White and LMM.

## Key Formula

Each **caplet** for period $[T_k, T_{k+1}]$ pays $\delta_k \max(L_k - K, 0)$ at $T_{k+1}$, where $L_k$ is the LIBOR/SOFR rate fixed at $T_k$, $K$ is the strike, and $\delta_k$ is the accrual fraction. Under **Black's model** (log-normal rates):

$$\text{Caplet}(T_k) = P(0, T_{k+1})\,\delta_k\!\left[F_k N(d_1) - K N(d_2)\right]$$

$$d_{1,2} = \frac{\ln(F_k/K) \pm \tfrac{1}{2}\sigma_k^2 T_k}{\sigma_k\sqrt{T_k}}$$

where $F_k$ is the forward rate for $[T_k, T_{k+1}]$, $\sigma_k$ is the **caplet vol**, and $P(0, T_{k+1})$ is the discount factor. The **cap price** is $\sum_k \text{Caplet}(T_k)$ and satisfies **put-call parity**:

$$\text{Cap} - \text{Floor} = \text{Swap}$$

## Example

A 2-year 3% cap on 3-month LIBOR (8 quarterly caplets). Forward rates are 2.8%–3.5% across the 8 periods; caplet vols are 25%–35% (higher for shorter maturities — the vol term structure). The cap costs 45 bps upfront. A corporate CFO paying floating on a £50m loan buys this cap for £225k to eliminate the risk of LIBOR rising above 3% over the next 2 years.

## Remember

The **implied vol surface for caps** is the primary calibration target for all short-rate and forward-rate models — Hull-White is calibrated to match ATM caplet vols across maturities, and LMM is calibrated to match caplet vols by construction (each forward rate is log-normal). For RL, a TDBP agent trained on Hull-White paths learns to price individual caplets; the cap price is then the sum of individual caplet predictions, which can be evaluated in parallel — one network forward pass per caplet. The **cap-floor-swap parity** provides a model-free arbitrage check: any RL pricer whose cap and floor prices violate this parity has a bug in its sign convention or discounting.
