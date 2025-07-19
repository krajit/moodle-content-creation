<page>

# Example 

### Example 18
If $R_1$ and $R_2$ are equivalence relations in a set $A$, show that $R_1 \cap R_2$ is also an equivalence relation.

<ans> 

**Solution**  

Since $R_1$ and $R_2$ are equivalence relations, $(a, a) \in R_1$ and $(a, a) \in R_2$, $\forall\, a \in A$.  
This implies that $(a, a) \in R_1 \cap R_2$, $\forall\, a$, showing $R_1 \cap R_2$ is reflexive.  
Further, $(a, b) \in R_1 \Rightarrow (a, b) \in R_1$ and $(b, a) \in R_1$, and $(a, b) \in R_2 \Rightarrow (b, a) \in R_2$.  
Hence, $(a, b) \in R_1 \cap R_2 \Rightarrow (b, a) \in R_1 \cap R_2$, so $R_1 \cap R_2$ is symmetric.  
Similarly, $(a, b) \in R_1 \cap R_2$ and $(b, c) \in R_1 \cap R_2 \Rightarrow (a, c) \in R_1$ and $(a, c) \in R_2$.  
This shows that $(a, c) \in R_1 \cap R_2$ is transitive.  
Thus, $R_1 \cap R_2$ is an equivalence relation.

</ans>

</page>

----

<page>

# Example

### Example 19
Let $R$ be a relation on the set $A$ of ordered pairs of positive integers defined by $(x, y) R (u, v)$ if and only if $xv = yu$. Show that $R$ is an equivalence relation.

<ans> 

**Solution**  
Clearly, $(x, y) R (x, y)$, $\forall (x, y) \in A$, since $xy = yx$.  
This shows that $R$ is reflexive.  
Further, $(x, y) R (u, v) \Rightarrow y u = v x$ and hence $(u, v) R (x, y)$.  
This shows that $R$ is symmetric.  
Similarly, $(x, y) R (u, v)$ and $(u, v) R (a, b) \Rightarrow y u = v x$ and $v a = u b \Rightarrow a u = y a$ and hence $(x, y) R (a, b)$.  
Thus, $R$ is transitive.  
Thus, $R$ is an equivalence relation.

</ans>

</page>

----

<page>

# Example

### Example 20
Let $X = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}$.  
Let $R_1$ be a relation in $X$ given by $R_1 = \{(x, y) : x - y$ is divisible by $3\}$ and $R_2$ be another relation on $X$ given by $R_2 = \{(x, y) : \{x, y\} \subset \{1, 4, 7\}$ or $\{x, y\} \subset \{2, 5, 8\}$ or $\{x, y\} \subset \{3, 6, 9\}\}$.  
Show that $R_1 = R_2$.

<ans>

**Solution**  
Note that the characteristic of sets $\{1, 4, 7\}$, $\{2, 5, 8\}$ and $\{3, 6, 9\}$ is that difference between any two elements of these sets is a multiple of 3.  
Therefore, $(x, y) \in R_1 \Rightarrow x - y$ is a multiple of 3 $\Rightarrow \{x, y\} \subset \{1, 4, 7\}$ or $\{x, y\} \subset \{2, 5, 8\}$ or $\{x, y\} \subset \{3, 6, 9\} \Rightarrow (x, y) \in R_2$.  
Hence, $R_1 \subset R_2$.  
Similarly, $(x, y) \in R_2 \Rightarrow x - y$ is divisible by 3 $\Rightarrow (x, y) \in R_1$.  
Thus, $R_2 \subset R_1 \Rightarrow R_1 = R_2$.

</ans>

</page>

----

<page>

# Example

### Example 21
Let $f : X \rightarrow Y$ be a function. Define a relation $R$ in $X$ given by  
$R = \{(a, b) : f(a) = f(b)\}$. Examine whether $R$ is an equivalence relation or not.

<ans>

**Solution**  
For every $a \in X$, $(a, a) \in R$, since $f(a) = f(a)$, showing that $R$ is reflexive.  
Similarly, $(a, b) \in R \Rightarrow f(a) = f(b) \Rightarrow f(b) = f(a) \Rightarrow (b, a) \in R$.  
Therefore, $R$ is symmetric.  
Further, $(a, b) \in R$ and $(b, c) \in R \Rightarrow f(a) = f(b)$ and $f(b) = f(c) \Rightarrow f(a) = f(c) \Rightarrow (a, c) \in R$, which implies that $R$ is transitive.  
Hence, $R$ is an equivalence relation.

</ans>

</page>

----

<page>

# Example

### Example 22
Find the number of all one-one functions from set $A = \{1, 2, 3\}$ to itself.

<ans>

**Solution**  
One-one function from $\{1, 2, 3\}$ to itself is simply a permutation of three symbols $1, 2, 3$.  
Therefore, total number of one-one maps from $\{1, 2, 3\}$ to itself is same as total number of permutations on three symbols $1, 2, 3$ which is $3! = 6$.

</ans>

</page>

----

<page>

# Example

### Example 23
Let $A = \{1, 2, 3\}$. Then show that the number of relations containing $(1, 2)$ and $(2, 3)$ which are reflexive and transitive but not symmetric is three.

<ans>

**Solution**  
The smallest relation $R_1$ containing $(1, 2)$ and $(2, 3)$ which is reflexive and transitive but not symmetric is  
$$
\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)\}.
$$

Now, if we add the pair $(2, 1)$ to $R_1$ to get $R_2$, then the relation will be reflexive, transitive but not symmetric.  
Similarly, we can obtain $R_3$ by adding $(3, 2)$ to $R_1$ to get the desired relation.  
However, we cannot add two pairs $(2, 1), (3, 2)$ or single pair $(3, 1)$ to $R_1$ at a time, as by doing so, we will be forced to add the remaining pair in order to maintain transitivity and in the process, the relation will become symmetric also which is not required.  
Thus, the total number of desired relations is three.

</ans>

</page>

----

<page>

# Example

### Example 24
Show that the number of equivalence relations in the set $\{1, 2, 3\}$ containing $(1, 2)$ and $(2, 1)$ is two.

<ans>

**Solution**  
The smallest equivalence relation $R_1$ containing $(1, 2)$ and $(2, 1)$ is  
$$
\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)\}.
$$

Now we are left with only 4 pairs namely (2, 3), (3, 2), (1, 3) and (3, 1).  
If we add any one, say (2, 3) to $R_1$, then for symmetry we must add (3, 2) also and now for transitivity we are forced to add (1, 3) and (3, 1).  
Thus, the only equivalence relation bigger than $R_1$ is the universal relation.  
This shows that the total number of equivalence relations containing $(1, 2)$ and $(2, 1)$ is two.

</ans>

</page>

----

<page>

# Example 

### Example 25
Consider the identity function $I_{\mathbb{N}} : \mathbb{N} \rightarrow \mathbb{N}$ defined as $I_{\mathbb{N}}(x) = x$, $\forall\, x \in \mathbb{N}$.  
Show that although $I_{\mathbb{N}}$ is onto but $I_{\mathbb{N}} + I_{\mathbb{N}} : \mathbb{N} \rightarrow \mathbb{N}$ defined as
$$
(I_{\mathbb{N}} + I_{\mathbb{N}})(x) = I_{\mathbb{N}}(x) + I_{\mathbb{N}}(x) = x + x = 2x
$$
is not onto.

<ans>

**Solution**  
Clearly $I_{\mathbb{N}}$ is onto.  
But $I_{\mathbb{N}} + I_{\mathbb{N}}$ is not onto, as we can find an element $3$ in the co-domain $\mathbb{N}$ such that there does not exist any $x$ in the domain $\mathbb{N}$ with $(I_{\mathbb{N}} + I_{\mathbb{N}})(x) = 2x = 3$.

</ans>

</page>

---

<page>

# Example 

### Example 26
Consider a function $f : \left[0, \frac{\pi}{2}\right] \rightarrow \mathbb{R}$ given by $f(x) = \sin x$  
and  
$g : \left[0, \frac{\pi}{2}\right] \rightarrow \mathbb{R}$ given by $g(x) = \cos x$.  
Show that $f$ and $g$ are one-one, but $f + g$ is not one-one.


<ans>

**Solution**  
Since for any two distinct elements $x_1$ and $x_2$ in $\left[0, \frac{\pi}{2}\right]$,  
$\sin x_1 \neq \sin x_2$ and $\cos x_1 \neq \cos x_2$, both $f$ and $g$ must be one-one.  
But  
$$
(f + g)(0) = \sin 0 + \cos 0 = 1
$$  
and  
$$
(f + g)\left(\frac{\pi}{2}\right) = \sin\left(\frac{\pi}{2}\right) + \cos\left(\frac{\pi}{2}\right) = 1
$$  
Therefore, $f + g$ is not one-one.

</ans>

</page>