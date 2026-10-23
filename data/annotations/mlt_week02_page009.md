We managed compute $\phi(x)^T\phi(x')$ w/o explicitly computing $\phi(x)$!

**Another example:**

$$k(x,x') = (x^Tx'+1)^p \qquad x \in \mathbb{R}^d \text{ for some } p \geq 1$$

$\rightarrow$ can be shown to be a "valid" function if $\exists \phi: \mathbb{R}^d \rightarrow \mathbb{R}^D$ such that $k(x,x') = \phi(x)^T\phi(x')$

**Another example:**

$$k(x,x') = \exp\left(\frac{-\|x-x'\|^2}{2\sigma^2}\right) \text{ for some } \sigma>0$$

$\uparrow$ Radial Basis Function

$\rightarrow$ can be shown to be a "valid" mapping as
$\rightarrow$ Interestingly, $\phi$ maps to an "infinite" dimension

These "valid" functions are called **Kernel functions**

$$k(x,x') = (x^Tx+1)^p \rightarrow \text{polynomial kernel}$$
$$k(x,x') = \exp\left(\frac{-\|x-x'\|^2}{2\sigma^2}\right) \rightarrow \text{gaussian kernel / radial basis}$$
