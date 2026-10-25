# Pitfalls of Naïve Bayes Algorithm

- If a word does not appear in the training set then, $\hat{p}_j'=\hat{p}_j^0=0$ (Probability of word being spam or not will be 0)

$$\therefore P(y^{test}=1/x^{test}=[f_1\;f_2\;\dots\;f_d]) \propto \prod_{i=1}^{d}\left((\hat{p}_i')^{f_i}(1-\hat{p}_i')^{(1-f_i)}\right)\hat{p}' \;\; \underline{0} \; \therefore = 0$$

Similarly,
$$P(y^{test}=0/x^{test}=[f_1\;f_2\;\dots\;f_d]) \propto \prod_{i=1}^{d}\left((\hat{p}_i^0)^{f_i}(1-\hat{p}_i^0)^{(1-f_i)}\right)\hat{p}^0 \;\; \underline{0} \; \therefore = 0$$

---

## Solution

- Add two "pseudo" emails with each label with all the words present
$$x_1^{pseudo} = [1\;1\;1\;1\;\dots\;1], \; y^{pseudo}=1$$
$$x_0^{pseudo} = [0\;0\;0\;0\;\dots\;0], \; y^{pseudo}=0$$

This is called **Laplace Smoothing**
