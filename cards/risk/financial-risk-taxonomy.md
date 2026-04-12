# Financial Risk Taxonomy

**Topic:** Risk
**Tags:** market risk, credit risk, liquidity risk, operational risk, risk classification, Basel III
**Created:** 2026-04-12
**Author:** Claude Sonnet 4.6

---

## Definition

Financial risk is conventionally divided into two primary categories:

**Market risk** is the risk of loss from adverse movements in market prices. Regulators and practitioners sub-divide it into:

- **Equity risk** — losses from falls in share prices
- **Interest rate risk** — losses from shifts in yield curves (general) or spread widening on specific bonds (specific)
- **FX risk** — losses from exchange rate movements
- **Commodity risk** — losses from price moves in energy, metals, and agricultural products

Each category splits further into *general market risk* (broad market moves) and *specific risk* (idiosyncratic moves in individual instruments), plus *gap risk* (sudden large jumps rather than smooth drift).

**Credit risk** is the risk of loss when a counterparty fails to meet its financial obligations. Sub-types include:

- **Transaction risk** — loss on a single trade or loan
- **Portfolio concentration risk** — excess exposure to a single issuer, sector, or geography
  - *Issue risk* — risk tied to a specific bond or instrument
  - *Issuer risk* — risk tied to the borrowing entity
  - *Counterparty risk* — risk that the other side of a derivative defaults before settlement

Beyond these two primary categories: **liquidity risk** (inability to sell or fund positions), **operational risk** (process, system, or human failures), **model risk** (errors in quantitative models), and **regulatory risk** (adverse changes in rules or capital requirements).

## Key Formula

No single equation governs the taxonomy, but the categories map directly to capital charges under Basel III:

| Risk Type | Primary Driver | Regulatory Capital Approach |
|---|---|---|
| Market risk — general | Index or rate moves | IMA (Internal Models Approach) or Standardised Approach |
| Market risk — specific | Issuer spread / jump-to-default | Included in IMA; DRC charge under SA |
| Credit risk — counterparty | Default before settlement | CVA capital charge; IMM or SA-CCR |
| Credit risk — portfolio | Concentration / correlation | IRB or Standardised Approach |
| Liquidity risk | Funding outflows | LCR (30-day stress) and NSFR (structural) |

## Example

Two landmark crises illustrate the distinction:

**Market risk — 2020 oil price crash:** In April 2020, WTI crude futures fell to −$37 per barrel. Banks and funds holding long commodity positions suffered immediate mark-to-market losses purely from price moves — no counterparty failed. This is textbook market risk: the loss arose from a market price, not a default.

**Credit risk — Lehman Brothers 2008:** When Lehman filed for bankruptcy in September 2008, counterparties holding OTC derivatives, repo agreements, and unsecured bonds suffered losses because Lehman *failed to pay*, not because a market price moved against them. This is textbook credit risk: the loss arose from a counterparty's inability to meet its obligations.

## Remember

Basel III enforces the taxonomy in capital rules. **Market risk capital** is computed using either the Internal Models Approach (IMA, based on Expected Shortfall at 97.5% over 10 days) or the Standardised Approach (SA, sensitivity-based buckets) under FRTB — applied to the *trading book*. **Credit risk capital** is computed using the Internal Ratings-Based approach (IRB, based on PD, LGD, EAD) or the Standardised Approach — applied to the *banking book*. The boundary between trading book and banking book is strictly controlled, because the capital treatment differs substantially: trading-book positions can use market risk models, whilst banking-book positions attract credit risk charges. Getting the taxonomy wrong means holding the wrong amount of capital against the wrong risk.
