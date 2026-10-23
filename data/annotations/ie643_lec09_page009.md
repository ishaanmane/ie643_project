$$KL(p \to q)$$
$$KL(q \to p) = KL(q \| p) = \sum_{j=1}^{C} q_j \log \frac{q_j}{p_j} \quad \text{(not equal to } KL(p\|q))$$

$$KL(p\|q) = \sum_{j=1}^{C} p_j \log p_j \quad \rightarrow \text{negative entropy}$$
$$- \sum_{j=1}^{C} p_j \log q_j$$

$p \equiv q \Rightarrow KL \downarrow 0$, &nbsp; $KL \uparrow$
