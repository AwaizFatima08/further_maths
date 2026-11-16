UNIT = {
    "number": "AS4",
    "title": "Permutations and combinations",
    "tag": "AS · OCR A (5.01a–b) · prior knowledge for CAIE 9231 Paper 4 (9709 S1) · useful background for every board "
           "(binomial coefficients, negative binomial, hypergeometric-type probabilities)",
    "notes": [
        ("p", "Many probability questions reduce to counting: if all outcomes are equally likely, then "
              "P(event) = (number of outcomes in the event)/(total number of outcomes). This unit gives systematic ways to count "
              "arrangements (where order matters) and selections (where it does not), with repeated objects and restrictions. "
              "OCR A examines it directly; for other boards it explains where the binomial coefficients come from."),

        ("h2", "4.1 The counting principle and factorials"),
        ("p", "<b>Multiplication rule.</b> If one choice can be made in m ways and, for each of these, a second choice can be made in "
              "n ways, the two choices together can be made in m × n ways. <b>Addition rule.</b> If the outcomes split into separate "
              "cases that cannot happen together, add the counts for the cases."),
        ("p", "The number of ways to arrange n different objects in a line is n × (n − 1) × … × 2 × 1 = n! (n factorial): n choices "
              "for the first position, n − 1 for the second, and so on. By definition 0! = 1, which makes the formulas below work "
              "when r = 0 or r = n."),

        ("h2", "4.2 Permutations: arranging r objects from n"),
        ("p", "A <b>permutation</b> is an ordered arrangement. The number of ways to choose and arrange r objects from n different "
              "objects is"),
        ("box", "Permutations and combinations", [
            "ⁿPᵣ = n!/(n − r)! = n(n − 1)…(n − r + 1)   — order matters (arrangements)",
            "ⁿCᵣ = C(n, r) = n!/(r!(n − r)!) = ⁿPᵣ/r!   — order does not matter (selections)",
            "Each selection of r objects can be arranged in r! ways, which is why ⁿPᵣ = r! × ⁿCᵣ.",
            "ⁿCᵣ = ⁿCₙ₋ᵣ: choosing r to take is the same as choosing n − r to leave.",
        ]),
        ("p", "Example: the number of 3-letter codes using different letters from A to H is ⁸P₃ = 8 × 7 × 6 = 336; the number of "
              "3-person teams from 8 people is ⁸C₃ = 336/3! = 56."),

        ("h2", "4.3 Arrangements with repeated objects"),
        ("p", "If some objects are identical, swapping them gives the same arrangement, so dividing by the number of ways of "
              "permuting each identical group removes the double counting."),
        ("box", "Repeated objects", [
            "n objects, of which p are alike of one kind, q alike of another kind, …: number of arrangements = n!/(p! q! …).",
            "Example: STRAIT has 6 letters with T twice: 6!/2! = 360 arrangements. ARTIST uses the same letters, so it is one of these 360.",
        ]),

        ("h2", "4.4 Arrangements with restrictions"),
        ("bullets", [
            "<b>Fixed positions:</b> fill the restricted positions first, then arrange the rest. E.g. the number of arrangements of "
            "STRAIT beginning with a vowel: 2 choices for the first letter, then 5!/2! = 60 for the rest, giving 120.",
            "<b>Objects together:</b> glue them into one block. Arrange the block with the other objects, then multiply by the number "
            "of arrangements inside the block.",
            "<b>Objects apart (no two adjacent):</b> arrange the other objects first, then place the restricted objects in the gaps "
            "between and at the ends (k objects in a line create k + 1 gaps).",
            "<b>Two objects not together:</b> it is often quickest to use total − (arrangements with them together).",
        ]),
        ("p", "OCR A's specification uses examples such as arranging TRAITS so that the consonants are, or are not, adjacent. "
              "TRAITS has consonants T, R, T, S and vowels A, I, with T repeated. All 4 consonants together: arrange the block of "
              "consonants internally in 4!/2! = 12 ways, then arrange block, A, I in 3! = 6 ways, giving 72. OCR A arrangements are "
              "in a line only; circular arrangements (section 4.7) are an extension."),

        ("h2", "4.5 Selections"),
        ("p", "ⁿCᵣ counts the ways to choose r objects from n different objects when order does not matter, for example a committee, "
              "a hand of cards or a sample of items. Selections from groups use the multiplication rule: choosing 2 women from 6 "
              "and 3 men from 8 gives ⁶C₂ × ⁸C₃ = 15 × 56 = 840 committees."),
        ("p", "'At least one' problems are usually easiest by the complement: number with at least one = total − number with none. "
              "Avoid counting 'choose one woman, then choose the rest freely', which counts the same committee several times."),

        ("h2", "4.6 Probability by counting"),
        ("p", "When an arrangement or selection is made <b>at random</b>, every arrangement or selection is equally likely, so"),
        ("box", "Equally likely outcomes", [
            "P(event) = (number of arrangements or selections in the event)/(total number of arrangements or selections).",
            "Count the numerator and denominator in the same way: both ordered, or both unordered.",
            "Treat identical-looking tiles as different objects (label them) when selecting at random: each tile is equally likely.",
        ]),
        ("p", "For example (OCR A 5.01b), 5 of the 10 letter tiles of CALCULATOR are chosen at random. There are 4 vowel tiles "
              "(A, U, A, O) and 6 consonant tiles. P(3 vowels and 2 consonants) = ⁴C₃ × ⁶C₂/¹⁰C₅ = 4 × 15/252 = 5/21. "
              "Selecting 'without replacement' like this gives probabilities that are not binomial; the binomial is the 'with "
              "replacement' version."),

        ("h2", "4.7 Links with distributions, and circular arrangements"),
        ("bullets", [
            "<b>Binomial coefficients.</b> In n trials, the number of different sequences with exactly x successes is C(n, x): choose "
            "which x of the n positions are successes. Each sequence has probability pˣ(1 − p)ⁿ⁻ˣ, giving the binomial formula.",
            "<b>Negative binomial (A2.3).</b> For the r-th success on trial x, the last trial is a success and the other r − 1 "
            "successes go in any of the first x − 1 positions: C(x − 1, r − 1) ways.",
            "<b>Pascal's rule.</b> C(n, r) + C(n, r + 1) = C(n + 1, r + 1), the addition in Pascal's triangle.",
            "<b>Circular arrangements (extension; not OCR A or CAIE).</b> n different people round a circular table, where only "
            "relative positions matter, can be seated in (n − 1)! ways: fix one person, then arrange the rest.",
        ]),
        ("table", ["Situation", "Order matters?", "Count"], [
            ["Arrange all n different objects in a line", "yes", "n!"],
            ["Arrange r of n different objects", "yes", "ⁿPᵣ = n!/(n − r)!"],
            ["Arrange n objects with p alike, q alike, …", "yes", "n!/(p! q! …)"],
            ["Choose r of n different objects", "no", "ⁿCᵣ = n!/(r!(n − r)!)"],
            ["k objects together (block) among n in a line", "yes", "(n − k + 1)! × k!"],
            ["n different objects round a table (extension)", "relative order", "(n − 1)!"],
        ]),
        ("warn", "Common mistakes", [
            "Using ⁿPᵣ when order does not matter (committees, hands of cards), or ⁿCᵣ for arrangements.",
            "Forgetting to divide by p! for repeated letters, or dividing when the objects are actually different.",
            "Gluing objects into a block and forgetting to arrange the objects inside the block.",
            "'At least one' by choosing one first and then any others: this double counts. Use total − none.",
            "Mixing ordered and unordered counts in the numerator and denominator of a probability.",
            "For 'not adjacent', subtracting only one case when three or more objects must be separated; use the gaps method.",
        ]),
    ],
    "examples": [
        {
            "title": "Repeated letters and a fixed position",
            "question": "Find the number of different arrangements of the letters of STATISTICS. Find the probability that a random "
                        "arrangement begins and ends with S.",
            "steps": [
                "10 letters: S three times, T three times, I twice, A and C once each.",
                "Number of arrangements = 10!/(3! 3! 2!) = 3628800/72 = 50400.",
                "Put S at each end. The remaining 8 letters are S, T, T, T, I, I, A, C: 8!/(3! 2!) = 3360 arrangements.",
                "P(begins and ends with S) = 3360/50400 = 1/15 ≈ 0.0667.",
            ],
        },
        {
            "title": "Together and apart (OCR A style)",
            "question": "The letters of TRAITS are arranged in a line. (a) How many arrangements are there? (b) Find the probability "
                        "that the four consonants are all together. (c) Find the number of arrangements in which the two vowels are "
                        "not next to each other.",
            "steps": [
                "(a) 6 letters with T twice: 6!/2! = 360.",
                "(b) Block of consonants T, R, T, S: 4!/2! = 12 internal orders. Arrange block, A, I: 3! = 6. Total 72. "
                "Probability = 72/360 = 0.2.",
                "(c) Gaps method: arrange the consonants T, R, T, S in 4!/2! = 12 ways; this creates 5 gaps. Place A and I in "
                "different gaps in ⁵P₂ = 20 ways. Total 12 × 20 = 240.",
                "Check: vowels together = 2 (AI or IA) × 5!/2! = 120, and 360 − 120 = 240.",
            ],
        },
        {
            "title": "Selections with 'at least'",
            "question": "A committee of 5 is chosen at random from 6 men and 4 women. Find the probability that it contains at least 2 women.",
            "steps": [
                "Total number of committees: ¹⁰C₅ = 252.",
                "Complement: 0 women: ⁶C₅ = 6; exactly 1 woman: ⁴C₁ × ⁶C₄ = 4 × 15 = 60.",
                "P(at least 2 women) = 1 − (6 + 60)/252 = 186/252 = 31/42 ≈ 0.738 (3 s.f.).",
            ],
        },
        {
            "title": "Choosing letter tiles (OCR A 5.01b)",
            "question": "The 10 letters of CALCULATOR are written on tiles. 5 tiles are chosen at random. Find the probability that "
                        "exactly 3 vowels and 2 consonants are chosen.",
            "steps": [
                "Vowel tiles: A, U, A, O (4). Consonant tiles: C, L, C, L, T, R (6). Treat the tiles as different.",
                "Number of ways: ⁴C₃ × ⁶C₂ = 4 × 15 = 60. Total: ¹⁰C₅ = 252.",
                "P = 60/252 = 5/21 ≈ 0.238 (3 s.f.).",
            ],
        },
        {
            "title": "People in a row with two restrictions",
            "question": "Eight people, including Ali, Ben and Cara, sit in a row of 8 seats. In how many ways can they sit if Cara must "
                        "sit at one end and Ali and Ben must not sit next to each other? If the seating is random, find the "
                        "probability that both conditions hold.",
            "steps": [
                "Cara at an end: 2 choices; the other 7 people fill 7 seats in 7! = 5040 ways. Total 2 × 5040 = 10080.",
                "Of these, Ali and Ben together: Cara at an end (2), block AB or BA (2), arrange the block and 5 others in the 7 seats: 6! = 720. Total 2 × 2 × 720 = 2880.",
                "Required number = 10080 − 2880 = 7200.",
                "Probability = 7200/8! = 7200/40320 = 5/28 ≈ 0.179 (3 s.f.).",
            ],
        },
        {
            "title": "Links: binomial coefficients and a circular table",
            "question": "(a) Explain why P(X = 3) = C(10, 3)(0.2)³(0.8)⁷ when X ~ B(10, 0.2), and evaluate it. (b) (Extension) Six "
                        "people sit at random round a circular table. Find the probability that two particular people sit next to each other.",
            "steps": [
                "(a) Any one sequence of 3 successes and 7 failures has probability 0.2³ × 0.8⁷. The number of such sequences is the "
                "number of ways to choose the 3 success positions from 10: C(10, 3) = 120. So P(X = 3) = 120 × 0.2³ × 0.8⁷ = 0.201 (3 s.f.).",
                "(b) Round a table there are (6 − 1)! = 120 arrangements. Treat the pair as a block (2 internal orders): 5 units "
                "round the table give 4! = 24, so 48 arrangements. P = 48/120 = 0.4.",
            ],
        },
    ],
    "practice": [
        "Evaluate ⁷P₃ and ⁹C₄, and find the number of ways to arrange 5 different books on a shelf.",
        "Find the number of arrangements of the letters of BANANA. Find the probability that a random arrangement begins with B.",
        "Four-digit numbers are made from the digits 1 to 7, with no digit repeated. How many can be made? How many are even? "
        "Find the probability that a random such number is even.",
        "A team of 4 is chosen at random from 7 boys and 5 girls. Find the number of possible teams and the probability that the "
        "team has exactly 2 girls.",
        "The letters of STRAIT are arranged at random. Find the probability that the arrangement (a) spells ARTIST, (b) begins with a vowel.",
        "Seven people stand in a line. Find the probability, for a random order, that three particular people are all next to each other.",
        "Seven people stand in a line. Find the probability, for a random order, that no two of three particular people are next to each other.",
        "A bag contains 5 red, 4 blue and 3 green counters. Three are taken at random without replacement. Find the probability that "
        "(a) all three are the same colour, (b) there is one of each colour.",
        "Solve ⁿC₂ = 45. Verify Pascal's rule C(6, 2) + C(6, 3) = C(7, 3).",
        "Find the number of arrangements of the letters of PARALLEL. Find the probability that a random arrangement has the three L's together.",
        "In a lottery, 6 numbers are chosen at random from 1 to 49. A player picks 6 numbers. Find the probability that exactly 3 of "
        "the player's numbers are chosen, giving your answer to 3 significant figures.",
        "(Extension) Eight people sit at random round a circular table. Find the number of different arrangements and the probability "
        "that two particular people sit next to each other.",
    ],
    "answers": [
        "⁷P₃ = 7 × 6 × 5 = 210. ⁹C₄ = 126. 5! = 120.",
        "6!/(3! 2!) = 60. Beginning with B: arrange AAANN in 5!/(3! 2!) = 10 ways. P = 10/60 = 1/6.",
        "⁷P₄ = 840. Even: last digit 2, 4 or 6 (3 ways), then ⁶P₃ = 120 for the rest: 360. P = 360/840 = 3/7.",
        "¹²C₄ = 495. Exactly 2 girls: ⁵C₂ × ⁷C₂ = 10 × 21 = 210. P = 210/495 = 14/33 ≈ 0.424.",
        "There are 6!/2! = 360 arrangements. (a) 1/360. (b) 2 × 5!/2! = 120, so P = 120/360 = 1/3.",
        "Block of 3 (3! orders) with 4 others: 5! × 3! = 720. P = 720/7! = 720/5040 = 1/7.",
        "Arrange the other 4 people (4! = 24), then place the 3 in different gaps out of 5: ⁵P₃ = 60. 24 × 60 = 1440. P = 1440/5040 = 2/7.",
        "Total ¹²C₃ = 220. (a) (⁵C₃ + ⁴C₃ + ³C₃)/220 = (10 + 4 + 1)/220 = 3/44 ≈ 0.0682. (b) 5 × 4 × 3/220 = 60/220 = 3/11 ≈ 0.273.",
        "n(n − 1)/2 = 45 gives n² − n − 90 = 0, (n − 10)(n + 9) = 0, so n = 10. C(6, 2) + C(6, 3) = 15 + 20 = 35 = C(7, 3).",
        "8 letters: A twice, L three times: 8!/(2! 3!) = 3360. LLL as a block with P, A, R, A, E: 6!/2! = 360. P = 360/3360 = 3/28 ≈ 0.107.",
        "Total ⁴⁹C₆ = 13983816. Exactly 3: ⁶C₃ × ⁴³C₃ = 20 × 12341 = 246820. P = 246820/13983816 ≈ 0.0177.",
        "(8 − 1)! = 5040 arrangements. Pair as a block: 2 × 6! = 1440. P = 1440/5040 = 2/7.",
    ],
    "exam": [
        "The letters of ARRANGE are written on 7 tiles. (a) Find the number of different arrangements of the 7 letters in a line. [2]  "
        "(b) Find the number of these arrangements that begin and end with R. [2]  (c) Find the number of arrangements in which the two "
        "A's are next to each other. [2]  (d) The letters are arranged at random. Find the probability that the two A's are not next to "
        "each other. [2]  (e) Four of the 7 tiles are chosen at random. Find the probability that both R tiles are chosen. [3]",
        "A club has 8 male and 6 female members. A committee of 5 is chosen at random. (a) Find the number of possible committees. [1]  "
        "(b) Find the probability that the committee has exactly 3 women. [3]  (c) Find the probability that it has at least one woman. [2]  "
        "(d) Mr and Mrs Khan are both members. Find the probability that exactly one of them is on the committee. [3]  "
        "(e) X is the number of women on the committee. Given P(X = 0) = 28/1001, P(X = 1) = 210/1001, P(X = 2) = 420/1001, "
        "P(X = 3) = 280/1001, P(X = 4) = 60/1001, find P(X = 5) and E(X). [3]",
        "Four boys and three girls stand in a row for a photograph. (a) Find the number of arrangements in which the three girls stand "
        "together. [2]  (b) Find the number of arrangements in which no two girls stand next to each other. [3]  (c) Find the number "
        "of arrangements in which boys and girls alternate. [2]  (d) The seven stand in a random order. Find the probability that a boy "
        "stands at each end. [3]",
        "A box contains 10 batteries, of which 3 are flat. Four batteries are chosen at random without replacement. X is the number of "
        "flat batteries chosen. (a) Show that P(X = 1) = 1/2. [2]  (b) Find the rest of the probability distribution of X. [3]  "
        "(c) Find E(X) and Var(X). [4]  (d) If the batteries were chosen with replacement, X would have a binomial distribution. Find "
        "P(X = 1) in that case, and explain why it differs from (a). [2]",
    ],
    "exam_answers": [
        "(a) 7 letters with A twice, R twice: 7!/(2! 2!) (M1) = 1260 (A1).  (b) Remaining A, A, N, G, E: 5!/2! (M1) = 60 (A1).  "
        "(c) Block AA with R, R, N, G, E: 6!/2! (M1) = 360 (A1).  (d) 1 − 360/1260 (M1) = 5/7 ≈ 0.714 (A1).  "
        "(e) Both R's plus 2 of the other 5 tiles: ⁵C₂ = 10 (M1); total ⁷C₄ = 35 (M1); P = 10/35 = 2/7 ≈ 0.286 (A1).",
        "(a) ¹⁴C₅ = 2002 (B1).  (b) ⁶C₃ × ⁸C₂ = 20 × 28 = 560 (M1 A1); P = 560/2002 = 40/143 ≈ 0.280 (A1).  "
        "(c) No women: ⁸C₅ = 56 (M1); P = 1 − 56/2002 = 139/143 ≈ 0.972 (A1).  (d) Exactly one: 2 × ¹²C₄ = 2 × 495 = 990 (M1 A1); "
        "P = 990/2002 = 45/91 ≈ 0.495 (A1).  (e) P(X = 5) = ⁶C₅/2002 = 6/2002 = 3/1001 (B1). E(X) = (210 + 840 + 840 + 240 + 15)/1001 "
        "(M1) = 2145/1001 = 15/7 ≈ 2.14 (A1).",
        "(a) Block of girls (3! orders) with 4 boys: 5! × 3! (M1) = 720 (A1).  (b) Arrange boys 4! = 24 (M1); girls into 5 gaps: ⁵P₃ = 60 (M1); "
        "1440 (A1).  (c) B G B G B G B: 4! × 3! (M1) = 144 (A1).  (d) Ends: 4 × 3 = 12 ordered choices of boys (M1); middle 5! = 120 (M1); "
        "P = 1440/5040 = 2/7 ≈ 0.286 (A1).",
        "(a) ³C₁ × ⁷C₃/¹⁰C₄ (M1) = 3 × 35/210 = 1/2 (A1).  (b) P(X = 0) = ⁷C₄/210 = 35/210 = 1/6 (B1); P(X = 2) = ³C₂ × ⁷C₂/210 = 63/210 = 0.3 "
        "(B1); P(X = 3) = ⁷C₁/210 = 7/210 = 1/30 (B1).  (c) E(X) = 0.5 + 0.6 + 0.1 = 1.2 (M1 A1). E(X²) = 0.5 + 1.2 + 0.3 = 2 (M1); "
        "Var(X) = 2 − 1.44 = 0.56 (A1).  (d) B(4, 0.3): P(X = 1) = 4 × 0.3 × 0.7³ = 0.4116 (B1). Without replacement the probability "
        "of a flat battery changes after each draw, so the trials are not independent (B1).",
    ],
}
