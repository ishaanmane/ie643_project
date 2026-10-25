$$\min_{\text{weights}} \sum_{i=1}^{N}\left(-\sum_{j=1}^{C}y_j^i\log\hat{y}_j^i\right)$$

$$\min_{\text{weights}} \sum_{j=1}^{C}\hat{y}_j\log\frac{\hat{y}_j}{y_j} = \sum_{j=1}^{C}\hat{y}_j\log\hat{y}_j - \sum_{j=1}^{C}\hat{y}_j\log y_j$$