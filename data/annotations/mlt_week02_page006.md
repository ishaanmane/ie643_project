## Feature Transformation

**Issue 2:** Non linear relationships among features.

[Diagram: Axes $f_1, f_2$ with two lines $w_1, w_2$ crossing near a point $\begin{bmatrix}a\\b\end{bmatrix}$ labeled "centre", with a dashed red circle of radius around that centre.]

What would PCA give on this dataset? $\{w_1, w_2\}$

**Relation b/w features**

$$(f_1-a)^2 + (f_2-b)^2 = r^2$$
$$f_1^2+a^2-f_1a+f_2^2+b^2-2f_2b-r^2=0 \quad (*)$$

Clearly not linear.

$$[f_1 \; f_2] \xrightarrow{\text{map}} [1 \; f_1^2 \; f_2^2 \; f_1f_2 \; f_1 \; f_2] \in \mathbb{R}^6$$
$$x \in \mathbb{R}^2 \xrightarrow{\phi} \phi \in \mathbb{R}^6$$

Let $u \in \mathbb{R}^6$: $[a^2+b^2-r^2 \;\; 1 \;\; 1 \;\; 0 \;\; -2a \;\; -2b]$

Each datapoint satisfies $\boxed{\phi(x)^Tu=0} \equiv (*)$

$\Rightarrow$ The datapoints lie in a linear subspace of $\mathbb{R}^6$
