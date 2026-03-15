# Kronecker Product

**Topic:** Linear Algebra
**Tags:** kronecker product, tensor product, multi-asset, covariance, state space models
**Created:** 2026-03-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **Kronecker product** $A \otimes B$ of an $m \times n$ matrix $A$ and a $p \times q$ matrix $B$ is the $mp \times nq$ block matrix formed by replacing each entry $a_{ij}$ of $A$ with the scaled block $a_{ij}B$. It is the natural matrix operation for representing the joint structure of two independent systems.

## Key Formula

$$A \otimes B = \begin{pmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{pmatrix}$$

Key properties:
- $(A \otimes B)(C \otimes D) = (AC) \otimes (BD)$ (mixed-product property)
- $(A \otimes B)^{-1} = A^{-1} \otimes B^{-1}$
- $(A \otimes B)^\top = A^\top \otimes B^\top$
- $\text{vec}(AXB) = (B^\top \otimes A)\,\text{vec}(X)$ — the vectorisation identity

## Example

$$\begin{pmatrix}1&2\\3&4\end{pmatrix} \otimes \begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}0&1&0&2\\1&0&2&0\\0&3&0&4\\3&0&4&0\end{pmatrix}$$

## Remember

In multi-asset options pricing and risk, the joint covariance structure of returns across $n$ assets observed at $T$ time points is naturally represented as a Kronecker product $\Sigma_{\text{asset}} \otimes \Sigma_{\text{time}}$, assuming separable (asset, time) dependence. This reduces the number of parameters from $O(n^2T^2)$ to $O(n^2 + T^2)$ — crucial for calibrating covariance matrices in high-dimensional settings. The vectorisation identity $\text{vec}(AXB) = (B^\top \otimes A)\,\text{vec}(X)$ also appears in the analytical solution of the **Lyapunov equation**, which arises in mean-reverting interest rate models.
