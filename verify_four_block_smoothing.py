import sympy as sp

def apply_phi(poly, vars_orig, vars_u):
    degrees = {v: sp.degree(poly, v) for v in vars_orig}
    p = sp.Poly(poly, *vars_orig)
    
    transformed_poly = 0
    for powers, coeff in zip(p.monoms(), p.coeffs()):
        term = coeff
        for i, (v, u) in enumerate(zip(vars_orig, vars_u)):
            k = powers[i]
            d = degrees[v]
            term *= (4*u)**k * (1+u)**(d - k)
        transformed_poly += term
        
    return sp.expand(transformed_poly)

def generate_positivity_certificate():
    print("Initializing algebraic variables:")
    
    sigma = sp.symbols('sigma1:5')
    eta = sp.symbols('eta1:5')
    z = sp.symbols('z')

    # Define the 4 blocks
    Q = [1 + (4 + s)*z + (2 + 4*s + e)*z**2 + (4 + s)*z**3 + z**4 for s, e in zip(sigma, eta)]
    F = sp.expand(Q[0]*Q[1]*Q[2]*Q[3])

    C = [F.coeff(z, k) for k in range(17)]
    C[0] = 1 

    u_sigma = sp.symbols('u_sigma1:5')
    u_eta = sp.symbols('u_eta1:5')
    vars_orig = sigma + eta
    vars_u = u_sigma + u_eta

    print("\nExecuting explicit Lemma 1 transformation (k=2 to 8)...")
    print("-" * 65)
    
    for k in range(2, 9):
        Lk = sp.expand(C[k]**2 - C[k-1]*C[k+1])
        
        d_sigma = sp.diff(Lk, sigma[0])
        d_eta = sp.diff(Lk, eta[0])

        Phi_sigma = apply_phi(d_sigma, vars_orig, vars_u)
        Phi_eta = apply_phi(d_eta, vars_orig, vars_u)
        
        # Extract coefficients
        coeffs_sigma = sp.Poly(Phi_sigma, *vars_u).coeffs()
        coeffs_eta = sp.Poly(Phi_eta, *vars_u).coeffs()
        
        min_sigma = min(coeffs_sigma)
        min_eta = min(coeffs_eta)
        
        print(f"k={k} | Min coeff dL/dsigma: {min_sigma} | Min coeff dL/deta: {min_eta}")
        assert min_sigma > 0 and min_eta > 0, f"Positivity certificate failed at k={k}!"
        
    print("-" * 65)
    print("Certificate complete. All exact coefficients are strictly positive.")


if __name__ == "__main__":
    generate_positivity_certificate()