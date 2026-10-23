# Separability

$$* \sum_{i=1}^{n}|x_i| \leq 10$$

$$x_1+x_2\cdots x_n \leq 10$$
$$-x_1+x_2\cdots \leq 10$$
$$x_1-x_2\cdots \leq 10$$
$$\vdots$$
$$-x_1-x_2-x_3\cdots \leq 10$$

$2^n$ constants, $n \to$ variables

**Reformulation**
$$\sum_{i=1}^{n}w_i \leq 10, \quad |x_i|\leq w_i \; i=1,2,\dots n$$

$$\Leftrightarrow \sum_{i=1}^{n}w_i \leq 10, \quad x_i\leq w_i \; i=1,2,\dots n, \quad -x_i\leq w_i \; i=1,2,\dots n$$

$2n+1$ constraints, $2n$ variables

$$\to x_1^2+x_2^2+x_3^2+x_4^2+x_5^2 \leq 100$$

**Scheme①**
Say point① $(10,0,0,0,0)$: $F(\hat{x})+\nabla\cdots-100\leq0$

pt② $(0,10,0,0,0)$: $\hat{F}(\hat{x})+\nabla\cdots-100\leq0$ → Linearization

pt③ ... pt⑩

[Diagram: pt①-related sketch — a circle intersected by lines, labeled "pt① sqd" (squared).]

- Both schemes are equivalent → more tighter than above; any point that satisfies above also satisfies this

**Scheme②**
$$w_1+w_2+w_3+w_4+w_5\leq100$$
$$x_1^2\leq w_1, \; x_2^2\leq w_2, \; x_3^2\leq w_3, \; x_4^2\leq w_4, \; x_5^2\leq w_5$$

$\hat{x}$ (10,0,0,0,0); $\hat{w}$ (100,0,0,0,0)

$$x_1^2\leq w_1 \to x_1^2-w_1\leq0 \to 0+[20\;{-1}]\begin{bmatrix}x_1-0\\w_1-100\end{bmatrix}\leq0$$

[Diagram: a rectangle with diagonal, labeled $F(\hat{x})+\nabla\cdots$]

$\Rightarrow f\leq0$

$$f = f_1(x_1,x_2,x_3)+f_2(x_4,x_5,x_6)+f_3(x_4,x_8,x_9)+f_4(\dots)$$

Linearise $f$ at $k$ points $\to$ weak
$$f_1(x_1,x_2,x_3)\leq w_1 \to \exists \lim, \; w_2 \to 3 \text{ linearizations}$$
$w_1,\;w_4$

equivalent to $w_1+w_2+w_3+w_4+w_5\leq0$ [as] $3^4=81$ linearization in original
