## Multi-class classification.

$$Y = \{1, 2, \dots C\}$$

$y \in Y$ — typically $k \in Y$.

$$y = \begin{bmatrix} 0 \\ \vdots \\ 0 \\ 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix} \rightarrow k^{th} \text{ coordinate}$$

$\rightarrow$ CE loss fn.

$$e = -\sum_{j=1}^{C} y_j \log \hat{y}_j$$

$$\sum_{i=1}^{N} \left(-\sum_{j=1}^{C} y_j^i \log \hat{y}_j^i\right)$$
