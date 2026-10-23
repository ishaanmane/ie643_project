## SGD with momentum.

$$w^0, m^0 = 0$$
for $k=0,1,2,\dots$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow g^k = $ mini-batch stoc. gradient
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow m^{k+1} = \beta g^k + (1-\beta) m^k$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow w^{k+1} = w^k + \eta_k(-m^{k+1})$

## ADAM (mu-SGD, mu-ON)

$$w^0, m^0 = 0, v^0 = 0$$
for $k=0,1,2,\dots$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow g^k = $ mini-batch grad
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow m^{k+1} = \beta_1 g^k + (1-\beta_1) m^k$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow v^{k+1} = \beta_2 (g^k)^2 + (1-\beta_2) v^k$
&nbsp;&nbsp;&nbsp;&nbsp;$\hookrightarrow w^{k+1} = w^k + \eta_k\left(-\dfrac{m^{k+1}}{\sqrt{v^{k+1}}+\epsilon}\right)$
