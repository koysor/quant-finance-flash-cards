# Out-of-Sample Yield Curve Extrapolation

**Topic:** Fixed Income
**Tags:** yield curve, extrapolation, ultimate forward rate, solvency ii, pension, eiopa
**Created:** 2026-06-20
**Author:** Claude Sonnet 4.6

---

## Definition

Out-of-sample yield curve extrapolation is the process of estimating interest rates beyond the last liquid market tenor by blending observed market rates with a long-run anchor — the Ultimate Forward Rate (UFR) — to produce a smooth, stable curve for discounting very long-dated liabilities.

## Key Formula

In the Nelson-Siegel family, as tenor $\tau \to \infty$, the extrapolated yield converges to the level parameter:

$$\lim_{\tau \to \infty} y(\tau;\,\boldsymbol{\theta}) = \beta_0$$

EIOPA's Smith-Wilson extrapolation blends market rates at the Last Liquid Point (LLP, typically 20Y for EUR) with the fixed UFR over a convergence horizon of 60Y:

$$y(\tau) = y_{\text{LLP}} + \left[\text{UFR} - y_{\text{LLP}}\right] \cdot \phi\!\left(\frac{\tau - \text{LLP}}{60 - \text{LLP}}\right), \quad \tau > \text{LLP}$$

where $\phi$ is a smooth convergence function (equal to zero at the LLP and one at the 60Y convergence point). The UFR is set by EIOPA — 3.45% for 2025.

## Example

EUR swap rates are liquid up to 50Y, but a Dutch pension fund must discount a liability maturing in 80Y. EIOPA's extrapolation blends the 20Y market rate (say 3.1%) with the 3.45% UFR, reaching full convergence at 60Y. A 10 bp reduction in the UFR (from 3.55% to 3.45%) raises the present value of that 80Y liability by roughly DV01(80Y) $\times$ 10 bp $\times$ notional — on a \$1 bn liability this can exceed \$50 m.

## Remember

Actuarial standards mandate a policy-set UFR rather than allowing the Nelson-Siegel $\beta_0$ to float freely in the fit, because a freely estimated long-rate can swing by tens of basis points when a single liquid instrument is added or repriced. Anchoring extrapolation to the UFR decouples pension balance sheets from short-run market noise at very long tenors — but it also means liabilities change when regulators revise the UFR, making the UFR itself a source of regulatory risk for insurers and pension funds.
