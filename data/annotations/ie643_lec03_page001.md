# Recap: Supervised Learning with Perceptron

## Dataset
$$\mathcal{D} = \{ (x^i, y^i) \}_{i=1}^{N < \infty}$$

where each input vector $x^i$ is defined as:

$$x^i = \begin{bmatrix} x^i_1 \\ x^i_2 \\ \vdots \\ x^i_d \end{bmatrix} \in \mathbb{R}^d =: \mathcal{X}$$

## Categorization / Binary Classification

$$y^i \in \{ +1, -1 \} =: \mathcal{Y}$$

Hypothesis function:

$$h : \mathcal{X} \rightarrow \mathcal{Y}$$

> $\underline{h}$: parametrized function