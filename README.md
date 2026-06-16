# Fox's Trapezoidal Conjecture for Four-Strand Turk's Head Knots

[![arXiv](https://img.shields.io/badge/arXiv-2606.15256-b31b1b.svg)](https://arxiv.org/abs/2606.15256)

This repository contains the computer-assisted proofs accompanying the paper **[Fox's Trapezoidal Conjecture for the Four-Strand Turk's Head Knots](https://arxiv.org/abs/2606.15256)**. 

The scripts provided here verify the log-concavity of the core polynomial sequence $D_n(z)$ associated with the Alexander polynomials of the infinite knot family $Th(4, 2n+1)$. By establishing strict log-concavity, these certificates formally complete the proof of Fox's Trapezoidal Conjecture for this family.

## Related Work

This paper utilizes the spectral factorization derived in the prerequisite manuscript **[Spectral Factorization and Hypergeometric Representations of the Alexander Polynomials of Th(4,2n+1)](https://arxiv.org/abs/2606.11301)**. The computational suite for that work is available [here](https://github.com/saurabh-suman2/Th4q-Alexander-Generating-Function).

## Mathematical Context

The Alexander polynomial $A_{2n+1}(z)$ of $Th(4, 2n+1)$ factors into a uniform distribution and a squared core polynomial $D_n(z)$. The log-concavity of $D_n(z)$ is established via two distinct regimes:

1. **The Asymptotic Regime $(n >= 16)$:** Proved via the Four-Block Smoothing Lemma, which guarantees that the discrete convolution of any four complementary trigonometric pair-blocks is log-concave.
2. **The Finite Regime $(1 <= n <= 15)$:** Proved via direct algebraic expansion using the linear recurrence of $D_n(z)$.

Because the continuous semialgebraic parameter space is bounded, the asymptotic bounds are verified using a rational transformation to the positive orthant.

## Files in this Repository

### 1. `verify_four_block_smoothing.py`
This script provides the symbolic positivity certificate for the Generalized Four-Block Smoothing Lemma.
* **Method:** Utilizes the rational transformation $x = 4u / (1+u)$ to map the bounded parameter hypercube $[0,4]^8$ to the positive orthant $[0, \infty)^8.$ 
* **Rigor:** Computes the exact multivariable polynomials for the partial derivatives of the log-concavity discriminants $L_k$ and evaluates their coefficients over $Z[u_1, ..., u_m, v_1, ..., v_m]$. By proving all monomial coefficients are strictly positive integers, it provides an exact integer certificate that the discriminants are coordinatewise strictly increasing, isolating the global minimum at the origin.
* **Dependencies:** `sympy`
* **Execution Time:** ~3-4 minutes on a standard commercial machine.

### 2. `finite_checks.py`
This script serves as the finite-case Wronskian verifier for the core polynomial $D_n(z)$.
* **Method:** Generates the polynomials for $1 <= n <= 15$ utilizing the established initial conditions and the recurrence relation $D_n(z) = (1+z)^2 D_{n-1}(z) - z^2 D_{n-2}(z).$ It then directly evaluates the log-concavity condition $c_k^2 - c_{k-1}c_{k+1} > 0$ for all internal coefficients.
* **Dependencies:** `sympy`
* **Execution Time:** < 1 second.

## Requirements and Usage

Execution of these verification scripts requires Python 3 and the `sympy` library for symbolic mathematics.

## Citation

If you utilize this code or the associated mathematical framework in your work, please cite the preprint:

```bibtex
@article{saurabh2026fox,
  title={Fox's Trapezoidal Conjecture for the Four-Strand Turk's Head Knots},
  author={Saurabh, Suman},
  journal={arXiv preprint arXiv:2606.15256},
  year={2026}
}
