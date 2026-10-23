If we keep fitting lines using the procedure we will (finding residue of the residue of residue ...) get,

$$\{w_1, w_2, \dots, w_d\} \text{ such that } \|w_k\|^2=1 \; \forall k \; \& \; w_i^Tw_j = 0 \; \forall i \neq j$$

set of orthonormal vectors

For low dimensional data, the residue becomes 0 very early. Suppose it gets 0 after 3 rounds then what?

$$\text{Dataset: } \{x_1, x_2, \dots, x_n\} \in \mathbb{R}^d$$

$$\forall i, \; x_i = (x_i^Tw_1)w_1 + (x_i^Tw_2)w_2 + (x_i^Tw_3)w_3$$

Reps: $\{w_1, w_2, w_3\}$   Coeffs: $x_i \rightarrow [x_i^Tw_1 \;\; x_i^Tw_2 \;\; x_i^Tw_3] \in \mathbb{R}^3$

Now numbers = $d\times k + k\times n$

$k \rightarrow$ no. of rounds where residue became 0
$d \rightarrow$ no. of dimensions
$n \rightarrow$ no. of datapoints
