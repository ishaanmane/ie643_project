$$W^1, W^2, \dots, W^L$$

for ... epochs ($< 100/1000/10^9$)
&nbsp;&nbsp;&nbsp;&nbsp;for $k$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ sample minibatch.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ compute predictions over minibatch using fwd pass
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ compute loss over minibatch.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ compute error/loss gradients wrt $W^1, W^2, \dots, W^L$
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow$ update weights (using opt scheme)

**Stopping criteria:**
1. $|\text{loss}^k - \text{loss}^{k-1}| < \tau$
2. $|\nabla \text{loss}^k| \to 0$
3. $\sum_{k=1}^{L} |W^k - W^{k-1}| < \tau_3$ &nbsp; $\rightarrow$ generalization

Validation set.
