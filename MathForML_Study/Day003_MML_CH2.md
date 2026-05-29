# Day003 - Ch 02. Linear Algebra

- **Date**: 2026-05-29
- **Textbook**: Mathematics for Machine Learning (MML) - Ch 02. Linear Algebra

## Core Concepts

### 1. Vector Subspaces

A vector subspace is a subset of a vector space that is itself a vector space.

$$
U \subseteq V
$$

A subset (U) is a vector subspace if:

* The zero vector is contained in (U).
* (U) is closed under vector addition.
* (U) is closed under scalar multiplication.

Mathematically,

$$
u_1,u_2 \in U
\Rightarrow
u_1+u_2 \in U
$$

and

$$
\lambda u \in U
\quad
(\lambda \in \mathbb{R})
$$

for every 

$$
u \in U
$$

The set of all linear combinations of vectors forms a subspace.

---

### 2. Linear Independence

A set of vectors is linearly independent if no vector can be represented as a linear combination of the others.

Given vectors

$$
x_1,\dots,x_m
$$

they are linearly independent if

$$
\sum_{j=1}^{m}\psi_j x_j = 0
$$

implies

$$
\psi_1=\psi_2=\cdots=\psi_m=0
$$

only.

If there exists a nontrivial solution,

$$
(\psi_j \neq 0)
$$

then the vectors are linearly dependent.

Linearly independent vectors provide non-redundant directions in a vector space.

---

### 3. Generating Set and Basis

A generating set is a collection of vectors whose linear combinations span a vector space.

For vectors

$$
b_1,\dots,b_n
$$

their span is

$$
\text{span}(b_1,\dots,b_n)
$$

which contains all possible linear combinations of the vectors.

A basis is a set of vectors that is:

* linearly independent
* a generating set of the vector space

Therefore,

$$ \text{Basis} = \text{Linear Independence} + \text{Generating Set} $$

A basis provides the minimum set of vectors required to represent every vector in the space uniquely.


## AI-Driven Tech Interview Q&A

### Q1. Why is linear independence important in machine learning?

**Answer**:
Linear independence is important because it prevents redundant representations in data and mathematical models. If vectors are linearly dependent, some vectors can be expressed as linear combinations of others, meaning they do not contribute new information to the representation space. In machine learning, this becomes critical when working with high-dimensional data, since redundant features can increase computational cost while providing little additional value. Concepts such as Principal Component Analysis (PCA), feature selection, embedding representations, and dimensionality reduction all rely on identifying independent directions in vector spaces. Independent basis vectors allow models to represent data more efficiently, reduce redundancy, and improve numerical stability during optimization and learning.

---

### Q2. What is the relationship between vector subspaces, linear independence, generating sets, and bases?

**Answer**:
These concepts are closely connected and together form the foundation of linear algebra used in machine learning. A vector subspace is a subset of a vector space that remains closed under vector addition and scalar multiplication. Inside a subspace, vectors may either be linearly independent or linearly dependent depending on whether some vectors can be reconstructed from others. A generating set is a collection of vectors whose linear combinations can produce every vector in the space, but such a set may still contain redundant vectors. A basis is the minimal and most efficient representation of the space because it combines two essential properties simultaneously: it spans the entire space while remaining linearly independent. In practical machine learning systems, these ideas are fundamental for constructing compact feature spaces, reducing dimensionality, building embeddings, and understanding how information is represented geometrically inside high-dimensional vector spaces.


## Daily Reflection

I feel proud of the process of organizing concepts that were confusing. Even difficult concepts should be continuously pursued with the help of various tools.
