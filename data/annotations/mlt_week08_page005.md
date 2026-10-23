# Naive Bayes Algorithm

## Parameter Estimation of the Generative Model

$$p, \{p_1',\dots,p_d'\}, \{p_1^0,\dots,p_d^0\} \quad [\text{d features for each label}]$$

MLE, $\hat{p} = \frac{1}{n}\sum_{i=1}^{n}y_i \leftarrow$ fraction of spam emails in the dataset

$$\hat{p}_j^y = \frac{\sum_{i=1}^{n}\mathbb{1}(f_j^i=1,y_i=y)}{\sum_{i=1}^{n}\mathbb{1}(y_i=y)}$$

numerator ← emails with label $y$ & containing feature $j$
denominator ← no. of emails with label $y$

fraction of emails with label $y$ containing the $j^{th}$ word

## Prediction

Given $x^{test}\in\{0,1\}^d$, what is $\hat{y}^{test}$?

if $P(y^{test}=1/x^{test}) > P(y^{test}=0/x^{test})$ then $\hat{y}^{test}=1$, $=0$ otherwise

But how to obtain $P(y/x)$ from $P(y)$ & $P(x/y)$

**Bayes Rule!**
