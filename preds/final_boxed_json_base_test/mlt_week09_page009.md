```markdown
# Perceptron Convergence

The following steps outline the proof that the Perceptron algorithm converges:

1. **Equation 3**:
   \[
   l^2 \leq ||\omega^{t+1}||^2 \leq lR^2
   \]

2. **Text Block**:
   \[
   l \rightarrow \text{no. of mistakes}
   \]

3. **Equation**:
   \[
   \Rightarrow l^2 \leq R^2
   \]

4. **Equation**:
   \[
   \Rightarrow \sqrt{l} \leq \frac{R}{\delta}
   \leftarrow \text{Radius Margin Bound}
   \]

5. **Text Block**:
   Since \( \delta > 0 \), no. of mistakes is finite.

6. **Text Block**:
   \[
   \therefore \text{PERCEPTRON CONVERGES}
   \]
```