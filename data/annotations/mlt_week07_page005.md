# Introduction to Decision Trees

Input: $\{(x_1,y_1),\dots,(x_n,y_n)\}$, $\forall i \; x_i\in\mathbb{R}^d$, $y_i\in\{0,1\}$

Output: Decision Tree

[Diagram: A binary tree — Question 1 branches Yes/No to Question 2 and Question 3. Question 2 branches to Ques.4 and Ques.5. Question 3 branches to leaf nodes 1 and 0. Ques.4 branches to leaves 1, 0; Ques.5 branches to leaves 0, 1. All leaves are labeled "PREDICTION / LEAF NODES".]

**Prediction:** Given $x_{test}$, you traverse through the tree to reach a leaf node.
$y_{test}$: value in leaf node

We can throw away the dataset once we have our decision tree.

---

What should be the "question" in the decision tree?
→ A question is a (feature, value) pair
eg: height $\leq (f_{18})$ cm $(\theta)$, $(f_3)$ $(\theta)$

How to measure the "goodness" of a question?

$$D = \{(x_1,y_1),\dots,(x_n,y_n)\}, \quad f_k \leq \theta$$
