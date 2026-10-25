```markdown
The image contains a series of mathematical derivations related to linear regression or a similar statistical model. Here is the transcription:

---

### Derivation of Residual Sum of Squares (RSS)

1. **Initial Expression:**
   \[
   = \sum_{k \neq j} y_k \hat{y}_j - y_j + y_j \hat{y}_j
   \]

2. **Simplification:**
   \[
   = \sum_{k=1}^n y_k \hat{y}_j - y_j
   \]

3. **Further Simplification:**
   \[
   = \hat{y}_j \sum_{k=1}^n y_k - y_j
   \]

4. **Final Form:**
   \[
   = \hat{y}_j \bar{y}_j - y_j
   \]
   where $\bar{y}_j$ represents the mean of the observed values.

5. **Derivative Calculation:**
   \[
   \frac{\partial e}{\partial a_j}
   \]

---

This sequence of steps leads to the calculation of the residual sum of squares (RSS) and its partial derivative with respect to the parameter $a_j$. The final form shows how the RSS can be expressed in terms of the predicted value $\hat{y}_j$ and the mean $\bar{y}_j$.
```