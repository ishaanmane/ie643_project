```markdown
The image contains a mathematical equation written on a chalkboard. Here is the transcription of the content:

\[
\begin{aligned}
\left[\begin{array}{c}
\frac{\partial e}{\partial a_1} \\
\frac{\partial e}{\partial a_2} \\
\vdots \\
\frac{\partial e}{\partial a_c}
\end{array}\right] &= \left[\begin{array}{c}
\hat{y}_1 - y_1 \\
\hat{y}_2 - y_2 \\
\vdots \\
\hat{y}_c - y_c
\end{array}\right] \\
&= \sum_{i=1}^{c}
\]
```

This equation represents the partial derivatives of the error function \(e\) with respect to the parameters \(a_i\) (for \(i = 1, 2, \ldots, c\)). The right-hand side shows the differences between the predicted values \(\hat{y}_i\) and the actual values \(y_i\) for each parameter.

The final part of the equation indicates that these partial derivatives sum up to zero, which is a key property in many optimization algorithms used in machine learning, such as gradient descent.
```