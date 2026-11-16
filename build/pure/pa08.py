"""Unit A8: Proof by induction and other methods of proof (Ed CP 1.1, IAL FP1 8.1, AQA A1, OCR 4.01a-b,
MEI Pp4-Pp5 and proof statements, CAIE 1.7)."""

UNIT = {
    "number": "A8",
    "title": "Proof by induction and other methods of proof",
    "tag": "AS (harder induction at A level) · Edexcel CP 1.1 · IAL FP1 8.1 · AQA A1 · OCR A 4.01a (AS), 4.01b (A) · "
           "OCR MEI Pp4 (AS), Pp5 (A), deduction, exhaustion and counter-example (AS), contradiction (A) · "
           "CAIE 9231 P1 1.7",
    "notes": [
        ("p", "A proof is a chain of logical steps showing that a statement must be true. In A level Mathematics you met "
              "proof by deduction, by exhaustion, by counter-example (to disprove) and by contradiction; Further "
              "Mathematics adds <b>proof by mathematical induction</b>, the standard way to prove a statement about every "
              "positive integer n. Induction proofs are set on every board, usually for 5–7 marks, and the marks depend "
              "heavily on setting the proof out properly. This unit shows the layout examiners expect."),

        ("h2", "8.1 The principle of induction"),
        ("p", "Let P(n) be a statement about the integer n, such as “Σ<sub>r=1</sub>ⁿ r = ½n(n + 1)”. Suppose that"),
        ("bullets", [
            "P(1) is true (the <b>basis</b>), and",
            "whenever P(k) is true for some positive integer k, P(k + 1) is also true (the <b>inductive step</b>).",
        ]),
        ("p", "Then P(1) is true, so P(2) is true, so P(3) is true, and so on: P(n) is true for every positive integer n. "
              "Think of an infinite line of dominoes: the first one falls, and each falling domino knocks over the next. "
              "Both parts are essential. Without the basis nothing starts; without the step there is no chain. If the "
              "statement only holds from some n₀ (e.g. n ≥ 4), start the basis at n₀."),
        ("box", "The four parts of an induction proof (mark scheme layout)", [
            "<b>Basis.</b> Show the statement is true for n = 1 (or the first value). Work out <i>both</i> sides separately "
            "and say they are equal: “When n = 1, LHS = …, RHS = …, so the result is true for n = 1.”",
            "<b>Assumption.</b> “Assume the result is true for n = k, for some positive integer k, i.e. …” and write the "
            "statement out with k in place of n.",
            "<b>Inductive step.</b> Using the assumption, show the statement with n = k + 1. Write down the target first, "
            "so you know where you are heading, and show every line of algebra.",
            "<b>Conclusion.</b> “If the result is true for n = k, then it is true for n = k + 1. As it is true for n = 1, "
            "it is true for all positive integers n by mathematical induction.”",
            "Each part carries marks. The conclusion mark is usually lost if any earlier part is missing.",
        ]),

        ("h2", "8.2 Sums of series (all boards)"),
        ("p", "To prove Σ<sub>r=1</sub>ⁿ uᵣ = S(n): in the step, split off the last term, Σ<sub>r=1</sub>ᵏ⁺¹ uᵣ = Σ<sub>r=1</sub>ᵏ uᵣ + uₖ₊₁ "
              "= S(k) + uₖ₊₁, then use algebra to show this equals S(k + 1). Take out common factors rather than "
              "expanding everything."),
        ("p", "<b>Example: Σ<sub>r=1</sub>ⁿ r³ = ¼n²(n + 1)².</b> Basis: n = 1 gives LHS = 1³ = 1 and RHS = ¼ × 1 × 4 = 1. "
              "Assume Σ<sub>r=1</sub>ᵏ r³ = ¼k²(k + 1)² for some positive integer k. Then Σ<sub>r=1</sub>ᵏ⁺¹ r³ = ¼k²(k + 1)² + (k + 1)³ "
              "= ¼(k + 1)²[k² + 4(k + 1)] = ¼(k + 1)²(k + 2)², which is the formula with n = k + 1. Conclusion as in the box."),

        ("h2", "8.3 Divisibility (all boards)"),
        ("p", "To prove f(n) is divisible by m for all n, there are two common methods. Either way you must explain "
              "clearly why f(k + 1) is divisible by m."),
        ("bullets", [
            "<b>Method 1 (write f(k + 1) in terms of f(k)).</b> Assume f(k) = mA for an integer A. Rewrite f(k + 1) so that "
            "f(k) appears, e.g. 3²ᵏ⁺² = 9 × 3²ᵏ = 9(f(k) − 11) for f(k) = 3²ᵏ + 11. Then show f(k + 1) is m times an "
            "integer.",
            "<b>Method 2 (difference).</b> Show that f(k + 1) − c f(k) is divisible by m for a suitable constant c (often the "
            "base of the power). Then f(k + 1) = c f(k) + [f(k + 1) − c f(k)] is a sum of two multiples of m.",
        ]),
        ("p", "<b>Example: 3²ⁿ + 11 is divisible by 4.</b> n = 1: 9 + 11 = 20 = 4 × 5. Assume 3²ᵏ + 11 = 4A. Then "
              "3²ᵏ⁺² + 11 = 9 × 3²ᵏ + 11 = 9(4A − 11) + 11 = 36A − 88 = 4(9A − 22), a multiple of 4."),

        ("h2", "8.4 Powers of matrices (Edexcel, IAL, AQA, OCR A, MEI, CAIE)"),
        ("p", "Where matrix entries are expressions, they are separated by commas, e.g. (2n + 1, −4n; n, 1 − 2n). To prove a formula for Mⁿ, use Mᵏ⁺¹ = Mᵏ M (or M Mᵏ) and multiply out. Show the product matrix entry "
              "by entry and then write it in the target form with n = k + 1."),
        ("p", "<b>Example (Edexcel): M = (3 −4; 1 −1), Mⁿ = (2n + 1, −4n; n, 1 − 2n).</b> n = 1 gives (3 −4; 1 −1) = M. "
              "Assume Mᵏ = (2k + 1, −4k; k, 1 − 2k). Then Mᵏ⁺¹ = Mᵏ M = (3(2k + 1) − 4k, −4(2k + 1) + 4k; 3k + 1 − 2k, "
              "−4k − 1 + 2k) = (2k + 3, −4k − 4; k + 1, −2k − 1) = (2(k + 1) + 1, −4(k + 1); k + 1, 1 − 2(k + 1))."),

        ("h2", "8.5 Sequences defined by recurrence relations (IAL FP1, CAIE, MEI Pp4, OCR A)"),
        ("p", "If uₙ is defined by a recurrence and you must prove a closed form uₙ = g(n): the basis checks g(1) = u₁; the "
              "step assumes uₖ = g(k) and uses the recurrence to show uₖ₊₁ = g(k + 1). For a second-order recurrence "
              "(where uₖ₊₂ depends on uₖ₊₁ and uₖ) you need <b>two</b> basis cases and you assume the result for "
              "n = k and n = k + 1 (see Section B, question A8.15, and Unit C11)."),
        ("p", "<b>Example (IAL): u₁ = 1, uₙ₊₁ = 3uₙ + 4. Prove uₙ = 3ⁿ − 2.</b> u₁ = 3 − 2 = 1 ✓. Assume uₖ = 3ᵏ − 2. "
              "Then uₖ₊₁ = 3(3ᵏ − 2) + 4 = 3ᵏ⁺¹ − 2 ✓."),

        ("h2", "8.6 Harder induction: conjecture, derivatives and inequalities (OCR A 4.01b, MEI Pp5, CAIE)"),
        ("bullets", [
            "<b>Conjecture then prove.</b> Work out the first few cases, spot a pattern, state it as a formula, then prove "
            "it by induction. Typical cases: the nth derivative of x eˣ or x²eˣ; Σ r × r!; the terms of a sequence.",
            "<b>nth derivatives.</b> The step is: differentiate the formula for dᵏy/dxᵏ once more and show you get the "
            "formula with k + 1. Example: dⁿ/dxⁿ(x eˣ) = (x + n)eˣ, since d/dx[(x + k)eˣ] = eˣ + (x + k)eˣ = (x + k + 1)eˣ.",
            "<b>Inequalities.</b> Start from the left side for n = k + 1, use the assumption to replace part of it by "
            "something smaller (or larger), then show that this is at least the right side for n = k + 1. Use the "
            "condition on k (e.g. k ≥ 4) explicitly, and keep “>” or “≥” correct at every step.",
            "<b>De Moivre's theorem</b> is proved by induction in Unit B1 (IAL and CAIE require the proof).",
        ]),

        ("h2", "8.7 Other methods of proof (A level Mathematics; OCR MEI lists them in Further Maths)"),
        ("table", ["Method", "Idea", "Example"], [
            ["Deduction", "Start from known facts and use logical steps to reach the result.",
             "The sum of two odd numbers is even: (2a + 1) + (2b + 1) = 2(a + b + 1)."],
            ["Exhaustion", "Split into a finite number of cases and check every case.",
             "Every square is 3k or 3k + 1: n = 3m, 3m + 1 or 3m + 2 give n² = 3(3m²), 3(3m² + 2m) + 1, 3(3m² + 4m + 1) + 1."],
            ["Counter-example (disproof)", "One example where the statement fails shows it is false.",
             "“n² + n + 41 is always prime” is false: n = 40 gives 1681 = 41²."],
            ["Contradiction (MEI A level)", "Assume the statement is false and deduce something impossible.",
             "√2 is irrational; there are infinitely many primes."],
        ]),
        ("p", "<b>√2 is irrational.</b> Suppose √2 = p/q with p, q integers with no common factor. Then p² = 2q², so p² is "
              "even and hence p is even (if p were odd, p² would be odd). Write p = 2s: 4s² = 2q², so q² = 2s² and q is "
              "even. Then p and q have the common factor 2, a contradiction. So √2 is irrational."),
        ("p", "<b>There are infinitely many primes.</b> Suppose there are only finitely many, p₁, p₂, …, pₘ. Let "
              "N = p₁p₂…pₘ + 1. N leaves remainder 1 when divided by every pᵢ, so no pᵢ divides N. But N > 1 has a prime "
              "factor, which must be a prime not in the list: a contradiction."),
        ("warn", "Common mistakes", [
            "A basis that only works out one side, or just writes “1 = 1”. Show both sides of the statement with n = 1 "
            "substituted, and say the statement is true for n = 1.",
            "Assuming what you have to prove: “Assume true for all n” or “Assume P(n)” gains nothing. Write “Assume true "
            "for n = k, for some positive integer k”. CAIE examiners note that for divisibility you must assume that "
            "f(k) <i>is divisible by m</i>, not that “f(k) is true”.",
            "In divisibility proofs, finding f(k + 1) − f(k) and stopping. Say why that makes f(k + 1) divisible by m.",
            "For matrices: adding instead of multiplying, multiplying in an inconsistent order, or dividing by a scalar "
            "illegally. Mᵏ⁺¹ = Mᵏ M = M Mᵏ.",
            "Writing the conclusion without having completed the step, or omitting it. Use the full sentence.",
            "Using a counter-example to “prove” a general statement, or checking a few cases and calling it a proof "
            "(that is a conjecture, not a proof, unless the cases are exhaustive).",
        ]),
    ],
    "examples": [
        {
            "title": "Induction for the sum of a series",
            "question": "Prove by induction that, for all positive integers n, Σ<sub>r=1</sub>ⁿ r(r + 1) = ⅓n(n + 1)(n + 2).",
            "steps": [
                "<b>Basis.</b> When n = 1: LHS = 1 × 2 = 2; RHS = ⅓ × 1 × 2 × 3 = 2. So the result is true for n = 1.",
                "<b>Assumption.</b> Assume the result is true for n = k, for some positive integer k: "
                "Σ<sub>r=1</sub>ᵏ r(r + 1) = ⅓k(k + 1)(k + 2).",
                "<b>Step.</b> Target: Σ<sub>r=1</sub>ᵏ⁺¹ r(r + 1) = ⅓(k + 1)(k + 2)(k + 3).",
                "Σ<sub>r=1</sub>ᵏ⁺¹ r(r + 1) = Σ<sub>r=1</sub>ᵏ r(r + 1) + (k + 1)(k + 2) = ⅓k(k + 1)(k + 2) + (k + 1)(k + 2)",
                "= ⅓(k + 1)(k + 2)(k + 3), which is the result with n = k + 1.",
                "<b>Conclusion.</b> If the result is true for n = k, it is true for n = k + 1. Since it is true for n = 1, it "
                "is true for all positive integers n by mathematical induction.",
            ],
        },
        {
            "title": "Induction for divisibility (CAIE)",
            "question": "Prove by induction that 3²ⁿ⁺² + 8n − 9 is divisible by 8 for every positive integer n.",
            "steps": [
                "Let f(n) = 3²ⁿ⁺² + 8n − 9.",
                "<b>Basis.</b> f(1) = 3⁴ + 8 − 9 = 80 = 8 × 10, which is divisible by 8. True for n = 1.",
                "<b>Assumption.</b> Assume f(k) is divisible by 8 for some positive integer k, i.e. f(k) = 8A for some "
                "integer A.",
                "<b>Step.</b> f(k + 1) = 3²ᵏ⁺⁴ + 8(k + 1) − 9 = 9 × 3²ᵏ⁺² + 8k − 1.",
                "Consider f(k + 1) − 9f(k) = 9 × 3²ᵏ⁺² + 8k − 1 − 9 × 3²ᵏ⁺² − 72k + 81 = 80 − 64k = 8(10 − 8k).",
                "So f(k + 1) = 9f(k) + 8(10 − 8k) = 8[9A + 10 − 8k], which is divisible by 8.",
                "<b>Conclusion.</b> If f(k) is divisible by 8 then so is f(k + 1). Since f(1) is divisible by 8, f(n) is "
                "divisible by 8 for all positive integers n by mathematical induction.",
            ],
        },
        {
            "title": "Induction for a matrix power (CAIE)",
            "question": "Given M = (4 −1; 6 −1), prove by induction that Mⁿ = (3 × 2ⁿ − 2, 1 − 2ⁿ; 6 × 2ⁿ − 6, "
                        "3 − 2ⁿ⁺¹) for all positive integers n.",
            "steps": [
                "<b>Basis.</b> n = 1: (6 − 2, 1 − 2; 12 − 6, 3 − 4) = (4 −1; 6 −1) = M. True for n = 1.",
                "<b>Assumption.</b> Assume Mᵏ = (3 × 2ᵏ − 2, 1 − 2ᵏ; 6 × 2ᵏ − 6, 3 − 2ᵏ⁺¹) for some positive "
                "integer k.",
                "<b>Step.</b> Mᵏ⁺¹ = Mᵏ M. Top left: 4(3 × 2ᵏ − 2) + 6(1 − 2ᵏ) = 12 × 2ᵏ − 8 + 6 − 6 × 2ᵏ "
                "= 6 × 2ᵏ − 2 = 3 × 2ᵏ⁺¹ − 2.",
                "Top right: −(3 × 2ᵏ − 2) − (1 − 2ᵏ) = −2 × 2ᵏ + 1 = 1 − 2ᵏ⁺¹.",
                "Bottom left: 4(6 × 2ᵏ − 6) + 6(3 − 2ᵏ⁺¹) = 24 × 2ᵏ − 24 + 18 − 12 × 2ᵏ = 12 × 2ᵏ − 6 = 6 × 2ᵏ⁺¹ − 6.",
                "Bottom right: −(6 × 2ᵏ − 6) − (3 − 2ᵏ⁺¹) = −6 × 2ᵏ + 6 − 3 + 2 × 2ᵏ = 3 − 4 × 2ᵏ = 3 − 2ᵏ⁺².",
                "So Mᵏ⁺¹ = (3 × 2ᵏ⁺¹ − 2, 1 − 2ᵏ⁺¹; 6 × 2ᵏ⁺¹ − 6, 3 − 2ᵏ⁺²), the formula with n = k + 1.",
                "<b>Conclusion.</b> True for n = 1, and true for n = k implies true for n = k + 1, so true for all positive "
                "integers n by mathematical induction.",
            ],
        },
        {
            "title": "Induction for a sequence (CAIE)",
            "question": "The sequence u₁, u₂, u₃, … is defined by u₁ = 1 and uₙ₊₁ = 3uₙ − 1. Prove by induction that "
                        "uₙ = ½(1 + 3ⁿ⁻¹) for all positive integers n.",
            "steps": [
                "<b>Basis.</b> n = 1: ½(1 + 3⁰) = ½ × 2 = 1 = u₁. True for n = 1.",
                "<b>Assumption.</b> Assume uₖ = ½(1 + 3ᵏ⁻¹) for some positive integer k.",
                "<b>Step.</b> uₖ₊₁ = 3uₖ − 1 = (3/2)(1 + 3ᵏ⁻¹) − 1 = 3/2 + ½ × 3ᵏ − 1 = ½(1 + 3ᵏ), which is the "
                "formula with n = k + 1 (since 3⁽ᵏ⁺¹⁾⁻¹ = 3ᵏ).",
                "<b>Conclusion.</b> True for n = 1, and if true for n = k then true for n = k + 1; so true for all positive "
                "integers n by mathematical induction.",
            ],
        },
        {
            "title": "Conjecture then prove: an nth derivative (OCR A)",
            "question": "Let y = x²eˣ. (a) Find dy/dx, d²y/dx² and d³y/dx³, and suggest a formula for dⁿy/dxⁿ. "
                        "(b) Prove your formula by induction.",
            "steps": [
                "(a) dy/dx = (x² + 2x)eˣ; d²y/dx² = (x² + 4x + 2)eˣ; d³y/dx³ = (x² + 6x + 6)eˣ.",
                "The coefficient of x goes up by 2 each time and the constants 0, 2, 6 are n(n − 1). Conjecture: "
                "dⁿy/dxⁿ = (x² + 2nx + n(n − 1))eˣ.",
                "(b) <b>Basis.</b> n = 1: (x² + 2x + 0)eˣ = dy/dx. True for n = 1.",
                "<b>Assumption.</b> Assume dᵏy/dxᵏ = (x² + 2kx + k(k − 1))eˣ for some positive integer k.",
                "<b>Step.</b> dᵏ⁺¹y/dxᵏ⁺¹ = d/dx[(x² + 2kx + k² − k)eˣ] = (2x + 2k)eˣ + (x² + 2kx + k² − k)eˣ "
                "= (x² + 2(k + 1)x + k² + k)eˣ = (x² + 2(k + 1)x + (k + 1)k)eˣ, the formula with n = k + 1.",
                "<b>Conclusion.</b> True for n = 1, and true for n = k implies true for n = k + 1; hence true for all "
                "positive integers n by mathematical induction.",
            ],
        },
        {
            "title": "Induction for an inequality (OCR A, MEI)",
            "question": "Prove by induction that n! > 2ⁿ for all integers n ≥ 4.",
            "steps": [
                "<b>Basis.</b> n = 4: 4! = 24 and 2⁴ = 16; 24 > 16, so the result is true for n = 4. (It is false for "
                "n = 1, 2, 3, so the basis must be n = 4.)",
                "<b>Assumption.</b> Assume k! > 2ᵏ for some integer k ≥ 4.",
                "<b>Step.</b> (k + 1)! = (k + 1) × k! > (k + 1) × 2ᵏ (using the assumption, since k + 1 > 0).",
                "Since k ≥ 4, k + 1 > 2, so (k + 1) × 2ᵏ > 2 × 2ᵏ = 2ᵏ⁺¹. Hence (k + 1)! > 2ᵏ⁺¹.",
                "<b>Conclusion.</b> True for n = 4, and true for n = k (k ≥ 4) implies true for n = k + 1; so true for all "
                "integers n ≥ 4 by mathematical induction.",
            ],
        },
    ],
    "practice": [
        "Prove by induction that Σ<sub>r=1</sub>ⁿ (2r − 1) = n² for all positive integers n.",
        "Prove by induction that Σ<sub>r=1</sub>ⁿ 1/(r(r + 1)) = n/(n + 1) for all positive integers n.",
        "Prove by induction that Σ<sub>r=1</sub>ⁿ r × 2ʳ = (n − 1)2ⁿ⁺¹ + 2 for all positive integers n.",
        "Prove by induction that 7ⁿ − 3ⁿ is divisible by 4 for all positive integers n.",
        "Prove by induction that 5ⁿ + 8n + 3 is divisible by 4 for all positive integers n.",
        "Prove by induction that 3²ⁿ + 7 is divisible by 8 for all positive integers n.",
        "Prove by induction that (1 2; 0 3)ⁿ = (1, 3ⁿ − 1; 0, 3ⁿ) for all positive integers n.",
        "Prove by induction that (2 1; −1 0)ⁿ = (n + 1, n; −n, 1 − n) for all positive integers n.",
        "A sequence is defined by u₁ = 1 and uₙ₊₁ = uₙ/(1 + uₙ). Find u₂, u₃ and u₄, conjecture a formula for uₙ, and "
        "prove it by induction.",
        "Prove by induction that dⁿ/dxⁿ (x e²ˣ) = 2ⁿ⁻¹(2x + n)e²ˣ for all positive integers n.",
        "Prove by induction that 2ⁿ > n² for all integers n ≥ 5.",
        "(a) Prove, by deduction, that the sum of any three consecutive integers is divisible by 3.\n"
        "(b) Prove, by exhaustion, that n² − n is even for every integer n.\n"
        "(c) Disprove: “2ⁿ − 1 is prime for every prime n.”\n"
        "(d) Prove by contradiction that √3 is irrational. (You may use: if p² is a multiple of 3, then p is a "
        "multiple of 3.)",
    ],
    "answers": [
        "n = 1: LHS 1, RHS 1. Assume Σ<sub>r=1</sub>ᵏ(2r − 1) = k². Then sum to k + 1 = k² + 2k + 1 = (k + 1)². Conclusion.",
        "n = 1: 1/2 = 1/2. Assume k/(k + 1). Add 1/((k + 1)(k + 2)): [k(k + 2) + 1]/((k + 1)(k + 2)) = (k + 1)²/((k + 1)(k + 2)) "
        "= (k + 1)/(k + 2). Conclusion.",
        "n = 1: LHS 2, RHS 0 + 2 = 2. Assume (k − 1)2ᵏ⁺¹ + 2. Add (k + 1)2ᵏ⁺¹: 2k × 2ᵏ⁺¹ + 2 = k × 2ᵏ⁺² + 2 "
        "= ((k + 1) − 1)2⁽ᵏ⁺¹⁾⁺¹ + 2. Conclusion.",
        "n = 1: 4. Assume 7ᵏ − 3ᵏ = 4A. 7ᵏ⁺¹ − 3ᵏ⁺¹ = 7(7ᵏ − 3ᵏ) + 4 × 3ᵏ = 4(7A + 3ᵏ). Conclusion.",
        "f(1) = 16 = 4 × 4. f(k + 1) − 5f(k) = 8 − 32k − 12 = −4(8k + 1), so f(k + 1) = 5f(k) − 4(8k + 1), a multiple of 4. "
        "Conclusion.",
        "f(1) = 16. Assume 3²ᵏ + 7 = 8A. 3²ᵏ⁺² + 7 = 9(8A − 7) + 7 = 72A − 56 = 8(9A − 7). Conclusion.",
        "n = 1: (1 2; 0 3) ✓. (1, 3ᵏ − 1; 0, 3ᵏ)(1 2; 0 3) = (1, 2 + 3ᵏ⁺¹ − 3; 0, 3ᵏ⁺¹) = (1, 3ᵏ⁺¹ − 1; 0, 3ᵏ⁺¹). "
        "Conclusion.",
        "n = 1: (2 1; −1 0) ✓. (k + 1, k; −k, 1 − k)(2 1; −1 0) = (2k + 2 − k, k + 1; −2k − 1 + k, −k) "
        "= (k + 2, k + 1; −(k + 1), 1 − (k + 1)). Conclusion.",
        "u₂ = ½, u₃ = ⅓, u₄ = ¼; conjecture uₙ = 1/n. n = 1 ✓. Assume uₖ = 1/k: uₖ₊₁ = (1/k)/(1 + 1/k) = 1/(k + 1). "
        "Conclusion.",
        "n = 1: (2x + 1)e²ˣ = e²ˣ + 2x e²ˣ ✓. Differentiate 2ᵏ⁻¹(2x + k)e²ˣ: 2ᵏ⁻¹[2 + 2(2x + k)]e²ˣ "
        "= 2ᵏ(2x + k + 1)e²ˣ. Conclusion.",
        "n = 5: 32 > 25. Assume 2ᵏ > k² (k ≥ 5). 2ᵏ⁺¹ > 2k² = (k + 1)² + (k² − 2k − 1) and k² − 2k − 1 = (k − 1)² − 2 > 0 "
        "for k ≥ 3, so 2ᵏ⁺¹ > (k + 1)². Conclusion (all n ≥ 5).",
        "(a) n + (n + 1) + (n + 2) = 3(n + 1). (b) n even, n = 2m: n² − n = 2(2m² − m); n odd, n = 2m + 1: n² − n "
        "= (2m + 1)(2m) = 2m(2m + 1). Both even. (c) n = 11: 2¹¹ − 1 = 2047 = 23 × 89. (d) Suppose √3 = p/q in lowest terms; "
        "p² = 3q², so 3 | p; p = 3s gives q² = 3s², so 3 | q; common factor 3, contradiction.",
    ],
    "exam": [
        "(a) Prove by induction that, for all positive integers n, Σ<sub>r=1</sub>ⁿ r × r! = (n + 1)! − 1. [5]\n"
        "(b) Prove by induction that 2ⁿ⁺² + 3²ⁿ⁺¹ is divisible by 7 for all positive integers n. [6]",
        "(Edexcel) M = (3 −4; 1 −1).\n"
        "(a) Prove by induction that, for all positive integers n, Mⁿ = (2n + 1, −4n; n, 1 − 2n). [6]\n"
        "(b) Find M⁻¹ and show that the formula in part (a) also holds for n = 0 and n = −1. [3]",
        "A sequence is defined by u₁ = 1, u₂ = 5 and uₙ₊₂ = 5uₙ₊₁ − 6uₙ for n ≥ 1.\n"
        "(a) Prove by induction that uₙ = 3ⁿ − 2ⁿ for all positive integers n. [7]\n"
        "(b) Deduce that uₙ is odd for every positive integer n. [2]",
        "(OCR A) (a) Prove by induction that, for all positive integers n, dⁿ/dxⁿ (eˣ sin x) = 2<sup>n/2</sup> eˣ sin(x + nπ/4). "
        "[6]\n"
        "(b) Prove by induction that n! > 3ⁿ for all integers n ≥ 7, and explain why the basis cannot be n = 6. [5]",
    ],
    "exam_answers": [
        "(a) n = 1: LHS 1 × 1! = 1, RHS 2! − 1 = 1 B1. Assume Σ<sub>r=1</sub>ᵏ r × r! = (k + 1)! − 1 for some positive integer k "
        "M1. Then Σ<sub>r=1</sub>ᵏ⁺¹ = (k + 1)! − 1 + (k + 1)(k + 1)! M1 = (k + 1)!(k + 2) − 1 = (k + 2)! − 1 A1. Conclusion: true "
        "for n = 1, and true for n = k ⇒ true for n = k + 1, so true for all positive integers n A1.\n"
        "(b) f(1) = 8 + 27 = 35 = 7 × 5 B1. Assume f(k) = 2ᵏ⁺² + 3²ᵏ⁺¹ is divisible by 7 for some positive integer k "
        "M1. f(k + 1) = 2 × 2ᵏ⁺² + 9 × 3²ᵏ⁺¹ M1 = 2f(k) + 7 × 3²ᵏ⁺¹ M1 A1; both terms are multiples of 7, so f(k + 1) "
        "is divisible by 7. Conclusion A1.",
        "(a) n = 1: (3 −4; 1 −1) = M B1. Assume Mᵏ = (2k + 1, −4k; k, 1 − 2k) M1. Mᵏ⁺¹ = Mᵏ M M1 "
        "= (3(2k + 1) − 4k, −4(2k + 1) + 4k; 3k + 1 − 2k, −4k − 1 + 2k) A1 = (2k + 3, −4k − 4; k + 1, −2k − 1) "
        "= (2(k + 1) + 1, −4(k + 1); k + 1, 1 − 2(k + 1)) A1. Conclusion A1.\n"
        "(b) det M = −3 + 4 = 1, M⁻¹ = (−1 4; −1 3) B1. n = 0 gives (1 0; 0 1) = I B1; n = −1 gives (−1 4; −1 3) = M⁻¹ B1.",
        "(a) n = 1: 3 − 2 = 1 = u₁; n = 2: 9 − 4 = 5 = u₂ B1 B1. Assume uₖ = 3ᵏ − 2ᵏ and uₖ₊₁ = 3ᵏ⁺¹ − 2ᵏ⁺¹ for "
        "some positive integer k M1. uₖ₊₂ = 5(3ᵏ⁺¹ − 2ᵏ⁺¹) − 6(3ᵏ − 2ᵏ) M1 = 15 × 3ᵏ − 10 × 2ᵏ − 6 × 3ᵏ + 6 × 2ᵏ "
        "A1 = 9 × 3ᵏ − 4 × 2ᵏ = 3ᵏ⁺² − 2ᵏ⁺² A1. Conclusion: true for n = 1, 2; true for n = k and k + 1 ⇒ true for "
        "n = k + 2; so true for all positive integers n A1.\n"
        "(b) 3ⁿ is odd and 2ⁿ is even for n ≥ 1 M1; odd − even = odd, so uₙ is odd A1.",
        "(a) n = 1: d/dx(eˣ sin x) = eˣ(sin x + cos x) = √2 eˣ sin(x + π/4) B1 (using sin(x + π/4) = (sin x + cos x)/√2). "
        "Assume dᵏ/dxᵏ = 2<sup>k/2</sup> eˣ sin(x + kπ/4) M1. Differentiate: 2<sup>k/2</sup> eˣ[sin(x + kπ/4) + cos(x + kπ/4)] M1 "
        "= 2<sup>k/2</sup> eˣ × √2 sin(x + kπ/4 + π/4) M1 A1 = 2<sup>(k+1)/2</sup> eˣ sin(x + (k + 1)π/4). Conclusion A1.\n"
        "(b) n = 7: 7! = 5040 > 3⁷ = 2187 B1. Assume k! > 3ᵏ for some k ≥ 7 M1. (k + 1)! = (k + 1)k! > (k + 1)3ᵏ M1 "
        "> 3 × 3ᵏ = 3ᵏ⁺¹ since k + 1 ≥ 8 > 3 A1. Conclusion; n = 6 fails since 6! = 720 < 3⁶ = 729 B1.",
    ],
}
