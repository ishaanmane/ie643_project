Then there exists a single hidden layer MLP with $N$ neurons in hidden layer (all with sigmoid activations) and a single o/p neuron with linear act. s.t.

$$\left| f(x) - \sum_{j=1}^{N} \alpha_j \sigma(w_j^T x + b_j) \right| < \epsilon \quad \forall x \in [0,1]^d$$

**Cybenko'** (theorem name)

[Diagram: A chain of nodes labeled $h: X \to Y$.]
