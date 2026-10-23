$$\nabla f(x^*) = 0$$

If $x^*$ is a local opt pt for $f$, then it is also the **global** opt.

[Diagram: A linear autoencoder chain — $n$ neurons $\xrightarrow{B}$ $p$ neurons $\xrightarrow{A}$ $n$ neurons, $p \leq n$.]

$$E(A,B) = \sum_{s=1}^{S} \|ABx^s - y^s\|_2^2$$

For a fixed $A$, $E(A,B)$ is cnvx w.r.t. wts $B$.
For a fixed $B$, $E(A,B)$ is invx wrt wts $A$.

$\rightarrow$ **PCA**
