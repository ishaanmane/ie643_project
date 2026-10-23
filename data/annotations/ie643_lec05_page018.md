$$W^l = \begin{bmatrix} w_{11}^l & w_{12}^l & \cdots & w_{1N_{l-1}}^l \\ w_{21}^l & w_{22}^l & \cdots & w_{2N_{l-1}}^l \\ \vdots & & & \vdots \\ w_{N_l 1}^l & w_{N_l 2}^l & \cdots & w_{N_l N_{l-1}}^l \end{bmatrix}$$

$$N_l \times N_{l-1}$$

[Diagram: A chain of network-layer boxes connected left to right, with $\vec{x}$ feeding into the first.]

$$\hat{y} = \vec{a}^L = \phi(W^L a^{L-1}) = \phi(W^L \phi(W^{L-1} a^{L-2}))$$
