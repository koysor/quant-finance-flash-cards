# Brennan–Schwartz Model

**Topic:** Fixed Income
**Tags:** Brennan-Schwartz, two-factor, spot rate, long rate, yield spread, observable factors, finite-time explosion
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Brennan–Schwartz (1979) model uses the short rate $r$ and the long-term consol yield $l$ as two directly observable state variables, exploiting the intuition that the slope $l - r$ drives mean-reversion; it is historically the first two-factor term structure model.

## Key Formula

$$dr = \bigl(\alpha_1 + \beta_1 r + \gamma_1(l - r)\bigr)dt + \sigma_1 r\,dX_1$$

$$dl = \bigl(\alpha_2 + \beta_2 l + \gamma_2(r - l)/l\bigr)dt + \sigma_2 l\,dX_2, \qquad \mathbb{E}[dX_1\,dX_2] = \rho\,dt$$

The spread $l - r$ appears in both drifts, creating mutual mean-reversion: short rates are pulled toward the long rate, and the long rate is anchored by its own mean-reversion $\beta_2 l$.

No closed-form bond price exists; numerical PDE methods are required.

## Example

$r = 3\%$, $l = 5\%$, $\gamma_1 = 0.5$: the short rate feels a drift $+0.5(5\% - 3\%) = +1\%$ from the spread term, pulling it toward the long rate. The long rate simultaneously feels a small pull back toward $r$, creating a self-consistent yield-curve dynamics — but the lognormal-type diffusion terms $\sigma_1 r$ and $\sigma_2 l$ mean that $l$ can grow without bound.

## Remember

Brennan–Schwartz was influential for using two observable yields as state variables — a natural economic choice — but the model has a fatal flaw: the lognormal-type diffusion ($\sigma_2 l$) allows the long rate to explode to infinity in finite time with positive probability. This mathematical failure, identified by subsequent researchers, means the model is rarely used in practice despite its intuitive design. It illustrates how economic appeal and mathematical admissibility are separate requirements when building term structure models.
