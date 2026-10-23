# Decision Tree Algorithm

- Step 1: Discretize each feature in the [min, max] range
- Step 2: Pick the question with the largest information gain
- Step 3: Repeat the procedure for $D_{yes}$ & $D_{no}$

**Points to remember:**
- Stop growing the tree if the node becomes "sufficiently" pure, $p \in [0,0.1]\cup[0.9,1]$
- Depth of tree is a hyperparameter

[Diagram: Left — a 2D scatter plot ($f_1$=height, $f_2$=weight) split into rectangular regions by decision boundaries at $f_1=5$ and $f_2=7$, colored red/green by class, labeled "DECISION BOUNDARY". Right — the corresponding decision tree: root $f_1\leq5$ (No→leaf 1), Yes→$f_2\leq7$ (No→leaf 0), Yes→$f_1\leq3$ (Yes→leaf 1, No→leaf 0).]
