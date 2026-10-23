30/03/26

**Project Work:** 15 minute presentation, your own work
- diagram
- example
- what work, what doesn't?
- assumptions → why? why not?
- Can result [be] extended or simplified to other cases..
- Don't repeat the result..

Next 2-3 class → cutting plane → Linear, NL, Quad...

**Cutting planes for MINLO:**
- QG algorithm
- Padberg's triangle inequalities for boolean quadratic models.

**MINLO:**
- Non-convex non-linearities
- Convex non-linearities
- Integer constraints

**Integer Linear Case:**
$$S=\left\{y=\begin{matrix}y_1\leq2.8\\y_1\in\mathbb{Z}\end{matrix}\right\}$$

Relax: $R=\{y: y_1\leq2.8, y_1\in\mathbb{R}\}$

Cutting plane: $y_1\leq2$

$$y_1\leq b, \; y_1\in\mathbb{Z} \Rightarrow y_1\leq\lfloor b\rfloor, \; y_1\in\mathbb{Z}$$

[Diagram: An irregular polygon with scattered "x" points, several crossing cutting lines, labeled "cutting plane not possible..".]
