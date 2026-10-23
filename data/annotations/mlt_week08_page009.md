# Decision Function for Naive Bayes

Given $x_{test}$, $y_{test}=1$ if $\dfrac{P(y_{test}=1/x_{test})}{P(y_{test}=0/x_{test})} \geq 1$

It means that, $\log\left(\dfrac{P(y_{test}=1/x_{test})}{P(y_{test}=0/x_{test})}\right) \geq 0$

$$\log\left(\frac{P(x_{test}/y_{test}=1)\cdot P(y_{test}=1)/P(x_{test})}{P(x_{test}/y_{test}=0)\cdot P(y_{test}=0)/P(x_{test})}\right) \geq 0$$

$$\log\left(\prod_{i=1}^{d}\frac{(\hat{p}_i')^{f_i}(1-\hat{p}_i')^{(1-f_i)}\;\hat{p}'}{(\hat{p}_i^0)^{f_i}(1-\hat{p}_i^0)^{(1-f_i)}\cdot(1-\hat{p}^0)}\right) \geq 0$$

$$\log\left(\prod_{i=1}^{d}\left(\frac{\hat{p}_i'}{\hat{p}_i^0}\right)^{f_i}\left(\frac{1-\hat{p}_i'}{1-\hat{p}_i^0}\right)^{(1-f_i)}\left(\frac{\hat{p}'}{1-\hat{p}^0}\right)\right) \geq 0$$

$$\sum_{i=1}^{d}\left[f_i\log\left(\frac{\hat{p}_i'}{\hat{p}_i^0}\right) + (1-f_i)\log\left(\frac{1-\hat{p}_i'}{1-\hat{p}_i^0}\right) + \log\left(\frac{\hat{p}'}{1-\hat{p}^0}\right)\right] \geq 0$$

$$\sum_{i=1}^{d}\left[f_i\left(\log\left(\frac{\hat{p}_i'(1-\hat{p}_i^0)}{\hat{p}_i^0(1-\hat{p}_i')}\right)\right) + \log\left(\frac{(1-\hat{p}_i')\hat{p}'}{\cdots}\right)\right] \geq 0$$
