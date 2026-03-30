# Outer Product

**Topic:** Linear Algebra
**Tags:** linear algebra, vectors, outer product, rank-1 matrix, covariance, EWMA
**Author:** Claude Opus 4.6

---

## Definition

The **outer product** of two vectors $\mathbf{u} \in \mathbb{R}^m$ and $\mathbf{v} \in \mathbb{R}^n$ is the $m \times n$ matrix $\mathbf{u}\mathbf{v}^\top$. Unlike the inner (dot) product, which returns a scalar, the outer product returns a matrix. The result is always a **rank-1 matrix** — every row is a scalar multiple of $\mathbf{v}^\top$ and every column is a scalar multiple of $\mathbf{u}$.

## Key Formula

**Outer product:**

$$\mathbf{u}\mathbf{v}^\top = \begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_m \end{pmatrix} \begin{pmatrix} v_1 & v_2 & \cdots & v_n \end{pmatrix} = \begin{pmatrix} u_1 v_1 & u_1 v_2 & \cdots & u_1 v_n \\ u_2 v_1 & u_2 v_2 & \cdots & u_2 v_n \\ \vdots & \vdots & \ddots & \vdots \\ u_m v_1 & u_m v_2 & \cdots & u_m v_n \end{pmatrix}$$

**Entry formula:** the $(i,j)$ entry of the outer product is simply $u_i \, v_j$.

**Key properties:**

- $\operatorname{rank}(\mathbf{u}\mathbf{v}^\top) = 1$ whenever $\mathbf{u} \neq \mathbf{0}$ and $\mathbf{v} \neq \mathbf{0}$
- $\operatorname{trace}(\mathbf{u}\mathbf{v}^\top) = \mathbf{u} \cdot \mathbf{v}$ (the trace equals the inner product)
- $(\mathbf{u}\mathbf{v}^\top)^\top = \mathbf{v}\mathbf{u}^\top$

## Example

Let $\mathbf{u} = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$ and $\mathbf{v} = \begin{pmatrix} 4 \\ 1 \end{pmatrix}$.

$$\mathbf{u}\mathbf{v}^\top = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \begin{pmatrix} 4 & 1 \end{pmatrix} = \begin{pmatrix} 2 \times 4 & 2 \times 1 \\ -1 \times 4 & -1 \times 1 \\ 3 \times 4 & 3 \times 1 \end{pmatrix} = \begin{pmatrix} 8 & 2 \\ -4 & -1 \\ 12 & 3 \end{pmatrix}$$

This is a $3 \times 2$ rank-1 matrix. Notice each row is a multiple of $(4, 1)$: the first row is $2 \times (4, 1)$, the second is $-1 \times (4, 1)$, and the third is $3 \times (4, 1)$.

**Trace check** (for square outer products): if $\mathbf{u} = \mathbf{v} = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$, then $\operatorname{trace}(\mathbf{u}\mathbf{u}^\top) = 4 + 1 + 9 = 14 = \mathbf{u} \cdot \mathbf{u}$ ✓

## Remember

In quantitative finance, the outer product is the building block of the **sample covariance matrix**. Given $T$ centred return observations $\mathbf{r}_t \in \mathbb{R}^n$, the sample covariance matrix is a sum of outer products:

$$\hat{\Sigma} = \frac{1}{T-1} \sum_{t=1}^{T} \mathbf{r}_t \, \mathbf{r}_t^\top$$

Each term $\mathbf{r}_t \mathbf{r}_t^\top$ is a rank-1 matrix capturing one day's contribution to total covariance. The **EWMA (Exponentially Weighted Moving Average)** volatility model used by RiskMetrics exploits this structure: each update adds a single rank-1 outer product $\mathbf{r}_t \mathbf{r}_t^\top$ with exponentially decaying weights, making real-time covariance updates efficient. The **Sherman–Morrison formula** further exploits rank-1 structure to update the inverse of a matrix cheaply when a rank-1 outer product is added — critical for portfolio optimisation when the covariance matrix changes daily.
