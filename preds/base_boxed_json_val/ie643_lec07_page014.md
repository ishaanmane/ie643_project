```markdown
# Adam

## SGD with Momentum

### Generalization Performance

$$
m_k = \alpha \cdot \text{grad}_k + (1 - \alpha) m_{k-1}
$$

## Adam:

### AMSGrad

$$
u^k = \alpha (\text{mini-batch gradient}) + (1 - \alpha) \cdot \text{past gradients}
$$

$$
w^{k+1} \leftarrow w^k + \eta_k'
$$

$$
\frac{\text{running avg of gradients}}{\sqrt{\text{running avg of sq. comp of gradients}} + \epsilon}
$$
```