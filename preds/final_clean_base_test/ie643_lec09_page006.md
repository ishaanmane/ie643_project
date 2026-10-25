```markdown
# Handwritten Lecture Note Conversion

## Transformation of Discrete Labels into One-Hot Vectors

### Overview
The image shows the process of converting a discrete label `y` (which can take values from 1 to C) into a one-hot vector representation.

### Diagram: One-Hot Vector Representation
The diagram illustrates how a prediction `ŷ` is transformed into a one-hot vector. Here's the breakdown:

1. **Prediction and Label**: 
   - The prediction `ŷ` is shown alongside the true label `y`.
   - Both `ŷ` and `y` belong to the set `{1, 2, ..., c}`.

2. **Transformation Process**:
   - The true label `y` is transformed into a C-dimensional vector.
   - This transformation results in a one-hot vector where only the component corresponding to `y` is marked as 1, while all other components are 0.

3. **One-Hot Vector**:
   - For example, if `y = k`, the resulting one-hot vector will have a 1 in the `k`-th position and 0s elsewhere.

4. **Notation**:
   - The notation `y = k ∈ {1, 2, ..., c}` indicates that `y` is an element of the set `{1, 2, ..., c}`.

5. **One-Hot Vector Representation**:
   - The one-hot vector is depicted with a vertical line indicating the position of the 1.

This conversion is crucial in many machine learning algorithms, particularly in classification tasks, where the model outputs a probability distribution over the possible classes rather than a single class label.

---

This markdown structure captures the essence of the handwritten notes, including the mathematical expressions and the visual elements described in the diagram.