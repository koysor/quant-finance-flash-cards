# Signature-Based Option Pricing

**Topic:** Computational Finance
**Tags:** path signature, option pricing, linear model, path-dependent, rough path, exotic options
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Signature-based option pricing** uses the truncated path signature of a price trajectory as a universal feature map, then fits a linear model on those features to price path-dependent options. By the universal approximation theorem for signatures, any continuous pricing functional can be approximated as a linear map on a sufficiently deep signature — replacing neural networks with a transparent, auditable linear model that respects the path's full sequential structure.

## Key Formula

For a price path $X: [0,T] \to \mathbb{R}^d$ with signature truncated at depth $N$, the option price approximation is:

$$\hat{C}(X) = \langle \mathbf{w},\, S^{\le N}(X)_{0,T}\rangle = \sum_{k=0}^{N}\sum_{i_1,\ldots,i_k} w^{i_1\cdots i_k}\cdot S(X)^{i_1\cdots i_k}_{0,T}$$

Training minimises the squared pricing error across simulated paths:

$$\min_{\mathbf{w}} \sum_{j=1}^{M} \Bigl(\hat{C}(X^{(j)}) - C_{\text{ref}}(X^{(j)})\Bigr)^2$$

The reference prices $C_{\text{ref}}$ come from Monte Carlo, closed-form (where available), or Longstaff-Schwartz.

## Example

An arithmetic Asian call with $N = 6$ averaging dates. A linear model on the depth-4 signature of $(S_t, t)$ uses $1 + 2 + 4 + 8 + 16 = 31$ features. Trained on 20,000 GBM paths with Kemna-Vorst Monte Carlo reference prices, the model achieves mean absolute error of £0.09 across 10,000 test paths — comparable to a TDBP neural network (£0.06 MAE) but with a fully interpretable linear weight vector that can be inspected to understand which path features drive the price.

## Remember

Signature-based pricing is the **interpretable sibling of TDBP**: both learn option prices from simulated paths, but TDBP uses a deep neural network while signature pricing uses a linear model on hand-computed features. The signature's universal approximation guarantee means the linear model is as expressive as any continuous functional — the trade-off is that depth-$N$ signatures for $d$-dimensional paths grow as $O(d^N)$ features, making depth $\ge 5$ expensive for multi-asset problems. In regulatory contexts where SR 11-7 requires model interpretability, a linear model on signature features can pass model governance review that a black-box neural network cannot.
