$$\min_{\text{weights}} \sum_{i=1}^{N} \left( -\sum_{j=1}^{C} y_j^i \log \hat{y}_j^i \right)$$

$$KL(\hat{y} \parallel y) = \sum \hat{y}_j \log \frac{\hat{y}_j}{y_j}$$

$$= \min \quad \sum \hat{y}_j \log \hat{y}_j - \sum \hat{y}_j \log y_j$$