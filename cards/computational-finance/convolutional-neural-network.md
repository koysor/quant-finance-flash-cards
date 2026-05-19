# Convolutional Neural Network (CNN)

**Topic:** Computational Finance
**Tags:** convolutional neural network, cnn, filters, feature extraction, alternative data, image recognition
**Created:** 2026-04-26
**Author:** Claude Sonnet 4.6

---

## Definition

A **convolutional neural network (CNN)** is a feedforward network where some layers apply learnable filters (kernels) by sliding them across the input, sharing weights across positions. This parameter sharing exploits local structure — nearby inputs are more related than distant ones — making CNNs efficient for data with spatial or temporal locality such as images, text grids, and ordered time series.

## Key Formula

A 1D convolution of input $\mathbf{x}$ with filter $\mathbf{k}$ of length $F$ at position $t$:

$$(x \star k)_t = \sum_{f=0}^{F-1} k_f \cdot x_{t+f}$$

For a 2D image input $X$ with filter $K$ of size $F \times F$:

$$(X \star K)_{i,j} = \sum_{p=0}^{F-1}\sum_{q=0}^{F-1} K_{p,q} \cdot X_{i+p,\, j+q}$$

The same filter $\mathbf{k}$ is applied at every position — **weight sharing** reduces parameters from $O(n^2)$ (fully connected) to $O(F)$ (convolutional).

## Example

A hedge fund processes daily satellite images of 500 retailer car parks ($224 \times 224$ pixels each) to nowcast consumer spending. A CNN with three convolutional layers learns filters that detect: (layer 1) edges and contrast, (layer 2) car-shaped blobs, (layer 3) crowd density patterns. The final dense layer maps the extracted features to next-quarter same-store sales surprises — a cross-sectional signal that feedforward networks on tabular data cannot extract from raw pixels.

## Remember

CNNs entered quantitative finance via **alternative data**: satellite imagery of oil storage tanks (inventory signals), shipping port activity, retail traffic, and construction site progress are all pixel-based signals that traditional factor models cannot use. The CNN's weight sharing means it can process images regardless of where in the frame the relevant object appears — a car park in the top-left and one in the bottom-right are recognised by the same filter. In time-series applications, 1D CNNs act as learnable moving-average filters, extracting local temporal patterns at multiple scales simultaneously without needing hand-crafted technical indicators.
