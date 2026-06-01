# Day006 - Ch 02. Linear Algebra _ END

- **Date**: 2026-06-01
- **Textbook**: Mathematics for Machine Learning (MML) - Ch 02. Linear Algebra

## Core Concepts

### 1. Affine Spaces
An affine space extends the concept of a vector space by separating geometric points from their directional vectors, effectively removing the restriction that the space must contain a fixed origin.
* **Geometric Intuition**: An affine space can be viewed as a vector space where the choice of the origin $(\mathbf{0})$ is forgotten or arbitrary.
* **Points and Vectors**: Elements of an affine space are called points. While points cannot be added together, the difference between any two points $P$ and $Q$ uniquely yields a displacement vector $\mathbf{v} = Q - P$ belonging to an underlying vector space.

---

### 2. Affine Subspaces
An affine subspace represents a linear structure (such as a line or a plane) that has been shifted away from the origin by a fixed translation vector.
* **Mathematical Definition**: Given a vector space $V$, a subspace $U \subseteq V$, and a fixed support vector $\mathbf{x}_0 \in V$, an affine subspace $L$ is defined as:

$$
L = \mathbf{x}_0 + U = \{ \mathbf{x}_0 + \mathbf{u} : \mathbf{u} \in U \}
$$

* **Support and Direction**: The vector $\mathbf{x}_0$ is referred to as the **support vector**, representing a specific point on the affine subspace. The subspace $U$ is called the **direction subspace**, which dictates the orientation of the structure.
* **Dimension**: Since an affine subspace $L$ is not a vector space itself, its dimension is strictly defined as the dimension of its associated direction subspace: $\dim(L) := \dim(U)$.
* **Connection to Linear Systems**: The solution set of a non-homogeneous linear system $\mathbf{A}\mathbf{x} = \mathbf{b}$ forms an affine subspace, where a particular solution serves as the support vector $\mathbf{x}_0$ and the kernel $\text{ker}(\mathbf{A})$ serves as the direction subspace $U$.

---

### 3. Affine Mappings
An affine mapping is a combination of a standard linear mapping and a constant vector translation.
* **Mathematical Definition**: For vector spaces $V$ and $W$, a linear mapping $\Phi: V \rightarrow W$, and a fixed translation vector $\mathbf{b} \in W$, a mapping $\phi: V \rightarrow W$ is an affine mapping if it satisfies:

$$
\phi(\mathbf{x}) = \Phi(\mathbf{x}) + \mathbf{b}
$$

* **Matrix Representation**: Expressed using matrix-vector notation, an affine mapping is codified as:

$$
\phi(\mathbf{x}) = \mathbf{A}\mathbf{x} + \mathbf{b}
$$

* **Violation of Linearity**: If $\mathbf{b} \neq \mathbf{0}$, an affine mapping is strictly **not linear** because it does not preserve the origin: $\phi(\mathbf{0}_V) = \mathbf{A}\mathbf{0}_V + \mathbf{b} = \mathbf{b} \neq \mathbf{0}_W$.
* **Structure Preservation**: Although it violates standard linearity conditions, an affine mapping perfectly preserves **affine combinations**. For any scalars satisfying $\sum_{i=1}^k \lambda_i = 1$, the following property holds:

$$
\phi\left( \sum_{i=1}^k \lambda_i \mathbf{x}_i \right) = \sum_{i=1}^k \lambda_i \phi(\mathbf{x}_i)
$$

## AI-Driven Tech Interview Q&A

### Q1. In machine learning, a fully connected layer is computed as $\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}$. Explain why this operation is classified as an 'affine mapping' rather than a 'linear mapping', and describe the geometric consequence of omitting the bias term $\mathbf{b}$.

**Answer**:
A fully connected layer computed as $\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}$ is strictly an affine mapping because it involves a linear transformation $\mathbf{W}\mathbf{x}$ followed by a constant translation vector $\mathbf{b}$. According to the textbook definitions, a mapping is only truly linear if it satisfies the property $\Phi(\mathbf{0}) = \mathbf{0}$. When a non-zero bias term $\mathbf{b}$ is present, evaluating the layer at an input of zero yields $\mathbf{y} = \mathbf{b}$, which violates the axiom of preserving the origin. 

Geometrically, the linear part $\mathbf{W}\mathbf{x}$ can only rotate, scale, or shear the data space around a fixed origin. The addition of the bias term $\mathbf{b}$ shifts the entire transformed space away from the origin. If we omit this bias term, the transformation is forced to remain a pure linear mapping. This means the decision boundary or regression plane must pass exactly through the origin. Omitting the bias severely restricts the expressivity of the neural network, preventing it from shifting its learned representations freely across the data space to fit patterns that do not naturally center around zero.

---

### Q2. How does the textbook connect the general solution of a non-homogeneous linear system $\mathbf{A}\mathbf{x} = \mathbf{b}$ to the geometric structure of an affine subspace, and how do we determine its dimension?

**Answer**:
The textbook frames the general solution of a non-homogeneous linear equation $`\mathbf{A}\mathbf{x} = \mathbf{b}`$ as a direct physical realization of an affine subspace $`\mathbf{L} = \mathbf{x}_0 + U`$. The solution vector can be decomposed into two distinct components: $`\mathbf{x}_{\text{general}} = \mathbf{x}_0 + \mathbf{x}_{\text{homogeneous}}`$. 

Here, $`\mathbf{x}_0`$ represents a particular solution that satisfies the equation $`\mathbf{A}\mathbf{x}_0 = \mathbf{b}`$, acting precisely as the **support vector** that anchors the space to a specific location. The term $`\mathbf{x}_{\text{homogeneous}}`$ represents the solution space of the corresponding homogeneous system $`\mathbf{A}\mathbf{x} = \mathbf{0}`$, which is the kernel $`\text{ker}(\mathbf{A})`$. This kernel serves as the **direction subspace** $`\mathbf{U}`$, defining the linear directions in which the solutions can extend. Because an affine subspace does not form a vector space on its own, its dimension is defined entirely by its direction subspace. Therefore, the dimension of this solution space is exactly $`\dim(\text{ker}(\mathbf{A}))`$, which is the nullity of the transformation matrix.


## Daily Reflection

As of today, I've officially wrapped up Chapter 2. Since I had already studied this material before, it was relatively easy for me to grasp. Moving on to Chapter 3 brings a mix of nervousness and excitement.
