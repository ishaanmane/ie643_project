# Alternate Generative Model-Based Algorithm

## The Generative Story

[Diagram: A box $p$ branches to SPAM ($y=1$) and NON-SPAM ($y=0$). Under spam, each word (word1, $w_2$, $w_3$) gets its own coin with probability $p_1',p_2',p_3'$; under non-spam, each word gets probability $p_1^0,p_2^0,p_3^0$. Each per-word coin flip (tail/head) independently generates that word's bit.]

$$\#\text{parameters} = 1 + d + d = (2d+1) \quad \text{Manageable}$$

**Assumption: Class Conditional Independence Assumption.**
It means, given the class (spam or non spam), the features are independent of each other.

---

**Step 1:** $P(y=1) = p$

**Step 2:** $P(x=[f_1\;f_2\;f_3\;\dots\;f_d]/y) = \prod_{i=1}^{d}(p_i^y)^{f_i}(1-p_i^y)^{(1-f_i)}$

**Example:** $y=1$: $P(x=[0\;1\;0]/y) = ?$
