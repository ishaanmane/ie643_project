```markdown
# Logistic Regression

## Key Concepts

1. **Kullback-Leibler Divergence (KL)**

   - Definition:
     $$ \text{KL}(y_i, \hat{y}_i) = e(y_i, \hat{y}_i) $$
   
   - Properties:
     - KL = 0 when \( y_i = \hat{y}_i \)
     - KL > 0 when \( y_i \neq \hat{y}_i \)

2. **Objective Function**

   - Minimize the weighted sum of KL divergences:
     $$ \min_{\text{weights}} \sum_{i=1}^{N} \text{KL}(y_i, \hat{y}_i) $$

3. **Cross-Entropy Loss**

   - Alternative objective function:
     $$ \min_{\text{weights}} \sum_{i=1}^{N} \text{CE}(y_i, \hat{y}_i) $$

4. **Logistic Regression and Bernoulli Likelihood**

   - Logistic regression can be viewed as maximizing the Bernoulli likelihood:
     $$ E[y|x=\vec{x}] \rightarrow \text{Bernoulli likelihood} $$

## Diagrams

- [Diagram: Flowchart showing the relationship between KL divergence, cross-entropy loss, logistic regression, and Bernoulli likelihood]
```