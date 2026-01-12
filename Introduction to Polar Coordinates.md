---
Prerequisites:
- [[The Distance Formula]]
- [[Calculating Reference Angles]]
---
# Introduction
To specify the position of a point $P$ in the Cartesian plane, we normally use its $x$ - and $y$ - coordinates, also called the Cartesian coordinates of $P.$ We then write the position of the point as $P(x,y).$
For example, the point below has coordinates $x=3$ and $y=4,$ so we write it as $P(3,4).$
However, this is not the only way of specifying the position of a point.
We could identify a point by writing down its distance to the origin $(r)$ and the angle that it makes with the positive $x$ -axis $(\theta),$ also called the polar angle, defined such that $0\leq \theta \lt 2\pi .$ The coordinates $r$ and $\theta$ are called polar coordinates.
Let's see how to express a point $P(x,y)$ in polar coordinates $P(r,\theta).$

---
# Converting from Cartesian Coordinates to Polar Coordinates:  First or Fourth Quadrant
To express a point $P(x,y)$ in polar coordinates $P(r,\theta ),$ we use the Cartesian coordinates and some trigonometry.
First, let's find $r,$ which is the distance from $P$ to the origin. Notice that in the diagram above, the distance $r$ is the hypotenuse of a right triangle with sides $x$ and $y.$ So, according to the Pythagorean theorem, we have
$r = \sqrt{x^2 + y^2}.$
Furthermore, the polar angle $\theta$ is an angle in this right triangle. The opposite side has length $y$ and the adjacent side has length $x,$ so we have
$\theta = \arctan\left(\dfrac y x\right).$
For the point $P(3,4),$ for example, we have that the distance from the origin is $$\begin{align} r &= \sqrt{3^2 + 4^2}\\[5pt] &=\sqrt{9+16}\\[5pt] &= 5, \end{align}$$ and the polar angle is $$\begin{align} \theta &= \arctan\left(\dfrac{4}{3}\right) \\[5pt] & \approx 0.927 \end{align}$$ rounded to three decimal places.
Watch out! The polar angle is always expressed in radians.
Therefore, the point $P(3,4)$ can be expressed in polar coordinates as $P(5,0.927).$
Computing the polar angle in this instance was pretty straightforward because $P$ is in the first quadrant. When our point lies in one of the other quadrants, it's usually the safest to compute the reference angle $\theta_R,$ and then compute the polar angle $\theta.$ Let's see an example.

---
# Example: Converting from Cartesian Coordinates to Polar Coordinates:  First or Fourth Quadrant
Express the Cartesian point $P (1,-\sqrt{3})$ in polar coordinates.
The first thing to realize is that the point $P$ lies in the fourth quadrant.
First, we determine $r\mathbin{:}$ $\eqalign{ r &= \sqrt{x^2 + y^2}\[3pt] &= \sqrt{1^2 + (-\sqrt{3})^2}\[3pt] &=\sqrt{1+3}\[3pt] &= 2 }$
We then compute the reference angle $\theta_R\mathbin{:}$
$\eqalign{ \theta_R &= \left|\arctan\left(\dfrac y x\right)\right|\ &= \left|\arctan\left(\dfrac{-\sqrt{3}}{1}\right)\right|\ &= \left|\arctan\left(-\sqrt 3\right)\right|\ &= \left|-\dfrac{\pi}{3}\right|\ &= \dfrac{\pi}{3} }$
Since the point lies in the fourth quadrant, we subtract the reference angle from $2\pi,$ and we get
$$\begin{align*} \theta &= 2\pi - \theta_R\\[5pt] &= 2\pi - \dfrac\pi 3 \\[5pt] &= \dfrac{5\pi}{3}. \end{align*}$$
Therefore, the polar coordinates of $P$ are $\left(2, \dfrac{5\pi}{3}\right).$

---
# Converting from Cartesian Coordinates to Polar Coordinates:  Second or Third Quadrant
As we've already seen, if a point does not lie in the first quadrant, then it's usually safest to compute the reference angle $\theta_R$ first.
To demonstrate, let's express the Cartesian point $P (-5, -5)$ in polar coordinates, shown below.
First, we determine $r\mathbin{:}$ $\eqalign{ r &= \sqrt{x^2 + y^2}\ &= \sqrt{(-5)^2 + (-5)^2}\ &=\sqrt{50}\ &= 5\sqrt{2}. }$
For the reference angle, we get $\eqalign{ \theta_R &= \left|\arctan\left(\dfrac y x\right)\right|\[5pt] &= \left|\arctan\left(\dfrac {-5}{-5}\right)\right|\[5pt] &= \left|\arctan(1)\right|\[5pt] &= \left|\dfrac{\pi}{4}\right|\[5pt] &=\dfrac\pi 4. }$
Since the point lies in the third quadrant, we add the reference angle to $\pi,$ and we get
$$\begin{align} \theta &= \pi + \theta_R\\[5pt] &= \pi +\dfrac{\pi}{4}\\[5pt] &= \dfrac{5\pi}{4}. \end{align}$$
Therefore, the polar coordinates of $P$ are $\left(5\sqrt{2},\dfrac{5\pi}{4}\right).$

---
# Example: Converting from Cartesian Coordinates to Polar Coordinates:  Second or Third Quadrant
Express the Cartesian point $P (-6, 8)$ in polar coordinates. Round your answer to three decimal places where appropriate.
First, we determine $r\mathbin{:}$ $\eqalign{ r &= \sqrt{x^2 + y^2}\[3pt] &= \sqrt{(-6)^2 + 8^2}\[3pt] &=\sqrt{100}\[3pt] &= 10 }$
For the reference angle, we get
$\eqalign{ \theta_R &= \left|\arctan\left(\dfrac y x\right)\right|\[3pt] &= \left|\arctan\left(-\dfrac 8{6}\right)\right|\[3pt] &\approx 0.927\,29 . }$
Since the point $P$ lies in the second quadrant, we subtract the reference angle from $\pi,$ and we get
$$\begin{align} \theta &= \pi - \theta_R\\ &= \pi - 0.927\,29\\ &\approx 2.214\,29\\ &\approx 2.214 \end{align}$$ to three decimal places. Therefore, the polar coordinates of $P$ are $(10,2.214).$

---
# Converting from Cartesian Coordinates to Polar Coordinates for a Point on an Axis
When the point lies on an axis, we can determine the polar angle by inspection, rather than calculating an inverse tangent that might not be defined.
If the point lies on:
* the positive half of $x$ -axis, then the polar angle is $\theta=0.$
* the positive half of $y$ -axis, then the polar angle is $\theta=\dfrac{\pi}{2}.$
* the negative half of $x$ -axis, then the polar angle is $\theta=\pi.$
* the negative half of $y$ -axis, then the polar angle is $\theta=\dfrac{3\pi}{2}.$

---
# Example: Converting from Cartesian Coordinates to Polar Coordinates for a Point on an Axis
Express the Cartesian point $P (0,-7)$ in polar coordinates.
First, we determine $r\mathbin{:}$ $\eqalign{ r &= \sqrt{0^2 + (-7)^2}\ &= \sqrt{7^2}\ &= 7 }$
Since the point $P$ lies on the negative half of the $y$ -axis, we have $\theta=\dfrac{3\pi}{2}.$
Therefore, the polar coordinates of $P$ are $\left(7, \dfrac{3\pi}{2}\right).$

---
