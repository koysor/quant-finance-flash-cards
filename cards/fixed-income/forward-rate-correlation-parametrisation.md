# Forward-Rate Correlation Parametrisation

**Topic:** Fixed Income
**Tags:** libor market model, correlation, factor reduction, pca, forward rates
**Created:** 2026-11-19
**Author:** Claude Opus 5.5

---

## Definition

A multifactor forward-rate model such as the LIBOR market model needs the correlation between every pair of forward rates. Instead of estimating each entry separately, it is usually parametrised so that forwards with nearby expiries are highly correlated and the correlation decays with the gap between them. The full matrix is then often approximated with only a few driving factors, by keeping its largest principal components and rescaling so each forward still has unit variance.

## Key Formula

Exponential decay in the gap between expiries $T_i$ and $T_j$:

$$\rho_{ij} = e^{-\beta\,\lvert T_i - T_j \rvert}, \qquad \beta > 0$$

Rank-$m$ reduction: with eigenvalues $\lambda_1 \ge \dots \ge \lambda_m$ and eigenvectors $v_k$ of $\rho$, set $b_{ik} = v_{ik}\sqrt{\lambda_k}$, rescale each row of $B$ to unit length, and use

$$\rho \approx B B^\top, \qquad dW_i = \sum_{k=1}^{m} b_{ik}\,dZ_k$$

## Example

Five forwards expiring at 1 to 5 years with $\beta = 0.1$:

- neighbours one year apart: $\rho = e^{-0.1} = 0.905$
- the 1-year and 5-year forwards: $\rho = e^{-0.4} = 0.670$

The eigenvalues are $4.30,\ 0.44,\ 0.14,\ 0.08,\ 0.06$, so two factors carry $94.6\%$ of the total. The rank-2 approximation keeps the ends close ($0.676$ instead of $0.670$) but pushes neighbouring correlations up to $0.988$ instead of $0.905$, a largest error of about $0.10$.

## Remember

Correlation decides how much forwards can move independently, and products that pay on the shape of the curve, such as spread options and Bermudan swaptions, are priced on exactly that. A one-factor model makes every forward perfectly correlated and so values these products wrongly. Cutting to two or three factors speeds up simulation a lot, but the example shows the cost: nearby forwards become more correlated than they should be, so check the reduced matrix against the products you price before relying on it.
