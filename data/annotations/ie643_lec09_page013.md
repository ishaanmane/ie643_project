$$\hat{y} = \begin{bmatrix} \hat{y}_1 \\ \hat{y}_2 \\ \vdots \\ \hat{y}_C \end{bmatrix}, \quad \hat{y}_j > 0, \quad \sum_j \hat{y}_j = 1$$

[Diagram: raw output activations $a_1^L, a_2^L, \dots, a_C^L$ mapped via min-max scaling idea, and $\dfrac{|a_1|}{\sum |a_j|}$ shown as a normalization approach $\to$ "min-max scaling [0,1]".]

## Soft-max function

$$\hat{y}_j = \frac{\exp(a_j^L)}{\sum_{k=1}^{C} \exp(a_k^L)} \quad \rightarrow \text{soft-max}$$
