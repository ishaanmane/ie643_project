## Kernel Functions

Issue - what if $\phi(x)$ is too difficult to compute?

Consider this example - $x=\begin{bmatrix}f_1\\f_2\end{bmatrix}$, $x'=\begin{bmatrix}g_1\\g_2\end{bmatrix}$

Take this arbitrary function:
$$(x^Tx'+1)^2 = \left([f_1 \; f_2]\begin{bmatrix}g_1\\g_2\end{bmatrix}+1\right)^2 = (f_1g_1+f_2g_2+1)^2$$

$$= f_1^2g_1^2+f_2^2g_2^2+1+2f_1g_1+2f_2g_2+2f_1g_1f_2g_2$$

$$= [f_1^2 \;\; f_2^2 \;\; 1 \;\; \sqrt{2}f_1f_2 \;\; \sqrt{2}f_1 \;\; \sqrt{2}f_2]\begin{bmatrix}g_1^2\\g_2^2\\1\\\sqrt{2}g_1g_2\\\sqrt{2}g_1\\\sqrt{2}g_2\end{bmatrix}$$

$$= \phi(x)^T\phi(x')$$

where $\phi(x) = \phi\left(\begin{bmatrix}a\\b\end{bmatrix}\right) = \begin{bmatrix}a^2\\b^2\\1\\\sqrt{2}ab\\\sqrt{2}a\\\sqrt{2}b\end{bmatrix}$
