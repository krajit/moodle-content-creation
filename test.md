# MATRICES

❖ *The essence of Mathematics lies in its freedom.* — **CANTOR** ❖

### 3.1 Introduction

The knowledge of matrices is necessary in various branches of mathematics. Matrices are one of the most powerful tools in mathematics. This mathematical tool simplifies our work to a great extent when compared with other straightforward methods. The evolution of concept of matrices is the result of an attempt to obtain compact and simple methods of solving systems of linear equations. Matrices are not only used as a representation of the coefficients in systems of linear equations, but utility of matrices far exceeds that use. Matrix notation and operations are used in electronic spreadsheet programs for personal computers, which in turn is used in different areas of business and science like budgeting, sales projection, cost estimation, analysing the results of an experiment etc. Also, many physical operations such as magnification, rotation and reflection through a plane can be represented mathematically by matrices. Matrices are also used in cryptography. This mathematical tool is not only used in certain branches of sciences, but also in genetics, economics, sociology, modern psychology and industrial management.

In this chapter, we shall find it interesting to become acquainted with the fundamentals of matrix and matrix algebra.

---

### 3.2 Matrix

Suppose we wish to express the information that Radha has 15 notebooks. We may express it as $[15]$ with the understanding that the number inside $[ \ ]$ is the number of notebooks that Radha has. Now, if we have to express that Radha has 15 notebooks and 6 pens. We may express it as $[15 \ 6]$ with the understanding that the first number inside $[ \ ]$ is the number of notebooks while the other one is the number of pens possessed by Radha. Let us now suppose that we wish to express the information of possession of notebooks and pens by Radha and her two friends Fauzia and Simran which is as follows:

- Radha has 15 notebooks and 6 pens,  
- Fauzia has 10 notebooks and 2 pens,  
- Simran has 13 notebooks and 5 pens.

Now this could be arranged in the tabular form as follows:

|             | Notebooks | Pens |
|-------------|------------|------|
| Radha       | 15         | 6    |
| Fauzia      | 10         | 2    |
| Simran      | 13         | 5    |

and this can be expressed as:

$$
\begin{bmatrix}
15 & 6 \\
10 & 2 \\
13 & 5
\end{bmatrix}
$$

↑ First Column (Notebooks)  
↑ Second Column (Pens)  
→ First Row (Radha)  
→ Second Row (Fauzia)  
→ Third Row (Simran)

or

|             | Radha | Fauzia | Simran |
|-------------|--------|---------|----------|
| Notebooks | 15     | 10       | 13        |
| Pens         | 6       | 2         | 5          |

which can be expressed as:

$$
\begin{bmatrix}
15 & 10 & 13 \\
6 & 2 & 5
\end{bmatrix}
$$

↑ First Column (Radha)  
↑ Second Column (Fauzia)  
↑ Third Column (Simran)  
→ First Row (Notebooks)  
→ Second Row (Pens)

In the first arrangement, the entries in the first column represent the number of notebooks possessed by Radha, Fauzia and Simran, respectively, and the entries in the second column represent the number of pens possessed by Radha, Fauzia and Simran, respectively.

Similarly, in the second arrangement, the entries in the first row represent the number of notebooks possessed by Radha, Fauzia and Simran, respectively. The entries in the second row represent the number of pens possessed by Radha, Fauzia and Simran, respectively.

An arrangement or display of the above kind is called a **matrix**. Formally, we define matrix as:

---

### Definition 1

A **matrix** is an ordered rectangular array of numbers or functions. The numbers or functions are called the **elements** or the **entries** of the matrix.

We denote matrices by capital letters. The following are some examples of matrices:

$$
A = \begin{bmatrix}
-2 & 5 \\
0 & \sqrt{5} \\
3 & 6
\end{bmatrix}, \quad
B = \begin{bmatrix}
2+i & 3 & -1 \\
\frac{1}{2} & 3.5 & -1 \\
\sqrt{3} & 5 & 7
\end{bmatrix}, \quad
C = \begin{bmatrix}
1+x & x^3 & 3 \\
\cos x & \sin x + 2 & \tan x
\end{bmatrix}
$$

In the above examples, the horizontal lines of elements are said to constitute **rows** of the matrix and the vertical lines of elements are said to constitute **columns** of the matrix. Thus A has 3 rows and 2 columns, B has 3 rows and 3 columns while C has 2 rows and 3 columns.

---

![alt text](image.png)

### 3.2.1 Order of a matrix

A matrix having $m$ rows and $n$ columns is called a matrix of **order** $m \times n$ or simply **$m \times n$ matrix** (read as "m by n" matrix). So referring to the above examples of matrices, we have A as $3 \times 2$ matrix, B as $3 \times 3$ matrix and C as $2 \times 3$ matrix. We observe that A has 6 elements, B and C have 9 and 6 elements, respectively.

In general, an $m \times n$ matrix has the following rectangular array:

$$
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} & \cdots & a_{1j} & \cdots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \cdots & a_{2j} & \cdots & a_{2n} \\
\vdots & \vdots & \vdots &        & \vdots &        & \vdots \\
a_{i1} & a_{i2} & a_{i3} & \cdots & a_{ij} & \cdots & a_{in} \\
\vdots & \vdots & \vdots &        & \vdots &        & \vdots \\
a_{m1} & a_{m2} & a_{m3} & \cdots & a_{mj} & \cdots & a_{mn}
\end{bmatrix}_{m \times n}
$$

or  
$A = [a_{ij}]_{m \times n}, \ 1 \leq i \leq m, \ 1 \leq j \leq n, \ i, j \in \mathbb{N}$

Thus, the $i$th row consists of the elements $a_{i1}, a_{i2}, a_{i3}, \ldots, a_{in}$, while the $j$th column consists of the elements $a_{1j}, a_{2j}, a_{3j}, \ldots, a_{mj}$.

In general, $a_{ij}$ is an element lying in the $i$th row and $j$th column. We can also call it as the $(i,j)$th element of $A$. The number of elements in an $m \times n$ matrix will be equal to $mn$.
