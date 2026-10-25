```markdown
# Projection of M on (x,y) space is convex hull of R1UR2

## M_convex
\[
M_{convex} = \left\{
\begin{array}{ll}
x^1, \overline{x}^1, \overline{x}^2, \overline{y}^1, \overline{y}^2 & x, y, \lambda^1, \lambda^2 \\
\lambda^1 g_i(\frac{\overline{x}^1}{\lambda^1}, \frac{y^1}{\lambda^1}) \leq 0 & \\
\lambda^2 g_i(\frac{\overline{x}^2}{\lambda^2}, \frac{y^2}{\lambda^2}) \leq 0 & \\
x = \frac{\overline{x}^1}{\lambda^1} + \frac{\overline{x}^2}{\lambda^2} & \\
y = \frac{\overline{y}^1}{\lambda^1} + \frac{\overline{y}^2}{\lambda^2} & \\
\end{array}
\right.
\]

## Perspective function
\[ p(x) = 
\begin{cases} 
\lambda^1 g_i(\frac{\overline{x}^1}{\lambda^1}, \frac{y^1}{\lambda^1}) & \lambda^1 > 0 \\
0 & \lambda^1 = 0
\end{cases}
\]

## Upcoming
- Intersection cuts
- Cut for non-convex Quadratic
- Heuristic

## Next Thursday
- 2-3 min per team short presentation
- Next to next
- Colout class
```