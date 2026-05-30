# Day004 - Ch 02. Linear Algebra

- **Date**: 2026-05-30
- **Textbook**: Mathematics for Machine Learning (MML) - Ch 02. Linear Algebra

## Core Concepts

### 1. Rank

The rank of a matrix is related to the number of linearly independent rows or columns.

* **Definition**: The column rank of a matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ is the maximal number of linearly independent columns. The row rank is the maximal number of linearly independent rows.

---

### 2. Linear Mappings

A mapping between two vector spaces that preserves the algebraic structure (addition and scaling).

For vector spaces $V, W$, a mapping $\Phi: V \rightarrow W$ is **linear** if for all $x, y \in V$ and $\lambda \in \mathbb{R}$:
1. **$\Phi(x + y) = \Phi(x) + \Phi(y)$**
2. **$\Phi(\lambda x) = \lambda \Phi(x)$**

This can be combined into a single condition:

$$
\Phi(\lambda x + \psi y) = \lambda \Phi(x) + \psi \Phi(y)
$$

Special Types of Linear Mappings:
* **Isomorphism**: A bijective linear mapping ($\Phi: V \rightarrow W$). $V$ and $W$ are isomorphic ($\cong$) if and only if $\dim(V) = \dim(W)$.
* **Endomorphism**: A linear mapping where the domain and codomain are the same ($\Phi: V \rightarrow V$).
* **Automorphism**: An endomorphism that is also bijective (an invertible endomorphism).

---

### 3. Matrix Representation of Linear Mapping

Any linear mapping between finite-dimensional vector spaces can be uniquely represented as a matrix multiplication.

Consider bases $B = (b_1, \dots, b_n)$ of $V$ and $C = (c_1, \dots, c_m)$ of $W$. 
* The coordinate vector of $x \in V$ with respect to $B$ is $\alpha$.
* The coordinate vector of $y = \Phi(x) \in W$ with respect to $C$ is $\beta$.

The transformation can be written using a unique transformation matrix $\mathbf{A}_\Phi \in \mathbb{R}^{m \times n}$:

$$
\beta = \mathbf{A}_\Phi \alpha
$$

Where the $j$-th column of $\mathbf{A}_\Phi$ is the coordinate vector of $\Phi(b_j)$ with respect to the basis $C$.

## AI-Driven Tech Interview Q&A

### Q1. From the perspective of dimensionality reduction and data representation, what does the 'rank' of a matrix signify, and what mathematical conditions must a transformation satisfy to prevent information loss during data mapping?

**Answer**:
In a technical context, the **rank** of a matrix represents the number of linearly independent dimensions, which defines the true vector space spanned by the data. If a transformation matrix is **rank deficient**, it implies that some features are redundant (linearly dependent). Consequently, the mapping collapses certain dimensions into zero, leading to an irreversible loss of information. 

To completely prevent information loss during a geometric transformation, the underlying linear mapping must be **bijective** (one-to-one and onto), ensuring that every unique input maps to a unique output. In terms of matrix representation, this requires the transformation matrix to have **full rank**, which guarantees **invertibility**. This full-rank condition ensures that the structural integrity of the high-dimensional data is preserved and can be perfectly reconstructed without any degradation.

---

### Q2. How does an abstract 'linear mapping' mathematically bridge into a concrete 'matrix multiplication' executed by a computer? Explain this connection using the concept of a 'basis'.

**Answer**:
An abstract linear mapping is translated into a concrete **matrix representation** that computers can process through the choice of a specific **basis** for both the domain and codomain. Because any vector in a finite-dimensional space can be uniquely represented as a coordinate vector relative to a chosen basis, we can fully determine a linear mapping simply by tracking how it transforms the input basis vectors.

By passing the input basis vectors through the linear mapping, expressing the resulting outputs as coordinate vectors in the target basis, and stacking them horizontally as columns, we construct a unique **transformation matrix ($\mathbf{A}$)**. This bridge allows us to substitute abstract, conceptual geometric operations with highly optimized, hardware-accelerated **matrix-vector multiplications ($\beta = \mathbf{A}\alpha$)**. This formulation is the fundamental reason why modern machine learning frameworks can efficiently scale complex high-dimensional models on GPUs.



## Daily Reflection

Formatting everything to match the GitHub template using AI tools is taking up way more time than expected due to my current proficiency level. It feels like a bit of a bottleneck. This really makes me want to build some sort of automated pipeline between AI and GitHub whenever I can spare some time.