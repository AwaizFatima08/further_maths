"""Unit C10: Number theory II: modular arithmetic and Fermat's little theorem.

Edexcel FP2 5.3, 5.4, 5.6 (AS FP2 4.3); OCR A Additional Pure 8.02e, 8.02f (AS), 8.02g, h, l, m, n, o (A level).
Every number is checked in checks_pure/pc10_check.py.
"""

POW7 = [[pow(a, k, 7) for k in range(1, 7)] for a in range(1, 7)]

UNIT = {
    "number": "C10",
    "title": "Number theory II: modular arithmetic and Fermat's little theorem",
    "tag": "Further Pure option · Edexcel FP2 5.3, 5.4, 5.6 (AS FP2 4.3: modular arithmetic only) · OCR A Additional "
           "Pure 8.02e, 8.02f (Y535 and Y545), 8.02g, h, l, m, n, o (Y545 only) · builds on C9",
    "notes": [
        ("p", "Modular arithmetic is arithmetic with remainders: clock times, days of the week and check digits all work "
              "this way. It turns questions about huge numbers (what is the last digit of 3²⁰²⁶?) into short calculations "
              "with small ones. This unit sets out the rules, solves linear and simultaneous congruences, and then "
              "studies powers modulo a prime through Fermat's little theorem. All letters are integers and n ≥ 2."),

        ("h2", "10.1 Congruence modulo n"),
        ("box", "Definition", [
            "a ≡ b (mod n) means n | (a − b). Equivalently a and b leave the same remainder on division by n, or a = b + kn for some integer k.",
            "Each integer is congruent to exactly one of 0, 1, …, n − 1, its <b>least non-negative residue</b>. These n "
            "residue classes form the set ℤₙ = {0, 1, …, n − 1} of integers modulo n.",
        ]),
        ("p", "For example 100 ≡ 2 (mod 7) because 100 − 2 = 98 = 14 × 7, and −23 ≡ 1 (mod 6) because −23 − 1 = −24. "
              "Negative representatives are often handy: 6 ≡ −1 (mod 7), so 6⁵⁰ ≡ (−1)⁵⁰ = 1 (mod 7)."),
        ("box", "Congruence is an equivalence relation (Edexcel 5.3)", [
            "<b>Reflexive:</b> a ≡ a (mod n), because n | 0.",
            "<b>Symmetric:</b> if a ≡ b then b ≡ a (mod n): if a − b = kn then b − a = (−k)n.",
            "<b>Transitive:</b> if a ≡ b and b ≡ c then a ≡ c (mod n): a − b = kn and b − c = ln give a − c = (k + l)n.",
        ]),

        ("h2", "10.2 Arithmetic laws"),
        ("box", "If a ≡ b (mod n) and c ≡ d (mod n), then", [
            "<b>addition and subtraction:</b> a ± c ≡ b ± d (mod n);",
            "<b>multiplication:</b> ac ≡ bd (mod n), since ac − bd = a(c − d) + d(a − b) is a sum of multiples of n; in particular ka ≡ kb;",
            "<b>powers:</b> aᵏ ≡ bᵏ (mod n) for every positive integer k (apply the multiplication law k − 1 times, or use induction).",
        ]),
        ("p", "So you may replace any number by anything congruent to it at any stage of a sum, product or power. To find "
              "a large power, look for a small power that is ≡ 1 or ≡ −1, or square repeatedly. For example 2³ = 8 ≡ 1 (mod 7), so "
              "2⁵⁰ = (2³)¹⁶ × 2² ≡ 1¹⁶ × 4 = 4 (mod 7)."),
        ("p", "<b>Division is different.</b> 2 × 3 ≡ 2 × 8 (mod 10), but 3 ≢ 8 (mod 10). You may cancel a factor c from "
              "ca ≡ cb (mod n) only when hcf(c, n) = 1. In general ca ≡ cb (mod n) gives a ≡ b (mod n/d) where d = hcf(c, n). "
              "Exponents are not reduced mod n either: 2¹⁰ ≢ 2³ (mod 7) although 10 ≡ 3 (mod 7). (Fermat's little theorem "
              "shows what exponents can be reduced by.)"),

        ("h2", "10.3 Linear congruences and multiplicative inverses (Edexcel A level, OCR A)"),
        ("box", "Solving ax ≡ b (mod n)", [
            "Let d = hcf(a, n). There is a solution if and only if d | b.",
            "If d | b there are exactly d solutions modulo n. Divide through by d to get (a/d)x ≡ b/d (mod n/d), which has "
            "one solution x₀ modulo n/d; the solutions mod n are x₀, x₀ + n/d, x₀ + 2n/d, …, x₀ + (d − 1)n/d.",
            "a has a <b>multiplicative inverse</b> a⁻¹ modulo n (a number with aa⁻¹ ≡ 1) if and only if hcf(a, n) = 1. "
            "Find it with Bezout: if ax + ny = 1 then ax ≡ 1, so a⁻¹ ≡ x (mod n). Then ax ≡ b has the single solution x ≡ a⁻¹b.",
        ]),
        ("p", "<b>Why.</b> If ax ≡ b then ax − b = kn, so b = ax − kn is a multiple of d. Conversely, if d | b, Bezout gives "
              "au + nv = d, and x = u(b/d) satisfies ax = b − nv(b/d) ≡ b. For small n you can also find solutions by trying "
              "every residue, or by adding multiples of n to b until the result is divisible by a: 5x ≡ 3 (mod 7) becomes "
              "5x ≡ 10, so x ≡ 2 (allowed because hcf(5, 7) = 1)."),

        ("h2", "10.4 Simultaneous linear congruences (OCR A A level)"),
        ("p", "OCR A sets up to three congruences x ≡ aᵢ (mod nᵢ). The usual method is substitution: write the first as "
              "x = a₁ + n₁k, put it into the second and solve for k, and repeat. The <b>Chinese remainder theorem</b> says "
              "that if the moduli are pairwise coprime there is exactly one solution modulo n₁n₂n₃; you may quote it but need not use it."),
        ("bullets", [
            "Pairwise coprime moduli: always a unique solution modulo the product.",
            "Moduli with a common factor: x ≡ a₁ (mod n₁) and x ≡ a₂ (mod n₂) are consistent only if a₁ ≡ a₂ (mod hcf(n₁, n₂)); "
            "then the solution is unique modulo lcm(n₁, n₂). For example x ≡ 1 (mod 4) and x ≡ 2 (mod 6) is impossible: the first makes x odd, the second even.",
            "Always check the answer in every original congruence.",
        ]),

        ("h2", "10.5 Fermat's little theorem and pseudo-primes (Edexcel A level, OCR A A level)"),
        ("box", "Fermat's little theorem (no proof required)", [
            "If p is prime then aᵖ ≡ a (mod p) for every integer a.",
            "Equivalently, if p is prime and p ∤ a, then a^(p−1) ≡ 1 (mod p).",
            "Consequences: exponents can be reduced modulo p − 1 when p ∤ a; and a⁻¹ ≡ a^(p−2) (mod p).",
        ]),
        ("p", "The two forms are equivalent: multiply a^(p−1) ≡ 1 by a to get the first; for the second, if p ∤ a then a has "
              "an inverse mod p, and multiplying aᵖ ≡ a by a⁻¹ gives a^(p−1) ≡ 1. The table shows the theorem for p = 7: "
              "the column for a⁶ is all 1s. It also shows the order of each element (10.6)."),
        ("table", ["a", "a¹", "a²", "a³", "a⁴", "a⁵", "a⁶", "order of a mod 7"],
         [[str(a)] + [str(v) for v in POW7[a - 1]] + [str(next(k for k in range(1, 7) if POW7[a - 1][k - 1] == 1))]
          for a in range(1, 7)]),
        ("p", "<b>Pseudo-primes.</b> The theorem gives a test for compositeness: if a^(n−1) ≢ 1 (mod n) for some a with "
              "hcf(a, n) = 1, then n is certainly not prime. The converse fails. A composite n with a^(n−1) ≡ 1 (mod n) is "
              "called a <b>pseudo-prime to base a</b>. The smallest pseudo-prime to base 2 is 341 = 11 × 31; 91 = 7 × 13 is a "
              "pseudo-prime to base 3. A number that passes the test for one base may fail for another, so in practice "
              "several bases are tried."),

        ("h2", "10.6 The order of a modulo p (OCR A A level)"),
        ("box", "Order", [
            "If p is prime and p ∤ a, the <b>order</b> of a modulo p is the least positive integer k with aᵏ ≡ 1 (mod p).",
            "The order divides p − 1. More generally aᵐ ≡ 1 (mod p) if and only if the order k divides m.",
            "An element of order p − 1 is a <b>primitive root</b>: its powers give every non-zero residue (3 and 5 mod 7).",
        ]),
        ("p", "Proof that k | m when aᵐ ≡ 1: by the division algorithm m = qk + r with 0 ≤ r < k. Then "
              "1 ≡ aᵐ = (aᵏ)^q × aʳ ≡ aʳ (mod p). Since k is the least positive power giving 1, r cannot be positive, so r = 0 "
              "and k | m. Taking m = p − 1 (Fermat) gives k | p − 1. So to find an order you only test the divisors of p − 1."),

        ("h2", "10.7 Quadratic residues (OCR A A level)"),
        ("p", "a is a <b>quadratic residue</b> modulo p if p ∤ a and x² ≡ a (mod p) has a solution; otherwise (for p ∤ a) a is a "
              "<b>quadratic non-residue</b>. To list the residues, square 1, 2, …, (p − 1)/2: since (p − x)² ≡ x², the other "
              "half repeat them. For an odd prime p there are exactly (p − 1)/2 quadratic residues, and when x² ≡ a has "
              "a solution x₀ the solutions are x ≡ ±x₀."),
        ("table", ["x mod 11", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], [
            ["x² mod 11", "1", "4", "9", "5", "3", "3", "5", "9", "4", "1"],
        ]),
        ("p", "So the quadratic residues mod 11 are 1, 3, 4, 5, 9, and 2, 6, 7, 8, 10 are non-residues: x² ≡ 6 (mod 11) has no "
              "solution. Euler's criterion (an extension, not required) says a is a residue exactly when a^((p−1)/2) ≡ 1 (mod p)."),

        ("h2", "10.8 The ‘freshman's dream’: (a + b)ᵖ ≡ aᵖ + bᵖ (mod p) (OCR A A level)"),
        ("box", "Result and proof", [
            "<b>Lemma.</b> If p is prime and 1 ≤ r ≤ p − 1 then p | ᵖCᵣ.",
            "Proof: p! = ᵖCᵣ × r! × (p − r)!. The prime p divides the left side. Every factor of r! and of (p − r)! is "
            "between 1 and p − 1, so none is divisible by p; by Euclid's lemma (C9) p ∤ r!(p − r)!. Hence, again by "
            "Euclid's lemma, p | ᵖCᵣ.",
            "<b>Theorem.</b> By the binomial theorem (a + b)ᵖ = aᵖ + ᵖC₁aᵖ⁻¹b + … + ᵖCₚ₋₁abᵖ⁻¹ + bᵖ. Every middle "
            "coefficient is divisible by p, so (a + b)ᵖ ≡ aᵖ + bᵖ (mod p).",
        ]),
        ("p", "The result fails for composite exponents: ⁴C₂ = 6 is not divisible by 4, and (1 + 1)⁴ = 16 ≢ 2 (mod 4). "
              "Applying the theorem repeatedly gives (n + 1)ᵖ ≡ nᵖ + 1, which leads to a proof of Fermat's little theorem by "
              "induction (Section B question 4). That proof is a nice exercise but the theorem's proof itself is not examined."),

        ("warn", "Common mistakes", [
            "Reducing an exponent modulo n instead of modulo p − 1, or using Fermat when p is not prime or when p | a.",
            "Cancelling a common factor that is not coprime to the modulus: 6x ≡ 9 (mod 15) is <b>not</b> 2x ≡ 3 (mod 15).",
            "Giving only one solution of ax ≡ b (mod n) when d = hcf(a, n) > 1: there are d solutions mod n.",
            "Writing ‘x = 4’ instead of ‘x ≡ 4 (mod 5)’, or giving a residue outside 0 to n − 1 when the least residue is asked for.",
            "Claiming n is prime because a^(n−1) ≡ 1 (mod n): it may be a pseudo-prime.",
            "Order: testing only k = p − 1. The order is the <b>least</b> k, so test each divisor of p − 1 in increasing order.",
            "Quadratic residues: forgetting the second root −x₀, or including 0 as a residue.",
        ]),
        ("p", "<b>Given or learn.</b> Nothing in this unit is in the formula booklet. Learn the arithmetic laws, the condition "
              "hcf(a, n) | b, Fermat's little theorem in both forms and the definitions of order and quadratic residue."),
    ],

    "examples": [
        {
            "title": "Using the arithmetic laws",
            "question": "(a) Find the remainder when 7¹⁰⁰ is divided by 100. (b) Prove that 13ⁿ − 6ⁿ is divisible by 7 for every "
                        "positive integer n. (c) Find the last digit of 3²⁰²⁶.",
            "steps": [
                "(a) 7² = 49, 7⁴ = 2401 ≡ 1 (mod 100).",
                "So 7¹⁰⁰ = (7⁴)²⁵ ≡ 1²⁵ = 1 (mod 100) by the power law. The remainder is 1 (7¹⁰⁰ ends in 01).",
                "(b) 13 ≡ 6 (mod 7), so by the power law 13ⁿ ≡ 6ⁿ (mod 7), i.e. 7 | 13ⁿ − 6ⁿ.",
                "(c) Last digit means the residue mod 10. 3¹ = 3, 3² = 9, 3³ = 27 ≡ 7, 3⁴ = 81 ≡ 1 (mod 10).",
                "2026 = 4 × 506 + 2, so 3²⁰²⁶ = (3⁴)⁵⁰⁶ × 3² ≡ 1 × 9 = 9. The last digit is 9.",
            ],
        },
        {
            "title": "Linear congruences: existence and the number of solutions",
            "question": "Solve, where possible: (a) 14x ≡ 6 (mod 22) (b) 15x ≡ 7 (mod 25). Give solutions as least residues.",
            "steps": [
                "(a) d = hcf(14, 22) = 2 and 2 | 6, so there are 2 solutions modulo 22.",
                "Divide by 2: 7x ≡ 3 (mod 11). The inverse of 7 mod 11 is 8, since 7 × 8 = 56 = 5 × 11 + 1.",
                "x ≡ 8 × 3 = 24 ≡ 2 (mod 11). Modulo 22 the solutions are x ≡ 2 and x ≡ 13.",
                "Check: 14 × 2 = 28 = 22 + 6 and 14 × 13 = 182 = 8 × 22 + 6.",
                "(b) d = hcf(15, 25) = 5 and 5 ∤ 7, so there is no solution. (Indeed 15x − 7 would have to be a multiple of 25, "
                "so of 5, but 15x is a multiple of 5 and 7 is not.)",
            ],
        },
        {
            "title": "A multiplicative inverse by Bezout",
            "question": "(a) Use Euclid's algorithm to show that 17 has an inverse modulo 60 and find it. (b) Hence solve 17x ≡ 5 (mod 60).",
            "steps": [
                "(a) 60 = 3 × 17 + 9;   17 = 1 × 9 + 8;   9 = 1 × 8 + 1. So hcf(17, 60) = 1 and an inverse exists.",
                "Back substitute: 1 = 9 − 8 = 9 − (17 − 9) = 2 × 9 − 17 = 2(60 − 3 × 17) − 17 = 2 × 60 − 7 × 17.",
                "Reading this modulo 60: −7 × 17 ≡ 1, so 17⁻¹ ≡ −7 ≡ 53 (mod 60). Check: 17 × 53 = 901 = 15 × 60 + 1.",
                "(b) Multiply both sides by 53: x ≡ 53 × 5 = 265 ≡ 25 (mod 60).",
                "Check: 17 × 25 = 425 = 7 × 60 + 5.",
            ],
        },
        {
            "title": "Three simultaneous congruences (OCR A)",
            "question": "Find all integers x with x ≡ 2 (mod 3), x ≡ 3 (mod 5) and x ≡ 2 (mod 7).",
            "steps": [
                "First congruence: x = 3k + 2.",
                "Second: 3k + 2 ≡ 3 (mod 5), so 3k ≡ 1 (mod 5). Since 3 × 2 = 6 ≡ 1, k ≡ 2 (mod 5): k = 5m + 2 and x = 15m + 8.",
                "Third: 15m + 8 ≡ 2 (mod 7). 15 ≡ 1 and 8 ≡ 1, so m + 1 ≡ 2, m ≡ 1 (mod 7): m = 7t + 1.",
                "x = 15(7t + 1) + 8 = 105t + 23, i.e. x ≡ 23 (mod 105).",
                "Check: 23 = 7 × 3 + 2 = 4 × 5 + 3 = 3 × 7 + 2. The moduli are pairwise coprime, so (CRT) this is the only "
                "solution modulo 3 × 5 × 7 = 105.",
            ],
        },
        {
            "title": "Fermat's little theorem and a pseudo-prime",
            "question": "(a) Find 4²⁰ mod 7. (b) Show that 2³⁴⁰ ≡ 1 (mod 341), and explain why this does not show that 341 "
                        "is prime. (c) Show that 3³⁴⁰ ≢ 1 (mod 31), and deduce that 3³⁴⁰ ≢ 1 (mod 341).",
            "steps": [
                "(a) 7 is prime and 7 ∤ 4, so 4⁶ ≡ 1 (mod 7). 20 = 6 × 3 + 2, so 4²⁰ = (4⁶)³ × 4² ≡ 16 ≡ 2 (mod 7).",
                "(b) 2¹⁰ = 1024 = 3 × 341 + 1, so 2¹⁰ ≡ 1 (mod 341) and 2³⁴⁰ = (2¹⁰)³⁴ ≡ 1 (mod 341).",
                "But 341 = 11 × 31 is composite. The converse of Fermat's theorem is false: 341 is a pseudo-prime to base 2.",
                "(c) 31 is prime and 31 ∤ 3, so 3³⁰ ≡ 1 (mod 31). 340 = 30 × 11 + 10, so 3³⁴⁰ ≡ 3¹⁰ (mod 31).",
                "3³ = 27 ≡ −4, so 3⁹ ≡ (−4)³ = −64 ≡ −2 and 3¹⁰ ≡ −6 ≡ 25 (mod 31). So 3³⁴⁰ ≡ 25 ≢ 1 (mod 31).",
                "If 3³⁴⁰ ≡ 1 (mod 341) then 341 | 3³⁴⁰ − 1, so 31 | 3³⁴⁰ − 1, a contradiction. Base 3 shows 341 is composite.",
            ],
        },
        {
            "title": "Orders and quadratic residues modulo 11 (OCR A)",
            "question": "(a) Find the order of 2 and of 3 modulo 11. Is either a primitive root? (b) Find the quadratic residues "
                        "modulo 11, and solve x² ≡ 5 (mod 11). (c) Explain why x² ≡ 6 (mod 11) has no solution.",
            "steps": [
                "(a) The order divides 11 − 1 = 10, so it is 1, 2, 5 or 10. Test these only.",
                "2¹ = 2, 2² = 4, 2⁵ = 32 ≡ 10 (mod 11): none is 1, so the order of 2 is 10. 2 is a primitive root.",
                "3² = 9, 3⁵ = 243 = 22 × 11 + 1 ≡ 1, so the order of 3 is 5. 3 is not a primitive root.",
                "(b) Squares of 1, 2, 3, 4, 5 are 1, 4, 9, 16 ≡ 5, 25 ≡ 3; the squares of 6 to 10 repeat these. "
                "Quadratic residues: 1, 3, 4, 5, 9.",
                "4² = 16 ≡ 5, so x ≡ ±4: x ≡ 4 or x ≡ 7 (mod 11). Check: 7² = 49 = 4 × 11 + 5.",
                "(c) 6 is not in the list 1, 3, 4, 5, 9, so no x has x² ≡ 6 (mod 11).",
            ],
        },
    ],

    "practice": [
        "(a) Find the least non-negative residue of (i) 100 mod 7 (ii) −23 mod 6 (iii) 3¹⁰⁰ mod 4. "
        "(b) Prove that if a ≡ b (mod n) and b ≡ c (mod n) then a ≡ c (mod n).",
        "Find the remainder when 2⁵⁰ is divided by 7, without a calculator.",
        "Find the last digit of 7²⁰²⁵, and prove that 11ⁿ − 4ⁿ is divisible by 7 for every positive integer n.",
        "Solve 5x ≡ 3 (mod 7).",
        "Solve 6x ≡ 9 (mod 15), giving all solutions modulo 15.",
        "(a) Explain why 4x ≡ 3 (mod 6) has no solutions. (b) Solve 4x ≡ 2 (mod 6).",
        "(a) Use Euclid's algorithm to find the inverse of 23 modulo 120. (b) Hence solve 23x ≡ 7 (mod 120).",
        "(OCR A) Find all x with x ≡ 3 (mod 4) and x ≡ 5 (mod 9).",
        "Use Fermat's little theorem to find (a) 3¹⁰⁰ mod 13 (b) 5²⁰²⁴ mod 11. "
        "(c) Prove that n⁵ − n is divisible by 30 for every integer n.",
        "(a) Show that 3⁹⁰ ≡ 1 (mod 7) and 3⁹⁰ ≡ 1 (mod 13). Deduce that 91 is a pseudo-prime to base 3. "
        "(b) By working modulo 13, show that 2⁹⁰ ≢ 1 (mod 91).",
        "(OCR A) (a) List the quadratic residues modulo 13. (b) Is 7 a quadratic residue mod 13? (c) Solve x² ≡ 10 (mod 13).",
        "(OCR A) Find the order of 2 and the order of 3 modulo 13. Which is a primitive root? What orders are possible for "
        "elements modulo 13, and why?",
    ],
    "answers": [
        "(a) (i) 2 (ii) 1 (iii) 3 ≡ −1, so 3¹⁰⁰ ≡ 1. (b) a − b = kn, b − c = ln, so a − c = (k + l)n.",
        "2³ ≡ 1 (mod 7); 2⁵⁰ = (2³)¹⁶ × 2² ≡ 4. Remainder 4.",
        "Powers of 7 mod 10: 7, 9, 3, 1 (period 4); 2025 = 4 × 506 + 1, so last digit 7. 11 ≡ 4 (mod 7) so 11ⁿ ≡ 4ⁿ.",
        "5x ≡ 3 ≡ 10 (mod 7), hcf(5, 7) = 1, so x ≡ 2 (mod 7). (Or 5⁻¹ ≡ 3: x ≡ 9 ≡ 2.)",
        "hcf(6, 15) = 3 and 3 | 9: three solutions. 2x ≡ 3 (mod 5) gives x ≡ 4 (mod 5): x ≡ 4, 9, 14 (mod 15).",
        "(a) hcf(4, 6) = 2 but 2 ∤ 3 (4x is even, 3 + 6k is odd). (b) 2x ≡ 1 (mod 3) so x ≡ 2 (mod 3): x ≡ 2 or 5 (mod 6).",
        "(a) 120 = 5 × 23 + 5; 23 = 4 × 5 + 3; 5 = 1 × 3 + 2; 3 = 1 × 2 + 1. 1 = 3 − 2 = 2 × 3 − 5 = 2 × 23 − 9 × 5 = "
        "47 × 23 − 9 × 120, so 23⁻¹ ≡ 47 (check 23 × 47 = 1081 = 9 × 120 + 1). (b) x ≡ 7 × 47 = 329 ≡ 89 (mod 120).",
        "x = 4k + 3; 4k + 3 ≡ 5 (mod 9), 4k ≡ 2, k ≡ 2 × 7 = 14 ≡ 5 (4⁻¹ ≡ 7 mod 9); x = 4(9m + 5) + 3 = 36m + 23. x ≡ 23 (mod 36).",
        "(a) 3¹² ≡ 1; 100 = 96 + 4; 3⁴ = 81 ≡ 3. Answer 3. (b) 5¹⁰ ≡ 1; 2024 = 2020 + 4; 5⁴ = 625 ≡ 9. Answer 9. "
        "(c) n⁵ ≡ n (mod 5) by Fermat; n³ ≡ n (mod 3) so n⁵ = n³n² ≡ n³ ≡ n; n² ≡ n (mod 2) so n⁵ ≡ n. 2, 3, 5 are distinct "
        "primes each dividing n⁵ − n, so 30 | n⁵ − n.",
        "(a) 3⁶ ≡ 1 (mod 7) and 6 | 90; 3³ = 27 ≡ 1 (mod 13) and 3 | 90. So 7 and 13 divide 3⁹⁰ − 1, hence 91 | 3⁹⁰ − 1, but "
        "91 = 7 × 13 is composite. (b) 2¹² ≡ 1 (mod 13), 90 = 84 + 6, 2⁶ = 64 ≡ 12 ≡ −1 (mod 13), so 2⁹⁰ ≢ 1 (mod 13) and so not mod 91.",
        "(a) 1, 3, 4, 9, 10, 12 (squares of 1 to 6: 1, 4, 9, 3, 12, 10). (b) No. (c) 6² = 36 ≡ 10, so x ≡ 6 or 7 (mod 13).",
        "Possible orders divide 12: 1, 2, 3, 4, 6, 12. 2: 2² = 4, 2³ = 8, 2⁴ ≡ 3, 2⁶ ≡ 12, so order 12 (primitive root). "
        "3: 3³ = 27 ≡ 1, so order 3.",
    ],

    "exam": [
        "(Edexcel) (a) Use Euclid's algorithm to show that hcf(97, 35) = 1. [2]\n"
        "(b) Hence find the multiplicative inverse of 35 modulo 97, giving your answer as a least residue. [3]\n"
        "(c) Solve the congruence 35x ≡ 4 (mod 97). [2]\n"
        "(d) Use Fermat's little theorem to find the remainder when 35²⁰⁰ is divided by 97. [4]",
        "(OCR A) A collector has between 100 and 400 coins. When she puts them in piles of 5 there are 2 left over, in "
        "piles of 6 there are 3 left over and in piles of 7 there are 4 left over.\n"
        "(a) Find the number of coins. [5]\n"
        "(b) Explain why no integer satisfies both x ≡ 1 (mod 4) and x ≡ 2 (mod 6). [2]\n"
        "(c) Solve 12x ≡ 18 (mod 30), giving all solutions modulo 30. [4]",
        "(OCR A) (a) State Fermat's little theorem in both of its forms. [2]\n"
        "(b) Show that 2¹¹ ≡ 1 (mod 23). Hence find the order of 2 modulo 23, justifying your answer. [4]\n"
        "(c) Verify that x = 5 satisfies x² ≡ 2 (mod 23) and find the other solution with 0 ≤ x ≤ 22. [2]\n"
        "(d) Given that 2047 = 23 × 89, show that 2047 is a pseudo-prime to base 2. [3]",
        "(OCR A) Let p be a prime.\n"
        "(a) Prove that p divides ᵖCᵣ for 1 ≤ r ≤ p − 1. [3]\n"
        "(b) Deduce that (a + b)ᵖ ≡ aᵖ + bᵖ (mod p) for all integers a and b. [2]\n"
        "(c) Use (b) and induction to prove that nᵖ ≡ n (mod p) for every non-negative integer n. [4]\n"
        "(d) Find the quadratic residues modulo 7, and solve x² ≡ 2 (mod 7). [2]",
    ],
    "exam_answers": [
        "(a) 97 = 2 × 35 + 27; 35 = 1 × 27 + 8; 27 = 3 × 8 + 3; 8 = 2 × 3 + 2; 3 = 1 × 2 + 1 M1; last non-zero remainder 1 A1. "
        "(b) 1 = 3 − 2 = 3 − (8 − 2 × 3) = 3 × 3 − 8 = 3(27 − 3 × 8) − 8 = 3 × 27 − 10 × 8 = 3 × 27 − 10(35 − 27) = "
        "13 × 27 − 10 × 35 = 13(97 − 2 × 35) − 10 × 35 = 13 × 97 − 36 × 35 M1 M1; 35⁻¹ ≡ −36 ≡ 61 (mod 97) A1 "
        "(check 35 × 61 = 2135 = 22 × 97 + 1). "
        "(c) x ≡ 4 × 61 = 244 M1 ≡ 50 (mod 97) A1. "
        "(d) 97 prime, 97 ∤ 35, so 35⁹⁶ ≡ 1 M1; 200 = 2 × 96 + 8, so 35²⁰⁰ ≡ 35⁸ M1; 35² = 1225 ≡ 61, 61² = 3721 ≡ 35, so "
        "35⁴ ≡ 35 and 35⁸ ≡ 35² ≡ 61 M1; remainder 61 A1.",
        "(a) x ≡ 2 (mod 5), x ≡ 3 (mod 6), x ≡ 4 (mod 7) B1; each says x ≡ −3 M1; 5, 6, 7 pairwise coprime so x ≡ −3 (mod 210) "
        "M1 A1 (or by substitution); x = 207, the only value between 100 and 400 A1 (next values 417, −3). "
        "(b) x ≡ 1 (mod 4) means x is odd; x ≡ 2 (mod 6) means x is even B1; contradiction (2 = hcf(4, 6) ∤ 2 − 1) B1. "
        "(c) hcf(12, 30) = 6 and 6 | 18, so 6 solutions M1; 2x ≡ 3 (mod 5) M1, x ≡ 4 (mod 5) A1; x ≡ 4, 9, 14, 19, 24, 29 (mod 30) A1.",
        "(a) p prime: aᵖ ≡ a (mod p) for all a B1; a^(p−1) ≡ 1 (mod p) if p ∤ a B1. "
        "(b) 2¹¹ = 2048 = 89 × 23 + 1 B1. The order k is the least positive k with 2ᵏ ≡ 1 and k | 22 (Fermat), so k ∈ {1, 2, 11, 22} M1; "
        "2¹ = 2, 2² = 4 ≢ 1 M1; so the order is 11 A1. "
        "(c) 5² = 25 = 23 + 2 B1; the other solution is −5 ≡ 18 B1. "
        "(d) 2¹¹ = 2048 = 2047 + 1 ≡ 1 (mod 2047) M1; 2046 = 11 × 186, so 2²⁰⁴⁶ = (2¹¹)¹⁸⁶ ≡ 1 (mod 2047) A1; 2047 is composite, "
        "so it is a pseudo-prime to base 2 A1.",
        "(a) p! = ᵖCᵣ × r!(p − r)! M1; p | p! but p divides no factor of r!(p − r)!, all of which are less than p, so by Euclid's "
        "lemma p ∤ r!(p − r)! M1; hence p | ᵖCᵣ A1. "
        "(b) Binomial expansion: (a + b)ᵖ = aᵖ + Σᵣ₌₁ᵖ⁻¹ ᵖCᵣaᵖ⁻ʳbʳ + bᵖ M1; each middle term is a multiple of p, so the result A1. "
        "(c) n = 0: 0ᵖ = 0 B1. Assume kᵖ ≡ k (mod p) M1. Then (k + 1)ᵖ ≡ kᵖ + 1ᵖ (by (b)) ≡ k + 1 M1. True for n = 0, and "
        "true for n = k implies true for n = k + 1, so true for all n ≥ 0 by induction A1. "
        "(d) Squares of 1, 2, 3: 1, 4, 2; residues 1, 2, 4 B1; x² ≡ 2: x ≡ 3 or 4 (mod 7) B1.",
    ],
}
