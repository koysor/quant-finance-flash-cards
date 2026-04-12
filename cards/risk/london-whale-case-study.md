# Case Study: The London Whale

**Topic:** Risk
**Tags:** var, model risk, governance, case study, tail risk, credit derivatives
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

In 2012, JPMorgan Chase — widely regarded as having best-in-class risk management — suffered multi-billion-dollar losses from a synthetic credit derivative portfolio run by Bruno Iksil (nicknamed the "London Whale") at its Chief Investment Office (CIO) in London.

As the portfolio grew to systemic proportions, JPMorgan **switched its VaR model mid-crisis**. The new model produced materially lower VaR figures, mechanically masking the true scale of risk and allowing positions to keep growing. When credit markets moved against the trades, realised losses reached **\$6.2 billion** — far beyond what either the old or the new VaR model had reported.

The US Senate Permanent Subcommittee on Investigations concluded:

> "Risk limit breaches were routinely disregarded, risk metrics were frequently criticised or downplayed, and risk evaluation models were targeted by bank personnel seeking to produce artificially lower capital requirements."

## Key Formula

Four lessons, each with a concrete implication for risk practice:

| Lesson | Implication |
|---|---|
| **VaR can be gamed** | Model choice directly affects reported risk; switching to a more favourable model reduces VaR on paper without reducing actual exposure |
| **VaR ≠ worst case** | VaR is a threshold, not a ceiling — losses in the tail can be multiples of the reported VaR figure, as the \$6.2 bn loss demonstrated |
| **Culture matters** | Risk governance must be structurally independent of trading desks; proximity creates pressure to validate, not challenge, positions |
| **Model risk is real** | A wrong or manipulated model provides false security — the institution may be unaware of its true risk until losses crystallise |

## Example

**Timeline of the London Whale episode:**

1. **2012 Q1** — The CIO's Synthetic Credit Portfolio (SCP) grew to notional exposure exceeding \$150 billion in credit default swap indices (CDX.NA.IG.9).
2. **Late January 2012** — JPMorgan switched from its old VaR model to a new "Basel II.5" model. The new model reported VaR approximately **50% lower** than the old model for the same positions.
3. **April 2012** — External traders noted the unusual size of the positions, press reports named Iksil the "London Whale", and JPMorgan's CEO initially dismissed concerns as "a tempest in a teapot".
4. **May–June 2012** — Credit markets moved against the book; losses crystallised rapidly. Final mark-to-market loss: **\$6.2 billion**.
5. **Post-mortem** — The Senate investigation found the model switch was approved internally with inadequate scrutiny, and that risk limit breaches had been waived or ignored for months.

The gap between reported VaR and actual loss illustrates that VaR measures the threshold of the loss distribution, not the severity of tail outcomes.

## Remember

The London Whale is the canonical example of **model risk in a governance failure context**. Two separate problems compounded each other:

- **Technical**: VaR is a quantile measure — it says nothing about losses beyond the threshold. A \$500 m VaR is consistent with a \$6 bn tail loss.
- **Behavioural**: Model selection became a tool to manage reported risk rather than actual risk. The switch to a lower-VaR model was convenient, not scientifically motivated.

**Expected Shortfall (ES)** is harder to game in this way: because it averages losses *beyond* the VaR threshold, a model producing a low ES must also assume moderate tail losses — there is less room to manufacture a favourable figure without distorting the entire tail. This is one reason FRTB (2016) replaced 99% VaR with 97.5% ES as the regulatory capital metric.
