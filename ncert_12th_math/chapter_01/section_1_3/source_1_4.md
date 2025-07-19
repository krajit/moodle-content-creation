<page>

# Composition of Functions

**Definition: Composition**  
Let $f : A \rightarrow B$ and $g : B \rightarrow C$ be two functions. Then the composition of $f$ and $g$, denoted by $gof$, is defined as the function $gof : A \rightarrow C$ given by  
$$
gof(x) = g(f(x)), \quad \forall \, x \in A.
$$

---

**Example**  
Let $f : \{2, 3, 4, 5\} \rightarrow \{3, 4, 5, 9\}$ and $g : \{3, 4, 5, 9\} \rightarrow \{7, 11, 15\}$ be functions defined as $f(2) = 3, f(3) = 4, f(4) = 5, f(5) = 5$ and $g(3) = g(4) = 7, g(5) = g(9) = 11$. Find $gof$.

<ans>

**Solution**  
We have  
$gof(2) = g(f(2)) = g(3) = 7$,  
$gof(3) = g(f(3)) = g(4) = 7$,  
$gof(4) = g(f(4)) = g(5) = 11$,  
$gof(5) = g(f(5)) = g(5) = 11$.

</ans> 

---

**Example**  
Find $gof$ and $fog$, if $f : \mathbb{R} \rightarrow \mathbb{R}$ and $g : \mathbb{R} \rightarrow \mathbb{R}$ are given by $f(x) = \cos x$ and $g(x) = 3x^2$. Show that $gof \ne fog$.


<ans>

**Solution**  
We have  
$gof(x) = g(f(x)) = g(\cos x) = 3(\cos x)^2 = 3 \cos^2 x$.  
Similarly,  
$fog(x) = f(g(x)) = f(3x^2) = \cos(3x^2)$.  

Note that $3 \cos^2 x \ne \cos(3x^2)$ for $x \ne 0$.  
Hence, $gof \ne fog$.

</ans>

</page>

------

<page>

# Invertible Functions

**Definition: Invertible Functions**

A function $f : X \rightarrow Y$ is defined to be **invertible**, if there exists a function $g : Y \rightarrow X$ such that  
$gof = I_X$ and $fog = I_Y$.  
The function $g$ is called the **inverse** of $f$ and is denoted by $f^{-1}$.

Thus, if $f$ is invertible, then $f$ must be one-one and onto and conversely, if $f$ is one-one and onto, then $f$ must be invertible.  
This fact significantly helps for proving a function $f$ to be invertible by showing that $f$ is one-one and onto, especially when the actual inverse of $f$ is not to be determined.

---

**Example**  
Let $f : \mathbb{N} \rightarrow Y$ be a function defined as $f(x) = 4x + 3$, where  
$Y = \{ y \in \mathbb{N} : y = 4x + 3 \text{ for some } x \in \mathbb{N} \}$.  
Show that $f$ is invertible. Find the inverse.

<ans>

**Solution**  
Consider an arbitrary element $y$ of $Y$.  
By the definition of $Y$, $y = 4x + 3$, for some $x$ in the domain $\mathbb{N}$.  
This shows that  
$$
x = \frac{(y - 3)}{4}.
$$

Define $g : Y \rightarrow \mathbb{N}$ by  
$$
g(y) = \frac{(y - 3)}{4}.
$$

Now,  
$$
gof(x) = g(f(x)) = g(4x + 3) = \frac{(4x + 3 - 3)}{4} = \frac{4x}{4} = x
$$

and  
$$
fog(y) = f(g(y)) = f\left( \frac{y - 3}{4} \right) = 4 \left( \frac{y - 3}{4} \right) + 3 = y - 3 + 3 = y.
$$

This shows that $gof = I_{\mathbb{N}}$ and $fog = I_Y$, which implies that $f$ is invertible and $g$ is the inverse of $f$.

</ans>

</page>