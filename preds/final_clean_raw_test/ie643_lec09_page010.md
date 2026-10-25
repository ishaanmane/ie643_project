## Entropy & KL Divergence

$$\text{Entropy}(p) := -\sum_{j=1}^{C} p_j \log p_j$$

$$KL = N\epsilon + C\epsilon \rightarrow \text{cross-entropy}$$

[Diagram: A sigmoid curve (logistic function) arching upwards.]

## Data Representation

$$D = \{(x^i,y^i)\}_{i=1}^{N}, \quad y^i = \begin{bmatrix}0\\0\\\vdots\\b\\\vdots\\0\end{bmatrix} \in \mathbb{R}^C$$

$$\hat{y}^i = \begin{bmatrix}\hat{y}_1^i\\\hat{y}_2^i\\\vdots\\\hat{y}_C^i\end{bmatrix}$$