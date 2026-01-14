---
Prerequisites:
- [[Subsets]]
---
## Introduction
Interesting mathematical problems often involve a large (or infinite) collection of sets. Labeling each set with a subscript is often convenient in such situations.
For example, suppose we define a collection of sets $A_i$ for $i\in\{1,2,3,\ldots\} = \mathbb N$ as follows:
$A_1 = \{1,2\}, \qquad A_2 = \{3,4\}, \qquad A_3 = \{5,6\}, \qquad \ldots$
Note the following:
* This collection of $A_i$ 's, which we denote $\big\{ A_i \big\}_{i \in \mathbb N},$ is called a family of indexed sets.
* The set $i=\{1,2,3,\ldots\} = \mathbb N$ is called the index set.
Writing each set with a subscript makes talking about a general $A_i$ easier. In this particular case, for example, we can express a general member of this family in terms of its index:
$A_i = \{2i-1,\, 2i\}, \qquad i\in\mathbb N$
So, if we wanted to write down the elements of $A_{100},$ we substitute $i=100$ into the definition of $A_i{:}$
$A_{100} = \big\{2(100)-1,\, 2(100)\big\} = \{199,200\}$
We can use any index set when defining a family of indexed sets.
For example, consider the indexed family $\big\{ B_x \big\}_{x \in \mathbb R},$ where $B_x$ is the real interval defined by
$B_x = \big[ 0, x^2 \big), \qquad x \in \mathbb{R}.$
Here, the index set is $\mathbb{R}.$
To write down, say, the elements of $B_{\color{blue}\sqrt{5}},$ we substitute $x={\color{blue}\sqrt{5}}$ into our definition of $B_x{:}$
$$\begin{align*} B_{\color{blue}\sqrt{5}} &= \left[ 0, \: ({\color{blue}\sqrt{5}})^2 \right) \\[5pt] &= \left[ 0, 5 \right) \end{align*}$$

---
## Example: Identifying Elements of an Indexed Family
Find $T_2$ given that $T_n = \{ 1, 2, \ldots, 2n+1 \},$ where $n \in \mathbb{N}.$
To write down the elements of $T_2,$ we substitute $n=2$ into the expression and get
$$\begin{align*} T_2 &= \{ 1, 2, \ldots, 2(2)+1 \} \\[5pt] &= \{ 1, 2, \ldots, 5 \} \\[5pt] &= \{ 1, 2, 3, 4, 5 \}. \end{align*}$$

---
## Unions of Indexed  Families
Suppose we have the indexed family $\{A_i\}_{i\in I}$ where $I$ is an index set.
The union of a family of indexed sets is the set containing all elements belonging to at least one set in the indexed family:
$\bigcup_{i \in I} A_i = \big\{ x\in U \: : \: x \in A_i \:\:\textrm{for at least one } A_i,\:\: i \in I \big\}$ where $U$ is a universal set.
For example, suppose we have the following family of indexed sets:
$X_i = \{ -i, \,0, \, i \}, \qquad i\in \mathbb N$
We wish to calculate the following union:
$\bigcup_{i \in \mathbb N} X_i$
To calculate our union, let's write down a few of our indexed sets:
* If $i=1,$ we have $X_1 = \{ -1, 0, 1 \}.$
* If $i=2,$ we have $X_2 = \{ -2, 0, 2 \}.$
* If $i=3,$ we have $X_3 = \{ -3, 0, 3 \}.$
* $\cdots$
and so on.
Now, note the following:
* It's clear that the $X_i$ 's contain only integers. Therefore, any union of $X_i$ 's will contain only integers. So, $\bigcup_{i \in \mathbb N} X_i \subseteq \mathbb Z.$
* Notice that any integer $n$ belongs to our union. For instance, $n \in \mathbb{N}$ lies in $X_n=\{ -n, 0, n \}$ and, consequently, lies in the union of all $X_i$ 's. Therefore, $\bigcup_{i \in \mathbb N} X_i \supseteq \mathbb Z.$
Thus, using the fact that $A\subseteq B$ and $B\subseteq A$ if and only if $A=B,$ we conclude that
$$\begin{align*} \bigcup_{i \in \mathbb N} X_i &= \overbrace{\{ -1, 0, 1 \}}^{X_1} \cup \overbrace{\{ -2, 0, 2 \}}^{X_2} \cup \overbrace{\{ -3, 0, 3 \}}^{X_3} \cup \cdots = \mathbb Z \end{align*}$$
Finally, since our index set $I = \mathbb N$ in this example, we can also use the following notation:
$$\begin{align*} \bigcup_{i =1}^\infty X_i = \mathbb Z \end{align*}$$

---
## Intersections of Indexed  Families
Similarly, the intersection of a family of indexed sets $\{A_i\}_{i\in I}$ contains all elements that belong to all sets in our family:
$\bigcap_{i \in I} A_i = \big\{ x\in U \: : \: x \in A_i \:\:\textrm{for all } A_i,\:\: i \in I \big\}$ where $U$ is a universal set.
For example, suppose we have the following family of indexed sets:
$S_i = \left[ 0, \: 10^{-i} \right], \qquad i \in \mathbb{N}$
We wish to compute the following intersection:
$\bigcap_{i \in \mathbb{N}} S_i$
To calculate our intersection, let's write down a few of our indexed sets:
* If $i=1,$ we have $S_1 = [0, 0.1]$
* If $i=2,$ we have $S_2 = \left[ 0, 0.01 \right]$
* If $i=3,$ we have $S_3 = \left[ 0, 0.001 \right]$
* $\cdots$
and so on.
Now, note the following:
* As $i$ increases, the right endpoint of $S_i$ approaches $0$ but never reaches it.
* The left endpoint equals zero for each $S_i.$
So, the only element that lies in all sets is $0.$ Therefore, the intersection of our indexed family is the set containing zero only:
$$\begin{align*} \bigcap_{i \in \mathbb{N}} S_i = \{0 \}. \end{align*}$$
Finally, since our index set $I = \mathbb N$ in this example, we can also use the following notation:
$$\begin{align*} \bigcap_{i =1}^\infty S_i = \{0 \} \end{align*}$$

---
## Example: Finding Unions and Intersections of Finite Families of Indexed Sets
Find $\,\displaystyle \bigcup_{i \in I} S_i$ , given that $I = \{ -1, 0, 1 \},$ and $S_i = (i-1, \,i+1).$
The union of a family of indexed sets is the set containing all elements belonging to at least one set in the indexed family:
$\bigcup_{i \in I} A_i = \big\{ x\in U \: : \: x \in A_i \:\:\textrm{for at least one } A_i,\:\: i \in I \big\}$ where $U$ is a universal set.
Therefore, in our case, we have
$$\begin{align*} \bigcup_{i \in I} S_i &= S_{-1} \cup S_0 \cup S_1 \\ &= (-2, 0) \: \cup \: (-1, 1) \: \cup \: (0, 2) \\[5pt] &= (-2, 2). \end{align*}$$

---
## Example: Finding Unions and Intersections of (Countably) Infinite Families of Indexed Sets
Find $\,\displaystyle \bigcap_{i \in I} X_i$ given that $I = \mathbb{N}$ and $X_i = \{ i, \, 2i \}.$
The intersection of a family of indexed sets $\{A_i\}_{i\in I}$ contains all elements that belong to all sets in our family:
$\bigcap_{i \in I} A_i = \big\{ x\in U \: : \: x \in A_i \:\:\textrm{for all } A_i,\:\: i \in I \big\}$ where $U$ is a universal set.
Let's now write down a few instances of our indexed sets:
* if $i=1,$ we have $X_1 = \{ 1, 2 \}$
* if $i=2,$ we have $X_2 = \{ 2, 4 \}$
* if $i=3,$ we have $X_3 = \{ 3, 6 \}$
* if $i=4,$ we have $X_4 = \{ 4, 8 \}$
and so on.
Notice that there is no element that belongs to all the sets. Therefore,
$$\begin{align*} \bigcap_{i \in I} X_i = \emptyset. \end{align*}$$

---
