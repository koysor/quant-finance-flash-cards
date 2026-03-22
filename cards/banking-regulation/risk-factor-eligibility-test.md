# Risk Factor Eligibility Test

**Topic:** Banking Regulation
**Tags:** FRTB, modellability, NMRF, expected shortfall, market data, regulation
**Created:** 2026-03-11
**Author:** Claude Sonnet 4.6

---

## Definition

The **Risk Factor Eligibility Test (RFET)** is the FRTB assessment that determines whether a risk factor used in an internal model may be included in the Expected Shortfall (ES) calculation. A risk factor is **modellable** only if there are at least 24 verified real price observations in the prior 12 months, with no single gap between consecutive observations exceeding 90 calendar days. Risk factors that fail the RFET are classified as **Non-Modellable Risk Factors (NMRFs)** and must receive a separate, typically more punitive, stress capital add-on.

## Key Formula

A risk factor $f$ is modellable if both of the following hold:

$$N_{\text{obs}}(f) \geq 24 \quad \text{over the trailing 12 months}$$

$$\max_{i} \Delta t_i \leq 90 \text{ days}$$

where $N_{\text{obs}}$ is the count of distinct, verifiable real transactions or committed quotes, and $\Delta t_i$ is the number of calendar days between the $i$-th and $(i+1)$-th consecutive observations. The NMRF stress scenario capital charge is:

$$\text{SES}_{\text{NMRF}} = \sqrt{\sum_{k} \rho_{k}^{2} \, \text{SES}_{k}^{2} + \left(1 - \rho_{k}\right)^{2} \sum_{k} \text{SES}_{k}^{2}}$$

where $\text{SES}_k$ is the stress expected shortfall for each NMRF bucket and $\rho_k$ is the within-bucket correlation parameter specified by the regulator.

## Example

A bank models a 10-year EUR interest rate swap using a mid-curve swaption volatility surface. During the prior 12 months:

- The 10Y×1Y point has 31 observed committed quotes, with a longest gap of 22 days → **passes** RFET; included in ES.
- The 30Y×10Y point has only 8 observed transactions, with a gap of 112 days in August → **fails** RFET; classified as NMRF; requires a separate stress scenario add-on.

The bank must calculate ES excluding the NMRF and add the NMRF stress capital separately before aggregating into total market risk capital.

## Remember

RFET is the mechanism by which FRTB enforces market discipline: only risk factors with genuine, frequent price discovery earn the right to be modelled using a bank's own historical data. Illiquid, thinly traded risk factors — such as long-dated cross-currency basis spreads or exotic implied volatility points — typically fail and attract higher capital charges. In practice, RFET failure drives banks to either source more price data via data-pooling utilities, or to reduce exposure to positions that are NMRF-intensive.
