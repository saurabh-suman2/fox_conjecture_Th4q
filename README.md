# Fox's Trapezoidal Conjecture for Four-Strand Turk's Head Knots and Links

[![arXiv](https://img.shields.io/badge/arXiv-2606.15256-b31b1b.svg)](https://arxiv.org/abs/2606.15256)

This repository contains the exact symbolic certificates accompanying the paper
**[Fox's Trapezoidal Conjecture for Four-Strand Turk's Head Knots and Links](https://arxiv.org/abs/2606.15256)**.

The paper proves the strong form of Fox's trapezoidal conjecture for the complete
four-strand Turk's head family

$$
Th(4,q)=\widehat{(\sigma_1\sigma_2^{-1}\sigma_3)^q},
\qquad q\ge 1.
$$

After alternating-sign normalization, the coefficients of the one-variable
Alexander polynomial form a positive log-concave sequence for every exponent
$q$. Thus the result covers both the odd-exponent knots and the even-exponent
links. For $\operatorname{Th}(4,2n+1)$, the coefficients are moreover strictly
unimodal, so their Hirasawa--Murasugi stable length is one.

## Structure of the proof

A uniform reduced-Burau calculation gives

$$
\Delta_{Th(4,q)}(-z)\doteq
(1+z+\cdots+z^{q-1})
\prod_{\substack{\omega^q=1\\ \omega\ne 1}}
\left(z^2+(2-\omega-\omega^{-1})z+1\right).
$$

Pairing reciprocal roots of unity produces reciprocal quartic blocks

$$
P_{a,b}(z)=(1+az+z^2)(1+bz+z^2),
\qquad 0\le a,b\le 4,
\qquad a+b\ge 4.
$$

The individual blocks need not be log-concave; in fact, the extremal block
$P_{0,4}$ and its square and cube all fail log-concavity. The key algebraic
statement is instead that every product of four admissible pair-blocks is
strictly log-concave. This is the **Four-Block Smoothing Theorem**.

The two parity cases arise from the same geometry:

- For $q=2n+1$, complementary parameters satisfy $a+b>4$, giving the odd
  interior case.
- For $q=2n$, complementary parameters satisfy $a+b=4$, and the fixed root
  $\omega=-1$ contributes the extra factor $z^2+4z+1$. This is the even
  boundary case.

## Exact role of the computer certificate

The code does **not** sample exponents, roots of unity, or points in a parameter
space, and it does not numerically test the theorem for many examples.

The proof in the paper first reduces the Four-Block Smoothing Theorem to a fixed
finite certificate. For four generalized quartic blocks, there are seven
independent log-concavity margins $L_k$, with $2\le k\le 8$. Block symmetry
reduces coordinatewise monotonicity to the two derivatives

$$
\frac{\partial L_k}{\partial \sigma_1},
\qquad
\frac{\partial L_k}{\partial \eta_1}.
$$

This gives exactly **fourteen fixed derivative polynomials**. For each one, the
script makes the rational substitution

$$
x=\frac{4u}{1+u},
$$

clears the positive denominators using the exact variablewise degrees, and
expands the resulting polynomial on the positive orthant. It then checks that
every nonzero coefficient is a positive integer. Consequently, the code checks
only fourteen finite coefficient lists; the reduction from all $q$ and all
continuous parameter choices to those lists is proved mathematically in the
paper.

All symbolic arithmetic is exact. No floating-point arithmetic, numerical root
approximation, parameter sampling, or tolerance is used.

## Files

### `verify_four_block_smoothing.py`

Constructs and verifies the exact positivity certificate for the Four-Block
Smoothing Theorem.

- Forms the product of four generalized reciprocal quartics.
- Computes the seven independent margins $L_k$, $2\le k\le 8$.
- Differentiates with respect to $\sigma_1$ and $\eta_1$; block symmetry covers
  the remaining coordinates.
- Applies the positive-orthant transformation and clears denominators exactly.
- Asserts that every nonzero transformed coefficient is a positive integer.

The transformed polynomial has 864 nonzero monomials for each derivative type
when $k=2$, and 2916 for each derivative type when $3\le k\le 8$.

### `finite_checks.py`

Reproduces both exact initial-range tables in the manuscript. For the odd
core, it generates $D_n(z)$ for $1\le n\le 15$ from

$$
D_0(z)=1,
\qquad
D_1(z)=z^2+3z+1,
$$

and

$$
D_n(z)=(1+z)^2D_{n-1}(z)-z^2D_{n-2}(z),
$$

then verifies every internal strict log-concavity margin exactly.

For the even core it starts from

$$
E_1(z)=1,
\qquad
E_2(z)=(1+z)^2,
$$

uses

$$
E_n(z)=(1+z)^2E_{n-1}(z)-z^2E_{n-2}(z),
$$

and checks $1\le n\le 9$. The script asserts strict positivity of every
internal margin and also compares the computed minimum margins with both
tables printed in the paper. The case $E_1(z)=1$ has no internal margin.

## Requirements and usage

- Python 3
- [`sympy`](https://www.sympy.org/)

Install the dependency and run both scripts from the repository root:

```bash
python -m pip install sympy
python verify_four_block_smoothing.py
python finite_checks.py
```

The Four-Block certificate is substantially larger than the recurrence check
and may take several minutes, depending on the machine. A successful run
finishes with all exact assertions satisfied.

## Relation to the spectral-factorization preprint

The odd-exponent specialization of the spectral factorization was first
obtained in
**[Spectral Factorization and Hypergeometric Representations of the Alexander
Polynomials of $Th(4,2n+1)$](https://arxiv.org/abs/2606.11301)**.
The present paper proves the uniform factorization needed for both odd and even
exponents and gives a self-contained proof of every result used here. The
computational material for the preliminary spectral work is available in the
[`Th4q-Alexander-Generating-Function`](https://github.com/saurabh-suman2/Th4q-Alexander-Generating-Function)
repository.

## Citation

If you use this code or the accompanying proof, please cite:

```bibtex
@misc{saurabh2026fox,
  author        = {Saurabh, Suman},
  title         = {Fox's Trapezoidal Conjecture for Four-Strand Turk's Head Knots and Links},
  year          = {2026},
  eprint        = {2606.15256},
  archivePrefix = {arXiv},
  primaryClass  = {math.GT}
}
```
