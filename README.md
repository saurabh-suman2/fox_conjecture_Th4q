# Fox's Trapezoidal Conjecture for Four-Strand Turk's Head Knots

This repository contains the computer-assisted proofs accompanying the paper **"Fox's Trapezoidal Conjecture for the Four-Strand Turk's Head Knots"**. 

The scripts provided here verify the log-concavity of the core polynomial sequence $D_n(z)$ associated with the Alexander polynomials of the infinite knot family $Th(4, 2n+1)$. By establishing strict log-concavity, these certificates formally complete the proof of Fox's Trapezoidal Conjecture for this family.

## Mathematical Context

The Alexander polynomial $A_{2n+1}(z)$ of $Th(4, 2n+1)$ factors into a uniform distribution and a squared core polynomial $D_n(z)$. The log-concavity of $D_n(z)$ is established via two distinct regimes:
1. **The Asymptotic Regime ($n \ge 16$):** Proved via the **Four-Block Smoothing Lemma**, which guarantees that the discrete convolution of any four complementary trigonometric pair-blocks is strictly log-concave.
2. **The Finite Regime ($1 \le n \le 15$):** Proved via direct algebraic expansion using the linear recurrence of $D_n(z)$.

Because the continuous semialgebraic parameter space is bounded, the asymptotic bounds are verified using a rational transformation to the positive orthant.

## Files in this Repository

### 1. `verify_four_block_smoothing.py`
This script provides the symbolic positivity certificate for the Generalized Four-Block Smoothing Lemma.
* **Method:** It utilizes the rational transformation $x = 4u / (1+u)$ to map the bounded parameter hypercube $[0,4]^8$ to the positive orthant $[0, \infty)^8$. 
* **Rigor:** It computes the exact multivariable polynomials for the partial derivatives of the log-concavity discriminants $\Delta_k$ and evaluates their coefficients over $\mathbb{Z}[u_1, \dots, u_m]$. By proving all monomial coefficients are strictly positive integers, it provides an exact integer certificate that the discriminants are coordinatewise strictly increasing, forcing the global minimum to the origin.
* **Dependencies:** `sympy`
* **Execution Time:** ~3-4 minutes on a standard machine.

### 2. `finite_checks.py`
This script acts as the finite-case Wronskian verifier for the core polynomial $D_n(z)$.
* **Method:** It generates the polynomials for $1 \le n \le 15$ utilizing the established initial conditions and the recurrence relation $D_n(z) = (1+z)^2 D_{n-1}(z) - z^2 D_{n-2}(z)$. It then directly checks the strict log-concavity condition $c_k^2 - c_{k-1}c_{k+1} > 0$ for all internal coefficients.
* **Dependencies:** `sympy`
* **Execution Time:** < 1 second.

## Requirements and Usage

To run these verification scripts locally, you must have Python 3 installed along with the `sympy` library for symbolic mathematics.
