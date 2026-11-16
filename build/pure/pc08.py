"""Unit C8: Groups II: structure and isomorphism
(Edexcel FP2 1.5; OCR A Y535/Y545 8.03i, 8.03j, 8.03l, 8.03m; OCR MEI Y435 Xa7, Xa8)."""

# Cayley tables printed in this unit (row x, column y holds x ∗ y; for symmetries x ∘ y = do y, then x).
# The check script verifies each one by brute force.
U7 = (["1", "3", "2", "6", "4", "5"], [  # multiplication modulo 7, listed as powers of 3
    ["1", "3", "2", "6", "4", "5"],
    ["3", "2", "6", "4", "5", "1"],
    ["2", "6", "4", "5", "1", "3"],
    ["6", "4", "5", "1", "3", "2"],
    ["4", "5", "1", "3", "2", "6"],
    ["5", "1", "3", "2", "6", "4"],
])
F6 = (["f₁", "f₂", "f₃", "f₄", "f₅", "f₆"], [  # composition of the six functions defined in 8.1
    ["f₁", "f₂", "f₃", "f₄", "f₅", "f₆"],
    ["f₂", "f₁", "f₄", "f₃", "f₆", "f₅"],
    ["f₃", "f₅", "f₁", "f₆", "f₂", "f₄"],
    ["f₄", "f₆", "f₂", "f₅", "f₁", "f₃"],
    ["f₅", "f₃", "f₆", "f₁", "f₄", "f₂"],
    ["f₆", "f₄", "f₅", "f₂", "f₃", "f₁"],
])
D4 = (["e", "r", "r²", "r³", "H", "V", "D₁", "D₂"], [
    ["e", "r", "r²", "r³", "H", "V", "D₁", "D₂"],
    ["r", "r²", "r³", "e", "D₁", "D₂", "V", "H"],
    ["r²", "r³", "e", "r", "V", "H", "D₂", "D₁"],
    ["r³", "e", "r", "r²", "D₂", "D₁", "H", "V"],
    ["H", "D₂", "V", "D₁", "e", "r²", "r³", "r"],
    ["V", "D₁", "H", "D₂", "r²", "e", "r", "r³"],
    ["D₁", "H", "D₂", "V", "r", "r³", "e", "r²"],
    ["D₂", "V", "D₁", "H", "r³", "r", "r²", "e"],
])
Q8 = (["1", "−1", "i", "−i", "j", "−j", "k", "−k"], [
    ["1", "−1", "i", "−i", "j", "−j", "k", "−k"],
    ["−1", "1", "−i", "i", "−j", "j", "−k", "k"],
    ["i", "−i", "−1", "1", "k", "−k", "−j", "j"],
    ["−i", "i", "1", "−1", "−k", "k", "j", "−j"],
    ["j", "−j", "−k", "k", "−1", "1", "i", "−i"],
    ["−j", "j", "k", "−k", "1", "−1", "−i", "i"],
    ["k", "−k", "j", "−j", "−i", "i", "−1", "1"],
    ["−k", "k", "−j", "j", "i", "−i", "1", "−1"],
])

# The isomorphism D₃ → F (Example C8.3), checked on all 36 products.
D3_TO_F6 = {"e": "f₁", "r": "f₄", "r²": "f₅", "a": "f₂", "b": "f₃", "c": "f₆"}


def cayley(op, table):
    els, rows = table
    return ("table", [op] + els, [[f"<b>{a}</b>"] + list(r) for a, r in zip(els, rows)])


UNIT = {
    "number": "C8",
    "title": "Groups II: structure and isomorphism",
    "tag": "Option · Edexcel FP2 1.5 (A level only) · OCR A Additional Pure 8.03i (AS Y535), 8.03j, 8.03l, 8.03m "
           "(A level Y545) · OCR MEI Extra Pure Y435 Xa7, Xa8 · builds on Unit C7",
    "notes": [
        ("p", "Different-looking groups can have exactly the same structure. Addition modulo 4, multiplication by powers of i "
              "and the rotations of a square all behave alike: only the names of the elements differ. This unit makes "
              "“the same structure” precise (isomorphism), shows how to prove that two groups are or are not isomorphic, "
              "and uses these ideas to list every group of small order. The notation of Unit C7 is used throughout."),

        ("h2", "8.1 Isomorphic groups (Edexcel 1.5; OCR 8.03l; MEI Xa7)"),
        ("box", "Isomorphism", [
            "Groups (G, ∗) and (H, ∘) are <b>isomorphic</b>, written G ≅ H, if there is a bijection (one-to-one "
            "correspondence) φ : G → H such that φ(a ∗ b) = φ(a) ∘ φ(b) for all a, b ∈ G. Such a φ is an <b>isomorphism</b>.",
            "Informally: rename each element of G by its partner in H, and the Cayley table of G becomes the Cayley table of "
            "H (possibly with rows and columns in a different order).",
            "An isomorphism sends the identity to the identity, inverses to inverses, and each element to an element of the "
            "same order: φ(aⁿ) = φ(a)ⁿ.",
        ]),
        ("p", "In practice (and on OCR “by informal methods”), you show two finite groups are isomorphic by writing down a "
              "correspondence, matching identity with identity and elements of each order with elements of the same order, "
              "and checking that the tables agree. With a generator the checking is quick: if g and h have the same order n, "
              "then gᵏ ↦ hᵏ is an isomorphism ⟨g⟩ → ⟨h⟩, because gʲ ∗ gᵏ = gʲ⁺ᵏ ↦ hʲ⁺ᵏ = hʲ ∘ hᵏ."),
        ("p", "For example, multiplication modulo 7 on {1, 2, 3, 4, 5, 6}, with the elements listed as powers of 3, has a table "
              "with the same diagonal pattern as (ℤ₆, +₆) in Unit C7. So 3ᵏ ↦ k is an isomorphism to (ℤ₆, +₆)."),
        cayley("×₇", U7),
        ("p", "A less obvious example: the six functions f₁(x) = x, f₂(x) = 1/x, f₃(x) = 1 − x, f₄(x) = 1/(1 − x), "
              "f₅(x) = (x − 1)/x and f₆(x) = x/(x − 1), on ℝ \\ {0, 1}, form a group F under composition (fᵢ ∘ fⱼ means "
              "apply fⱼ first). For instance f₄ ∘ f₄(x) = 1/(1 − 1/(1 − x)) = (x − 1)/x = f₅(x). Its table shows F is "
              "non-abelian of order 6; Example C8.3 shows it is isomorphic to D₃."),
        cayley("∘", F6),

        ("h2", "8.2 Showing that groups are not isomorphic"),
        ("p", "To prove two groups are <b>not</b> isomorphic, find a structural property that one has and the other lacks. "
              "Saying “I could not find a mapping” is not a proof."),
        ("table", ["Property preserved by isomorphism", "Example of its use"], [
            ["Order of the group", "Groups of different orders are never isomorphic."],
            ["Number of elements of each order", "{1, 3, 5, 7} under ×₈ has three elements of order 2; (ℤ₄, +₄) has one."],
            ["Being cyclic", "(ℤ₆, +₆) is cyclic; D₃ has no element of order 6."],
            ["Being abelian", "(ℤ₆, +₆) is abelian; D₃ is not (r ∘ a ≠ a ∘ r)."],
            ["Number of self-inverse elements", "Same as the number of elements of order 2, plus the identity."],
            ["Subgroups (number and type)", "D₄ has a cyclic subgroup of order 4; the quaternion group has three."],
        ]),

        ("h2", "8.3 Cyclic groups of the same order are isomorphic (MEI Xa8; all boards)"),
        ("box", "Key results", [
            "Any two cyclic groups of order n are isomorphic: if G = ⟨g⟩ and H = ⟨h⟩, the map gᵏ ↦ hᵏ (k = 0, 1, …, n − 1) is an "
            "isomorphism. Every cyclic group of order n is isomorphic to (ℤₙ, +ₙ), and is often called Cₙ.",
            "Every group of prime order p is cyclic (Lagrange, Unit C7), so all groups of order p are isomorphic to Cₚ.",
            "An isomorphism from a cyclic group must send a generator to a generator. An isomorphism from (ℤ₆, +₆) to a cyclic "
            "group H of order 6 is fixed by the image of 1, which must be one of the two generators of H, so there are "
            "exactly two such isomorphisms.",
        ]),
        ("p", "The fourth roots of unity {1, i, −1, −i} under ×, (ℤ₄, +₄), {1, 2, 3, 4} under ×₅ and the rotations of a "
              "square through 0°, 90°, 180°, 270° are all cyclic of order 4, so they are all isomorphic to C₄."),

        ("h2", "8.4 The structure of groups of order up to 7 (OCR 8.03i, AS; useful for all boards)"),
        ("table", ["Order", "Groups (up to isomorphism)", "Reason or example"], [
            ["1", "trivial group {e}", ""],
            ["2, 3, 5, 7", "C₂, C₃, C₅, C₇ only", "prime order, so cyclic"],
            ["4", "C₄ or the Klein group V₄", "C₄: (ℤ₄, +₄). V₄: {1, 3, 5, 7} under ×₈; three elements of order 2"],
            ["6", "C₆ or D₃ (≅ S₃)", "C₆: (ℤ₆, +₆). D₃: symmetries of a triangle; the smallest non-abelian group"],
        ]),
        ("p", "<b>Order 4.</b> If some element has order 4, the group is cyclic. Otherwise, by Lagrange every non-identity "
              "element has order 2. Take a ≠ b, both ≠ e. Then ab ≠ e (as a⁻¹ = a ≠ b), ab ≠ a and ab ≠ b (cancellation), "
              "so ab = c. The table is then fixed: this is V₄. So there are exactly two groups of order 4, and both are abelian."),
        ("p", "<b>Order 6 (sketch).</b> If there is an element of order 6 the group is C₆. Otherwise element orders are 1, 2 or "
              "3, and they cannot all be 2 (a group in which x² = e for all x is abelian, and then e, a, b, ab would form a "
              "subgroup of order 4, which does not divide 6). So take a of order 3 and b ∉ {e, a, a²}. The elements are "
              "e, a, a², b, ab, a²b. b² must be e (if b² = a or a², b would have order 6), and ba = ab would make ab of "
              "order 6, so ba = a²b. These rules give the table of D₃."),

        ("h2", "8.5 Groups of order 8 (Edexcel 1.5; OCR 8.03j)"),
        ("p", "There are five groups of order 8, distinguished by how many elements they have of each order. The symmetries "
              "of a square, D₄, are e, the rotations r, r², r³ through 90°, 180°, 270° anticlockwise, and the reflections H, V, "
              "D₁, D₂ in the lines shown below. The quaternion group Q₈ = {±1, ±i, ±j, ±k} has i² = j² = k² = −1, ij = k, "
              "jk = i, ki = j, ji = −k, kj = −i, ik = −j."),
        ("figure", "pc08_square.png", "Symmetries of a square: rotations about O through multiples of 90°, and reflections in "
                   "the fixed lines H, V, D₁ and D₂.", 75),
        cayley("∘", D4),
        cayley("×", Q8),
        ("table", ["Group", "Example", "Abelian?", "Elements of order 1, 2, 4, 8"], [
            ["C₈", "(ℤ₈, +₈); 8th roots of unity", "yes", "1, 1, 2, 4"],
            ["C₄ × C₂", "{1, 3, 5, …, 15} under ×₁₆", "yes", "1, 3, 4, 0"],
            ["C₂ × C₂ × C₂", "{1, 5, 7, 11, 13, 17, 19, 23} under ×₂₄", "yes", "1, 7, 0, 0"],
            ["D₄", "symmetries of a square", "no", "1, 5, 2, 0"],
            ["Q₈", "quaternion group", "no", "1, 1, 6, 0"],
        ]),
        ("p", "Since the five rows of order counts are all different, counting orders identifies which of the five types a "
              "group of order 8 is. (C₄ × C₂ and C₂ × C₂ × C₂ are names for these structures; the specifications do not "
              "require the notation.)"),

        ("h2", "8.6 Larger groups and infinite groups (OCR 8.03j, A level; MEI Xa1)"),
        ("bullets", [
            "Larger finite groups: Dₙ (symmetries of a regular n-gon, order 2n), Sₙ (order n!), the units modulo n, and finite "
            "matrix groups. Lagrange's theorem still limits the subgroups: S₄ (order 24) has no element of order 5.",
            "Infinite groups: (ℤ, +), (ℚ, +), (ℝ, +), (ℂ, +); (ℚ \\ {0}, ×), (ℝ⁺, ×), (ℂ \\ {0}, ×); the non-singular 2 × 2 "
            "matrices; rotations of the plane about O through any angle; {z ∈ ℂ : |z| = 1} under ×.",
            "An infinite group can contain elements of finite order: in (ℂ \\ {0}, ×), i has order 4 and e^(2πi/n) has order n, "
            "while 2 has infinite order. In (ℝ, +) only 0 has finite order.",
            "Infinite groups have finite and infinite subgroups: {1, −1} and (ℚ⁺, ×) are subgroups of (ℝ \\ {0}, ×).",
            "Isomorphisms between infinite groups are given by a formula. φ(x) = eˣ is an isomorphism (ℝ, +) → (ℝ⁺, ×): it is a "
            "bijection (inverse ln) and φ(x + y) = eˣ⁺ʸ = eˣeʸ = φ(x)φ(y). Similarly n ↦ 2ⁿ is an isomorphism from (ℤ, +) to "
            "{2ⁿ : n ∈ ℤ} under ×, and n ↦ 3n is an isomorphism from (ℤ, +) to (3ℤ, +): an infinite group can be isomorphic to "
            "a proper subgroup of itself.",
        ]),

        ("h2", "8.7 Abstract groups (OCR 8.03m, A level)"),
        ("p", "An abstract group is described by its algebraic properties, not by what its elements are. Often it is given by "
              "generators and rules, for example “G is generated by a and b, where a⁴ = e, b² = e and ba = a³b”. You use only "
              "the axioms and the given rules to deduce facts, then often recognise the structure (this one is D₄, with a = r "
              "and b = H)."),
        ("box", "Useful results proved from the axioms alone", [
            "If x² = e for every x ∈ G, then G is abelian: ab = (ab)⁻¹ = b⁻¹a⁻¹ = ba.",
            "If (ab)² = a²b² for all a, b, then G is abelian: abab = aabb, and cancelling a on the left and b on the right "
            "gives ba = ab.",
            "If ba = aᵐb, then baᵏ = aᵐᵏb for all k ≥ 1 (move b past one a at a time), so every product can be written as aⁱbʲ.",
            "a and its inverse have the same order; a and xax⁻¹ have the same order, because (xax⁻¹)ⁿ = xaⁿx⁻¹.",
        ]),

        ("warn", "Common mistakes", [
            "Showing a bijection exists but not that it preserves the operation. For infinite groups, prove φ(a ∗ b) = φ(a) ∘ φ(b) "
            "in general; for finite groups, check the table or use a generator.",
            "Matching elements of different orders, or not sending the identity to the identity.",
            "Claiming two groups are not isomorphic because their tables “look different”. Give an invariant: element orders, "
            "cyclic or not, abelian or not.",
            "Forgetting that a cyclic group of order n has an element of order n, so a group of order 8 with no element of "
            "order 8 is not isomorphic to (ℤ₈, +₈).",
            "In abstract groups, treating the operation as commutative. ba = a³b does not let you write ab = a³b.",
        ]),
        ("box", "Given or learn", [
            "Nothing here is in any formula booklet. Learn the definition of isomorphism, the invariants in 8.2, the groups of "
            "order 4 and 6 (all boards) and of order 8 (Edexcel, OCR A level).",
        ]),
    ],

    "examples": [
        {
            "title": "Three cyclic groups of order 4",
            "question": "Show that the groups G = ({1, i, −1, −i}, ×), H = (ℤ₄, +₄) and K = ({1, 2, 3, 4}, ×₅) are isomorphic, "
                        "giving explicit isomorphisms.",
            "steps": [
                "In G, i has order 4 (i² = −1, i³ = −i, i⁴ = 1), so G = ⟨i⟩. In H, 1 has order 4. In K, 2 has order 4 "
                "(2, 4, 3, 1). All three are cyclic of order 4.",
                "Map generator to generator: φ : H → G, φ(k) = iᵏ, so 0 ↦ 1, 1 ↦ i, 2 ↦ −1, 3 ↦ −i. It is a bijection and "
                "φ(j +₄ k) = i^(j+k) = iʲ × iᵏ = φ(j)φ(k), since i⁴ = 1 makes the exponent work modulo 4.",
                "Similarly ψ : H → K, ψ(k) = 2ᵏ mod 5: 0 ↦ 1, 1 ↦ 2, 2 ↦ 4, 3 ↦ 3. Then ψ ∘ φ⁻¹ : G → K sends 1 ↦ 1, i ↦ 2, "
                "−1 ↦ 4, −i ↦ 3.",
                "Another valid choice sends i ↦ 3 (the other generator of K). A map such as i ↦ 4 is not an isomorphism: i has "
                "order 4 but 4 has order 2.",
            ],
        },
        {
            "title": "Proving that groups are not isomorphic",
            "question": "V = {1, 3, 5, 7} under ×₈. (a) Show that V is not isomorphic to (ℤ₄, +₄). (b) M is the set of "
                        "matrices I, A = (1 0; 0 −1), B = (−1 0; 0 1), −I under matrix multiplication. Show that M is "
                        "isomorphic to V, giving an isomorphism.",
            "steps": [
                "(a) In V, 3² = 9 ≡ 1, 5² = 25 ≡ 1, 7² = 49 ≡ 1, so V has three elements of order 2 and none of order 4. ℤ₄ has "
                "an element of order 4 (1) and only one element of order 2 (2). An isomorphism preserves orders, so V ≇ ℤ₄.",
                "(b) A² = B² = (−I)² = I, AB = BA = −I, A(−I) = B and B(−I) = A. So M is closed, I is the identity and each "
                "element is self-inverse; matrix multiplication is associative. M is a group in which every non-identity "
                "element has order 2.",
                "Try φ: I ↦ 1, A ↦ 3, B ↦ 5, −I ↦ 7. Check the products of different non-identity elements: AB = −I and 3 × 5 = "
                "15 ≡ 7; A(−I) = B and 3 × 7 = 21 ≡ 5; B(−I) = A and 5 × 7 = 35 ≡ 3. Squares go to 1 in both. So φ is an "
                "isomorphism and M ≅ V (both are the Klein group V₄).",
            ],
        },
        {
            "title": "A group of functions isomorphic to D₃",
            "question": "Use the Cayley table of F = {f₁, …, f₆} in Section 8.1 and the table of D₃ in Unit C7. (a) Find the "
                        "order of each element of F. (b) Find an isomorphism from D₃ to F.",
            "steps": [
                "(a) f₁ is the identity. The diagonal gives f₂ ∘ f₂ = f₃ ∘ f₃ = f₆ ∘ f₆ = f₁, so f₂, f₃, f₆ have order 2. "
                "f₄ ∘ f₄ = f₅ and f₄ ∘ f₅ = f₁, so f₄ and f₅ have order 3.",
                "(b) D₃ has e (order 1), r, r² (order 3) and a, b, c (order 2), the same counts. Send e ↦ f₁, r ↦ f₄, r² ↦ f₅ "
                "(so that r² = r ∘ r ↦ f₄ ∘ f₄ = f₅), and choose a ↦ f₂.",
                "The images of b and c are then forced: in D₃, b = a ∘ r ↦ f₂ ∘ f₄ = f₃, and c = r ∘ a ↦ f₄ ∘ f₂ = f₆.",
                "So φ: e ↦ f₁, r ↦ f₄, r² ↦ f₅, a ↦ f₂, b ↦ f₃, c ↦ f₆. Rewriting the D₃ table with these names gives the F "
                "table exactly (all 36 entries agree), so φ is an isomorphism and F ≅ D₃.",
            ],
        },
        {
            "title": "Identifying groups of order 8",
            "question": "For each group, count the elements of each order and decide which of the five groups of order 8 it "
                        "is: (a) G₁ = {1, 3, 5, 7, 9, 11, 13, 15} under ×₁₆; (b) G₂ = {1, 5, 7, 11, 13, 17, 19, 23} under ×₂₄; "
                        "(c) G₃ = the 8th roots of unity under ×; (d) D₄. (e) Are any two of them isomorphic?",
            "steps": [
                "(a) In Unit C7 (Example C7.5): 7, 9, 15 have order 2 and 3, 5, 11, 13 have order 4. Counts 1, 3, 4, 0, "
                "abelian: C₄ × C₂.",
                "(b) 5² = 25 ≡ 1, 7² = 49 ≡ 1, 11² = 121 ≡ 1, 13² = 169 ≡ 1, 17² = 289 ≡ 1, 19² = 361 ≡ 1, 23² = 529 ≡ 1 "
                "(mod 24). Seven elements of order 2: C₂ × C₂ × C₂.",
                "(c) ω = e^(2πi/8) has order 8, so G₃ is cyclic, C₈. Its elements ωᵏ have orders 1, 8, 4, 8, 2, 8, 4, 8.",
                "(d) From the D₄ table: r and r³ have order 4; r², H, V, D₁, D₂ have order 2. Counts 1, 5, 2, 0 and "
                "non-abelian: D₄.",
                "(e) No two have the same order counts, so no two are isomorphic.",
            ],
        },
        {
            "title": "Infinite groups",
            "question": "(a) Show that (ℝ, +) is isomorphic to (ℝ⁺, ×). (b) Show that (ℝ \\ {0}, ×) is not isomorphic to (ℝ, +).",
            "steps": [
                "(a) Let φ(x) = eˣ. For every y > 0 there is exactly one x with eˣ = y, namely x = ln y, so φ is a bijection "
                "from ℝ to ℝ⁺.",
                "φ(x + y) = e^(x+y) = eˣ × eʸ = φ(x) × φ(y), so φ preserves the operation. Hence (ℝ, +) ≅ (ℝ⁺, ×). "
                "(The identity 0 maps to the identity 1, and −x maps to e^(−x) = 1/eˣ.)",
                "(b) In (ℝ \\ {0}, ×), (−1) × (−1) = 1, so −1 has order 2. In (ℝ, +), x + x = 0 only for x = 0, so no element "
                "has order 2.",
                "An isomorphism would send −1 to an element of order 2, which does not exist. So the groups are not isomorphic.",
            ],
        },
        {
            "title": "An abstract group of order 8",
            "question": "G is a group generated by a and b, where a⁴ = e, b² = e, ba = a³b, and the elements e, a, a², a³, b, ab, "
                        "a²b, a³b are distinct. (a) Show that ba² = a²b and ba³ = ab. (b) Find the order of ab and of a²b. "
                        "(c) Show that G is isomorphic to D₄.",
            "steps": [
                "(a) ba² = (ba)a = a³ba = a³(a³b) = a⁶b = a²b. Then ba³ = (ba²)a = a²ba = a²a³b = a⁵b = ab.",
                "(b) (ab)² = a(ba)b = a(a³b)b = a⁴b² = e, and ab ≠ e, so ab has order 2. (a²b)² = a²(ba²)b = a²a²bb = e, so "
                "a²b has order 2. In the same way a³b has order 2.",
                "So G has a² and the four elements b, ab, a²b, a³b of order 2 (five in all), and a, a³ of order 4: the counts "
                "1, 5, 2 of D₄.",
                "(c) In D₄ take a = r and b = H. Then r⁴ = e, H² = e and, from the table, H ∘ r = D₂ = r³ ∘ H, so the rule "
                "ba = a³b holds. The map aⁱbʲ ↦ rⁱ ∘ Hʲ is a bijection, and products in both groups are computed by the same "
                "rules, so it is an isomorphism: G ≅ D₄.",
            ],
        },
    ],

    "practice": [
        "Find an isomorphism from (ℤ₆, +₆) to ({1, 2, 3, 4, 5, 6}, ×₇).",
        "Show that ({1, 5, 7, 11}, ×₁₂) is not isomorphic to (ℤ₄, +₄).",
        "Show that ({1, 3, 7, 9}, ×₁₀) is isomorphic to (ℤ₄, +₄), giving the isomorphism.",
        "The matrices I, −I, P = (1 0; 0 −1) and Q = (−1 0; 0 1) form a group under matrix multiplication. Find an isomorphism "
        "from this group to ({1, 5, 7, 11}, ×₁₂).",
        "R is the group of rotations of a square about its centre through 0°, 90°, 180° and 270°. State, with reasons, which "
        "of (ℤ₄, +₄) and ({1, 3, 5, 7}, ×₈) it is isomorphic to, and give an isomorphism from R to ({1, i, −1, −i}, ×).",
        "(a) Explain why every group of order 5 is cyclic. (b) Hence explain why any two groups of order 5 are isomorphic.",
        "Prove that every group of order 4 is abelian.",
        "Use the Cayley table of D₄ in Section 8.5. (a) Find the order of each element. (b) Find the three subgroups of order 4 "
        "and state which of C₄ and V₄ each is isomorphic to.",
        "(a) Show that φ(n) = 3n is an isomorphism from (ℤ, +) to (3ℤ, +), where 3ℤ = {3n : n ∈ ℤ}. "
        "(b) Show that T = {2ⁿ : n ∈ ℤ} is a group under multiplication and that it is isomorphic to (ℤ, +).",
        "In the group (ℂ \\ {0}, ×), find the order of: (a) i, (b) −1, (c) 2, (d) (1 + i)/√2. "
        "(e) Write down a subgroup of order 8.",
        "G is a group. (a) Prove that (ab)⁻¹ = b⁻¹a⁻¹ for all a, b ∈ G. (b) Prove that if x² = e for all x ∈ G, then G is "
        "abelian. (c) The element a has order 6. Find the orders of a², a³ and a⁴.",
        "Label the corner positions of an equilateral triangle 1 (top), 2 (bottom left) and 3 (bottom right). Each symmetry "
        "in D₃ (Unit C7) permutes these positions. Write r, a, b, c as permutations in cycle notation and hence give an "
        "isomorphism from D₃ to S₃.",
    ],
    "answers": [
        "3 has order 6 in ×₇ (3, 2, 6, 4, 5, 1), so k ↦ 3ᵏ: 0 ↦ 1, 1 ↦ 3, 2 ↦ 2, 3 ↦ 6, 4 ↦ 4, 5 ↦ 5. "
        "(Using the generator 5 instead also works.)",
        "5² = 25 ≡ 1, 7² = 49 ≡ 1, 11² = 121 ≡ 1 (mod 12): three elements of order 2 and none of order 4. ℤ₄ has an element "
        "of order 4. Not isomorphic.",
        "3 has order 4 (3, 9, 7, 1), so the group is cyclic. k ↦ 3ᵏ mod 10: 0 ↦ 1, 1 ↦ 3, 2 ↦ 9, 3 ↦ 7 "
        "(or k ↦ 7ᵏ: 0 ↦ 1, 1 ↦ 7, 2 ↦ 9, 3 ↦ 3).",
        "Both have identity and three self-inverse elements, and in each the product of two different non-identity elements "
        "is the third. I ↦ 1, P ↦ 5, Q ↦ 7, −I ↦ 11 (PQ = −I and 5 × 7 = 35 ≡ 11). Any bijection with I ↦ 1 works.",
        "R is cyclic of order 4, generated by the 90° rotation, so R ≅ (ℤ₄, +₄). It is not isomorphic to {1, 3, 5, 7} under ×₈, "
        "which has no element of order 4. Rotation through 90k° ↦ iᵏ.",
        "(a) By Lagrange, any a ≠ e has order dividing 5 and greater than 1, so order 5, and a generates the group. "
        "(b) Both are cyclic of order 5, say ⟨g⟩ and ⟨h⟩; gᵏ ↦ hᵏ is an isomorphism.",
        "Element orders divide 4. If an element has order 4, the group is cyclic, hence abelian. Otherwise x² = e for every x, "
        "so ab = (ab)⁻¹ = b⁻¹a⁻¹ = ba: abelian.",
        "(a) e: 1; r, r³: 4; r², H, V, D₁, D₂: 2. (b) {e, r, r², r³} ≅ C₄; {e, r², H, V} ≅ V₄; {e, r², D₁, D₂} ≅ V₄.",
        "(a) Bijection: each 3n comes from exactly one n. φ(m + n) = 3m + 3n = φ(m) + φ(n). "
        "(b) 2ᵐ × 2ⁿ = 2ᵐ⁺ⁿ ∈ T; associative (×); identity 2⁰ = 1; inverse of 2ⁿ is 2⁻ⁿ ∈ T. n ↦ 2ⁿ is a bijection "
        "ℤ → T with 2ᵐ⁺ⁿ = 2ᵐ × 2ⁿ, so T ≅ (ℤ, +).",
        "(a) 4. (b) 2. (c) Infinite (2ⁿ ≠ 1 for n ≥ 1). (d) (1 + i)/√2 = e^(iπ/4), order 8. (e) The 8th roots of unity "
        "{e^(ikπ/4) : k = 0, 1, …, 7}.",
        "(a) (ab)(b⁻¹a⁻¹) = a(bb⁻¹)a⁻¹ = aa⁻¹ = e, and inverses are unique. (b) x = x⁻¹ for all x, so ab = (ab)⁻¹ = b⁻¹a⁻¹ = ba. "
        "(c) a² has order 3, a³ has order 2, a⁴ has order 3 (aᵏ has order 6/hcf(k, 6)).",
        "r = (1 2 3), r² = (1 3 2), a = (2 3), b = (1 3), c = (1 2). The map e ↦ identity, r ↦ (1 2 3), r² ↦ (1 3 2), "
        "a ↦ (2 3), b ↦ (1 3), c ↦ (1 2) is an isomorphism (a symmetry is determined by how it permutes the corners, and "
        "composition matches composition).",
    ],

    "exam": [
        "G = {1, 2, 4, 5, 7, 8} under multiplication modulo 9 is a group.\n"
        "(a) Find the order of each element of G. [3]\n"
        "(b) Show that G is cyclic and state all its generators. [2]\n"
        "(c) Write down an isomorphism from (ℤ₆, +₆) to G. [3]\n"
        "(d) Explain why G is not isomorphic to D₃, the group of symmetries of an equilateral triangle. [2]\n"
        "(e) Write down the subgroup of G of order 3. [1]",
        "D₄ is the group of symmetries of a square, with the Cayley table given in Section 8.5. H is the group "
        "{1, 3, 5, 7, 9, 11, 13, 15} under multiplication modulo 16.\n"
        "(a) Find the order of each element of D₄. [2]\n"
        "(b) Find the three subgroups of D₄ of order 4, stating whether each is cyclic. [3]\n"
        "(c) Find the number of elements of H of each order. [2]\n"
        "(d) Explain why H is not isomorphic to D₄, and why H is not isomorphic to (ℤ₈, +₈). [2]\n"
        "(e) Find a subgroup K of H and a subgroup L of D₄ such that K ≅ L ≅ V₄, the Klein group, and give an isomorphism "
        "from K to L. [3]",
        "For a ∈ ℝ, let M(a) = (1 a; 0 1), and let S = {M(a) : a ∈ ℝ}.\n"
        "(a) Show that M(a)M(b) = M(a + b). [2]\n"
        "(b) Prove that S is a group under matrix multiplication. [4]\n"
        "(c) Show that (S, ×) is isomorphic to (ℝ, +). [3]\n"
        "(d) Write down a subgroup of S that is isomorphic to (ℤ, +), and state the order of M(2) in S. [2]",
        "G is a group generated by a and b, where a⁴ = e, b² = a², ba = a³b, and the eight elements e, a, a², a³, b, ab, a²b, "
        "a³b are distinct.\n"
        "(a) Show that b has order 4. [2]\n"
        "(b) Prove that baᵏ = a³ᵏb for every positive integer k. [2]\n"
        "(c) Show that (aᵏb)² = a² for every k, and deduce that G has exactly one element of order 2. [3]\n"
        "(d) Hence show that G is not isomorphic to D₄ and is not cyclic. [2]\n"
        "(e) Show that G is not abelian. [1]",
    ],
    "exam_answers": [
        "(a) 1: 1; 2: 6 (2, 4, 8, 7, 5, 1); 4: 3 (4, 7, 1); 5: 6 (5, 7, 8, 4, 2, 1); 7: 3; 8: 2 (64 ≡ 1) B3 (B2 for four or "
        "five correct). (b) 2 has order 6 = |G|, so G is cyclic B1; generators 2 and 5 B1. "
        "(c) k ↦ 2ᵏ mod 9 M1: 0 ↦ 1, 1 ↦ 2, 2 ↦ 4, 3 ↦ 8, 4 ↦ 7, 5 ↦ 5 A1; this is a bijection and 2^(j+k) = 2ʲ2ᵏ with "
        "2⁶ ≡ 1 so exponents work modulo 6 A1. (d) G is cyclic (abelian) B1; D₃ is not abelian / has no element of order 6, "
        "so not isomorphic B1. (e) {1, 4, 7} B1.",
        "(a) e: 1; r, r³: 4; r², H, V, D₁, D₂: 2 B2. (b) {e, r, r², r³} cyclic; {e, r², H, V} and {e, r², D₁, D₂} not cyclic "
        "B3. (c) One of order 1, three of order 2 (7, 9, 15), four of order 4 (3, 5, 11, 13) B2. "
        "(d) D₄ has five elements of order 2, H has three (or H is abelian, D₄ is not) B1; H has no element of order 8, "
        "ℤ₈ has (1) B1. (e) K = {1, 7, 9, 15} B1, L = {e, r², H, V} B1, e.g. 1 ↦ e, 7 ↦ H, 9 ↦ r², 15 ↦ V (any bijection with "
        "1 ↦ e works since both are V₄) B1.",
        "(a) (1 a; 0 1)(1 b; 0 1) = (1 a + b; 0 1) = M(a + b) M1 A1. (b) Closure: a + b ∈ ℝ so M(a + b) ∈ S B1. Associativity: "
        "matrix multiplication is associative B1. Identity M(0) = I ∈ S B1. Inverse M(−a), since M(a)M(−a) = M(0) B1. "
        "(c) φ(a) = M(a) [from ℝ to S] is a bijection, since each matrix in S has a unique top-right entry B1; φ(a + b) = "
        "M(a + b) = M(a)M(b) = φ(a)φ(b) M1 A1. (d) {M(n) : n ∈ ℤ} B1; M(2) has infinite order (M(2)ⁿ = M(2n) ≠ I for n ≥ 1) B1.",
        "(a) b² = a² ≠ e and b⁴ = a⁴ = e M1, so b has order 4 A1. (b) k = 1 is given. If baᵏ = a³ᵏb, then baᵏ⁺¹ = (baᵏ)a = "
        "a³ᵏ(ba) = a³ᵏa³b = a³⁽ᵏ⁺¹⁾b M1 A1, so true for all k by induction. (c) (aᵏb)² = aᵏ(baᵏ)b = aᵏa³ᵏb² = a⁴ᵏa² = a² M1 A1. "
        "So each aᵏb has order 4; a and a³ have order 4; a² has order 2; so a² is the only element of order 2 A1. "
        "(d) D₄ has five elements of order 2, G has one, so not isomorphic B1. No element has order 8, so G is not cyclic B1. "
        "(e) ba = a³b, and a³b ≠ ab because a³ ≠ a (a has order 4), so ab ≠ ba B1. (G is the quaternion group Q₈.)",
    ],
}
