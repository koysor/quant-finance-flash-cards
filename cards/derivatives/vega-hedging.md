# Vega Hedging

**Topic:** Derivatives
**Tags:** vega hedging, vega neutral, volatility risk, options portfolio, risk management
**Created:** 2026-04-03
**Author:** Claude Opus 4.6

---

## Definition

Vega hedging is the practice of neutralising a portfolio's sensitivity to changes in implied volatility. While delta hedging removes exposure to the underlying's price movements, vega hedging removes exposure to shifts in the volatility surface. A **vega-neutral** portfolio has zero net vega, meaning its value is unaffected by parallel moves in implied volatility. Because options at different expiries have different vegas, vega hedging typically requires trading additional options — the underlying stock or futures cannot provide vega exposure.

## Key Formula

The portfolio vega is the sum of individual position vegas:

$$\mathcal{V}_{\text{portfolio}} = \sum_{k=1}^{n} N_k \, \mathcal{V}_k$$

where $N_k$ is the number of contracts and $\mathcal{V}_k$ is the vega per contract. To achieve vega neutrality using a hedging instrument with vega $\mathcal{V}_H$, the required hedge quantity is:

$$N_H = -\frac{\mathcal{V}_{\text{portfolio}}}{\mathcal{V}_H}$$

For **term-structure vega hedging** across two expiry buckets (short-dated vega $\mathcal{V}_S$ and long-dated vega $\mathcal{V}_L$), two hedging instruments are needed, solving:

$$\begin{pmatrix} \mathcal{V}_{S,1} & \mathcal{V}_{S,2} \\ \mathcal{V}_{L,1} & \mathcal{V}_{L,2} \end{pmatrix} \begin{pmatrix} N_1 \\ N_2 \end{pmatrix} = -\begin{pmatrix} \mathcal{V}_{S,\text{port}} \\ \mathcal{V}_{L,\text{port}} \end{pmatrix}$$

## Example

A derivatives desk has sold 3-month ATM calls, giving the book a vega of $-$£50,000 per 1% move in implied volatility. To hedge, the desk buys 3-month ATM straddles with vega of £2,000 each:

$$N_H = -\frac{-£50{,}000}{£2{,}000} = 25 \text{ straddles}$$

After the hedge, the book is vega-neutral. If implied volatility rises 2%, the loss on the short calls ($-$£100,000) is offset by the gain on the straddles (+£100,000). However, if the volatility surface tilts (short-dated vol rises but long-dated vol falls), the hedge may not protect perfectly because the straddles match only the aggregate vega, not the term-structure exposure.

## Remember

Vega hedging is essential for options market-makers and structured products desks who carry large inventories of options across strikes and expiries. Unlike delta hedging (which uses the underlying), vega hedging requires options — you cannot hedge volatility risk with stock. In practice, desks decompose vega exposure by expiry bucket and strike region, hedging each segment separately to manage term-structure and smile risk. The key challenge is that vega hedging is expensive: the hedging options carry their own theta, gamma, and bid-ask costs. For quant risk managers, the residual vega left after hedging — particularly in illiquid expiries or far-from-the-money strikes — is often the largest unhedged risk on a derivatives book.
