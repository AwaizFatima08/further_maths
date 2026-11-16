UNIT = {
    "number": "B1",
    "title": "Euler's form and de Moivre's theorem",
    "tag": "A level · Edexcel CP 2.8, 2.9 · IAL FP2 3.1, 3.2 (proof for any integer n) · AQA B8, B9 · OCR A 4.02d, m, n, q · "
           "OCR MEI Pj12–Pj14, Pj18 · CAIE 9231 P2 2.5 (proof for positive integers; multiple angles, powers, series) · "
           "builds on A1, A2",
    "notes": [
        ("p", "Unit A2 showed that to multiply complex numbers you multiply the moduli and add the arguments. Adding when you "
              "multiply is exactly how indices behave, which suggests writing cos θ + i sin θ as a power. This unit introduces "
              "the exponential form re<sup>iθ</sup>, proves de Moivre's theorem, and uses it to produce trigonometric identities "
              "and to sum series."),

        ("h2", "1.1 Euler's formula and the exponential form (Edexcel 2.9; AQA B9; OCR A 4.02d, 4.02n; MEI Pj14; IAL 3.1)"),
        ("box", "Euler's formula", [
            "e<sup>iθ</sup> = cos θ + i sin θ   (θ in radians).",
            "So every non-zero complex number can be written z = r(cos θ + i sin θ) = re<sup>iθ</sup>, with r = |z| and θ = arg z.",
            "|e<sup>iθ</sup>| = 1 for every real θ: e<sup>iθ</sup> lies on the unit circle.",
            "Conjugate: (re<sup>iθ</sup>)* = re<sup>−iθ</sup>. Special values: e<sup>iπ</sup> = −1, e<sup>iπ/2</sup> = i, "
            "e<sup>2πi</sup> = 1.",
        ]),
        ("p", "<b>Why it is reasonable.</b> The specifications treat Euler's formula as a definition; no proof is needed. Two "
              "arguments support it. First, the Maclaurin series (Unit B3) give e<sup>iθ</sup> = 1 + iθ − θ²/2! − iθ³/3! + θ⁴/4! + … "
              "= (1 − θ²/2! + θ⁴/4! − …) + i(θ − θ³/3! + …) = cos θ + i sin θ. Second, f(θ) = cos θ + i sin θ satisfies "
              "f′(θ) = −sin θ + i cos θ = i f(θ) with f(0) = 1, which is the defining property of e<sup>iθ</sup>."),
        ("p", "With the exponential form, the multiplication rules of Unit A2 become the laws of indices:"),
        ("box", "Products, quotients and powers in exponential form", [
            "r₁e<sup>iθ₁</sup> × r₂e<sup>iθ₂</sup> = r₁r₂e<sup>i(θ₁ + θ₂)</sup>;   r₁e<sup>iθ₁</sup> ÷ r₂e<sup>iθ₂</sup> = "
            "(r₁/r₂)e<sup>i(θ₁ − θ₂)</sup>.",
            "(re<sup>iθ</sup>)ⁿ = rⁿe<sup>inθ</sup> for integer n.",
            "Always reduce an argument to the principal range at the end: e<sup>13πi/6</sup> = e<sup>πi/6</sup>.",
        ]),
        ("p", "Adding and subtracting e<sup>iθ</sup> = cos θ + i sin θ and e<sup>−iθ</sup> = cos θ − i sin θ gives cos and sin "
              "in exponential form. These are the basis of section 1.5."),
        ("box", "cos and sin in exponential form (Edexcel 2.9; OCR A 4.02q)", [
            "cos θ = ½(e<sup>iθ</sup> + e<sup>−iθ</sup>)     sin θ = (1/(2i))(e<sup>iθ</sup> − e<sup>−iθ</sup>)",
        ]),

        ("h2", "1.2 The geometric effect of multiplication and division (OCR A 4.02m; MEI Pj18; CAIE 2.5)"),
        ("p", "Let w = Re<sup>iα</sup>. For any z = re<sup>iθ</sup>, wz = (Rr)e<sup>i(θ + α)</sup>. So multiplying every point of "
              "the Argand diagram by w is an <b>enlargement with scale factor R = |w|, centre O, combined with a rotation through "
              "α = arg w anticlockwise about O</b> (a “spiral similarity”). The two operations can be done in either order."),
        ("bullets", [
            "Dividing by w is the inverse: enlargement with factor 1/R and rotation through −α.",
            "Multiplying by e<sup>iα</sup> (R = 1) is a pure rotation through α; multiplying by i is a rotation through π/2.",
            "Areas are multiplied by R². Lengths are multiplied by R, and angles are preserved.",
            "Positive integer powers z, z², z³, … of z = re<sup>iθ</sup> have moduli r, r², r³, … and arguments θ, 2θ, 3θ, …: the "
            "points spiral outwards if r > 1, inwards if r < 1, and stay on the unit circle if r = 1.",
        ]),
        ("figure", "pb01_spiral.png",
         "Powers of z = 1.2e<sup>iπ/6</sup>. Each multiplication by z turns through π/6 and stretches by 1.2, so the points "
         "1, z, z², …, z⁸ lie on a spiral.", 90),

        ("h2", "1.3 De Moivre's theorem and its proof (Edexcel 2.8; AQA B8; OCR A 4.02q; MEI Pj12; IAL 3.2; CAIE 2.5)"),
        ("box", "De Moivre's theorem", [
            "(cos θ + i sin θ)ⁿ = cos nθ + i sin nθ for every integer n.",
            "Equivalently, (re<sup>iθ</sup>)ⁿ = rⁿe<sup>inθ</sup>.",
            "Printed in the Edexcel, AQA, OCR A, OCR MEI and IAL formula booklets; <b>not</b> in Cambridge's MF19, so CAIE students "
            "must learn it.",
        ]),
        ("p", "<b>Proof by induction for positive integers n</b> (required by CAIE and IAL; a common question elsewhere)."),
        ("bullets", [
            "<b>Basis.</b> For n = 1, (cos θ + i sin θ)¹ = cos θ + i sin θ = cos 1θ + i sin 1θ, so the result is true for n = 1.",
            "<b>Assumption.</b> Assume the result is true for n = k, where k is a positive integer: "
            "(cos θ + i sin θ)ᵏ = cos kθ + i sin kθ.",
            "<b>Inductive step.</b> Then (cos θ + i sin θ)ᵏ⁺¹ = (cos kθ + i sin kθ)(cos θ + i sin θ) "
            "= (cos kθ cos θ − sin kθ sin θ) + i(sin kθ cos θ + cos kθ sin θ) = cos(k + 1)θ + i sin(k + 1)θ, "
            "using the compound angle formulae. So the result is true for n = k + 1.",
            "<b>Conclusion.</b> The result is true for n = 1, and if it is true for n = k then it is true for n = k + 1. "
            "Therefore, by mathematical induction, it is true for all positive integers n.",
        ]),
        ("p", "<b>Extension to n = 0 and negative integers (IAL FP2 3.2 requires this).</b> For n = 0 both sides equal 1. For a "
              "negative integer n, write n = −m with m a positive integer. Then"),
        ("p", "(cos θ + i sin θ)⁻ᵐ = 1/(cos mθ + i sin mθ) = (cos mθ − i sin mθ)/(cos²mθ + sin²mθ) = cos mθ − i sin mθ "
              "= cos(−mθ) + i sin(−mθ) = cos nθ + i sin nθ,"),
        ("p", "using the positive-integer result, multiplying by the conjugate, and the facts that cos is even and sin is odd. So "
              "the theorem holds for all integers n."),
        ("p", "With Euler's formula the theorem is just (e<sup>iθ</sup>)ⁿ = e<sup>inθ</sup>. That is a neat way to remember it, "
              "but when a question says “prove”, give the induction proof. Unit B2 uses de Moivre with rational powers to find "
              "roots."),

        ("h2", "1.4 Multiple-angle formulae (Edexcel 2.8; AQA B8; OCR A 4.02q; MEI Pj13; CAIE 2.5)"),
        ("p", "To write cos nθ or sin nθ in terms of powers of cos θ and sin θ, expand (cos θ + i sin θ)ⁿ in two ways: by de "
              "Moivre, and by the binomial theorem. Then equate real parts (for cos nθ) or imaginary parts (for sin nθ). Write "
              "c = cos θ and s = sin θ to save writing."),
        ("p", "For n = 3: (c + is)³ = c³ + 3c²(is) + 3c(is)² + (is)³ = (c³ − 3cs²) + i(3c²s − s³). Equating with cos 3θ + i sin 3θ:"),
        ("box", "Triple-angle formulae", [
            "cos 3θ = c³ − 3cs² = c³ − 3c(1 − c²) = 4cos³θ − 3cos θ.",
            "sin 3θ = 3c²s − s³ = 3(1 − s²)s − s³ = 3sin θ − 4sin³θ.",
            "tan 3θ = sin 3θ/cos 3θ = (3c²s − s³)/(c³ − 3cs²) = (3t − t³)/(1 − 3t²), where t = tan θ (divide top and bottom by c³).",
        ]),
        ("p", "Use cos²θ = 1 − sin²θ (or the reverse) to remove the unwanted function. For tan nθ, divide the imaginary part by the "
              "real part, then divide top and bottom by cosⁿθ. The binomial coefficients from Pascal's triangle and the powers of "
              "i (1, i, −1, −i, 1, …) do most of the work."),

        ("h2", "1.5 Powers of sin and cos in terms of multiple angles (Edexcel 2.8; OCR A 4.02q; CAIE 2.5)"),
        ("p", "Going the other way, to write cosⁿθ or sinⁿθ as a sum of cosines or sines of multiples of θ, let z = e<sup>iθ</sup>. "
              "Then 1/z = e<sup>−iθ</sup>, and de Moivre gives zⁿ = e<sup>inθ</sup> and z⁻ⁿ = e<sup>−inθ</sup>."),
        ("box", "The key identities (z = cos θ + i sin θ)", [
            "z + 1/z = 2cos θ          z − 1/z = 2i sin θ",
            "zⁿ + 1/zⁿ = 2cos nθ          zⁿ − 1/zⁿ = 2i sin nθ",
            "Cambridge examiners expect you to state these when you use them.",
        ]),
        ("p", "<b>Method.</b> Write (2cos θ)ⁿ = (z + 1/z)ⁿ or (2i sin θ)ⁿ = (z − 1/z)ⁿ. Expand by the binomial theorem, pair "
              "the terms zᵏ with z⁻ᵏ, and replace each pair using the second line of the box. For example"),
        ("p", "(2cos θ)⁴ = (z + 1/z)⁴ = z⁴ + 4z² + 6 + 4z⁻² + z⁻⁴ = (z⁴ + z⁻⁴) + 4(z² + z⁻²) + 6 = 2cos 4θ + 8cos 2θ + 6, "
              "so cos⁴θ = ⅛(cos 4θ + 4cos 2θ + 3)."),
        ("p", "This is the standard way to integrate even powers of sin and cos: each term of the result integrates directly. "
              "Odd powers of sin θ give sines (because (z − 1/z)ⁿ with n odd has the factor (2i)ⁿ, which is imaginary)."),

        ("h2", "1.6 Sums of series: the C + iS method (Edexcel 2.8; AQA B8; OCR A 4.02q; MEI Pj13; CAIE 2.5)"),
        ("p", "To sum a series C of cosines, write down the matching series S of sines, form C + iS, and use "
              "cos rθ + i sin rθ = e<sup>irθ</sup>. The result is usually a geometric series or a binomial expansion. Find its sum, "
              "then take the real part (for C) or the imaginary part (for S)."),
        ("box", "Two useful tools", [
            "Geometric series: 1 + w + w² + … + wⁿ⁻¹ = (wⁿ − 1)/(w − 1), w ≠ 1; and 1 + w + w² + … = 1/(1 − w) when |w| < 1.",
            "Half-angle factor: 1 + e<sup>iθ</sup> = e<sup>iθ/2</sup>(e<sup>−iθ/2</sup> + e<sup>iθ/2</sup>) = "
            "2cos(θ/2) e<sup>iθ/2</sup>, and e<sup>iθ</sup> − 1 = 2i sin(θ/2) e<sup>iθ/2</sup>.",
            "To take the real part of a quotient, multiply top and bottom by the conjugate of the denominator first.",
        ]),
        ("p", "Example: Σ (r = 0 to n) C(n, r) cos rθ, where C(n, r) is the binomial coefficient, uses "
              "C + iS = Σ C(n, r)e<sup>irθ</sup> = (1 + e<sup>iθ</sup>)ⁿ (worked example B1.6)."),

        ("warn", "Common mistakes", [
            "Applying de Moivre to a number that is not in the form cos θ + i sin θ: rewrite cos θ − i sin θ as cos(−θ) + i sin(−θ) "
            "first, and include the modulus as rⁿ.",
            "Losing the powers of i when expanding (c + is)ⁿ: (is)² = −s², (is)³ = −is³, (is)⁴ = s⁴.",
            "Forgetting the factor 2ⁿ (or (2i)ⁿ) when dividing back: (z + 1/z)⁴ = 16cos⁴θ, not cos⁴θ.",
            "In an induction proof, omitting the basis, the assumption statement or the concluding sentence. All four parts earn "
            "marks.",
            "In C + iS questions, taking the real part of a fraction before making its denominator real.",
            "Giving an argument outside the principal range in the final answer.",
        ]),
        ("box", "Given or learn? (formula booklets)", [
            "De Moivre's theorem is printed by Edexcel, AQA, OCR A, OCR MEI and IAL; Euler's formula is printed by IAL. "
            "Learn both anyway, together with z ± 1/z and zⁿ ± z⁻ⁿ.",
            "Cambridge 9231 prints neither: learn de Moivre's theorem, zⁿ + z⁻ⁿ = 2cos nθ and zⁿ − z⁻ⁿ = 2i sin nθ.",
        ]),
    ],
    "examples": [
        {
            "title": "Powers using the exponential form",
            "question": "Express in the form x + iy: (a) (√3 + i)⁹, (b) (1 − i)⁻⁶.",
            "steps": [
                "(a) |√3 + i| = 2 and arg(√3 + i) = π/6, so √3 + i = 2e<sup>iπ/6</sup>.",
                "(√3 + i)⁹ = 2⁹e<sup>9iπ/6</sup> = 512e<sup>3πi/2</sup> = 512(cos(3π/2) + i sin(3π/2)) = −512i.",
                "(b) 1 − i = √2e<sup>−iπ/4</sup>, so (1 − i)⁻⁶ = (√2)⁻⁶e<sup>6iπ/4</sup> = ⅛e<sup>3πi/2</sup> = −⅛i.",
                "Check: (1 − i)² = −2i, so (1 − i)⁶ = (−2i)³ = 8i, and 1/(8i) = −i/8. ✓",
            ],
        },
        {
            "title": "Multiplication as an enlargement and a rotation",
            "question": "The unit square S has vertices 0, 1, 1 + i and i. It is mapped by w = (1 + √3 i)z. Describe the "
                        "transformation, find the images of the vertices, and find the area of the image.",
            "figure": "pb01_rotate.png", "caption": "Multiplying by 2e<sup>iπ/3</sup>: enlarge by 2 and rotate through π/3.",
            "width_mm": 85,
            "steps": [
                "1 + √3 i = 2e<sup>iπ/3</sup>, so the transformation is an enlargement, scale factor 2, centre O, together with a "
                "rotation through π/3 anticlockwise about O.",
                "Images: 0 → 0; 1 → 1 + √3 i; i → (1 + √3 i)i = −√3 + i; 1 + i → (1 + √3 i)(1 + i) = (1 − √3) + (1 + √3)i.",
                "The image is a square of side 2, so its area is 2² × 1 = 4.",
            ],
        },
        {
            "title": "A multiple-angle formula and an exact value",
            "question": "(a) Use de Moivre's theorem to show that cos 5θ = 16cos⁵θ − 20cos³θ + 5cos θ.\n(b) Hence show that "
                        "cos²(π/10) = (5 + √5)/8.",
            "steps": [
                "(a) cos 5θ + i sin 5θ = (c + is)⁵. The real terms of the binomial expansion are c⁵ + 10c³(is)² + 5c(is)⁴ "
                "= c⁵ − 10c³s² + 5cs⁴.",
                "Replace s² by 1 − c²: c⁵ − 10c³(1 − c²) + 5c(1 − c²)² = c⁵ − 10c³ + 10c⁵ + 5c − 10c³ + 5c⁵ "
                "= 16c⁵ − 20c³ + 5c. ✓",
                "(b) When θ = π/10, cos 5θ = cos(π/2) = 0, so c = cos(π/10) ≠ 0 satisfies 16c⁴ − 20c² + 5 = 0.",
                "c² = (20 ± √(400 − 320))/32 = (20 ± 4√5)/32 = (5 ± √5)/8.",
                "π/10 is a small angle, so cos²(π/10) is close to 1: (5 + √5)/8 ≈ 0.905, while (5 − √5)/8 ≈ 0.345 "
                "(that is cos²(3π/10)). So cos²(π/10) = (5 + √5)/8.",
            ],
        },
        {
            "title": "tan 4θ and a quartic equation (MEI Pj13; Edexcel tan rθ)",
            "question": "(a) Show that tan 4θ = (4t − 4t³)/(1 − 6t² + t⁴), where t = tan θ.\n(b) Hence find the roots of "
                        "t⁴ + 4t³ − 6t² − 4t + 1 = 0 in the form tan(kπ), giving k exactly.",
            "steps": [
                "(a) (c + is)⁴ = c⁴ + 4c³(is) + 6c²(is)² + 4c(is)³ + (is)⁴ = (c⁴ − 6c²s² + s⁴) + i(4c³s − 4cs³).",
                "So tan 4θ = (4c³s − 4cs³)/(c⁴ − 6c²s² + s⁴). Divide top and bottom by c⁴: (4t − 4t³)/(1 − 6t² + t⁴).",
                "(b) Setting tan 4θ = 1 gives 4t − 4t³ = 1 − 6t² + t⁴, i.e. t⁴ + 4t³ − 6t² − 4t + 1 = 0.",
                "tan 4θ = 1 ⇒ 4θ = π/4 + nπ ⇒ θ = π/16 + nπ/4. Taking n = 0, 1, 2, 3 gives four different values of tan θ.",
                "The roots are tan(π/16), tan(5π/16), tan(9π/16) and tan(13π/16).",
            ],
        },
        {
            "title": "A power of sin θ, and an integral",
            "question": "(a) Express sin⁶θ in the form a + b cos 2θ + c cos 4θ + d cos 6θ.\n(b) Hence find ∫<sub>0</sub><sup>π/2</sup> sin⁶θ dθ.",
            "steps": [
                "(a) With z = e<sup>iθ</sup>: (2i sin θ)⁶ = (z − 1/z)⁶. The left side is (2i)⁶sin⁶θ = −64sin⁶θ.",
                "(z − 1/z)⁶ = z⁶ − 6z⁴ + 15z² − 20 + 15z⁻² − 6z⁻⁴ + z⁻⁶ = (z⁶ + z⁻⁶) − 6(z⁴ + z⁻⁴) + 15(z² + z⁻²) − 20.",
                "= 2cos 6θ − 12cos 4θ + 30cos 2θ − 20, using zⁿ + z⁻ⁿ = 2cos nθ.",
                "So sin⁶θ = (1/32)(10 − 15cos 2θ + 6cos 4θ − cos 6θ).",
                "(b) ∫<sub>0</sub><sup>π/2</sup> sin⁶θ dθ = (1/32)[10θ − (15/2)sin 2θ + (6/4)sin 4θ − (1/6)sin 6θ] from 0 to π/2.",
                "Every sine term is 0 at both limits, so the integral is (1/32)(10 × π/2) = 5π/32.",
            ],
        },
        {
            "title": "Summing a binomial series by C + iS",
            "question": "Show that Σ (r = 0 to n) C(n, r) cos rθ = 2ⁿcosⁿ(θ/2) cos(nθ/2), and write down the corresponding "
                        "result for Σ (r = 0 to n) C(n, r) sin rθ.",
            "steps": [
                "Let C = Σ C(n, r) cos rθ and S = Σ C(n, r) sin rθ (r = 0 to n).",
                "C + iS = Σ C(n, r)(cos rθ + i sin rθ) = Σ C(n, r)(e<sup>iθ</sup>)ʳ = (1 + e<sup>iθ</sup>)ⁿ by the binomial theorem.",
                "1 + e<sup>iθ</sup> = e<sup>iθ/2</sup>(e<sup>−iθ/2</sup> + e<sup>iθ/2</sup>) = 2cos(θ/2)e<sup>iθ/2</sup>.",
                "So C + iS = 2ⁿcosⁿ(θ/2)e<sup>inθ/2</sup> = 2ⁿcosⁿ(θ/2)[cos(nθ/2) + i sin(nθ/2)].",
                "Real parts: C = 2ⁿcosⁿ(θ/2) cos(nθ/2). Imaginary parts: S = 2ⁿcosⁿ(θ/2) sin(nθ/2).",
                "Check with n = 2, θ = π/2: C = 1 + 2cos(π/2) + cos π = 0, and 4cos²(π/4)cos(π/2) = 0. ✓",
            ],
        },
    ],
    "practice": [
        "Write in the form re<sup>iθ</sup>, with −π < θ ≤ π: (a) −4 (b) 1 − √3 i (c) 3i.",
        "Write in the form x + iy: (a) 4e<sup>5iπ/6</sup> (b) √2e<sup>−iπ/4</sup> (c) e<sup>iπ</sup> + e<sup>−iπ/2</sup>.",
        "z = 3e<sup>iπ/4</sup> and w = 2e<sup>iπ/3</sup>. Find, in exponential form with principal arguments:\n"
        "(a) zw (b) z/w (c) z⁴ (d) w*.",
        "Simplify, giving answers in the form cos kθ + i sin kθ or x + iy:\n(a) (cos(π/9) + i sin(π/9))⁶ "
        "(b) (cos θ + i sin θ)⁵/(cos 2θ − i sin 2θ)³.",
        "Use de Moivre's theorem to find, in the form x + iy: (a) (1 + i)¹⁰ (b) (1 − √3 i)⁻⁴.",
        "Describe fully the transformation of the Argand diagram given by:\n(a) multiplying by 3i (b) multiplying by 1 − i "
        "(c) dividing by 2e<sup>iπ/6</sup>.",
        "Use de Moivre's theorem to prove that sin 3θ = 3sin θ − 4sin³θ and cos 3θ = 4cos³θ − 3cos θ.",
        "Show that tan 3θ = (3t − t³)/(1 − 3t²), where t = tan θ.",
        "(a) Using z = e<sup>iθ</sup>, show that cos³θ = ¼(cos 3θ + 3cos θ).\n(b) Hence find the exact value of "
        "∫<sub>0</sub><sup>π/3</sup> cos³θ dθ.",
        "Show that sin⁴θ = ⅛(cos 4θ − 4cos 2θ + 3).",
        "(a) Show that 1 + e<sup>iθ</sup> = 2cos(θ/2)e<sup>iθ/2</sup>.\n(b) Hence write down the modulus and argument of "
        "1 + e<sup>iθ</sup> for 0 < θ < π.",
        "By considering the geometric series Σ (r = 0 to ∞) (½e<sup>iθ</sup>)ʳ, show that\nΣ (r = 0 to ∞) (½)ʳcos rθ = "
        "(4 − 2cos θ)/(5 − 4cos θ), and find the corresponding sum of (½)ʳsin rθ.",
    ],
    "answers": [
        "(a) 4e<sup>iπ</sup> (b) 2e<sup>−iπ/3</sup> (c) 3e<sup>iπ/2</sup>.",
        "(a) −2√3 + 2i (b) 1 − i (c) −1 − i.",
        "(a) 6e<sup>7iπ/12</sup> (b) (3/2)e<sup>−iπ/12</sup> (c) 81e<sup>iπ</sup> = −81 (d) 2e<sup>−iπ/3</sup>.",
        "(a) cos(2π/3) + i sin(2π/3) = −½ + (√3/2)i (b) e<sup>5iθ</sup>/e<sup>−6iθ</sup> = cos 11θ + i sin 11θ.",
        "(a) (√2e<sup>iπ/4</sup>)¹⁰ = 32e<sup>5iπ/2</sup> = 32i (b) (2e<sup>−iπ/3</sup>)⁻⁴ = (1/16)e<sup>4iπ/3</sup> "
        "= −1/32 − (√3/32)i.",
        "(a) enlargement scale factor 3, centre O, and rotation π/2 anticlockwise about O (b) enlargement scale factor √2 and "
        "rotation through −π/4 (π/4 clockwise), both about O (c) enlargement scale factor ½ and rotation through −π/6, both "
        "about O.",
        "(c + is)³ = (c³ − 3cs²) + i(3c²s − s³). Imaginary parts: sin 3θ = 3(1 − s²)s − s³ = 3s − 4s³. Real parts: "
        "cos 3θ = c³ − 3c(1 − c²) = 4c³ − 3c.",
        "tan 3θ = (3c²s − s³)/(c³ − 3cs²); divide top and bottom by c³.",
        "(a) (z + 1/z)³ = z³ + 3z + 3z⁻¹ + z⁻³ = 2cos 3θ + 6cos θ = 8cos³θ. (b) ¼[⅓sin 3θ + 3sin θ] from 0 to π/3 "
        "= ¼(0 + 3√3/2) = 3√3/8.",
        "(z − 1/z)⁴ = 16sin⁴θ = (z⁴ + z⁻⁴) − 4(z² + z⁻²) + 6 = 2cos 4θ − 8cos 2θ + 6; divide by 16.",
        "(a) 1 + e<sup>iθ</sup> = e<sup>iθ/2</sup>(e<sup>−iθ/2</sup> + e<sup>iθ/2</sup>) = e<sup>iθ/2</sup> × 2cos(θ/2). "
        "(b) cos(θ/2) > 0, so modulus 2cos(θ/2), argument θ/2.",
        "C + iS = 1/(1 − ½e<sup>iθ</sup>) = 2/(2 − cos θ − i sin θ) = 2(2 − cos θ + i sin θ)/((2 − cos θ)² + sin²θ) "
        "= 2(2 − cos θ + i sin θ)/(5 − 4cos θ). Real part (4 − 2cos θ)/(5 − 4cos θ); sine sum 2sin θ/(5 − 4cos θ). "
        "(|½e<sup>iθ</sup>| = ½ < 1, so the series converges.)",
    ],
    "exam": [
        "(a) Prove by induction that (cos θ + i sin θ)ⁿ = cos nθ + i sin nθ for all positive integers n. [5]\n"
        "(b) Show that the result is also true for all negative integers n. [3]\n(c) Hence find (1 + i)⁻⁸. [2]",
        "(a) Use de Moivre's theorem to show that sin 5θ = 16sin⁵θ − 20sin³θ + 5sin θ. [4]\n(b) Hence find the four "
        "non-zero roots of 16x⁴ − 20x² + 5 = 0 in the form ±sin(kπ). [4]\n(c) Deduce the exact value of "
        "sin²(π/5) sin²(2π/5). [3]",
        "(a) Given z = cos θ + i sin θ, show that zⁿ + 1/zⁿ = 2cos nθ for any positive integer n. [2]\n(b) Show that "
        "cos⁵θ = (1/16)(cos 5θ + 5cos 3θ + 10cos θ). [4]\n(c) Hence find the exact value of ∫<sub>0</sub><sup>π/2</sup> cos⁵θ dθ. [3]",
        "Let n ≥ 2 be an integer and z = e<sup>iπ/n</sup>.\n(a) Show that 1 + z + z² + … + zⁿ⁻¹ = 2/(1 − z). [2]\n"
        "(b) Show that 2/(1 − z) = 1 + i cot(π/(2n)). [4]\n(c) Hence find Σ (r = 0 to n − 1) sin(rπ/n) and "
        "Σ (r = 0 to n − 1) cos(rπ/n). [3]",
    ],
    "exam_answers": [
        "(a) n = 1: both sides cos θ + i sin θ [B1]. Assume true for n = k [M1]. (cos θ + i sin θ)ᵏ⁺¹ = (cos kθ + i sin kθ)"
        "(cos θ + i sin θ) = (cos kθ cos θ − sin kθ sin θ) + i(sin kθ cos θ + cos kθ sin θ) [M1] = cos(k + 1)θ + "
        "i sin(k + 1)θ [A1]. True for n = 1 and true for n = k ⇒ true for n = k + 1, so true for all positive integers n "
        "[A1]. (b) n = −m, m > 0 [M1]: (cos θ + i sin θ)⁻ᵐ = 1/(cos mθ + i sin mθ) = cos mθ − i sin mθ [M1] = cos(−mθ) + "
        "i sin(−mθ) = cos nθ + i sin nθ [A1]. (c) (√2e<sup>iπ/4</sup>)⁻⁸ = (1/16)e<sup>−2πi</sup> [M1] = 1/16 [A1].",
        "(a) Imaginary part of (c + is)⁵: 5c⁴s − 10c²s³ + s⁵ [M1 A1]; c² = 1 − s²: 5(1 − s²)²s − 10(1 − s²)s³ + s⁵ [M1] "
        "= 16s⁵ − 20s³ + 5s [A1]. (b) sin 5θ = 0 with sin θ ≠ 0 [M1]: θ = π/5, 2π/5, 3π/5, 4π/5 [A1], giving x = sin θ "
        "[M1]: x = ±sin(π/5), ±sin(2π/5) [A1] (sin(3π/5) = sin(2π/5), and −sin(π/5) = sin(−π/5)). (c) As a quadratic in u = x², "
        "16u² − 20u + 5 = 0 has roots sin²(π/5) and sin²(2π/5) [M1 A1]; product = 5/16 [A1].",
        "(a) zⁿ = cos nθ + i sin nθ and z⁻ⁿ = cos nθ − i sin nθ by de Moivre [M1]; adding gives 2cos nθ [A1]. "
        "(b) (z + 1/z)⁵ = 32cos⁵θ [B1]; = z⁵ + 5z³ + 10z + 10z⁻¹ + 5z⁻³ + z⁻⁵ [M1] = 2cos 5θ + 10cos 3θ + 20cos θ [M1]; "
        "divide by 32 [A1]. (c) (1/16)[⅕sin 5θ + (5/3)sin 3θ + 10sin θ] from 0 to π/2 [M1] = (1/16)(⅕ − 5/3 + 10) [M1] "
        "= 8/15 [A1].",
        "(a) Geometric series: (1 − zⁿ)/(1 − z) [M1]; zⁿ = e<sup>iπ</sup> = −1, so the sum is 2/(1 − z) [A1]. (b) With "
        "α = π/n: 1 − e<sup>iα</sup> = −2i sin(α/2)e<sup>iα/2</sup> [M1 A1]; 2/(1 − z) = (i/sin(α/2))e<sup>−iα/2</sup> "
        "= (i cos(α/2) + sin(α/2))/sin(α/2) [M1] = 1 + i cot(π/(2n)) [A1]. (c) Imaginary parts: Σ sin(rπ/n) = cot(π/(2n)) "
        "[M1 A1]; real parts: Σ cos(rπ/n) = 1 [A1].",
    ],
}
