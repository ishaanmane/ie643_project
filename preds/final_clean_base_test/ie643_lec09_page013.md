```markdown
# Soft-Max Function

## Overview

The soft-max function is a mathematical function that converts a vector of real numbers into a probability distribution. It is widely used in machine learning, particularly in the context of classification problems.

## Formulation

### Soft-Max Function

The soft-max function is defined as follows:

$$
\hat{y}_j = \frac{\exp(a_j)}{\sum_{k=1}^{K} \exp(a_k)}
$$

where:
- $\hat{y}_j$ represents the probability of the j-th class.
- $a_j$ is the score or raw prediction for the j-th class.
- K is the total number of classes.

### Min-Max Scaling

Min-max scaling is a technique used to scale the input features to a fixed range, typically between 0 and 1. This is often done before applying the soft-max function to ensure that all inputs are on a similar scale.

### Example Calculation

Consider the following scores for three classes:

| Class | Score (a) |
|-------|-----------|
| 1     | 2         |
| 2     | 3         |
| 3     | 1         |

To calculate the probabilities using the soft-max function:

1. Compute the exponentials of the scores:
   - $\exp(2) = e^2 \approx 7.389$
   - $\exp(3) = e^3 \approx 20.086$
   - $\exp(1) = e^1 \approx 2.718$

2. Sum these exponentials:
   - $\sum_{k=1}^{3} \exp(a_k) = 7.389 + 20.086 + 2.718 = 30.193$

3. Calculate the probabilities:
   - $\hat{y}_1 = \frac{7.389}{30.193} \approx 0.245$
   - $\hat{y}_2 = \frac{20.086}{30.193} \approx 0.666$
   - $\hat{y}_3 = \frac{2.718}{30.193} \approx 0.089$

Thus, the probabilities for the three classes are approximately:
- Class 1: 0.245
- Class 2: 0.666
- Class 3: 0.089

### Diagrams

[Diagram: Flowchart showing the steps from raw scores to probabilities]

[Diagram: Graphical representation of the soft-max function applied to a set of scores]
```