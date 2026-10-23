$$f(w) = \frac{1}{n}\sum_{i=1}^{n} \|x_i - (x_i^Tw)w\|^2 \quad \text{[let this be average error instead of sum of error]}$$

$$f(w) = \frac{1}{n}\sum_{i=1}^{n} (x_i-(x_i^Tw)w)^T(x_i-(x_i^Tw)w)$$

$$f(w) = \frac{1}{n}\sum_{i=1}^{n} \left[x_i^Tx_i \; (x_i^Tw)^2 - (x_i^Tw)^2 + (x_i^Tw)\cdot 1\right]$$

$$f(w) = \frac{1}{n}\sum_{i=1}^{n} \left[x_i^Tx_i - (x_i^Tw)^2\right]$$

$x_i^Tx_i \rightarrow$ this is a constant & not relevant for our minimization

$$\min_{w, \|w\|^2=1} g(w) = \frac{1}{n}\sum_{i=1}^{n} -(x_i^Tw)^2 \quad \text{[whichever $w$ minimizes $g(w)$ also does the same for $f(w)$]}$$

$$\max_{w, \|w\|^2=1} g(w) = \frac{1}{n}\sum_{i=1}^{n} (x_i^Tw)^2$$

$$= \frac{1}{n}\sum_{i=1}^{n} (w^Tx_i)(x_i^Tw) = \frac{1}{n}\sum_{i=1}^{n} w^T(x_ix_i^T)w = w^T\left(\frac{1}{n}\sum_{i=1}^{n}x_ix_i^T\right)w$$

$(d \times d) \rightarrow$ covariance matrix $C$
