# Graph Neural Networks

**Topic:** Computational Finance
**Tags:** graph neural networks, gnn, graph convolution, asset correlation, systemic risk, message passing
**Created:** 2026-05-13
**Author:** Claude Sonnet 4.6

---

## Definition

A **graph neural network (GNN)** learns representations of nodes in a graph by aggregating information from their neighbours through **message passing**. Each node updates its embedding by combining its own features with a weighted sum of its neighbours' embeddings, applied iteratively over multiple layers. In quantitative finance, the graph encodes the dependency structure between assets, sectors, or counterparties — enabling models that respect the network structure of markets rather than treating assets as independent.

## Key Formula

**Graph convolutional network (GCN) layer update:**

$$\mathbf{H}^{(l+1)} = \sigma\!\left(\tilde{\mathbf{D}}^{-1/2} \tilde{\mathbf{A}} \, \tilde{\mathbf{D}}^{-1/2} \mathbf{H}^{(l)} \mathbf{W}^{(l)}\right)$$

where:
- $\tilde{\mathbf{A}} = \mathbf{A} + \mathbf{I}$ — adjacency matrix with self-loops
- $\tilde{\mathbf{D}}_{ii} = \sum_j \tilde{A}_{ij}$ — degree matrix
- $\mathbf{H}^{(l)}$ — node feature matrix at layer $l$; $\mathbf{H}^{(0)} = \mathbf{X}$ (input features)
- $\mathbf{W}^{(l)}$ — learnable weight matrix; $\sigma$ — activation function

**Graph construction** from asset return correlations:

$$A_{ij} = \begin{cases} 1 & \text{if } \rho_{ij} > \tau \\ 0 & \text{otherwise} \end{cases} \quad \text{or} \quad A_{ij} = \rho_{ij} \; (\text{weighted adjacency})$$

## Example

A GCN trained to predict next-day stock return direction for 500 FTSE stocks. Graph edges: pairs with rolling 60-day Pearson correlation $> 0.5$ (approximately 8,000 edges). Node features: 10 technical indicators per stock. After 2 GCN layers, each stock's embedding aggregates information from its 2-hop neighbourhood (stocks correlated with its correlates). Test accuracy: 57%, versus 53% for a standard feedforward network with no graph structure — the 4pp gain reflects the informational value of sector-level contagion patterns encoded in the graph.

## Remember

GNNs are the natural architecture when the relationship between assets is as informative as their individual features — which is precisely the case in financial markets where contagion, sector clustering, and supply-chain dependencies drive co-movement. Three financial applications stand out: (1) **systemic risk modelling** — GNNs on interbank exposure graphs predict which institutions will amplify a shock across the network; (2) **credit portfolio management** — GNNs on obligor industry graphs model correlated default clustering beyond what copula models capture; (3) **factor model enhancement** — node embeddings from a GCN over the asset correlation matrix can replace hand-crafted factor exposures as input features to a return prediction model, since they adapt dynamically to changing correlation structure rather than using fixed industry classifications.
