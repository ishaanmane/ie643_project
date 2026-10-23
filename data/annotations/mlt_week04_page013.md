# Convex Functions and Jensen's Inequality

[Diagram: A convex bowl-shaped curve with points $a$, $\frac{a+b}{2}$, $b$ marked, showing $f(a)$, $f(b)$, the chord midpoint $\frac{f(a)+f(b)}{2}$ above the curve value $f(\frac{a+b}{2})$.]

$$\forall a,b: \; f\left(\frac{a+b}{2}\right) \leq \frac{f(a)+f(b)}{2}$$

When the linear interpolation of two points has a strictly higher value the function itself $\forall a,b$ then it is a **convex function**.

Concave is just the opposite: $f\left(\frac{a+b}{2}\right) \geq \frac{f(a)+f(b)}{2}$

Linear functions are both concave & convex: $f\left(\frac{a+b}{2}\right) = \frac{f(a)+f(b)}{2}$

[Diagram: A straight increasing line labeled with $f(a), f(b)$ at $a, b$ (linear = both). Beside it, a wildly oscillating curve labeled "Neither concave nor convex".]

We can write convex functions like this:
$$f\left(\tfrac{1}{2}a+\tfrac{1}{2}b\right) \leq \tfrac{1}{2}f(a)+\tfrac{1}{2}f(b)$$
$$f(\lambda a+(1-\lambda)b) \leq \lambda f(a)+(1-\lambda)f(b) \quad \lambda \in [0,1]$$
