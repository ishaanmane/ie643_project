```markdown
Consider a round \( t \) at which perception makes a mistake.

\[
\begin{aligned}
& y^t \neq y^t \\
& w^{t+1} = w^t + y^t x^t \\
& \langle w^{t+1}, w^* \rangle \\
& \quad = \langle w^t + y^t x^t, w^* \rangle \\
& \quad = \langle w^t, w^* \rangle + \langle y^t x^t, w^* \rangle \\
& \quad = \langle w^t, w^* \rangle + y^t \langle x^t, w^* \rangle
\end{aligned}
\]

After the mistake:

\[
\langle w^*, w^{t+1} \rangle \text{ and } \langle w^*, w^t \rangle
\]
```
