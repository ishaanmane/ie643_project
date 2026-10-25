Yes ↙ &nbsp;&nbsp; No ↘

$D_{yes} = \{(x_1,y_1),(x_4,y_{10})\dots\}$ &nbsp;&nbsp; $D_{no} = \{(x_2,y_2),(x_3,y_3),\dots,\}$

The best question is the one which will divide the entire dataset into two parts where the labels of one side will be the same but different from the other side.

But such pure questions **may not exist**.

To find the goodness, we will need a measure of the "impurity" of the set of labels.

We can see the fraction of 1s in the labels set. Let the value be $p \in [0,1]$

Best case: $p=0$ or $1$ &nbsp; Impurity = 0%
Worst case: $p=0.5$ &nbsp; Impurity = 100%

Function to determine impurity: **Entropy**

$$\text{Entropy}(\{y_1,\dots,y_n\}) = \text{Entropy}(p) = -(p\log p + (1-p)\log(1-p))$$
