```markdown
# Mathematical Programming

## Linear Programming Problem

\[
\begin{aligned}
& \min \quad c^T x + d^T y \\
& \text{s.t. } g_i(x,y) \leq 0 \quad i=1,2,\ldots,m \\
& x \in \mathbb{R}^n \\
& y \in \mathbb{Z}^p
\end{aligned}
\]

## Set Definitions

### Set S

\[ 
S = \left\{ (x,y): x \in \mathbb{R}^n, y \in \mathbb{Z}^p, g_i(x,y) \leq 0 \quad i=1,2,\ldots,m \right\}
\]

### Set R

\[ 
R = \left\{ (x,y): x \in \mathbb{R}^n, y \in \mathbb{R}^p, g_i(x,y) \leq 0 \quad i=1,2,\ldots,m \right\}
\]

## Finding Valid Points

Find $(x,y)$ such that it is valid for $S$ but not for $R$.

### Step ①: Pick a Disjunction (OR)

- $y_1 \leq 0$ or $y_1 > 0$
- $y_5 \leq 4$ or $y_5 > 5$
- $y_5 + y_6 + y_4 \leq 1$ or $y_5 + y_6 + y_4 \geq 2$

### Step ②: Define Sets $S_1$ and $S_2$

\[ 
S_1 = \left\{ (x,y): x \in \mathbb{R}^n, y \in \mathbb{Z}^p, g_i(x,y) \leq 0 \quad i=1,2,\ldots,m, y_1 \leq 1 \right\}
\]

\[ 
S_2 = \left\{ (x,y): y_1 > 1 \right\}
\]

\[ 
S = S_1 \cup S_2
\]

### Step ③: Relaxation

Relax $R_1$ and $R_2$:

\[ 
R_1 = \left\{ (x,y): x \in \mathbb{R}^n, y \in \mathbb{R}^p, g_i(x,y) \leq 0 \quad i=1,2,\ldots,m \right\}
\]

\[ 
R_2 = \left\{ (x,y): y \in \mathbb{R}^p, y_1 \geq 2 \right\}
\]
```