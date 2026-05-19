# Federated Learning

**Topic:** Computational Finance
**Tags:** federated learning, privacy, distributed training, credit risk, model aggregation
**Created:** 2026-05-19
**Author:** Claude Sonnet 4.6

---

## Definition

**Federated learning** trains a shared model across multiple data-holding clients without any client sharing its raw data. Each client trains locally on its own data, sends only model weight updates to a central server, and the server aggregates these updates into a global model that is then broadcast back. The raw financial data never leaves each institution.

## Key Formula

The **FedAvg** algorithm aggregates client updates weighted by their dataset sizes. In each global round $t$:

1. Server broadcasts current weights $\mathbf{w}_t$ to all $K$ clients
2. Each client $k$ runs $E$ epochs of local SGD on its private data $\mathcal{D}_k$:

$$\mathbf{w}_k^{(t+1)} = \mathbf{w}_t - \eta\,\nabla_{\mathbf{w}}\mathcal{L}_k(\mathbf{w}_t)$$

3. Server aggregates by dataset size $n_k$, where $n = \sum_k n_k$:

$$\mathbf{w}_{t+1} = \sum_{k=1}^{K} \frac{n_k}{n}\,\mathbf{w}_k^{(t+1)}$$

The model converges to the minimiser of the global objective $\frac{1}{n}\sum_k n_k \mathcal{L}_k(\mathbf{w})$ without any $\mathcal{D}_k$ being transmitted.

## Example

Five banks want to jointly train a corporate default prediction model. Each bank has 50,000 loan records with proprietary covenants, rating histories, and credit officer notes — data they cannot share under GDPR and banking secrecy regulations. Using FedAvg over 100 global rounds: each bank trains locally for $E = 5$ epochs per round, sends weight deltas ($\sim$ 10 MB) to the coordinating server, and receives the aggregated model. The federated model achieves AUC 0.84 versus 0.79 for any individual bank's model — the improvement arises from learning across a broader range of borrower types than any single institution sees.

## Remember

Federated learning directly addresses the data-sharing problem that limits collaborative financial modelling: credit risk, fraud detection, and anti-money-laundering models would all benefit from cross-institution training, but regulatory constraints (GDPR, BCBS 239, banking secrecy laws) and competitive concerns prevent data pooling. Federated learning offers a partial solution — the aggregated model benefits from scale whilst raw data stays local. The main practical challenges in finance are: (1) **statistical heterogeneity** — each bank's loan book has different borrower demographics, making client data non-IID and slowing convergence; (2) **Byzantine robustness** — a single malicious client could corrupt the global model through adversarial updates; (3) **model inversion attacks** — even weight gradients can leak information about individual records, motivating differential privacy augmentation. Despite these challenges, federated credit risk models are actively deployed in regulatory sandbox environments across the EU and UK.
