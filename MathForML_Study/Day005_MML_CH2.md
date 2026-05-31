# Day005 - Ch 02. Linear Algebra

- **Date**: 2026-05-31
- **Textbook**: Mathematics for Machine Learning (MML) - Ch 02. Linear Algebra

## Core Concepts

### 1. Basis Change

A basis change describes how the transformation matrix of a linear mapping $\Phi$ changes when we transition to a new set of basis vectors for the domain and codomain.

* **Transformation Matrix Mapping**: For a linear mapping $\Phi: V \rightarrow W$, if we change the basis of $V$ from $B$ to $\tilde{B}$ and the basis of $W$ from $C$ to $\tilde{C}$, the new transformation matrix $\tilde{\mathbf{A}}_\Phi$ is uniquely determined.
* **General Formula**: The transformation is rigorously formulated using the transition matrices $\mathbf{S}$ (for the domain) and $\mathbf{T}$ (for the codomain) as:

$$
\tilde{\mathbf{A}}_\Phi = \mathbf{T}^{-1} \mathbf{A}_\Phi \mathbf{S}
$$

* **Special Case (Endomorphism)**: If $\Phi: V \rightarrow V$ is an endomorphism and we apply the same basis change ($\mathbf{S} = \mathbf{T} = \mathbf{P}$), the relation simplifies to:

$$
\tilde{\mathbf{A}} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P
}$$

In this case, the matrices $\mathbf{A}$ and $\tilde{\mathbf{A}}$ are explicitly defined as **similar matrices**.

---

### 2. Image and Kernel

The kernel and image are fundamental vector subspaces that completely describe the structural behavior, structural dimensions, and mapping properties of a linear transformation.

* **Kernel (Null Space)**: The kernel of a linear mapping $\Phi: V \rightarrow W$ is the set of all vectors in the domain $V$ that are mapped to the zero vector $\mathbf{0}_W$ in the codomain. It is formally denoted as:

$$
\text{ker}(\Phi) := \{\mathbf{v} \in V : \Phi(\mathbf{v}) = \mathbf{0}_W\}
$$

* **Image (Range)**: The image of $\Phi: V \rightarrow W$ is the set of all vectors in the codomain $W$ that can be mapped from at least one vector in the domain $V$. It is formally denoted as:

$$
\text{Im}(\Phi) := \{\mathbf{w} \in W : \exists \mathbf{v} \in V, \Phi(\mathbf{v}) = \mathbf{w}\}
$$

* **The Rank-Nullity Theorem (The Fundamental Theorem of Linear Mappings)**: For a finite-dimensional vector space $V$, the dimension of the domain is conserved and split between the kernel and the image:

$$
\dim(\text{ker}(\Phi)) + \dim(\text{Im}(\Phi)) = \dim(V)
$$

Here, $\dim(\text{Im}(\Phi))$ is exactly the **rank** of the transformation matrix, and $\dim(\text{ker}(\Phi))$ is the **nullity**.

## AI-Driven Tech Interview Q&A

### Q1. In the context of a linear mapping $\Phi: V \rightarrow W$, how does the 'Kernel' mathematically determine whether a transformation is strictly invertible, and what does a non-trivial kernel imply geometrically?

**Answer**:
According to the textbook, a linear mapping $\Phi$ is strictly invertible if and only if it is an isomorphism, which requires the mapping to be bijective (both injective and surjective). The mathematical structure of the **kernel** directly determines the injectivity of the mapping. For a linear transformation to be injective (one-to-one), the kernel must be trivial, meaning it contains only the zero vector, $\text{ker}(\Phi) = \{\mathbf{0}_V\}$. 

Geometrically, if a mapping has a **non-trivial kernel** (containing non-zero vectors), it implies that an entire subspace of the domain $V$ is being collapsed and flattened into a single zero vector $\mathbf{0}_W$ in the codomain. This mathematical collapse means that distinct, unique input vectors from the domain are projected onto the exact same output location. Consequently, the mapping becomes structural lossy, making it impossible to reconstruct the original input from the output, which completely violates the condition for invertibility.

---

### Q2. When looking at the basis change formula for an endomorphism, $\tilde{\mathbf{A}} = \mathbf{P}^{-1} \mathbf{A} \mathbf{P}$, explain the precise operational sequence of these three matrices from right to left when transforming a coordinate vector.

**Answer**:
The basis change formula for an endomorphism acts as a coordinate transformation bridge that allows us to evaluate the same abstract linear mapping using a new coordinate perspective. When we apply this matrix product to a coordinate vector $\tilde{\mathbf{x}}$ expressed in the **new basis $\tilde{B}$**, the operations execute sequentially from right to left:

First, the rightmost matrix **$\mathbf{P}$** takes the coordinate vector from the new basis $\tilde{B}$ and transforms it back into the coordinate representation of the **old basis $B$**. Second, the central matrix **$\mathbf{A}$** executes the core linear transformation entirely within the framework of the old basis $B$, producing an output vector also represented in $B$. Finally, the leftmost matrix **$\mathbf{P}^{-1}$** takes that output coordinate vector and translates it back into the representation of the new basis $\tilde{B}$. This precise sequence ensures that while the numerical coordinates change at each step, the underlying geometric transformation performed by the system remains completely identical.

## Daily Reflection
It's only been 5 days, but I can already feel myself getting used to the study routine. I'm starting to see the power of consistency. I can't wait to see where I’ll be in 300 days if I keep this up