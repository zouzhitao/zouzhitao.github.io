---
title: "个人凸优化见到那学习笔记"
date: 2019-01-23T23:49:12+08:00
draft: false
TableOfContents: true
tags: ["optimization","convex"]
categories : ["math"]
---


>本文来源于个人的凸优化学习笔记参考cs229 cvxoptnote,写成笔记的原因仅仅是想通过个人的笔记自己讲述与推导一下这些数学公式，内容可能会很简单，强力建议想得到一手资料的人好好学习文末参考资料

# 凸集合

定义就直接跳过了，这里简单写一些常见的凸集

- **凸集的交**, 设 $C_i,i = 1,2,3,...,n$ 是凸集，那么我们有$\cap _{i=0}^n C_i$ 也是凸集
- **affine subspace** 即 $Ax+b=0,x \in R^n$, 这既是 convex,也是concave
- **凸函数的sublevel** 即 $if \ f(x)\  is\  convex\ function,then \\{f(x) <=\alpha\\} is\ convex\ set$

# 凸函数

**Define**

![convex](/img/math/convex.png)

**性质**，两条重点

1. **first-order-approximation**<br>
   $$
   f(y)\ge f(x)+(\nabla f(x))^T(y-x)
   $$
2. **二阶导数大于0**<br>
   $$
   \nabla_x^2 f(x) \ge 0
   $$

**一些简单的凸函数**

1. **Affine funciton**<br>
   $f(x) =A^Tx+b,x\in R^n$
2. **quadratic function**<br>
   $f:R^n->R,f(x) = 2^{-1}x^TAx+b^Tx+c,A\in S^n,b\in R^n,c\in R$<br>
   这里简单说一下 $\nabla^2 f(x)=A$, 因此如果 $A$ 是半正定(positive-semidefinite)的,那么$f(x)$ is **convex**
3. **Norm**,e.g $f(x) = ||x||_2^2$
4. **凸函数的非负权重和**<br>
   $f(x)=\sum_{i=0}^nc_if_i(x),f_i(x)\in convex\ function\ class$
5. **凸函数集合的最大值函数**<br>
   $f(x) = \max f_i(x),f_i(x)\in convex\ function\ class$<br>
   证明:
   $$
   \begin{aligned}
       f(\theta x + (1-\theta)y)&= \max f_i(\theta x + (1-\theta)y)\\\\\\
       &\le \max \theta f_i(x) +(1-\theta)f_i(y)\\\\\\
       &\le \theta f(x) + (1-\theta)f(y)
   \end{aligned}
   $$

# 凸优化问题


**define**

![](/img/math/convex-opt.png)

## 凸优化问题的局部最优解一定是全局最优解

接下来是凸优化问题最重要，也是最有趣的一个性质

**证明**

我们用反证法，
设 $x\in R^n,f(x) \in convex\ function\ class$,且， $x$ 是 凸优化问题 $f(x)$ 的一个局部最优解，那么我们有，**在$x$ 的邻域中,i.e.$||x-z||_2 <R$ ,不存在一个点 $z$,使得$f(z)<f(x)$**, 同时，假设 $x$ 不是全局最优解，那么我们有,在定义域中，存在一点 $y,s.t.\ f(y)<f(x)$

设 $z=\theta y + (1-\theta)x,\theta=\frac{R}{2||x-y||_2}$,可以证明$||x-z||_2=2^{-1}R<R$

同时,

$$
\begin{aligned}
f(z)&=f(\theta y + (1-\theta)x)\\\\\\
&\le \theta f(y)+(1-\theta)f(x)\\\\\\
&\le f(x)
\end{aligned}
$$

矛盾

## 一些机器学习的example

1. **线性回归**<br>
   $J(\theta) = ||W^T\Phi (X)-Y||_2^2=\sum (w^t\phi(x_i)-y_i)^2$
   因为 $f_i(w)=(w^t\phi(x_i)-y_i)^2$ 是一个复合affine 凸函数(i.e. x^2 是凸函数，而 $w^t\phi(x_i)-y_i$ 是对 $w$ 的affine function)
2. **logistic reg**<br>
   $J(\theta)=-\sum y_i\log g(\theta x_i) + (1-y_i)\log 1- g(\theta x_i)$
3. **SVM**<br>
   SVM 的目标函数是一个 QP(quadratic opt) 问题，$O(n^3)$
   这个问题还引出一些凸问题有趣的性质，比如lagrange duality 和 KKT,我们后面分析

# lagrange & KKT

## lagrange mutiplier

对于上面的凸优化问题来说，我们有它的lagrange function

$$
\begin{aligned}
\mathcal{L}(x,\alpha,\beta)&=f(x)+\sum \alpha_i g_i(x) + \sum \beta_i h_i(x)\\\\\\
&s.t. \alpha_i >=0
\end{aligned}
$$

其中 $x$ 称为 primal variable, $\alpha,\beta$ 是dual variable

**NOTE** 其实可以将 $\alpha,\beta$ 理解成打破原来约束的代价

## primal & dual 原问题与对偶问题

![](/img/math/primal-dual.png)

中间那段 english 不用看，直接看形式就行了

我们下面试图证明这样一个弱对偶性(weak duality)

即 $d^\*=\theta_D(\alpha^\*,\beta^\*)\le p^\*=\theta_P(x^\*)$,反之(**strong duality**) 是说$d^\*=p^\*$

## 原问题的解释

首先我们化简一下$\theta_P(x)$
![](/img/math/thetap.png)

可以证明如下两个性质

1. $\theta_P(x)$ 是一个凸函数<br>
   $f(x)$ 是凸函数，$g(x)$ 是凸函数， $h(x)$ 是affine function $\alpha_i\ge 0$, 所以， $\sum \alpha_i g(x) + \beta_i h(x)$ 也是凸函数,凸函数集合的最大值是凸函数，所以$\theta_P(x)$ 是一个凸函数
2. $\theta_P(x)$ 的简化<br>
   ![](/img/math/thetap-sample.png)
   关于这一点，我们可以从上面化简后的例子得到

## 弱对偶性(weak duality)

$$
\begin{aligned}
\theta_D(\alpha,\beta)&=\min \mathcal{L}(x,\alpha,\beta)\\\\\\
&\le \mathcal{L}(x^\*,\alpha,\beta)\\\\\\
&\le f(x^\*) + \max \\{\sum \alpha_ig(x^\*) + \beta_i h(x^\*)\\}\\\\\\
&=\theta_P (x^\*)\\\\\\
&\le p^\* 
\end{aligned}
$$

即 对偶问题的最优解总是小于等于原问题的最优解

当然**强对偶性**(strong duality) 指的就是 $d^\*=p^\*$ 了

不过这要满足一些条件，参考文献中指出 一个 **Slater's Condition** ，指出如果存在一些可行解，严格满足所有的限制条件，即 $g_i(x)<0$, 不过没有证明，同时指出几乎所有的图问题都满足 strong duility,这其实解释了为什么我们往往可以套用lagrange 乘数法求导解决这种限制性优化问题


接下来还有一个重要的结论，互补松弛(complementary slackness)

## 互补松弛(complementary slackness)

这个定理是说，如果强对偶性满足，那么我们有 $a_i^\*g_i(x^\*)=0,i =1,2,\dots,m$

简单证明一下

$$
\begin{aligned}
p^\*=d^\*=\theta_D(\alpha^\*,\beta^\*)&=\min \mathcal{L}(x,\alpha^\*,\beta^\*)\\\\\\
&\le \mathcal{L}(x^\*,\alpha^\*,\beta^\*)\\\\\\
&=f(x^\*) + \sum \alpha_i^\*g(x^\*) + \beta_i^\* h(x^\*)\\\\\\
&\le f(x^\*)\\\\\\
&= p^\* \\\\\\
\end{aligned}
$$

着意味着 
$$
\begin{aligned}
&\sum \alpha_i^\*g_i(x^\*) + \beta_i^\* h(x^\*)\\\\\\
&=\sum \alpha_i^\*g_i(x^\*)\\\\\\
&=0
\end{aligned}
$$

而我们有 $\alpha_i\ge 0, g_i(x)\le 0,\alpha_i^\* g_i(x^\*)\le 0$, 最终，他们的和等于0，因此 $\alpha_i^\* g_i(x^\*)=0$, 这意味着，

$$
if\ \alpha_i^\* >0,then,g_i(x^\*)=0\\\\\\
or \\\\\\
if\ g_i(x^\*)>0,then,\alpha_i^\* =0 
$$

好，最后是 KKT条件，其实就是前几个性质的总结

# KKT

![](/img/math/KKT.png)

   










# 参考

1. [cvxopt-note1](http://cs229.stanford.edu/section/cs229-cvxopt.pdf)
2. [cvxopt-note2](http://cs229.stanford.edu/section/cs229-cvxopt2.pdf)



>**版权声明**
>
>本作品为作者原创文章，采用[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/) 
>
>**作者:** [taotao](https://zouzhitao.github.io/)
>
>**转载请保留此版权声明，并注明出处**



