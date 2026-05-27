# Day001 - Ch 02. Linear Algebra

- **Date**: 2026-05-27
- **Textbook**: Mathematics for Machine Learning (MML) - Ch 02. Linear Algebra

## Core Concepts

### 1. Three Concepts of Machine Learning: Data, Model, Learning

- **Data**
  - Machine learning is inherently data driven.
  - Data is represented as vectors.

$$
x \in \mathbb{R}^D
$$

- **Model**
  - A model describes a process for generating data.
  - In regression:

$$
f : \mathbb{R}^D \rightarrow \mathbb{R}
$$

- **Learning**
  - Learning optimizes model parameters using data.

$$
\theta^* = \arg\min_{\theta} L(\theta)
$$

---

### 2. Vector (General Concepts)

> “Vectors are special objects that can be added together and multiplied by scalars to produce another object of the same kind.”

---

### 3. Inverse Matrix and Determinant

#### Inverse Matrix

For

$$
A \in \mathbb{R}^{n \times n}
$$

if

$$
AB = I_n = BA
$$

then

$$
B = A^{-1}
$$

#### Identity Matrix

$$
I_n =
\begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{bmatrix}
$$

#### Determinant of a $2 \times 2$ Matrix

$$
\det(A)=a_{11}a_{22}-a_{12}a_{21}
$$

$$
\det(A)\neq0
\Longleftrightarrow
A^{-1}\text{ exists}
$$

---

### 4. Particular and General Solution (Trivial and Non-trivial)

System of linear equations:

$$
A\mathbf{x}=\mathbf{b}
$$

#### Particular Solution

A specific solution satisfying the system.

$$
\mathbf{x}=
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}
$$

#### General Solution

$$
\left(
\frac{5}{2}-\frac{3}{2}a,
\frac{1}{2}+\frac{1}{2}a,
a
\right),
\quad a\in\mathbb{R}
$$

#### Trivial Solution

$$
\mathbf{x}=\mathbf{0}
$$

#### Non-trivial Solution

$$
\mathbf{x}\neq\mathbf{0}
$$

---

### 5. Augmented Matrix

$$
\begin{aligned}
2x_1+3x_2+5x_3&=1\\
4x_1-2x_2-7x_3&=8\\
9x_1+5x_2-3x_3&=2
\end{aligned}
$$

$$
\left[
\begin{array}{ccc|c}
2 & 3 & 5 & 1 \\
4 & -2 & -7 & 8 \\
9 & 5 & -3 & 2
\end{array}
\right]
$$

---

### 6. Row Echelon Form (REF) and Reduced Row Echelon Form (RREF)

#### REF

Conditions:

1. Nonzero rows are above zero rows.
2. Leading entries move rightward.
3. Entries below pivots are zero.

Example:

$$
\begin{bmatrix}
1 & 2 & 3 \\
0 & 1 & 4 \\
0 & 0 & 5
\end{bmatrix}
$$

#### RREF

Additional conditions:

1. Pivot entries are $1$
2. Pivot columns contain only one nonzero entry

$$
\begin{bmatrix}
1 & 0 & 2 \\
0 & 1 & -1 \\
0 & 0 & 0
\end{bmatrix}
$$

---

### 7. Pivot

A pivot is the leading nonzero entry in a row.

$$
\begin{bmatrix}
\boxed{1} & 2 & 3 \\
0 & \boxed{4} & 5 \\
0 & 0 & \boxed{6}
\end{bmatrix}
$$

#### Role of Pivots

- determine rank
- identify free variables
- solve linear systems
- determine invertibility

## AI-Driven Tech Interview Q&A
### Q1. Why is linear algebra important in machine learning?

- **Answer**: Linear algebra is essential in machine learning because almost all machine learning data and models are represented using vectors and matrices. Input data is expressed as vectors in high-dimensional space, and models transform these vectors through matrix operations. Neural networks, regression models, and optimization algorithms all rely heavily on matrix multiplication, vector operations, and linear transformations. Without linear algebra, it would be impossible to efficiently represent, compute, and optimize machine learning systems.
Q2. Why are pivots important when solving 

### Q2. Why are pivots important when solving linear systems?

- **Answer**: Pivots are important because they reveal the structural properties of a matrix during Gaussian elimination. By examining pivots, we can determine the rank of a matrix, identify free variables, and decide whether a system has a unique solution, infinitely many solutions, or no solution at all. Pivots also determine whether a matrix is invertible.
## Daily Reflection
Although I had already learned these concepts in a university course on linear algebra, I now regret not making a genuine effort to fully understand them at the time. This experience has reminded me that all knowledge eventually becomes part of one’s foundation and growth.
