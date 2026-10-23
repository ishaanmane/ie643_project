## Issues with PCA

- **Time Complexity** — Finding the Eigenvector & Eigenvalues of Covariance matrix $\in \mathbb{R}^{d\times d}$ = $O(d^3)$

  When $d$ is large it is a problem. Example - face recognition. Yale dataset (where $d=32000$, $n=20000$)

- **Data may not necessarily lie on low dimensional subspace** — Features have a **non-linear** relationship

  [Diagram: A 3D plot with axes $f_1, f_2, f_3$, showing a curved purple surface (non-linear) enclosed by a flat green hyperplane, labeled "This is a curve (non-linear)" and "PCA algorithm will give this hyperplane (linear)".]

  Surprising fact: We will have the same solution for both these issues!
