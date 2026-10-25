```markdown
# Handwritten Lecture Note Page

## Diagram: Transformation of Discrete Y into a C-dim Vector

The diagram illustrates the process of transforming a discrete label `y` into a one-hot encoded vector.

### Step-by-Step Explanation:

1. **Input:**
   - A prediction `y` which can be any integer from 1 to C (`y ∈ {1, 2, ..., C}`).

2. **Transformation:**
   - Convert the discrete label `y` into a C-dimensional vector where:
     - The k-th component of the vector is set to 1 if `y = k`.
     - All other components are set to 0.

3. **One-Hot Encoding:**
   - For each possible value of `y`, create a vector of length C with all elements set to 0.
   - Set the element at position `k` (where `k` is the value of `y`) to 1.

### Mathematical Representation:

#### Prediction and Label:
- Let \( \hat{y} \) represent the predicted label.
- Let \( y \) represent the true label.

#### One-Hot Encoding:
- If \( y = k \), then the one-hot encoded vector will have a 1 in the k-th position and 0s elsewhere.

### Example:
If \( y = 3 \) and \( C = 5 \), the one-hot encoded vector would be:
\[ [0, 0, 1, 0, 0] \]

This vector indicates that the third component is 1, corresponding to the label `3`.

---

This process ensures that the model can learn from the discrete labels by converting them into a form that can be used in a neural network.