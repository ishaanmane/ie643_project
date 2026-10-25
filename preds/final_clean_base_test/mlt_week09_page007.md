```markdown
# Lecture Notes

## Week 9 Page 7

### Proof of Convergence

#### Step-by-Step Analysis

1. **Initial Setup**
   \[
   \|w^{l+1}\|^2 = \|w^l + xy\|^2
   \]
   \[
   = (w^l + xy)^T(w^l + xy)
   \]
   \[
   = \|w^l\|^2 + 2(w^Tx)y + \|x\|^2y^2
   \]

2. **Bounding the Expression**
   \[
   \|w^{l+1}\|^2 \leq \|w^l\|^2 + R^2
   \]
   \[
   \|w^{l+1}\|^2 \leq (\|w^{l-1}\|^2 + R^2) + R^2
   \]
   \[
   \|w^{l+1}\|^2 \leq \|w^0\|^2 + lR^2
   \]

3. **Final Bound**
   \[
   \|w^{l+1}\|^2 \leq lR^2
   \]

4. **Misclassification Count**
   - Number of mistakes: \( m \)

5. **Inner Product Analysis**
   \[
   (w^{l+1})^Tw^* = (w^l + xy)^Tw^*
   \]
   \[
   = w^Tw^* + (w^*Tx)y
   \]

6. **Lower Bound**
   \[
   (w^{l+1})^Tw^* \geq w^Tw^* + \delta
   \]
   \[
   \geq (w^{l-1}Tw^* + \delta) + \delta
   \]

This sequence demonstrates the convergence properties of the algorithm under consideration.
```