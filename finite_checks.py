import sympy as sp

def check_finite_cases(max_n=15):
    """
    Directly verifies the log-concavity of the Alexander polynomial core 
    sequence D_n(z) for finite n using the exact linear recurrence.
    """
    z = sp.symbols('z')
    
    # Initial conditions from Lemma 4.1
    D = [sp.Integer(1), z**2 + 3*z + 1]
    
    print(f"Verifying discrete log-concavity of D_n(z) for 1 <= n <= {max_n}...\n")
    print("-" * 50)
    
    # Generate polynomials via recurrence
    for n in range(2, max_n + 1):
        Dn = sp.expand((z + 1)**2 * D[n-1] - z**2 * D[n-2])
        D.append(Dn)
        
    all_passed = True
    
    for n in range(1, max_n + 1):
        Dn = D[n]
        coeffs = [Dn.coeff(z, k) for k in range(2*n + 1)]
        
        is_lc = True
        failed_indices = []
        
        # Check strict log-concavity: c_k^2 - c_{k-1}*c_{k+1} > 0
        for k in range(1, 2*n):
            margin = coeffs[k]**2 - coeffs[k-1]*coeffs[k+1]
            if margin <= 0:
                is_lc = False
                failed_indices.append(k)
                all_passed = False
        
        status = "PASS" if is_lc else f"FAIL at k={failed_indices}"
        print(f"n = {n:<2} | Degree = {2*n:<2} | Status: {status}")
        
    print("-" * 50)
    if all_passed:
        print("Verification successful: All finite sequences are strictly log-concave.")
    else:
        print("Verification failed.")

if __name__ == "__main__":
    check_finite_cases()