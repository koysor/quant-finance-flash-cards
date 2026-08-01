# kth-to-Default Basket CDS

**Topic:** Derivatives
**Tags:** basket cds, credit exotic, default correlation, premium leg, default leg, fair spread
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

A kth-to-default basket credit default swap is an over-the-counter credit exotic written on a small pool of reference names, typically five. The protection seller pays out once — when the $k$-th name in the basket defaults — and the contract terminates at that point, regardless of how many names default afterwards.

## Key Formula

The fair spread equates the expected default leg to the expected premium leg:

$$s = \frac{\langle DL\rangle}{\langle PL\rangle} = \frac{(1-R)\sum_{i=1}^{m} Z(0,t_i)\left[F_k(t_i) - F_k(t_{i-1})\right]}{\Delta t \sum_{i=1}^{m} Z(0,t_i)\left[1 - F_k(t_i)\right]}$$

where $R$ is the recovery rate, $Z(0,t_i)$ the risk-free discount factor, $\Delta t$ the accrual fraction, and $F_k$ the cumulative distribution of the $k$-th default time $\tau_k$.

$F_k$ has no closed form, so the spread is obtained by Monte Carlo: sample correlated uniforms from a copula, convert each to a default time using that name's hazard rates, sort them, and take the $k$-th. Average the two legs across paths **separately**, then divide once:

$$\mathbb{E}[s] = \frac{\text{mean}(DL)}{\text{mean}(PL)} \neq \text{mean}\!\left(\frac{DL}{PL}\right)$$

## Example

Five names, £2m notional each, $T = 5$ years, $R = 40\%$. Simulated default times for one path are $\tau = (2.1,\ 3.4,\ 4.8,\ 6.2,\ 7.0)$ years.

- **1st-to-default:** $\tau_1 = 2.1 < 5$, so protection pays. Loss $= (1 - 0.40)\times\tfrac{1}{5}\times £10\text{m} = £1.2\text{m}$, discounted from $t = 2.1$.
- **3rd-to-default:** $\tau_3 = 4.8 < 5$, still triggers, but only just.
- **5th-to-default:** $\tau_5 = 7.0 > 5$, no payout on this path.

Averaged over 10,000 paths the fair spreads come out around 22 bps, 10 bps and 1.6 bps for the 1st, 2nd and 5th respectively — each successive $k$ requires more defaults, so it is strictly cheaper.

## Remember

The basket is the simplest product that makes **default correlation** a priced quantity rather than a risk-management afterthought, which is why it is the standard teaching route into tranched products such as CDOs. The intuition runs through the two extremes: at zero correlation the names default independently, so at least one failing is near-certain and the 1st-to-default spread approaches the sum of the individual spreads, while the 5th-to-default is nearly worthless; as correlation rises towards one the names default together, and every $k$-th spread converges to the single-name spread. The 1st-to-default therefore behaves like a CDO **equity tranche** — it is short correlation — and the senior $k$ are long it. A model validation check falls straight out of this: spreads must decrease in $k$, and if your simulation ever prices the 3rd above the 2nd, the default-time sorting or the leg accounting is wrong.
