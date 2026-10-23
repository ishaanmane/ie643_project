# Introduction to Estimation

There is some probabilistic mechanism which generates the data, about which we don't know "something". Given the data, find/estimate what we don't know.

Let's say we have a black box with a biased coin inside. $[P(X=1)=p \neq 0.5]$ $[P(X=0)=1-p]$. There is a button which flips the coin when pressed. Let's say we press the button $n$ times & we get Heads (1) $k$ times & Tails (0) $(n-k)$ times.

Now, we are seeing (observing) only the data (no. of Heads & Tails). We are **assuming** that there is a mechanism which is producing (black box & button) the data. That part is unknown to us. The parameter 'p' is an unknown quantity. The bias of the coin is needed to know the story of how the data is generated.

**Goal of estimation:**
1. Observe the data
2. "Assume" a probabalistic model that generates data
3. Estimate unknown parameters using the data

Let's say we have 12 observations: $\{1,0,0,1,1,0,1,1,1,1,1,1\}$
