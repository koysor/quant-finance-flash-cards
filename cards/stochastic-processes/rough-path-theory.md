# Rough Path Theory

**Topic:** Stochastic Processes
**Tags:** rough path theory, controlled rough paths, lyons, non-semimartingale, signature, rough volatility
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Rough path theory** (Lyons, 1998) provides a rigorous framework for defining and solving differential equations driven by irregular signals — including fractional Brownian motion with $H < \tfrac{1}{2}$ — that are not semimartingales and therefore outside the scope of Itô calculus. A rough path lifts a path $X$ to the pair $(X, \mathbb{X})$ where $\mathbb{X}$ encodes the iterated integrals of $X$ against itself, supplying the "missing information" that regularity alone cannot provide.

## Key Formula

For a path $X: [0,T] \to \mathbb{R}^d$, the **rough path lift** is the pair $\mathbf{X} = (X, \mathbb{X})$ where the **Lévy area** (second-order iterated integral) is:

$$\mathbb{X}^{ij}_{s,t} = \int_s^t (X^i_r - X^i_s)\,dX^j_r$$

A **controlled rough path** $Y$ satisfies $Y_t - Y_s \approx Y'_s(X_t - X_s)$ for a derivative process $Y'$, generalising the Itô stochastic integral. Solutions to rough differential equations (RDEs):

$$dY_t = f(Y_t)\,d\mathbf{X}_t$$

exist and are unique for $f$ sufficiently smooth, even when $X = W^H$ with $H > \tfrac{1}{4}$.

## Example

The **path signature** $S(X)_{0,T} = \left(1, \int_0^T dX, \int_0^T\!\int_0^t dX_s\,dX_t, \ldots\right)$ is the sequence of all iterated integrals of a path. For a stock price path, the signature encodes all statistical features of the path in a universal linear representation. A linear map on the signature can approximate any continuous functional of the path — a result that underpins **signature-based feature engineering** in quantitative finance, where the first 20 signature terms replace hand-engineered technical indicators as inputs to ML models.

## Remember

Rough path theory resolves the fundamental obstacle to using fractional Brownian motion in finance: fBm with $H < \tfrac{1}{2}$ is not a semimartingale, so Itô's lemma and the classical stochastic integral are undefined. By lifting fBm to a rough path $\mathbf{W}^H = (W^H, \mathbb{W}^H)$ using the Mandelbrot-Van Ness Volterra representation, rough volatility models achieve mathematical rigour without abandoning the roughness that matches empirical vol dynamics. The **signature** is the applied side of rough path theory — its universal approximation property for path functionals makes it a theoretically grounded alternative to RNNs for sequential financial data, where the iterated integrals of the price path replace manually designed time-series features.
