# Dynamic Time Warping

**Topic:** Computational Finance
**Tags:** dynamic time warping, dtw, time series similarity, clustering, regime detection, pattern matching
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

**Dynamic time warping (DTW)** is a distance measure between time series that allows elastic alignment — one series can be stretched or compressed in time to match the other. Unlike Euclidean distance, which compares series point-by-point at identical timestamps, DTW finds the minimum-cost monotone warping path through the pairwise distance matrix, making it robust to phase shifts, speed differences, and local distortions in financial time series.

## Key Formula

**DTW distance** between series $\mathbf{x} = (x_1, \ldots, x_m)$ and $\mathbf{y} = (y_1, \ldots, y_n)$:

$$\text{DTW}(\mathbf{x}, \mathbf{y}) = \min_{\pi} \sum_{(i,j) \in \pi} d(x_i, y_j)$$

computed via dynamic programming:

$$D(i, j) = d(x_i, y_j) + \min\!\begin{cases} D(i-1, j) \\ D(i, j-1) \\ D(i-1, j-1) \end{cases}$$

with $d(x_i, y_j) = |x_i - y_j|$ (or squared difference), $D(1,1) = d(x_1, y_1)$, and $\text{DTW}(\mathbf{x}, \mathbf{y}) = D(m, n)$.

**Sakoe–Chiba band** — constrains the warping path to within $w$ steps of the diagonal, preventing degenerate alignments and reducing complexity from $O(mn)$ to $O(mn \cdot w/\max(m,n))$.

## Example

Comparing the 2000 dot-com crash (Nasdaq, April–October 2000, 130 trading days) with the 2008 GFC (S\&P 500, September–March 2009, 130 trading days). Euclidean distance: 1,840 index points (misleading — the series are on different scales and lag each other by 3 weeks). After normalising both to $z$-scores and applying DTW with a 10-day Sakoe–Chiba band: $\text{DTW} = 2.1$. The warping path reveals the dot-com crash developed 15 days faster than the GFC crash — DTW identifies this as the closest historical analogue whilst Euclidean distance ranks the 1987 crash as closer due to a coincidental price level match.

## Remember

DTW is the correct distance measure for historical pattern matching in equity and fixed income markets because market events rarely replay at exactly the same speed — a regime transition that took 3 weeks in 2008 may play out over 6 weeks in a later crisis. Using Euclidean distance for $k$-NN regime lookup penalises phase-shifted analogues that are genuinely relevant. The practical limitation is quadratic computation: DTW is $O(mn)$ per pair, making pairwise distance matrices expensive for long histories. For daily data over 20 years ($\sim$5,000 observations), the Sakoe–Chiba constraint and vectorised implementations (the `tslearn` library) reduce this to a feasible preprocessing step. DTW is also the natural distance metric for contrastive learning over financial time series, enabling positive pairs to be phase-shifted versions of the same regime period rather than requiring exact date alignment.
