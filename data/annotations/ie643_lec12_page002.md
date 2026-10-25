Loss fn: Squared error.

For $D = \{(x^s,y^s)\}_{s=1}^{S}$:

$$E(A,B) = \sum_{s=1}^{S} \|\hat{y}^s - y^s\|^2 = \sum_{s=1}^{S} \|ABx^s - y^s\|^2$$

$$\boxed{\min_{A,B} E(A,B)}$$

[Diagram: single-neuron chain $\xrightarrow{b}$ neuron $\xrightarrow{a}$ neuron.]

$$\sum_{s=1}^{S} (abx^s - y^s)^2 =: E(a,b)$$

When $a$ is fixed: observe that $E(a_{fixed}, b)$ is **convex** wrt $b$.
When $b$ is fixed, $E(a, b_{fixed})$ is cvx wrt $a$.
