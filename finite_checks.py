"""Exact initial-range checks for the odd and even core polynomials.

This script reproduces the two finite tables in the manuscript.  Every
coefficient and every log-concavity margin is computed symbolically over the
integers; no floating-point arithmetic is used.
"""

from __future__ import annotations

import sympy as sp


ODD_MAX_N = 15
EVEN_MAX_N = 9

ODD_EXPECTED_MINIMA = {
    1: 8,
    2: 18,
    3: 32,
    4: 50,
    5: 72,
    6: 98,
    7: 128,
    8: 162,
    9: 200,
    10: 242,
    11: 288,
    12: 338,
    13: 392,
    14: 450,
    15: 512,
}

EVEN_EXPECTED_MINIMA = {
    1: None,
    2: 3,
    3: 9,
    4: 23,
    5: 39,
    6: 59,
    7: 83,
    8: 111,
    9: 143,
}


def odd_cores(z: sp.Symbol, max_n: int = ODD_MAX_N) -> list[sp.Expr]:
    """Return D_0(z), ..., D_max_n(z) from the exact recurrence."""
    cores = [sp.Integer(1), z**2 + 3 * z + 1]
    for n in range(2, max_n + 1):
        cores.append(sp.expand((1 + z) ** 2 * cores[n - 1] - z**2 * cores[n - 2]))
    return cores


def even_cores(z: sp.Symbol, max_n: int = EVEN_MAX_N) -> list[sp.Expr | None]:
    """Return a list indexed by n containing E_1(z), ..., E_max_n(z)."""
    cores: list[sp.Expr | None] = [None, sp.Integer(1)]
    if max_n == 1:
        return cores
    cores.append((1 + z) ** 2)
    for n in range(3, max_n + 1):
        cores.append(sp.expand((1 + z) ** 2 * cores[n - 1] - z**2 * cores[n - 2]))
    return cores


def log_concavity_margins(poly: sp.Expr, z: sp.Symbol) -> list[sp.Integer]:
    """Return c_k^2-c_{k-1}c_{k+1} for every internal coefficient."""
    expanded = sp.Poly(sp.expand(poly), z, domain=sp.ZZ)
    degree = expanded.degree()
    coefficients = [expanded.nth(k) for k in range(degree + 1)]
    return [
        coefficients[k] ** 2 - coefficients[k - 1] * coefficients[k + 1]
        for k in range(1, degree)
    ]


def verify_table(
    family_name: str,
    cores: list[sp.Expr | None],
    expected_minima: dict[int, int | None],
    z: sp.Symbol,
) -> None:
    """Verify strict margins and the published minimum for one family."""
    print(f"{family_name} core")
    print("-" * 42)
    print(f"{'n':>3}  {'degree':>6}  {'minimum margin':>14}  status")
    print("-" * 42)

    for n, expected in expected_minima.items():
        poly = cores[n]
        assert poly is not None
        degree = sp.Poly(poly, z).degree()
        margins = log_concavity_margins(poly, z)

        if not margins:
            actual = None
            assert expected is None
            status = "PASS (no internal margin)"
        else:
            assert all(margin > 0 for margin in margins)
            actual = int(min(margins))
            assert actual == expected
            status = "PASS"

        displayed = "--" if actual is None else str(actual)
        print(f"{n:>3}  {degree:>6}  {displayed:>14}  {status}")

    print()


def main() -> None:
    z = sp.symbols("z")
    verify_table("Odd D_n", odd_cores(z), ODD_EXPECTED_MINIMA, z)
    verify_table("Even E_n", even_cores(z), EVEN_EXPECTED_MINIMA, z)
    print("All exact initial-range checks passed.")


if __name__ == "__main__":
    main()
