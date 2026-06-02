# Day007 - Ch 03. Analytic Geometry

- **Date**: 2026-06-02
- **Textbook**: Mathematics for Machine Learning (MML) - Ch 03. Analytic Geometry

## Core Concepts

### 1. Norms
A norm is a function that assigns a strictly positive length or size to each vector in a vector space (except for the zero vector).
* **Definition**: A norm on a vector space $V$ is a function $\|\cdot\|: V \rightarrow \mathbb{R}$ that satisfies the following three axioms for all $x, y \in V$ and $\lambda \in \mathbb{R}$:
  1. **Positive Definiteness**: $\|x\| \geq 0$, and $\|x\| = 0 \iff x = 0$.
  2. **Absolute Homogeneity**: $\|\lambda x\| = |\lambda| \|x\|$.
  3. **Triangle Inequality**: $\|x + y\| \leq \|x\| + \|y\|$.
* **Common Examples**:
  * **$L_{1}$ Norm (Manhattan Norm)**: $\vert\vert x\vert\vert_{1} = \sum_{i=1}^{n} \vert x_{i}\vert$
  * **$L_{2}$ Norm (Euclidean Norm)**: $\vert\vert x\vert\vert_{2} = \sqrt{\sum_{i=1}^{n} x_{i}^{2}} = \sqrt{x^{\top} x}$

---

### 2. Inner Products
An inner product is a formulation that allows the introduction of intuitive geometrical concepts such as the length of a vector or the angle between two vectors.
* **Dot Product**: The standard inner product in $\mathbb{R}^n$, defined as:

  $$\langle x, y \rangle = x^\top y = \sum_{i=1}^n x_i y_i$$

* **General Inner Product**: A function $\langle \cdot, \cdot \rangle: V \times V \rightarrow \mathbb{R}$ is an inner product if it satisfies three properties for all $x, y, z \in V$ and $\lambda, \psi \in \mathbb{R}$:
  1. **Bilinearity**: $\langle \lambda x + \psi y, z \rangle = \lambda \langle x, z \rangle + \psi \langle y, z \rangle$
  2. **Symmetry**: $\langle x, y \rangle = \langle y, x \rangle$
  3. **Positive Definiteness**: $\langle x, x \rangle \geq 0$, and $\langle x, x \rangle = 0 \iff x = 0$
* **Symmetric, Positive Definite Matrices**: A square matrix $\mathbf{A} = \mathbf{A}^\top$ is positive definite if $x^\top \mathbf{A} x > 0$ for all $x \neq 0$. It can be used to define a customized inner product:

  $$\langle x, y \rangle_\mathbf{A} = x^\top \mathbf{A} y$$


---

### 3. Lengths and Distances
With an inner product defined on a vector space, geometric metrics such as length and distance can be naturally induced.
* **Induced Norm (Length)**: The length of a vector $x$ is induced by the inner product as:

  $$\|x\| = \sqrt{\langle x, x \rangle}$$

* **Induced Distance**: The distance between two vectors $x$ and $y$ is defined as the norm of their difference:

  $$d(x, y) = \|x - y\| = \sqrt{\langle x - y, x - y \rangle}$$

  * For the standard dot product, this yields the **Euclidean distance**:

    $$d(x, y) = \sqrt{(x - y)^\top (x - y)} = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$


## AI-Driven Tech Interview Q&A

### Q1. What are the three essential mathematical axioms that a function must satisfy to be defined as a valid 'norm' (length of a vector)?

**Answer**:
To be defined as a valid norm, a function must strictly satisfy three properties: positive definiteness, absolute homogeneity, and the triangle inequality. Positive definiteness ensures that the length of any non-zero vector is strictly positive and equals zero only for the zero vector. Absolute homogeneity dictates that scaling a vector multiplies its length by the absolute value of that scalar. Finally, the triangle inequality states that the length of the sum of two vectors is always less than or equal to the sum of their individual lengths, which geometrically ensures that a straight line remains the shortest distance.

---

### Q2. How can we define a general inner product using a matrix instead of the standard dot product, and what conditions must this matrix meet?

**Answer**:
We can define a generalized inner product by inserting a square matrix $\mathbf{A}$ between two vectors to compute $x^\top \mathbf{A} y$. For this operation to be a mathematically valid inner product that preserves the core geometric properties, the matrix must strictly be a symmetric, positive definite matrix. The symmetry condition ensures that the inner product is commutative, meaning the order of vectors does not matter. The positive definite condition satisfies the axiom of positive definiteness, guaranteeing that the inner product of any non-zero vector with itself is always strictly greater than zero.

## Daily Reflection
I am still struggling a bit with reading and fully understanding the mathematical formulas.