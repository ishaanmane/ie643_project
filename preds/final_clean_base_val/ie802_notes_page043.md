```markdown
# Mathematical Programming

## Linear Programming Problem
\[
\begin{aligned}
& \text{minimize } c^T x + d^T \theta \\
& \text{subject to } g_i(x,\theta) \leq 0 \quad i=1,2,...,m \\
& x \in \mathbb{R}^n \\
& \theta \in \mathbb{Z}^p
\end{aligned}
\]

## Sets Definitions
- **S**: 
  \[
  S = \left\{(x,\theta): x \in \mathbb{R}^n, \theta \in \mathbb{Z}^p, g_i(x,\theta) \leq 0, i=1,2,...,m\right\}
  \]
- **R**:
  \[
  R = \left\{(x,\theta): x \in \mathbb{R}^n, \theta \in \mathbb{R}^p, g_i(x,\theta) \leq 0, i=1,2,...,m\right\}
  \]

## Finding (x,θ) Valid for S but not R
### Step 1: Pick a Disjunction (OR)
- Example: \( y_1 \leq 0 \) or \( y_1 \geq 1 \)
- Example: \( y_5 \leq 4 \) or \( y_5 \geq 5 \)
- Example: \( y_5 + y_6 + y_4 \leq 1 \) or \( y_5 + y_6 + y_4 \geq 2 \)

### Step 2: Define Sets
- **S1**:
  \[
  S_1 = \left\{(x,\theta): x \in \mathbb{R}^n, \theta \in \mathbb{Z}^p, g_i(x,\theta) \leq 0, i=1,2,...,m, y_1 \leq 1\right\}
  \]
- **S2**:
  \[
  S_2 = \left\{(x,\theta): x \in \mathbb{R}^n, \theta \in \mathbb{Z}^p, y_1 \geq 2\right\}
  \]
- **S**: 
  \[
  S = S_1 \cup S_2
  \]

### Step 3: Relaxation
- **R1**:
  \[
  R_1 = \left\{(x,\theta): x \in \mathbb{R}^n, \theta \in \mathbb{R}^p, g_i(x,\theta) \leq 0, i=1,2,...,m, y_1 \leq 1\right\}
  \]
- **R2**:
  \[
  R_2 = \left\{(x,\theta): x \in \mathbb{R}^n, \theta \in \mathbb{R}^p, y_1 \geq 2\right\}
  \]
```