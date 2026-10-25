$$\min KL(\hat{y}\|y) = \sum \hat{y}_j \log \frac{\hat{y}_j}{y_j}$$

$$= \underbrace{\sum \hat{y}_j \log \hat{y}_j}_{\text{min}} - \sum \hat{y}_j \log y_j$$

$$\min_{\text{weights}} \sum_{i=1}^{N} \left(-\sum_{j=1}^{C} y_j^i \log \hat{y}_j^i\right)$$
