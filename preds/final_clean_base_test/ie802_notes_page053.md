```markdown
# Heuristics for MINLO

## Initial Construction Heuristic

- **Feasibility Pump (Expensive)**
  - Rounding (Sophisticated)

- **MILP Case:** (Pure Binary)
  \[
  \min c^T x \\
  Ax \leq b \\
  x \in \{0,1\}^n
  \]

### Step 1: Solve the LP
\[
\begin{cases}
\min c^T x \\
Ax \leq b \\
0 \leq x \leq 1
\end{cases}
\]

#### If fractional $\rightarrow$ round it to nearest integer
- Not always works

#### Simple rounding of $\bar{x} = \left[ \begin{array}{c} \lfloor x_1 \rfloor \\ \vdots \\ \lfloor x_n \rfloor \end{array} \right]$
\[
\min \sum_{i=1}^{n} |x_i - \bar{x}_i|
\]
Subject to:
\[
Ax \leq b \\
0 \leq x \leq 1
\]

#### Example:
If $\bar{x} = \left[ \begin{array}{c} 0.4 \\ 0.6 \\ 0.8 \\ 0.2 \end{array} \right]$
Then $\bar{x}$ rounded is $\left[ \begin{array}{c} 0 \\ 1 \\ 1 \\ 0 \end{array} \right]$

### Step 2: Network Flow Heuristic
\[
\min \sum_{i=1}^{n} |x_i - \bar{x}_i|
\]
Subject to:
\[
Ax \leq b \\
0 \leq x \leq 1
\]

#### If $\bar{x} = \left[ \begin{array}{c} 0.1 \\ 0.9 \\ 0 \\ 0 \end{array} \right]$
Again rounding off gives same gain.

#### We have to stop heuristics and flip some variables.
```
