```markdown
# Handwritten Lecture Note Page

## Linear Algebra and Perceptron Algorithm

### Problem Statement
Given the equation:
\[ x_1 + x_2 = 4 \]

We need to find the values of \( w_1 \) and \( w_2 \).

### Solution
Let's define the vector:
\[ \vec{w} = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \]

The dot product of \( \vec{w} \) and \( \vec{x} \) is given by:
\[ <\vec{w}, \vec{x}> = 4 \]

This can be written as:
\[ w_1 x_1 + w_2 x_2 = 4 \]

### Perceptron Update Rule
The perceptron update rule is:
\[ \tilde{\omega} = \omega + y \tilde{x} \]

Where:
- \( \omega \) is the current weight vector.
- \( y \) is the label (1 or -1).
- \( \tilde{x} \) is the input vector.

### Example Calculation
Consider the following vectors:
\[ \vec{w} = \begin{bmatrix} 1 \\ 1 \\ -4 \end{bmatrix} \]
\[ \vec{x} = \begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix} \]

Using the perceptron update rule:
\[ \tilde{\omega} = \begin{bmatrix} 1 \\ 1 \\ -4 \end{bmatrix} + (-1) \begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix} \]
\[ = \begin{bmatrix} 1 \\ 1 \\ -4 \end{bmatrix} + \begin{bmatrix} -2 \\ -1 \\ -1 \end{bmatrix} \]
\[ = \begin{bmatrix} -1 \\ 0 \\ -5 \end{bmatrix} \]

### Perceptron Function
The perceptron function is defined as:
\[ \text{Perceptron}(\tilde{x}) = \text{sign}(<\tilde{\omega}, \tilde{x}>) \]

For the updated weights:
\[ \tilde{\omega} = \begin{bmatrix} -1 \\ 0 \\ -5 \end{bmatrix} \]

Calculate the dot product:
\[ <\tilde{\omega}, \tilde{x}> = -1 \cdot 2 + 0 \cdot 1 + (-5) \cdot 1 \]
\[ = -2 + 0 - 5 \]
\[ = -7 \]

Thus:
\[ \text{Perceptron}(\tilde{x}) = \text{sign}(-7) = -1 \]
```