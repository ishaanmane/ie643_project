```markdown
# Projection of M on (x,y) space is convex hull of R1 U R2

## M_convex
The projection of M onto the (x,y) space forms the convex hull of the regions R1 and R2.

\[
M_{convex} = \left\{
\begin{array}{ll}
x_1, y_1, x_2, y_2 & x, y, \lambda^1, \lambda^2 \\
\lambda^1 g_i\left(\frac{x_1}{\lambda^1}, \frac{y_1}{\lambda^1}\right) \leq 0 & \lambda^1 + \lambda^2 = 1 \\
\lambda^2 g_i\left(\frac{x_2}{\lambda^2}, \frac{y_2}{\lambda^2}\right) \leq 0 & y \geq 0 \\
x = \frac{x_1}{\lambda^1} + \frac{x_2}{\lambda^2} & \\
y = \frac{y_1}{\lambda^1} + \frac{y_2}{\lambda^2} &
\end{array}
\right.
\]

## Perspective Function
The perspective function p(⋅) is defined as:

$$
p(⋅) = 
\begin{cases}
\lambda^1 g_i\left(\frac{x_1}{\lambda^1}, \frac{y_1}{\lambda^1}\right) & \lambda^1 > 0 \\
0 & \lambda^1 = 0
\end{cases}
$$

## Upcoming Topics
- Intersection cuts
- Cuts for non-convex Quadratic
- Heuristic

## Next Thursday
- 2-3 min per team short presentation
- Next to next
- Colorful class
```