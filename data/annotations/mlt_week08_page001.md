# Generative Model Based Algorithm

$$\text{Data} = \{(x_1,y_1),\dots,(x_n,y_n)\}, \quad x_i \in \{0,1\}^d, \; y_i\in\{0,1\}$$

d features but each feature can take the value 0 or 1

**Example:** Spam Classification. $x_i \in \{0,1\}^d \leftarrow$ no. of words in dictionary

Email → "Hello how are you?"
$$[0\;0\;0\;\dots\;1\;\dots\;1\;\dots\;1\;\dots\;0]$$

The above is a d-dimensional vector with 0's & 1's. Every word in the dictionary gets one component of the above feature vector. We are going to take every word in the email & mark the corresponding entry in the feature vector as 1.

---

$$P(x,y) = P(\text{"Hello. How are you?"}, \text{spam}) = \dots$$
$$P(x,y) = P(x)\cdot P(y/x) = \frac{P(y)\cdot P(x/y)}{P(\text{spam})\cdot P(\text{email/spam})} \; \text{We'll be modelling this}$$

We need a Generative Story when we are making a
