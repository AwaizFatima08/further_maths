"""Unit C9: Number theory I: division, Euclid's algorithm and counting.

Edexcel FP2 5.1, 5.2, 5.5, 5.7 (AS FP2 4.1, 4.2, 4.4); OCR A Additional Pure 8.02a, b, c, d, i, j, k (AS).
Every number is checked in checks_pure/pc09_check.py.
"""

UNIT = {
    "number": "C9",
    "title": "Number theory I: division, Euclid's algorithm and counting",
    "tag": "Further Pure option · Edexcel FP2 5.1, 5.2, 5.5, 5.7 (AS FP2 4.1, 4.2, 4.4: no counting) · "
           "OCR A Additional Pure Y535/Y545 8.02a–d, 8.02i–k (AS) · continued in C10 (modular arithmetic)",
    "notes": [
        ("p", "Number theory studies the integers ℤ = {…, −2, −1, 0, 1, 2, …}: which numbers divide which, how to find "
              "highest common factors, and how numbers are written in different bases. Everything rests on one fact, the "
              "division algorithm, and one method, Euclid's algorithm. The unit ends with the counting principles that "
              "Edexcel examines in the same section. In this unit all letters stand for integers unless stated otherwise."),

        ("h2", "9.1 Divisibility, primes and the fundamental theorem"),
        ("bullets", [
            "<b>a divides b</b>, written a | b, means b = ka for some integer k. Then a is a <b>factor</b> (divisor) of b and b is "
            "a <b>multiple</b> of a. For example 6 | 42, 6 | −42 and 6 | 0, but 6 ∤ 15 (∤ means “does not divide”).",
            "A <b>prime</b> is an integer p > 1 whose only positive divisors are 1 and p. An integer n > 1 that is not prime is "
            "<b>composite</b>: n = ab with 1 < a, b < n. The number 1 is neither prime nor composite.",
            "The <b>highest common factor</b> hcf(a, b) (also called the greatest common divisor, gcd) is the largest positive "
            "integer dividing both a and b. The <b>lowest common multiple</b> lcm(a, b) is the smallest positive common multiple.",
            "a and b are <b>coprime</b> (relatively prime) if hcf(a, b) = 1, e.g. 8 and 15 are coprime although neither is prime.",
        ]),
        ("box", "Key results on divisibility", [
            "<b>Linear combinations (OCR 8.02j).</b> If a | b and a | c, then a | (bx + cy) for all integers x and y.",
            "Proof: b = ma and c = na for integers m, n. Then bx + cy = max + nay = a(mx + ny), and mx + ny is an integer, so a | (bx + cy).",
            "<b>Fundamental theorem of arithmetic.</b> Every integer n > 1 can be written as a product of primes, and this "
            "factorisation is unique apart from the order of the factors. (Proof not required.)",
            "From prime factorisations: hcf takes the <b>lower</b> power of each prime, lcm the <b>higher</b> power, and "
            "hcf(a, b) × lcm(a, b) = ab for positive a, b.",
        ]),
        ("p", "For example 360 = 2³ × 3² × 5 and 756 = 2² × 3³ × 7, so hcf(360, 756) = 2² × 3² = 36 and "
              "lcm(360, 756) = 2³ × 3³ × 5 × 7 = 7560. Check: 36 × 7560 = 272 160 = 360 × 756. To test whether n is prime it "
              "is enough to try prime divisors up to √n, because if n = ab with a ≤ b then a ≤ √n."),

        ("h2", "9.2 The division algorithm and the notation of congruence"),
        ("box", "Division algorithm (division theorem)", [
            "For any integers a and b with b > 0 there are <b>unique</b> integers q (the quotient) and r (the remainder) with",
            "a = bq + r,   0 ≤ r < b.",
            "r = 0 exactly when b | a. The remainder is never negative: −17 = 5 × (−4) + 3, so q = −4 and r = 3 (not q = −3, r = −2).",
        ]),
        ("p", "Two integers that leave the same remainder on division by n are called <b>congruent modulo n</b>, written "
              "a ≡ b (mod n). Equivalently n | (a − b). For example 38 ≡ 3 (mod 5), since both leave remainder 3 and 5 | 35, "
              "and −17 ≡ 3 (mod 5). Every integer is congruent modulo n to exactly one of 0, 1, …, n − 1 (its remainder). Congruences can "
              "be added, subtracted and multiplied like equations, and raised to powers: if a ≡ b then aᵏ ≡ bᵏ (mod n). "
              "These rules are proved in C10; here they give quick proofs of divisibility tests."),

        ("h2", "9.3 Number bases (OCR A)"),
        ("p", "In base b (b ≥ 2) the digits are 0, 1, …, b − 1 and the place values are powers of b. The base is written as a "
              "subscript: 2626₇ = 2 × 7³ + 6 × 7² + 2 × 7 + 6 = 686 + 294 + 14 + 6 = 1000. Bases above 10 need extra digits: "
              "A = 10, B = 11, so 4A3₁₂ = 4 × 144 + 10 × 12 + 3 = 699."),
        ("bullets", [
            "<b>Base b to base 10:</b> multiply each digit by its place value and add.",
            "<b>Base 10 to base b:</b> divide repeatedly by b using the division algorithm. The remainders, read from the "
            "last one to the first, are the digits. Alternatively subtract the largest multiples of b³, b², … in turn.",
            "<b>Arithmetic in base b</b> works like column arithmetic in base 10, but you carry when a column reaches b. "
            "In base 2: 1 + 1 = 10₂ and 1 + 1 + 1 = 11₂. If unsure, convert to base 10, work, and convert back.",
        ]),
        ("table", ["Division by 7", "Quotient", "Remainder"], [
            ["1000 ÷ 7", "142", "6  (units digit)"],
            ["142 ÷ 7", "20", "2"],
            ["20 ÷ 7", "2", "6"],
            ["2 ÷ 7", "0", "2  (leading digit)"],
        ]),
        ("p", "Reading the remainders upwards gives 1000 = 2626₇, agreeing with the value above."),

        ("h2", "9.4 Euclid's algorithm"),
        ("p", "If a = bq + r then any common divisor of a and b divides r = a − qb, and any common divisor of b and r divides "
              "a = bq + r (both by the linear combination result). So a, b and b, r have exactly the same common divisors, and "
              "hcf(a, b) = hcf(b, r). Repeating this with smaller and smaller numbers must end with remainder 0."),
        ("box", "Euclid's algorithm for hcf(a, b), a > b > 0", [
            "Divide: a = bq₁ + r₁, then b = r₁q₂ + r₂, then r₁ = r₂q₃ + r₃, and so on, each time dividing the last divisor by the last remainder.",
            "Stop when a remainder is 0. The <b>last non-zero remainder</b> is hcf(a, b).",
            "Example: 1071 = 2 × 462 + 147; 462 = 3 × 147 + 21; 147 = 7 × 21 + 0. So hcf(1071, 462) = 21.",
        ]),

        ("h2", "9.5 Bezout's identity and Euclid's lemma"),
        ("box", "Bezout's identity", [
            "For integers a, b, not both zero, there are integers x and y with ax + by = hcf(a, b).",
            "In particular a and b are coprime if and only if ax + by = 1 has an integer solution.",
            "More generally ax + by = c has integer solutions if and only if hcf(a, b) | c.",
        ]),
        ("p", "<b>Finding x and y by back substitution.</b> Rearrange each line of Euclid's algorithm to make its remainder the "
              "subject, then start from the line giving the hcf and substitute the earlier remainders one at a time, collecting "
              "multiples of the two original numbers. For 1071 and 462: 21 = 462 − 3 × 147, and 147 = 1071 − 2 × 462, so "
              "21 = 462 − 3(1071 − 2 × 462) = 7 × 462 − 3 × 1071. Always check: 3234 − 3213 = 21."),
        ("p", "The ‘only if’ part of the last line of the box: if ax + by = c then hcf(a, b) divides ax + by = c. For the ‘if’ "
              "part, multiply a Bezout solution by c ÷ hcf(a, b). Solutions are not unique: if ax₀ + by₀ = d then "
              "a(x₀ + kb/d) + b(y₀ − ka/d) = d for every integer k."),
        ("box", "Euclid's lemma (OCR 8.02k)", [
            "If p is prime and p | ab, then p | a or p | b.",
            "Proof: suppose p | ab and p ∤ a. The only positive divisors of p are 1 and p, and p ∤ a, so hcf(a, p) = 1. By Bezout "
            "there are integers x, y with ax + py = 1. Multiply by b: abx + pby = b. Now p | ab and p | p, so p divides "
            "abx + pby = b by the linear combination result. Hence p | b.",
            "The same proof shows: if n | ab and hcf(n, a) = 1, then n | b. The lemma fails for composite p: 6 | 4 × 9 but 6 ∤ 4 and 6 ∤ 9.",
        ]),
        ("p", "Euclid's lemma is the key step in proving that prime factorisation is unique, and it gives results such as: if a "
              "prime p divides n², then p | n (take a = b = n)."),

        ("h2", "9.6 Divisibility tests"),
        ("p", "Write N = dₖ…d₂d₁d₀ in base 10, so N = d₀ + 10d₁ + 10²d₂ + … . Each test comes from what the powers of 10 are "
              "congruent to. For example 10 ≡ 1 (mod 9), so 10ʲ ≡ 1 and N ≡ d₀ + d₁ + d₂ + … (mod 9): N and its digit sum leave "
              "the same remainder on division by 9. Since 10 ≡ −1 (mod 11), 10ʲ ≡ (−1)ʲ and N ≡ d₀ − d₁ + d₂ − … (mod 11)."),
        ("table", ["Divisor", "Test: N is divisible if and only if …", "Reason", "Boards"], [
            ["2, 5, 10", "the last digit is even / is 0 or 5 / is 0", "10 ≡ 0 (mod 2, 5, 10)", "Ed, OCR (10: Ed)"],
            ["4", "the number formed by the last two digits is divisible by 4", "100 = 4 × 25", "Ed, OCR"],
            ["8", "the number formed by the last three digits is divisible by 8", "1000 = 8 × 125", "OCR"],
            ["3, 9", "the digit sum is divisible by 3 (by 9)", "10 ≡ 1 (mod 9), so mod 3 too", "Ed, OCR"],
            ["6", "N passes the tests for both 2 and 3", "2 and 3 are coprime primes", "Ed"],
            ["11", "the alternating sum d₀ − d₁ + d₂ − … is divisible by 11", "10 ≡ −1 (mod 11)", "Ed, OCR"],
            ["7, 11, 13", "the alternating sum of 3-digit blocks from the right is divisible by 7 (11, 13)", "1000 ≡ −1, as 1001 = 7 × 11 × 13", "OCR 8.02c"],
            ["37", "the sum of 3-digit blocks from the right is divisible by 37", "1000 ≡ 1, as 999 = 27 × 37", "OCR 8.02c"],
        ]),
        ("p", "<b>Tests for other primes below 50 (OCR 8.02c).</b> Write N = 10a + b, where b is the last digit. If m is chosen "
              "with 10m ≡ 1 (mod p), then m(10a + b) ≡ a + mb (mod p), and since hcf(m, p) = 1, p | N if and only if p | (a + mb). "
              "So: remove the last digit, add m times it to what is left, and repeat. Multiples of p ending in 1 or 9 give m "
              "quickly: 21 = 3 × 7 gives 10 × (−2) ≡ 1 (mod 7), and 39 = 3 × 13 gives 10 × 4 ≡ 1 (mod 13)."),
        ("table", ["p", "7", "13", "17", "19", "23", "29", "31", "37", "41", "43", "47"], [
            ["m (10m ≡ 1)", "−2", "4", "−5", "2", "7", "3", "−3", "−11", "−4", "13", "−14"],
            ["test: p | a + mb", "a − 2b", "a + 4b", "a − 5b", "a + 2b", "a + 7b", "a + 3b", "a − 3b", "a − 11b", "a − 4b", "a + 13b", "a − 14b"],
        ]),
        ("p", "These ‘last digit’ tests decide divisibility only: a + mb usually does <b>not</b> leave the same remainder as N. "
              "The digit-sum, alternating-sum and block tests, by contrast, also give the remainder."),

        ("h2", "9.7 Counting principles (Edexcel A level FP2 only)"),
        ("bullets", [
            "<b>Multiplicative principle:</b> if a task is done in stages, with m ways for the first stage and n ways for the "
            "second whatever happened first, there are mn ways altogether. A 4-digit PIN has 10⁴ = 10 000 possibilities.",
            "<b>Addition principle:</b> if the outcomes split into cases that cannot happen together (disjoint cases), add the "
            "counts. Committees with exactly 2 or exactly 3 women: count each case and add.",
            "<b>Subtraction principle:</b> count what you do not want and subtract: number with at least one X = total − number with "
            "no X. For overlapping sets, |A ∪ B| = |A| + |B| − |A ∩ B| (inclusion–exclusion). Of 1, …, 1000, 333 are multiples "
            "of 3, 200 of 5 and 66 of 15, so 333 + 200 − 66 = 467 are multiples of 3 or 5.",
            "<b>Subsets:</b> a set with n elements has 2ⁿ subsets (each element is either in or out), including the empty set and the set itself.",
        ]),
        ("box", "Permutations and combinations", [
            "n! = n(n − 1)…2 × 1 is the number of arrangements of n different objects in a line; 0! = 1.",
            "ⁿPᵣ = n!/(n − r)! is the number of ordered selections (arrangements) of r objects from n different objects.",
            "ⁿCᵣ = n!/(r!(n − r)!) is the number of unordered selections (subsets of size r). Note ⁿPᵣ = r! × ⁿCᵣ.",
            "Arrangements of n objects of which p are alike, q alike, …: n!/(p! q! …). E.g. LETTER: 6!/(2! 2!) = 180.",
        ]),
        ("p", "Ask “does order matter?” before every count. Choosing a captain, vice-captain and secretary from 12 people is "
              "¹²P₃ = 1320 ways; choosing a committee of three is ¹²C₃ = 220 ways. Counting the divisors of a number combines "
              "the fundamental theorem with the multiplicative principle: a divisor of 2³ × 3² × 5 is 2ⁱ3ʲ5ᵏ with 4, 3 and 2 "
              "choices for i, j, k, so 360 has 4 × 3 × 2 = 24 positive divisors."),

        ("warn", "Common mistakes", [
            "Giving a negative remainder. In the division algorithm 0 ≤ r < b, so −45 = 7 × (−7) + 4, not 7 × (−6) − 3.",
            "Stopping Euclid's algorithm too early, or quoting the last divisor instead of the last <b>non-zero remainder</b>.",
            "Back substitution: losing track of which numbers are the originals. Keep the remainders in brackets until the "
            "last step, then collect, and always check the final identity numerically.",
            "Saying ‘coprime’ means ‘both prime’. 8 and 9 are coprime; 6 and 9 are not.",
            "Using Euclid's lemma for a composite divisor without checking coprimality.",
            "Base conversion: writing the remainders in the order found. The first remainder is the units digit.",
            "Counting: multiplying when the cases are alternatives (add), or using ⁿCᵣ when order matters (ⁿPᵣ). "
            "‘At least one’ is almost always total minus none.",
        ]),
        ("p", "<b>Given or learn.</b> No formula booklet gives these results. Learn the division algorithm, Bezout's identity, "
              "Euclid's lemma, the tests for your board and the formulae for ⁿPᵣ and ⁿCᵣ."),
    ],

    "examples": [
        {
            "title": "The division algorithm and number bases",
            "question": "(a) Find the quotient and remainder when 1000 and −1000 are divided by 37. (b) Write 1000 in base 2. "
                        "(c) Convert 4A3₁₂ to base 10 and then to base 7.",
            "steps": [
                "(a) 37 × 27 = 999, so 1000 = 37 × 27 + 1: q = 27, r = 1.",
                "For −1000 the remainder must satisfy 0 ≤ r < 37: −1000 = 37 × (−28) + 36, since 37 × (−28) = −1036. So q = −28, r = 36.",
                "(b) Repeated division by 2 gives remainders 0, 0, 0, 1, 0, 1, 1, 1, 1, 1 (1000, 500, 250, 125, 62, 31, 15, 7, 3, 1). "
                "Reading upwards, 1000 = 1111101000₂. Check: 512 + 256 + 128 + 64 + 32 + 8 = 1000.",
                "(c) 4A3₁₂ = 4 × 12² + 10 × 12 + 3 = 576 + 120 + 3 = 699.",
                "699 ÷ 7 = 99 r 6; 99 ÷ 7 = 14 r 1; 14 ÷ 7 = 2 r 0; 2 ÷ 7 = 0 r 2. So 699 = 2016₇. "
                "Check: 2 × 343 + 0 + 1 × 7 + 6 = 699.",
            ],
        },
        {
            "title": "Euclid's algorithm and Bezout's identity",
            "question": "(a) Use Euclid's algorithm to find hcf(1071, 462). (b) Hence find integers x and y with "
                        "1071x + 462y = hcf(1071, 462). (c) Explain whether 1071x + 462y = 50 has integer solutions, "
                        "and find one solution of 1071x + 462y = 105.",
            "steps": [
                "(a) 1071 = 2 × 462 + 147;   462 = 3 × 147 + 21;   147 = 7 × 21 + 0. The last non-zero remainder is 21, so hcf = 21.",
                "(b) From the second line, 21 = 462 − 3 × 147. From the first line, 147 = 1071 − 2 × 462.",
                "Substitute: 21 = 462 − 3(1071 − 2 × 462) = 462 + 6 × 462 − 3 × 1071 = 7 × 462 − 3 × 1071.",
                "So x = −3, y = 7. Check: 1071 × (−3) + 462 × 7 = −3213 + 3234 = 21.",
                "(c) 21 divides 1071x + 462y for all integers x, y, but 21 ∤ 50, so there are no integer solutions.",
                "105 = 5 × 21, so multiply the Bezout identity by 5: x = −15, y = 35. Check: −16 065 + 16 170 = 105.",
            ],
        },
        {
            "title": "Using linear combinations and Euclid's lemma",
            "question": "(a) Prove that hcf(3n + 1, 2n + 1) = 1 for every integer n. (b) Given that p is prime and p | n², "
                        "prove that p | n. Hence prove that p² | n².",
            "steps": [
                "(a) Let d = hcf(3n + 1, 2n + 1). Then d | (3n + 1) and d | (2n + 1), so d divides any combination of them.",
                "In particular d | 3(2n + 1) − 2(3n + 1) = 6n + 3 − 6n − 2 = 1.",
                "The only positive divisor of 1 is 1, so d = 1: 3n + 1 and 2n + 1 are always coprime.",
                "(b) n² = n × n and p | n × n. By Euclid's lemma (p prime), p | n or p | n; either way p | n.",
                "So n = kp for some integer k, and n² = k²p², which shows p² | n².",
                "Note: this is false for composite numbers in general, e.g. 4 | 6² = 36 but 4 ∤ 6.",
            ],
        },
        {
            "title": "Divisibility tests",
            "question": "Without dividing, determine which of 2, 3, 4, 5, 6, 8, 9, 11 divide N = 2 852 136. Then use 1001 = 7 × 11 × 13 "
                        "to decide whether 7 and 13 divide N.",
            "steps": [
                "Last digit 6 is even: 2 | N. Last digit is not 0 or 5: 5 ∤ N.",
                "Last two digits 36 = 4 × 9: 4 | N. Last three digits 136 = 8 × 17: 8 | N.",
                "Digit sum 2 + 8 + 5 + 2 + 1 + 3 + 6 = 27, divisible by 9 (and so by 3): 9 | N and 3 | N. As 2 | N and 3 | N, 6 | N.",
                "Alternating sum from the units digit: 6 − 3 + 1 − 2 + 5 − 8 + 2 = 1, not divisible by 11, so 11 ∤ N (N ≡ 1 mod 11).",
                "Blocks of three from the right: 136, 852, 2. Since 1000 ≡ −1 (mod 1001), N ≡ 136 − 852 + 2 = −714 (mod 1001), "
                "so N has the same remainder as −714 on division by 7, 11 or 13.",
                "−714 = −7 × 102, so 7 | N. −714 = 13 × (−55) + 1, so 13 ∤ N (remainder 1).",
                "Check with the a − 2b test for 7: 285213 − 12 = 285201 → 28520 − 2 = 28518 → 2851 − 16 = 2835 → 283 − 10 = 273 "
                "→ 27 − 6 = 21 = 3 × 7.",
            ],
        },
        {
            "title": "Prime factorisation, divisors, hcf and lcm",
            "question": "(a) Write 360 and 756 as products of primes. Hence find hcf(360, 756) and lcm(360, 756). "
                        "(b) How many positive divisors does 360 have? How many of them are even, and how many are perfect squares?",
            "steps": [
                "(a) 360 = 2³ × 3² × 5 and 756 = 2² × 3³ × 7.",
                "hcf: lower power of each prime: 2² × 3² = 36. lcm: higher power of each: 2³ × 3³ × 5 × 7 = 7560.",
                "Check: hcf × lcm = 36 × 7560 = 272 160 = 360 × 756.",
                "(b) By the fundamental theorem every positive divisor is 2ⁱ3ʲ5ᵏ with 0 ≤ i ≤ 3, 0 ≤ j ≤ 2, 0 ≤ k ≤ 1. "
                "By the multiplicative principle there are 4 × 3 × 2 = 24 divisors.",
                "Even divisors need i ≥ 1: 3 × 3 × 2 = 18 (or by subtraction, 24 − 6 odd divisors).",
                "Perfect squares need even exponents: i ∈ {0, 2}, j ∈ {0, 2}, k = 0: 2 × 2 × 1 = 4 (namely 1, 4, 9, 36).",
            ],
        },
        {
            "title": "Counting with the three principles (Edexcel)",
            "question": "(a) How many four-digit numbers (1000 to 9999) have four different digits? (b) How many four-digit "
                        "numbers contain at least one digit 7? (c) A team of 4 is chosen from 6 women and 5 men. How many "
                        "teams contain at least one man? (d) How many teams contain exactly 3 women or exactly 3 men?",
            "steps": [
                "(a) First digit: 9 choices (not 0). Then 9, 8, 7 choices for the rest (0 is now allowed, repeats are not). "
                "Multiplicative principle: 9 × 9 × 8 × 7 = 4536.",
                "(b) Subtraction principle. Total four-digit numbers: 9000. With no 7: first digit 8 choices (not 0 or 7), others 9 each: "
                "8 × 9³ = 5832. At least one 7: 9000 − 5832 = 3168.",
                "(c) Order does not matter. All teams: ¹¹C₄ = 330. Teams with no man: ⁶C₄ = 15. At least one man: 330 − 15 = 315.",
                "(d) The two cases are disjoint, so add. 3 women and 1 man: ⁶C₃ × ⁵C₁ = 20 × 5 = 100. "
                "3 men and 1 woman: ⁵C₃ × ⁶C₁ = 10 × 6 = 60. Total 160.",
            ],
        },
    ],

    "practice": [
        "Find the quotient q and remainder r, with 0 ≤ r < b, when a is divided by b: (a) a = 500, b = 17 (b) a = −45, b = 7.",
        "(a) Write 2520 and 3003 as products of primes. (b) Hence find hcf(2520, 3003) and lcm(2520, 3003).",
        "Use Euclid's algorithm to find hcf(2024, 1748). Are 2024 and 1748 coprime? Find lcm(2024, 1748).",
        "Use Euclid's algorithm and back substitution to find integers x and y with 43x + 17y = 1.",
        "(a) Find hcf(252, 198) using Euclid's algorithm. (b) Express it in the form 252x + 198y. "
        "(c) Explain why 252x + 198y = 100 has no integer solutions.",
        "(OCR A) (a) Write 345 in base 5. (b) Convert 101101₂ to base 10. (c) Convert 2B7₁₂ to base 10.",
        "(OCR A) Work in the given base, then check by converting to base 10: (a) 1011₂ + 111₂ (b) 34₅ × 23₅.",
        "Without dividing, decide whether 7 380 916 is divisible by (a) 4 (b) 8 (c) 9 (d) 11. Where it is not divisible "
        "by 9 or 11, state the remainder.",
        "(OCR A) (a) Show that 37 | 999. (b) Hence explain why a number is divisible by 37 if and only if the sum of its "
        "3-digit blocks (from the right) is divisible by 37. (c) Use the test on 4 567 317.",
        "(a) Prove that if a | b and a | c then a | (bx + cy) for all integers x, y. (b) Hence prove that 5n + 3 and 7n + 4 "
        "are coprime for every integer n.",
        "(Edexcel) (a) How many arrangements of 3 different letters can be made from A, B, C, D, E, F, G, H? "
        "(b) How many subsets does {A, B, …, H} have? (c) How many of these subsets have exactly 3 elements?",
        "(Edexcel) A code is 2 letters (A–Z) followed by 3 digits (0–9). (a) How many codes are there? (b) How many codes "
        "have at least one repeated digit? (c) How many positive divisors does 1800 have?",
    ],
    "answers": [
        "(a) 500 = 17 × 29 + 7: q = 29, r = 7. (b) −45 = 7 × (−7) + 4: q = −7, r = 4.",
        "(a) 2520 = 2³ × 3² × 5 × 7; 3003 = 3 × 7 × 11 × 13. (b) hcf = 3 × 7 = 21; lcm = 2³ × 3² × 5 × 7 × 11 × 13 = 360 360.",
        "2024 = 1 × 1748 + 276; 1748 = 6 × 276 + 92; 276 = 3 × 92 + 0. hcf = 92, so not coprime. lcm = 2024 × 1748 ÷ 92 = 38 456.",
        "43 = 2 × 17 + 9; 17 = 1 × 9 + 8; 9 = 1 × 8 + 1. 1 = 9 − 8 = 9 − (17 − 9) = 2 × 9 − 17 = 2(43 − 2 × 17) − 17 = "
        "2 × 43 − 5 × 17. x = 2, y = −5 (check 86 − 85 = 1).",
        "(a) 252 = 1 × 198 + 54; 198 = 3 × 54 + 36; 54 = 1 × 36 + 18; 36 = 2 × 18. hcf = 18. "
        "(b) 18 = 54 − 36 = 54 − (198 − 3 × 54) = 4 × 54 − 198 = 4(252 − 198) − 198 = 4 × 252 − 5 × 198. "
        "(c) 18 divides the left side for all integers x, y but 18 ∤ 100.",
        "(a) 345 = 2 × 125 + 3 × 25 + 4 × 5 + 0 = 2340₅. (b) 32 + 8 + 4 + 1 = 45. (c) 2 × 144 + 11 × 12 + 7 = 427.",
        "(a) 1011₂ + 111₂ = 10010₂ (11 + 7 = 18). (b) 34₅ × 23₅ = 1442₅ (19 × 13 = 247 = 125 + 4 × 25 + 4 × 5 + 2).",
        "(a) Last two digits 16 = 4 × 4: yes. (b) Last three digits 916 = 8 × 114 + 4: no. (c) Digit sum 34 = 9 × 3 + 7: "
        "no, remainder 7. (d) Alternating sum 6 − 1 + 9 − 0 + 8 − 3 + 7 = 26 = 2 × 11 + 4: no, remainder 4.",
        "(a) 999 = 27 × 37. (b) 1000 = 999 + 1 ≡ 1 (mod 37), so 1000ᵏ ≡ 1 and N = B₀ + 1000B₁ + 1000²B₂ + … ≡ B₀ + B₁ + B₂ + … "
        "(mod 37), where Bᵢ are the blocks. (c) 4 + 567 + 317 = 888 = 24 × 37, so 37 | 4 567 317.",
        "(a) b = ma, c = na, so bx + cy = a(mx + ny), a multiple of a. (b) If d divides both then d | 7(5n + 3) − 5(7n + 4) = 1, so d = 1.",
        "(a) ⁸P₃ = 8 × 7 × 6 = 336. (b) 2⁸ = 256. (c) ⁸C₃ = 56.",
        "(a) 26² × 10³ = 676 000. (b) No repeated digit: 26² × 10 × 9 × 8 = 486 720; so 676 000 − 486 720 = 189 280. "
        "(c) 1800 = 2³ × 3² × 5², so (3 + 1)(2 + 1)(2 + 1) = 36 divisors.",
    ],

    "exam": [
        "(a) Use Euclid's algorithm to find the highest common factor of 1001 and 357. [3]\n"
        "(b) Hence find integers x and y such that 1001x + 357y = hcf(1001, 357). [3]\n"
        "(c) Explain why there are no integers x and y with 1001x + 357y = 10. [2]\n"
        "(d) Find integers x and y with 1001x + 357y = 21. [1]\n"
        "(e) Find lcm(1001, 357). [2]",
        "(OCR A) (a) Show that 1001 = 7 × 11 × 13 and deduce that 10³ ≡ −1 (mod 7), (mod 11) and (mod 13). [2]\n"
        "(b) A positive integer N is written in 3-digit blocks from the right as N = B₀ + 10³B₁ + 10⁶B₂ + …, with "
        "0 ≤ Bᵢ ≤ 999. Prove that N ≡ B₀ − B₁ + B₂ − … (mod 7). [3]\n"
        "(c) Hence find the remainders when 6 342 715 is divided by 7, 11 and 13. [3]\n"
        "(d) Prove that an integer is divisible by 9 if and only if the sum of its digits is divisible by 9. [3]",
        "(a) State Bezout's identity. [1]\n"
        "(b) Prove that if p is prime, p | ab and p ∤ a, then p | b. [4]\n"
        "(c) Give an example to show that the result in (b) can fail when p is not prime. [1]\n"
        "(d) Use the fundamental theorem of arithmetic to prove that log₂3 is irrational. [4]",
        "(Edexcel) A club has 7 boys and 5 girls.\n"
        "(a) In how many ways can a captain, a vice-captain and a secretary be chosen, if no person holds two posts? [2]\n"
        "(b) How many committees of 4 members contain at least one girl? [3]\n"
        "(c) How many committees of 4 contain exactly 2 boys or exactly 3 boys? [3]\n"
        "(d) At a meeting any subset of the 12 members may attend. How many possible sets of attendees contain at least "
        "2 members? [3]",
    ],
    "exam_answers": [
        "(a) 1001 = 2 × 357 + 287 M1; 357 = 1 × 287 + 70; 287 = 4 × 70 + 7; 70 = 10 × 7 + 0 M1; hcf = 7 A1. "
        "(b) 7 = 287 − 4 × 70 = 287 − 4(357 − 287) = 5 × 287 − 4 × 357 M1 = 5(1001 − 2 × 357) − 4 × 357 = 5 × 1001 − 14 × 357 M1; "
        "x = 5, y = −14 A1 (check 5005 − 4998 = 7). (c) 7 | 1001x + 357y for all integers x, y M1, but 7 ∤ 10 A1. "
        "(d) Multiply by 3: x = 15, y = −42 B1. (e) lcm = 1001 × 357 ÷ 7 M1 = 51 051 A1.",
        "(a) 7 × 11 × 13 = 1001 B1, so 10³ = 1001 − 1 ≡ −1 modulo each of 7, 11, 13 B1. "
        "(b) 10³ ≡ −1 (mod 7) so 10³ᵏ = (10³)ᵏ ≡ (−1)ᵏ M1 (power law); N = ΣBₖ10³ᵏ ≡ ΣBₖ(−1)ᵏ M1 (multiplication and addition "
        "laws) = B₀ − B₁ + B₂ − … A1. "
        "(c) 715 − 342 + 6 = 379 M1. 379 = 7 × 54 + 1, 11 × 34 + 5, 13 × 29 + 2, so remainders 1, 5, 2 A1 A1. "
        "(d) 10 ≡ 1 (mod 9) so 10ʲ ≡ 1 M1; N = Σdⱼ10ʲ ≡ Σdⱼ (mod 9) A1; so 9 | N ⇔ 9 | Σdⱼ (both directions, since N − Σdⱼ "
        "is a multiple of 9) A1.",
        "(a) For integers a, b not both zero there exist integers x, y with ax + by = hcf(a, b) B1. "
        "(b) p prime and p ∤ a so hcf(a, p) = 1 M1 A1; ax + py = 1 for some integers x, y; multiply by b: abx + pby = b M1; "
        "p | ab and p | pb, so p | b A1. "
        "(c) e.g. 6 | 4 × 3 = 12 but 6 ∤ 4 and 6 ∤ 3 B1. "
        "(d) Suppose log₂3 = m/n with m, n positive integers (log₂3 > 0) M1. Then 2^(m/n) = 3, so 2ᵐ = 3ⁿ M1. "
        "The left side is even and has prime factorisation containing only 2; the right side contains only 3 M1; this "
        "contradicts uniqueness of prime factorisation (or: one side even, the other odd), so log₂3 is irrational A1.",
        "(a) ¹²P₃ M1 = 12 × 11 × 10 = 1320 A1. "
        "(b) ¹²C₄ − ⁷C₄ M1 = 495 − 35 M1 = 460 A1. "
        "(c) ⁷C₂ × ⁵C₂ + ⁷C₃ × ⁵C₁ M1 (add disjoint cases) = 21 × 10 + 35 × 5 M1 = 210 + 175 = 385 A1. "
        "(d) 2¹² subsets B1; subtract the empty set and the 12 single members M1: 4096 − 1 − 12 = 4083 A1.",
    ],
}
