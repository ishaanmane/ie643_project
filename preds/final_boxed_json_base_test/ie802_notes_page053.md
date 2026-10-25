```markdown
# Heuristics for MINLO

## Initial Construction Heuristic

- **Feasibility Pump** (expensive)
  - Rounding (sophisticated)
- **RNS**
- **Local Branching**

### MZLP Case: (Pure Binary)

$\min cx$

$Ax \leq b$

$x \in \{0,1\}^n$

1. Solve the LP

$$
\begin{aligned}
& \min cx \\
& Ax \leq b \\
& 0 \leq x \leq 1
\end{aligned}
$$

If fractional $\rightarrow$ round it to nearest integer

$\Rightarrow$ Not always good

Simple rounding of $\bar{x} = \left[\begin{array}{c}\lfloor x_1 \rfloor \\ \vdots \\ \lfloor x_n \rfloor\end{array}\right]$

$\Leftrightarrow$

$\min \sum_{i=1}^{n}|x_i - \bar{x}_i|$

$Ax \leq b$

$0 \leq x \leq 1$

$\bar{x} \rightarrow$ LP relaxation solution

Not working well

$\min |cx - c\bar{x}| + |x_2 - \bar{x}_2| + |x_3 - \bar{x}_3| + |x_4 - \bar{x}_4| + |x_5 - \bar{x}_5| + |x_6 - \bar{x}_6|$

$Ax \leq b$

$0 \leq x \leq 1$

If $\bar{x} = \left[\begin{array}{c}0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0\end{array}\right]$

Again round off gives same gain $\rightarrow$ We have to stop heuristic and flip some variables.

```
