$$\text{vec}(X) = \begin{bmatrix} \uparrow \\ x^1 \\ \downarrow \\ \uparrow \\ x^2 \\ \downarrow \\ \uparrow \\ x^3 \\ \downarrow \\ \vdots \\ \uparrow \\ x^S \end{bmatrix}$$

$$E(A,B) = \|\text{vec}(ABX-Y)\|_2^2 = \|\text{vec}(ABX) - \text{vec}(Y)\|_2^2$$

Fix the matrix $B$.

$$\min_{A} \|M \, \text{vec}(A) - \text{vec}(Y)\|_2^2$$
