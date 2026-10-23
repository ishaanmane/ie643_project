# Gradient Descent

- Start with random $w$'s and $\theta$

- Pass $x^t$ into **perceptron**

$$ \langle w, x^t \rangle - \theta \begin{cases} \ge 0 \longrightarrow +1 \\ < 0 \longrightarrow -1 \end{cases} \longrightarrow \text{prediction} $$

- Ground truth: $y^t$
- Prediction: $\hat{y}^t$

- Update $w, \theta$ based on matching nature of $y^t$ and $\hat{y}^t$

- **Stop**: when $y^t$ and $\hat{y}^t$ are same for all samples

[Diagram: An arrow loops from the update step back to the step "Pass $x^t$ into perceptron", indicating an iterative process for each sample/epoch until the stopping condition is met.]