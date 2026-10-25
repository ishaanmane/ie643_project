$$c(y^i,\hat{y}^i) = \text{KL}(y^i,\hat{y}^i)$$

$$\min_{\text{weights of NN}} \sum_{i=1}^{N} \text{KL}(y^i,\hat{y}^i)$$

$$\text{KL}=0 \text{ when } y^i=\hat{y}^i$$
$$\text{KL}>0 \text{ when } y^i\neq\hat{y}^i$$

$$\min_{\text{weights}} \sum_{i=1}^{N} \text{CE}(y^i,\hat{y}^i)$$

**logistic regression**

$$E[y|x=\vec{x}]$$

Bernoulli v.v. likelihood