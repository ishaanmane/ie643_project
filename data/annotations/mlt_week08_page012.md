$$\hat{\Sigma} = \frac{1}{n}\sum_{i=1}^{n}(x_i-\mu_{y_i})(x_i-\mu_{y_i})^T$$

## Prediction

$$P(y_{test}/x_{test}) \propto \underbrace{P(x_{test}/y_{test})}_{f(x_{test};\hat{\mu}_{y_{test}},\hat{\Sigma})} \cdot \underbrace{P(y_{test})}_{\hat{p}}$$

**Predict $y_{test}=1$ if**
$$f(x_{test};\hat{\mu}_1,\hat{\Sigma})\cdot\hat{p} \geq f(x_{test};\hat{\mu}_0,\hat{\Sigma})\cdot(1-\hat{p})$$

$$e^{-(x_{test}-\hat{\mu}_1)^T\hat{\Sigma}^{-1}(x_{test}-\hat{\mu}_1)}\cdot\hat{p} \geq e^{-(x_{test}-\hat{\mu}_0)^T\hat{\Sigma}^{-1}(x_{test}-\hat{\mu}_0)}\cdot(1-\hat{p})$$

on simplification after taking log,

$$(\hat{\mu}_1-\hat{\mu}_0)^T\hat{\Sigma}^{-1}x_{test} + \hat{\mu}_0^T\hat{\Sigma}^{-1}\hat{\mu}_0 - \hat{\mu}_1^T\hat{\Sigma}^{-1}\hat{\mu}_1 + \log\left(\frac{1-\hat{p}}{\hat{p}}\right) \geq 0$$

$$\downarrow \qquad w^Tx_{test} + b \geq 0$$

The Decision Function is Linear!
