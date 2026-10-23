generative model.

**Step 1:** Decide the label by tossing a coin. $P(y_i=1)=p$

**Step 2:** Decide the features using the label in step 1 by $P(x_i/y_i)$

[Diagram: For $d=3$, a table of all 8 binary feature vectors $(w_1,w_2,w_3)$ each mapped to a "probability of being spam" value (0.1, 0.01, 0.02, 0.03, 0.04, 0.5, 0.2, 0.1). Center: a box labeled $p$ branches to SPAM ($y=1$) and NON-SPAM ($y=0$) cubes, each showing example bit patterns like 000, 001, 011. Right: separate probability tables for $w_1,w_2,w_3$ under spam/non-spam.]

$$\text{No. of parameters} = \underbrace{1}_{\text{to decide label}} + \underbrace{(2^d-1)}_{P(x/y=1)} + \underbrace{(2^d-1)}_{P(x/y=0)}$$

$$\therefore \# \text{parameters} = (2^{d+1}-1)$$

The issue here is **TOO MANY PARAMETERS!**
We need to change our generative story
