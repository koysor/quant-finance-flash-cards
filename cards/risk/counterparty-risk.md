# Counterparty Risk

**Topic:** Risk
**Tags:** counterparty risk, credit risk, default, OTC derivatives, CVA, exposure
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Counterparty risk (or counterparty credit risk) is the risk that the other party to a financial contract will default on its obligations before the contract's final settlement. It is most significant in over-the-counter (OTC) derivatives, securities lending, and repo agreements where there is no central exchange guaranteeing performance. The risk is bilateral — both parties face it — and its magnitude depends on the current mark-to-market value of the contract, the probability of default, and the recovery rate.

## Key Formula

The **expected exposure** at time $t$ is:

$$\text{EE}(t) = E\bigl[\max(V(t), 0)\bigr]$$

where $V(t)$ is the mark-to-market value of the contract. Only positive values matter because the counterparty's default only harms you when they owe you money.

The **credit valuation adjustment** (CVA) prices counterparty risk into the contract:

$$\text{CVA} = (1 - R) \int_0^T \text{EE}(t) \, dP_{\text{default}}(t)$$

where $R$ is the recovery rate, $T$ is the contract maturity, and $P_{\text{default}}(t)$ is the cumulative default probability up to time $t$.

## Example

A bank holds an interest rate swap with a counterparty whose 5-year default probability is 2% and expected recovery rate is 40%. The expected positive exposure averages £5 million over the life of the swap.

$$\text{CVA} \approx (1 - 0.40) \times £5{,}000{,}000 \times 0.02 = 0.60 \times £100{,}000 = £60{,}000$$

The bank should charge £60,000 upfront (or adjust the swap rate) to compensate for the risk that the counterparty defaults while the swap has positive value.

## Remember

Counterparty risk became a central concern in quantitative finance after the 2008 financial crisis, when the collapse of Lehman Brothers left its counterparties with billions in unrecoverable obligations. Today, CVA desks at major banks actively price and hedge this risk, and regulators require banks to hold capital against it (Basel III CVA capital charge). For hedge funds, counterparty risk is concentrated in the prime brokerage relationship — if a prime broker fails, the fund may lose access to its assets, borrowed securities, and margin financing simultaneously.
