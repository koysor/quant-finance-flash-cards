# Netting Set and CSA

**Topic:** Banking Regulation
**Tags:** netting set, csa, isda, collateral, threshold, rehypothecation
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

A netting set is the legally defined group of OTC derivative trades governed by a single ISDA Master Agreement, within which close-out netting applies: if either party defaults, all trades in the set are terminated and netted to a single payment. The Credit Support Annex (CSA) is the collateral agreement appended to the Master Agreement, specifying the rules for posting Variation Margin and Initial Margin — including thresholds, minimum transfer amounts, eligible collateral, and rehypothecation rights.

## Key Formula

The net exposure of a netting set determines collateral requirements and SA-CCR EAD:

$$\text{Net MtM} = \sum_{i \in \text{netting set}} V_i$$

The CSA defines the **collateral to post** as:

$$\text{VM to post} = \max\!\left(\text{Net MtM} - \text{Threshold},\; 0\right) - \text{balance already posted}$$

rounded up to the **Minimum Transfer Amount (MTA)**. Key CSA parameters:

| Parameter | Typical value | Effect |
|---|---|---|
| Threshold (TH) | £0–£50 m | Uncollateralised exposure below TH |
| MTA | £100k–£1 m | Minimum size of each transfer |
| Rehypothecation | Permitted / forbidden | Receiver may reuse posted collateral |
| Eligible collateral | Cash, govts, IG bonds | Affects haircuts and operational complexity |

## Example

A CSA has Threshold = £5 m, MTA = £500k. If the net MtM is £8 m and £2 m collateral has already been posted, the additional VM required = max(£8 m − £5 m, 0) − £2 m = £3 m − £2 m = £1 m. Since £1 m > MTA = £500k, the transfer is made.

## Remember

The CSA terms materially affect both counterparty credit risk and funding: a zero-threshold, daily-margined CSA (standard post-2016 for large dealers) virtually eliminates uncollateralised exposure, while a £50 m threshold creates a persistent credit exposure of up to £50 m that must be capitalised under SA-CCR. Rehypothecation rights — allowing the collateral receiver to repost the same assets as their own collateral — create funding efficiency but also rehypothecation chains that amplify systemic fragility: in 2008, the freezing of rehypothecation chains was a major amplifier of the liquidity crisis, as securities pledged multiple times became unavailable to all parties simultaneously.
