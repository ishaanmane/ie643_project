```markdown
# Soft-max function

## Min-Max Scaling

The soft-max function is defined as:

$$
\hat{y}_j = \frac{\exp(a_j)}{\sum_{k=1}^{K} \exp(a_k)}
$$

Where:
- $\hat{y}_j$ represents the probability of class $j$.
- $a_j$ is the raw score for class $j$.
- $K$ is the total number of classes.

### Step-by-Step Explanation

1. **Compute Raw Scores ($a_j$)**:
   - For each class $j$, compute the raw score $a_j$.

2. **Apply Min-Max Scaling**:
   - Normalize the raw scores using min-max scaling:
     $$
     \hat{y}_j = \frac{a_j}{\sum_{j=1}^C a_j}
     $$

3. **Compute Soft-Max Values**:
   - Apply the soft-max function to obtain the final probabilities:
     $$
     \hat{y}_j = \frac{\exp(a_j)}{\sum_{k=1}^{K} \exp(a_k)}
     $$

This process ensures that the probabilities sum up to 1, making it suitable for classification tasks where the output is a distribution over classes.
```