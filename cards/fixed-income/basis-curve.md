# Basis Curve

**Topic:** Fixed Income
**Tags:** basis curve, interest rates, ois, libor, cross-currency basis, spread
**Created:** 2026-03-11
**Author:** claude-sonnet-4-6

---

## Definition

A **basis curve** is a spread curve showing the difference in rates between two benchmark interest rate curves at each maturity. The most common examples are the LIBOR-OIS basis (unsecured versus risk-free rates) and the cross-currency basis (the spread required to exchange funding in one currency for another via FX swaps). Basis curves are non-zero because the two reference rates carry different credit, liquidity, or funding risks.

## Key Formula

For a single-currency basis between Curve A and Curve B at maturity $T$:

$$\text{Basis}(T) = r_A(T) - r_B(T)$$

In cross-currency basis swaps, one party pays a floating rate plus a basis spread $b$ in currency 1 and receives a floating rate in currency 2:

$$r_{\text{USD, float}} + b = r_{\text{GBP, float}}$$

where $b$ is quoted in basis points and is negative when USD funding is scarce relative to GBP. The basis deviates from zero when covered interest rate parity (CIP) fails:

$$F = S \cdot \frac{(1 + r_{\text{USD}} + b)}{(1 + r_{\text{GBP}})}$$

where $S$ is the spot FX rate and $F$ is the forward rate.

## Example

In October 2008, the 3-month cross-currency basis for EUR/USD reached $-$150 basis points. This meant that a European bank wishing to borrow USD for 3 months by swapping EUR into USD had to pay 150 bps below USD LIBOR — because there was excess demand for USD funding from European institutions and insufficient supply, driving the basis deeply negative. Under normal conditions the same basis was near zero.

## Remember

Basis curves matter enormously for derivatives pricing after the 2008 crisis. Before the crisis, practitioners assumed all floating-rate curves were interchangeable and discounted everything on a single LIBOR curve. The crisis revealed that LIBOR-OIS, tenor basis (e.g. 3M vs 6M LIBOR), and cross-currency basis are all distinct and non-zero. Modern multi-curve frameworks build a separate discount curve (OIS) and separate forward curves for each tenor, with the basis between them captured explicitly. Ignoring basis can lead to material mispricings in interest rate swaps and cross-currency derivatives.
