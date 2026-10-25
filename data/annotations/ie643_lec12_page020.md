[Diagram: chain $x \to$ box $\to$ box $\to \hat{x}$, an autoencoder.]

$$\Sigma = \Sigma_{yx}\Sigma_{xx}^{-1}\Sigma_{xy} = \Sigma_{xx}\Sigma_{xx}^{-1}\Sigma_{xx}$$

$$\sum_{s} \|ABx^s - \hat{x}\|^2, \qquad D = \{(x^s,x^s)\}_{s=1}^{S}, \quad \Sigma = \Sigma_{xx}$$

$$E = \text{Tr}(\Sigma_{xx}) - \sum_{i \in \mathcal{I}} \lambda_i \Rightarrow \text{PCA objective.}$$

**Baldi & Hornik** (reference)

$$X = \begin{bmatrix} \uparrow & & \uparrow \\ x^1 & \cdots & x^S \\ \downarrow & & \downarrow \end{bmatrix}$$

## PCA:
variance(true data) $-$ var(proj. data)
