12/03/26

Relaxation of intersection of 2 non-convex sets tighter than Intersection of relaxations.

Let $S_1, S_2$ be two non convex sets, then take intersection.

$$\text{Convex Hull}(S_1) \cap \text{Convex hull}(S_2) \supseteq \text{Convex hull}(S_1\cap S_2)$$

**Convex hull:** in any non-convex set, the minimal convex set that can fit in [contain the] non-convex set.

[Diagram: A large oval labeled "Conv($S_1$)" (blue outline) enclosing an irregular blob labeled "non convex set $S_1$" (red outline).]

**Proof:** Pick any point in RHS. It is in LHS (Conv($S_1$) & Conv($S_2$))

we get 3 constraints. $g_1(x)\leq0 \leftarrow$ feasible region of 1st constraint $=S_1$
$g_2(x)\leq0 \leftarrow$ 2nd $\dots=S_2$
$g_3(x)\leq0 \leftarrow$ 3rd $\dots=S_2$

Ideally: find Conv($S_1\cap S_2\cap S_3$) → It is hard & complicated, this is much more difficult than finding original answer.

Separately find convex hull of $S_i$ individually for all, then intersect.

**Reality:** $\text{Conv}(S_1)\cap\text{Conv}(S_2)\cap\text{Conv}(S_3)$
