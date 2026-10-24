## Adam

**SGD with momentum**

$$m_k = \alpha \cdot \text{grad}_k + (1-\alpha) m_{k-1}$$

generalize perf

$$v^k = \alpha (\text{mini-batch gradient}) + (1-\alpha) \cdot \text{past gradients}$$

**Adam:**
$$w^{k+1} \leftarrow w^k - \eta_k$$

AMSGrad:
$$\left( \frac{\text{running avg of gradients}}{\sqrt{\text{running avg of sq. grad.}} + \epsilon} \right)$$