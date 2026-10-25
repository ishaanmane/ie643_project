[Diagram: A column of output neurons $\hat{y}_1, \hat{y}_2, \dots, \hat{y}_C$, each connected via a sigmoid neuron (circle) to a layer of "a" values $a_1^L, a_2^L, \dots, a_C^L$.]

$$\hat{y}_j > 0, \quad \sum_j \hat{y}_j = 1$$

$$\hat{y}_j = \frac{\exp(a_j^L)}{\sum_k \exp(a_k^L)}, \quad k=1$$

## Soft-max function

$$\hat{y}_j = \frac{\exp(a_j^L)}{\sum_k \exp(a_k^L)}, \quad k=1$$

soft-max