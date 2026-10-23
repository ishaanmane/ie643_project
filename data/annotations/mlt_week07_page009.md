# Generative & Discriminative Models

Let's assume Distribution $D$ over $X\times Y$ (feature space, label $\{+1,-1\}$)

It means every datapoint in the training set is drawn according to distribution $D$.

$$\{x_1,\dots,x_n\}, \; \{y_1,\dots,y_n\}, \qquad (x_i,y_i)\sim D$$

Let the test set also follow the same distribution $D$.

$\therefore D$ is the link b/w training & test data (unknown but fixed)

We can make some assumptions about $D$ which will lead us to different types of algorithms.

---

## Types of Models

**Generative Model**
- $P(x,y)$
- Eg:

**Discriminative Model**
- $P(y|x)$
- Eg: K-NN, Decision Tree
  - $P(y=1|x)=1$ if the decision tree for $x$ says 1
  - $P(y=1|x)=1$ if majority
