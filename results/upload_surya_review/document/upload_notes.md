---
title: "Lecture notes"
geometry: margin=2cm
papersize: letter
fontsize: 11pt
mainfont: DejaVu Serif
header-includes:
  - \usepackage{float}
  - \floatplacement{figure}{H}
  - \usepackage{fvextra}
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,breakanywhere,commandchars=\\\{\}}
  - \usepackage{cancel}
---


<!-- page: upload_notes_page001 -->

## Recap.

$$D = \{(x^s,y^s)\}_{s=1}^{S}, \quad x^s,y^s \in \mathbb{R}^n$$

## Encoder-decoder architecture

All hidden layer & output layer neurons have **linear** activations.

For input $x$, the prediction is:
$$\hat{y} = ABx$$

![A chain of three boxes — $p$-neuron layer $\xrightarrow{B}$ $n$-neuron layer ($p \leq n$) $\xrightarrow{A}$ output layer $\xrightarrow{\hat{y}}$.](figures/upload_notes_page001_b7.png){width=36.3101%}

<!-- page: upload_notes_page002 -->

## Loss fn.: Squared error.

For $D = \{(x^s,y^s)\}_{s=1}^{S}$,

$$E(A,B) = \sum_{s=1}^{S}\|y^s-y^*\|^2 = \sum_{s=1}^{S}\|ABx^s-y^s\|^2$$

$$\xrightarrow{b} \xrightarrow{a} \xrightarrow{}$$

$$\sum_{s=1}^{S}(abx^s-y^s)^2 =: E(a,b)$$

When $a$ is fixed:
observe that $E(a_{fixed},b)$ is **convex** wrt $b$.
When $b$ is fixed, $E(a,b_{fixed})$ is cvx wrt $a$.

![drawing from the page (no description in the notes)](figures/upload_notes_page002_b6.png){width=55.0000%}

<!-- page: upload_notes_page003 -->

## Convexity:

**Convex combination of 2 pts.**

![A line segment with two points $x_1$ (left) and $x_2$ (right), marked by an asterisk at the midpoint $\lambda x_1 + (1-\lambda)x_2$, `\lambda \in \[0,1\]` (not typeset).](figures/upload_notes_page003_b3.png){width=55.0000%}

![A triangle with a convex combination point marked inside it.](figures/upload_notes_page003_b5.png){width=55.0000%}

A set $C$ is convex if for any arbitrary pair $x_1, x_2 \in C$, the cvx combination $\lambda x_1 + (1-\lambda)x_2$ also belongs to $C$.

![An oval shape with a horizontal line segment drawn through its center.](figures/upload_notes_page003_b7.png){width=55.0000%}

<!-- page: upload_notes_page004 -->

## Convex function:

A function $f: C \to \mathbb{R}$ over a convex set $C$ is called **convex** if:

for any $x_1, x_2 \in C$ and for $\lambda \in [0,1]$

$$f(\lambda x_1 + (1-\lambda) x_2) \leq \lambda f(x_1) + (1-\lambda) f(x_2)$$

cvx comb of $x_1$ & $x_2$

Convex combination of fn evaluated at $x_1, x_2$

![A curve with points $(x_1,f(x_1))$, $(z,f(z))$, $(x_2,f(x_2))$ on it, showing the chord between $(x_1,f(x_1))$ and $(x_2,f(x_2))$ lying above the curve at point $z$.](figures/upload_notes_page004_b7.png){width=55.0000%}

graph $\leq$ Chord

<!-- page: upload_notes_page005 -->

## Optimization problem:

$$\min_{x \in C} f(x) \rightarrow \text{(P)}$$

convex set $\rightarrow$ convex fn.

(P) is a convex opt problem

$$\min_{w_1,w_2,\dots,w_L} E(\hat{y},y) \quad \hat{y} = \text{MLP}(x; w^1,w^2,\dots,w^L)$$

## Characterizations of convex fn:

1) If $f$ is cont. diff. then it satisfies some cdn.
[Diagram: A bowl-shaped curve with a tangent line at its minimum point.]

2) If $f$ is twice cont. diff. then: $f''(x) \geq 0 \; \forall x \in C$

![drawing from the page (no description in the notes)](figures/upload_notes_page005_b2.png){width=55.0000%}

![drawing from the page (no description in the notes)](figures/upload_notes_page005_b9.png){width=52.8962%}

<!-- page: upload_notes_page006 -->

## In n-dim case:

1) $\nabla_x^2 f = \begin{bmatrix} \frac{\partial^2 f}{\partial x_1 \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\ \vdots & & \vdots \\ \frac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n \partial x_n} \end{bmatrix}$

2) for twice diff $f$, $\nabla_x^2 f \geq 0$

Hessian if p.s.d. $\rightarrow$ the eigen values of $\nabla_x^2 f$ are non-negative.

A matrix $A$ is positive semi-def if:
$$v^T A v \geq 0 \quad \forall v \in \mathbb{R}^n$$
$$\langle v, Av \rangle \geq 0$$

<!-- page: upload_notes_page007 -->

$$\min_{A,B} \sum_{s=1}^{S} \|ABx^s - y^s\|_2^2 =: E(A,B) \quad x^s \in \mathbb{R}^n, \; y^s \in \mathbb{R}^n$$

When wts of $A$ are fixed, is $E(A_{fixed}, B)$ convex wrt wts of $B$?
When wts of $B$ are fixed, is $E(A, B_{fixed})$ convex wrt wts of $A$?

$$\sum_{s=1}^{S} \|\hat{y}^s - y^s\|_2^2$$

$$Y = \begin{bmatrix} \uparrow & \uparrow & & \uparrow \\ y^1 & y^2 & \cdots & y^S \\ \downarrow & \downarrow & & \downarrow \end{bmatrix}$$

sample 1 true, sample 2 true, ..., sample $S$ true

<!-- page: upload_notes_page008 -->

$$\hat{y} = \begin{bmatrix} \uparrow & \uparrow & & \uparrow \\ \hat{y}^1 & \hat{y}^2 & \cdots & \hat{y}^S \\ \downarrow & \downarrow & & \downarrow \end{bmatrix}$$

$$\sum_{s=1}^{S} \|\hat{y}^s - y^s\|^2 =$$

![A column of $\hat{y}^1, \hat{y}^2, \dots, \hat{y}^S$ (each with an up arrow above and down arrow below) next to a column of $y^1, y^2, \dots, y^S$ (each with an up arrow above and down arrow below), separated by a vertical line.](figures/upload_notes_page008_b3-b4.png){width=46.7464%}

$$- \left\| \begin{bmatrix} \uparrow & \uparrow & & \uparrow \\ \hat{y}^1 & \hat{y}^2 & \cdots & \hat{y}^S \\ \downarrow & \downarrow & & \downarrow \end{bmatrix} \right\|^2 =$$

<!-- page: upload_notes_page009 -->

$$\|\text{vec}(\hat{Y}) - \text{vec}(Y)\|^2 = E(A,B)$$

$\text{vec}(Y)$ = vectorization/flattening of $Y$

$$= \begin{bmatrix} \uparrow \\ y^1 \\ \downarrow \\ \uparrow \\ y^2 \\ \downarrow \\ \vdots \\ \uparrow \\ y^S \\ \downarrow \end{bmatrix}$$

$$\hat{y}^1 = ABx^1, \quad \hat{y}^2 = ABx^2, \quad \vdots \quad \hat{y}^S = ABx^S$$

$$E(A,B) = \|\text{vec}(ABX) - \text{vec}(Y)\|^2$$

$$AB\begin{bmatrix} \uparrow \\ x^1 \\ \downarrow \\ \uparrow \\ x^2 \\ \downarrow \\ \vdots \\ \uparrow \\ x^S \\ \downarrow \end{bmatrix} = \text{vec}(ABX)$$

<!-- page: upload_notes_page010 -->

$$E = \|\text{vec}(ABX) - \text{vec}(Y)\|^2$$

When we fix $A$, $E = \|M\text{vec}(B) - \text{vec}(Y)\|^2$

Suppose $Z = \text{vec}(B)$, $C = \text{vec}(Y)$

$$E = \|MZ-C\|_2^2 = (MZ-C)^T(MZ-C) = (Z^TM^T-C^T)(MZ-C) = Z^TM^TMZ - 2(MZ)^TC + C^TC$$

$$\min_Z \|MZ-C\|^2 / \text{convex opt problem}$$
Opt. problem is convex wrt. $Z$

$$F(Z) = \|MZ-C\|^2, \quad \nabla F(Z) = 2M^TMZ - 2M^TC$$
$$\nabla^2 F(Z) = 2M^TM, \quad M^TM \text{ is p.s.d.}$$

<!-- page: upload_notes_page011 -->

$M$ is of some size $q\times q$, for any $v\in\mathbb{R}^q$, $v^TM^TMv\geq0$. $\|Mv\|^2\geq0$

![A convex curve with a minimum marked at its lowest point.](figures/upload_notes_page011_b3.png){width=55.0000%}

$$\nabla F(z) = 2M^TMz - 2M^TC = 0$$

If $z^*$ satisfies $M^TMz^*-M^TC=0$, then $z^*$ is optimal pt. for min $\|Mz-c\|$.

**Optimality for cvx opt. problems:** A pt. $x^*\in C$ is an optimal point for the cvx. opt. problem $\min_{x\in C}f(x)$ if and only if $\nabla f(x^*)=0$

<!-- page: upload_notes_page012 -->

$$\| \text{vec}(ABX) - \text{vec}(Y) \|^2 = \epsilon$$

for fixed $A$, $\| M \text{vec}(B) - \text{vec}(Y) \|^2$

$$\| Mz-c \|_2$$

$$\text{vec}(ABX) = (X^T \otimes A) \text{vec}(B)$$

Kronecker product of $X^T$ & $A$

Suppose $G = \begin{bmatrix} g_{11} & g_{12} & \cdots & g_{1n} \\ \vdots & & & \vdots \\ g_{m1} & g_{m2} & \cdots & g_{mn} \end{bmatrix}_{m\times n}$

$$H = \begin{bmatrix} h_{11} & h_{12} & \cdots & h_{1q} \\ \vdots & & & \vdots \\ h_{p1} & h_{p2} & \cdots & h_{pq} \end{bmatrix}_{p\times q}$$

<!-- page: upload_notes_page013 -->

$$G \otimes H = \begin{bmatrix} g_{11}H & g_{12}H & \cdots & g_{1n}H \\ \vdots & & & \vdots \\ g_{m1}H & g_{m2}H & \cdots & g_{mn}H \end{bmatrix}_{mp\times nq}$$

$$\|Mz-c\|^2 =: F(z)$$
$$\|(X^T\otimes A)z-c\|^2$$
$$\nabla F(z) = 0 \Rightarrow M^TMz - M^Tc = 0$$

For an opt-$z^*$,
$$M^TMz^* = M^Tc$$
$$(X^T\otimes A)^T(X^T\otimes A)z^* = (X^T\otimes A)^Tc$$

<!-- page: upload_notes_page014 -->

**Prop 1:** $(G \otimes H)^T = G^T \otimes H^T$

**Prop 2:** $(G \otimes H)(U \otimes V) = GU \otimes HV$

$$(X^T \otimes A)^T (X^T \otimes A) z^* = (X^T \otimes A)^T c$$
$$(X \otimes A^T)(X^T \otimes A) z^* = (X \otimes A^T)c$$
$$(XX^T \otimes A^TA)z^* = (X \otimes A^T)c$$

$$\text{vec}(ABX) = (X^T \otimes A)\text{vec}(B)$$

$$(XX^T \otimes A^TA)\text{vec}(B^*) = (X \otimes A^T)\text{vec}(Y)$$
$$A^TA \; B^* \; XX^T = A^TYX^T$$
$$XX^T = \qquad YX^T$$

<!-- page: upload_notes_page015 -->

$$X = \begin{bmatrix} \uparrow & \uparrow & \uparrow \\ x^1 & x^2 & \cdots x^S \\ \downarrow & \downarrow & \downarrow \end{bmatrix}_{n\times S}$$

$$XX^T = \text{feature covariance matrix}, \quad n\times n \; \text{matrix}$$

$$XX^T = \sum_{s=1}^{S} x^s(x^s)^T, \quad YY^T = \sum_{s=1}^{S} y^s(x^s)^T, \quad XY^T = \sum_{s=1}^{S} x^s(y^s)^T$$

$$A^TA B^* XX^T = A^T Y X^T$$
$$\boxed{A^TA B^*\Sigma_{xx} = A^T\Sigma_{yx}}$$

Assume:
- $\Sigma_{xx}$ is invertible,
- $A$ is full rank $\Rightarrow A^TA$ is also inv.

$$A^TA B^*\Sigma_{xx} = A^T\Sigma_{yx}$$

<!-- page: upload_notes_page016 -->

$$B^* = (A^TA)^{-1} A^T \Sigma_{yx} (\Sigma_{xx})^{-1}$$

$\rightarrow$ **Unique soln?**

$$\min_{z} \|Mz-q\|^2$$

$\sum_{xx}$ is invertible?

Linear comb. of $v_1,v_2\dots v_k$: $\alpha_1v_1+\alpha_2v_2+\cdots+\alpha_kv_k$, $\alpha_1,\dots,\alpha_k$ are real nos.

A set $v_1,v_2\dots v_k$ is l.i. if $\alpha_1v_1+\alpha_2v_2+\cdots+\alpha_kv_k=0$ is written uniquely for $\alpha_1,\alpha_2\dots\alpha_k$. $X=\begin{bmatrix}\uparrow&\uparrow&\uparrow\\\vdots&\vdots&\vdots\\x^1&x^2&\dots x^S\end{bmatrix}$ has linearly independent columns.

<!-- page: upload_notes_page017 -->

$$v_j \neq \beta_1 v_1 + \beta_2 v_2 + \cdots + \beta_{j-1} v_{j-1} + \beta_{j+1} v_{j+1} + \cdots + \beta_k v_k$$

**A is full rank**

*[Diagram: A chain $B \to D \to A \to n$, with $p \leq n$.]*

$$A_{n\times p} \text{ matrix}, \quad p \leq n$$

$$A_{n\times p} \; h_{p\times 1} \rightarrow b_{n\times 1} \; \text{vector}$$

$$\text{rank}(A) = p \iff A^TA \text{ is positive definite}$$

$$\text{rank}(A) = \text{num of linearly ind rows/cols}$$

$$\text{rank}(A) \leq \min(p,n) \quad \text{(if } A^TA \text{ is invertible)}$$

$$\text{rank}(A) \leq p \quad \text{when } A \text{ is full rank, rank}(A)=p$$

<!-- page: upload_notes_page018 -->

$$\nabla^2 F = M^T M \; \text{is p.d.} \implies \|Mz-c\|^2 \text{ becomes strictly convex}$$

$$\left(X^T \otimes A\right)^T \left(X^T \otimes A\right)$$
$$\left(X \otimes A^T\right)\left(X^T \otimes A\right)$$
$$\left(XX^T \otimes A^TA\right) \rightarrow \text{p.d.}$$

![A strictly convex bowl shape with a unique minimum marked.](figures/upload_notes_page018_b7.png){width=53.9010%}

eigen values are strictly +ve

minimizer is unique

**Prop 3:** If $G$ is sym.p.d & $H$ is sym.p.d then $G \otimes H$ is also sym.p.d.

<!-- page: upload_notes_page019 -->

$$A = \begin{bmatrix} \uparrow & \uparrow & & \uparrow \\ A_1 & A_2 & \cdots & A_p \\ \downarrow & \downarrow & & \downarrow \end{bmatrix}, \quad h = \begin{bmatrix} h_1 \\ h_2 \\ \vdots \\ h_p \end{bmatrix}$$

*[Diagram: $D_B \xrightarrow{B} D_A \xrightarrow{A} D$, chain of three boxes.]*

$$Ah = h_1A_1 + h_2A_2 + \cdots + h_pA_p \quad \text{(b's)}$$

$$\min_{A,B} \|{\rm vec}(ABX) - {\rm vec}(Y)\|$$

$$W = AB$$
$$E(A,B) = \operatorname{Tr}(\Sigma_{yy}) - \sum_{i\in F}\lambda_i$$

<!-- page: upload_notes_page020 -->

![A chain $x \to B \to \hat{x}$](figures/upload_notes_page020_b1.png){width=52.8279%}

$$\Sigma = \Sigma_{yx} \Sigma_{xx}^{-1} \Sigma_{xy} = \Sigma_{xx} \Sigma_{xx}^{-1} \Sigma_{xx}$$

$$\sum_s \|ABx^s - x\|^2, \quad D = \{(x^s,x^s)\}_{s=1}^{S}, \qquad \Sigma = \Sigma_{xx}$$

$$E = \text{Tr}(\Sigma_{xx}) - \sum_{i \in J} \lambda_i \; \Rightarrow \text{PCA objective}$$

Baldi & Hornik:

$$X = \begin{bmatrix} \uparrow & & \uparrow \\ x^1 & \cdots & x^S \\ \downarrow & & \downarrow \end{bmatrix}$$

**PCA:** variance(true data) — var(proj. data)

# Original source pages

Original scans for checking transcription and diagrams.

![Original source page 1](sources/source_001.jpg){width=90.0000%}

![Original source page 2](sources/source_002.jpg){width=90.0000%}

![Original source page 3](sources/source_003.jpg){width=90.0000%}

![Original source page 4](sources/source_004.jpg){width=90.0000%}

![Original source page 5](sources/source_005.jpg){width=90.0000%}

![Original source page 6](sources/source_006.jpg){width=90.0000%}

![Original source page 7](sources/source_007.jpg){width=90.0000%}

![Original source page 8](sources/source_008.jpg){width=90.0000%}

![Original source page 9](sources/source_009.jpg){width=90.0000%}

![Original source page 10](sources/source_010.jpg){width=90.0000%}

![Original source page 11](sources/source_011.jpg){width=90.0000%}

![Original source page 12](sources/source_012.jpg){width=90.0000%}

![Original source page 13](sources/source_013.jpg){width=90.0000%}

![Original source page 14](sources/source_014.jpg){width=90.0000%}

![Original source page 15](sources/source_015.jpg){width=90.0000%}

![Original source page 16](sources/source_016.jpg){width=90.0000%}

![Original source page 17](sources/source_017.jpg){width=90.0000%}

![Original source page 18](sources/source_018.jpg){width=90.0000%}

![Original source page 19](sources/source_019.jpg){width=90.0000%}

![Original source page 20](sources/source_020.jpg){width=90.0000%}
