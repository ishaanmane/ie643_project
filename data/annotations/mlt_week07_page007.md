[Diagram: Entropy(p) plotted vs fraction of 1's — a bump peaking at $p=0.5$ (blue curve), with a flat red baseline from 0 to 1.]

[Diagram: $D$ splits via question $f_k\leq\theta?$ into $D_{yes}$ (Entropy($D_{yes}$)) and $D_{no}$ (Entropy($D_{no}$)), with Entropy($D$) labeling the root.]

**Information Gain** (feature, value) $=$

$$\text{Entropy}(D) - \left[\gamma\,\text{Entropy}(D_{yes}) + (1-\gamma)\text{Entropy}(D_{no})\right]$$

$\gamma \rightarrow$ fraction of data points that went on $D_{yes}$

$$= \frac{|D_{yes}|}{|D|}$$
