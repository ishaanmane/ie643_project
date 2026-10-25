## KL Divergence

$$\text{KL}(p \to q)$$

$$\text{KL}(q \to p) = \text{KL}(q \| p) = \sum_{j=1}^{C} q_j \log \frac{q_j}{p_j}$$

$$\text{KL}(p \| q) = \sum_{j=1}^{C} p_j \log p_j - \sum_{j=1}^{C} p_j \log q_j$$

$$p=q \implies \text{KL} \downarrow 0, \quad \text{KL} \uparrow \text{twice}$$

> negative entropy.