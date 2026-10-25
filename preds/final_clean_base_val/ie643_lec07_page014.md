```markdown
# Adam Optimization Algorithm

## SGD with Momentum

The update rule for momentum is given by:

$$
m_k = \alpha \cdot \text{grad}_k + (1 - \alpha) \cdot m_{k-1}
$$

This can be interpreted as a running average of gradients.

## Adam Algorithm

### Update Rule

The update rule for the parameters in Adam is:

$$
w^{k+1} \leftarrow w^k + \eta_k \cdot \frac{\text{running avg of gradients}}{\sqrt{\text{running avg of sq. comp of gradients}} + \epsilon}
$$

Here:
- $\eta_k$ is the learning rate at iteration k.
- The denominator includes a small constant $\epsilon$ to prevent division by zero.

### AMSGrad

AMSGrad is an extension of Adam that prevents the gradient from becoming too large. It does this by keeping track of the maximum gradient seen so far and using that instead of the running average of gradients.

```
```