# Representation Learning (1)

**Goal:** Given a set of "data points", "understand" something "useful" about them.

**Data Points:** Vectors in $\mathbb{R}^d$.

$$\begin{bmatrix} \text{height} \\ \text{weight} \\ \text{age} \end{bmatrix} \rightarrow \mathbb{R}^3$$

> Running Theme: **"COMPREHENSION is COMPRESSION"** (understanding $\rightarrow$ learning) — George Chaitin

## Problem

Given an input of data points $\{x_1, x_2, \dots, x_n\}$ in $\mathbb{R}^d$ ($d \rightarrow$ no. of features), we want some "compressed" representation of the dataset.

## Example

Input: $\left\{ x_1=\begin{bmatrix}-7\\-14\end{bmatrix}, x_2=\begin{bmatrix}2.5\\5\end{bmatrix}, x_3=\begin{bmatrix}0.5\\1\end{bmatrix}, x_4=\begin{bmatrix}0\\0\end{bmatrix} \right\}$

Question: How many real numbers to store this dataset? The naive answer is 8. Can we do better? Yes.

Explore the relationship in the input. We can use a representative & a coefficient to store the dataset efficiently.

Representative: $\begin{bmatrix}1\\2\end{bmatrix} \in \mathbb{R}^2$   Coefficient: $\{-7, 2.5, 0.5, 0\}$

Now we only need 6 real numbers to store it.

## Note

Using the representative & coefficient, we can "reconstruct"
