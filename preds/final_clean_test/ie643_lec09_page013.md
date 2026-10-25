[Diagram: A column of output neurons $\hat{y}_1, \hat{y}_2, \dots, \hat{y}_C$, each connected to a separate box (layer input).]

$$\hat{y}_j > 0, \quad \sum_j \hat{y}_j = 1$$

$$a_1^L \leftarrow 0, \; a_2^L \leftarrow 0, \; \dots, \; a_C^L \leftarrow 0$$

$$\hat{y}_j = \frac{\exp(a_j^L)}{\sum_k \exp(a_k^L)}, \quad k=1$$

## Soft-max function

$$\hat{y}_j = \frac{\exp(a_j^L)}{\sum_k \exp(a_k^L)}, \quad k=1$$

min-max scaling: 1.