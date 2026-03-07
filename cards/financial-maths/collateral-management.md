# Collateral Management

**Topic:** Financial Mathematics
**Tags:** collateral, margin, variation margin, haircut, counterparty risk
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Collateral management is the operational framework for posting, receiving, valuing, and adjusting assets pledged as security against financial obligations. It spans repos, derivatives, and securities lending, ensuring that exposure between counterparties is continuously covered by high-quality assets.

## Key Formula

The **required collateral** to cover a derivatives exposure with haircut $h$:

$$C = \frac{\text{MTM Exposure}}{1 - h}$$

where MTM is the mark-to-market value of the derivative.

**Variation margin** (VM) adjusts collateral daily to reflect changes in exposure:

$$\text{VM Call}_t = \text{MTM}_t - \text{MTM}_{t-1}$$

The **total collateral requirement** under a Credit Support Annex (CSA):

$$C_{\text{total}} = \max\left(\text{MTM} - \text{Threshold} - \text{MTA}, \; 0\right)$$

where Threshold is the unsecured exposure allowed and MTA is the minimum transfer amount.

## Example

A bank has a £5 million mark-to-market exposure on a swap portfolio with its counterparty. The CSA specifies a threshold of £1 million, an MTA of £250,000, and a haircut of 5% on posted gilts.

$$C_{\text{required}} = \max(5{,}000{,}000 - 1{,}000{,}000 - 250{,}000, \; 0) = £3{,}750{,}000$$

In gilt terms:

$$\text{Gilts to post} = \frac{3{,}750{,}000}{1 - 0.05} = £3{,}947{,}368$$

The next day, the MTM rises to £5.8 million. The variation margin call is:

$$\text{VM} = 5{,}800{,}000 - 5{,}000{,}000 = £800{,}000$$

## Remember

Collateral management became a systemically important function after the 2008 crisis, when uncleared derivatives left counterparties with uncovered exposures. Post-crisis reforms (EMIR, Dodd-Frank) mandate daily variation margin exchange and initial margin for non-centrally cleared derivatives. For quantitative analysts, collateral transforms affect derivatives pricing — the cheapest-to-deliver collateral option, the currency of the collateral, and the haircut schedule all influence the effective discount rate. The concept of **collateral optimisation** has emerged, where firms algorithmically allocate their cheapest eligible assets to margin calls, minimising the cost of meeting regulatory requirements.
