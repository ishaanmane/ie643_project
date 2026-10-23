## SGD

$\rightarrow w^0$
$\rightarrow$ for $k=0,1,2,\dots$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow g^k = \nabla_{w^k} e_{j_k}(y^{j_k}, \hat{y}^{j_k})$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow w^{k+1} \leftarrow w^k + \eta_k(-g^k)$ &nbsp; typical chosen close to zero ($10^{-4}, 10^{-10}, \dots$)

$j_k$: an index which is chosen randomly from $\{1,2,\dots N\}$

**Mini-batch version:**

$\rightarrow w^0$
$\rightarrow$ for $k=0,1,2,\dots$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow g^k = \sum_{j \in B_k} \nabla e_j(y^j, \hat{y}^j)$, &nbsp; $B_k \subseteq \{1,2,\dots k\}$: minibatch of samples

labels $\{+1,-1\}$
