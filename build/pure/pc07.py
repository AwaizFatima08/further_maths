"""Unit C7: Groups I: axioms, subgroups and Lagrange's theorem
(Edexcel FP2 1.1–1.4 and AS FP2 1.1–1.4; OCR A Y535/Y545 8.03a–h, 8.03k; OCR MEI Y435 XS1, XS2, Xa1–Xa6)."""

# Cayley tables printed in this unit. Row x, column y holds x ∗ y (for symmetries: x ∘ y, do y first, then x).
# The check script checks every one of them by brute force.
U5 = (["1", "2", "3", "4"], [
    ["1", "2", "3", "4"],
    ["2", "4", "1", "3"],
    ["3", "1", "4", "2"],
    ["4", "3", "2", "1"],
])
Z6 = (["0", "1", "2", "3", "4", "5"], [
    ["0", "1", "2", "3", "4", "5"],
    ["1", "2", "3", "4", "5", "0"],
    ["2", "3", "4", "5", "0", "1"],
    ["3", "4", "5", "0", "1", "2"],
    ["4", "5", "0", "1", "2", "3"],
    ["5", "0", "1", "2", "3", "4"],
])
U8 = (["1", "3", "5", "7"], [
    ["1", "3", "5", "7"],
    ["3", "1", "7", "5"],
    ["5", "7", "1", "3"],
    ["7", "5", "3", "1"],
])
M4 = (["0", "1", "2", "3"], [  # multiplication modulo 4: NOT a group
    ["0", "0", "0", "0"],
    ["0", "1", "2", "3"],
    ["0", "2", "0", "2"],
    ["0", "3", "2", "1"],
])
D3 = (["e", "r", "r²", "a", "b", "c"], [
    ["e", "r", "r²", "a", "b", "c"],
    ["r", "r²", "e", "c", "a", "b"],
    ["r²", "e", "r", "b", "c", "a"],
    ["a", "b", "c", "e", "r", "r²"],
    ["b", "c", "a", "r²", "e", "r"],
    ["c", "a", "b", "r", "r²", "e"],
])
# Example C7.4: the completed table of a group {e, a, b, c} with a ∗ a = b
G4 = (["e", "a", "b", "c"], [
    ["e", "a", "b", "c"],
    ["a", "b", "c", "e"],
    ["b", "c", "e", "a"],
    ["c", "e", "a", "b"],
])


def cayley(op, table):
    """A Cayley table as a note table: header row and bold first column."""
    els, rows = table
    return ("table", [op] + els, [[f"<b>{a}</b>"] + list(r) for a, r in zip(els, rows)])


UNIT = {
    "number": "C7",
    "title": "Groups I: axioms, subgroups and Lagrange's theorem",
    "tag": "Option · Edexcel FP2 1.1–1.4 (A level; also AS FP2 1.1–1.4) · OCR A Additional Pure 8.03a–h (AS Y535), "
           "8.03k (A level Y545) · OCR MEI Extra Pure Y435 XS1, XS2, Xa1–Xa6 · not on AQA, IAL or CAIE",
    "notes": [
        ("p", "A group is a set with one way of combining its elements that behaves like addition of integers or "
              "multiplication of non-zero numbers. The same four rules (the axioms) turn up in modular arithmetic, matrices, "
              "complex roots of unity, the symmetries of a shape and permutations. Group theory studies what follows from the "
              "rules alone, so a result proved once holds in every example. This unit sets up the language, the axioms, "
              "orders, cyclic groups and subgroups, and ends with Lagrange's theorem. Unit C8 compares groups using isomorphism."),

        ("h2", "7.1 Set language and notation (MEI XS1, XS2; used by every board)"),
        ("bullets", [
            "x ∈ A means x is an element of the set A; x ∉ A means it is not. A set is often written by listing, {1, 3, 5, 7}, "
            "or in set-builder form, {x ∈ ℤ : 0 ≤ x < 4} = {0, 1, 2, 3} (read the colon as “such that”).",
            "A ⊆ B: every element of A is in B (A is a <b>subset</b> of B). A ⊂ B: A is a <b>proper subset</b>, so A ⊆ B and A ≠ B.",
            "A ∪ B (union): elements in A or B or both. A ∩ B (intersection): elements in both. { } is the empty set (no elements)."
            "n(A) or |A| is the number of elements of A.",
            "Number sets: ℕ = {1, 2, 3, …} (natural numbers), ℕ₀ = {0, 1, 2, …}, ℤ (integers), ℚ (rationals), ℝ (reals), "
            "ℂ (complex numbers). So ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ.",
            "A superscript restricts the sign: ℚ⁺ and ℝ⁺ are the positive rationals and reals, and ℝ⁺₀ = {x ∈ ℝ : x ≥ 0}. "
            "ℝ \\ {0} (or ℝ*) means the non-zero reals.",
        ]),

        ("h2", "7.2 Binary operations (OCR 8.03a; Edexcel 1.1)"),
        ("p", "A <b>binary operation</b> ∗ on a set S is a rule that combines any two elements a, b of S, in that order, to "
              "give one result a ∗ b. Examples are + and × on ℝ, composition ∘ of functions, and multiplication of matrices. "
              "Three properties matter."),
        ("bullets", [
            "<b>Closed</b>: a ∗ b ∈ S for all a, b ∈ S. Subtraction is closed on ℤ but not on ℕ (2 − 5 ∉ ℕ). Division is not "
            "closed on ℝ because a ÷ 0 is undefined.",
            "<b>Commutative</b>: a ∗ b = b ∗ a for all a, b. Addition is; subtraction, matrix multiplication and composition of "
            "functions are not in general.",
            "<b>Associative</b>: (a ∗ b) ∗ c = a ∗ (b ∗ c) for all a, b, c. Then a ∗ b ∗ c has one meaning. Addition, "
            "multiplication, matrix multiplication and composition of functions are associative; subtraction is not, since "
            "(8 − 4) − 2 = 2 but 8 − (4 − 2) = 6.",
        ]),
        ("p", "To show a property fails, one counter-example with numbers is enough. To show it holds, argue for general "
              "elements. For example, for a ∗ b = a + b + ab on ℝ, (a ∗ b) ∗ c = a + b + c + ab + bc + ca + abc, and "
              "a ∗ (b ∗ c) gives the same expression, so ∗ is associative."),

        ("h2", "7.3 Cayley tables and the Latin square property (Edexcel 1.2; OCR 8.03b, 8.03d; MEI Xa2)"),
        ("p", "For a finite set, a <b>Cayley table</b> (group table) shows every product. The entry in row x and column y is "
              "x ∗ y: <b>row first, then column</b>. Below are multiplication modulo 5 on {1, 2, 3, 4} (written ×₅) and "
              "multiplication modulo 8 on {1, 3, 5, 7}. To find 3 ×₅ 4, work out 12 and take the remainder on division by 5, "
              "which is 2."),
        cayley("×₅", U5),
        cayley("×₈", U8),
        ("p", "A table in which every element appears exactly once in each row and exactly once in each column is a <b>Latin "
              "square</b>. The Cayley table of every finite group has this property, because the equation a ∗ x = b has the "
              "single solution x = a⁻¹ ∗ b (and x ∗ a = b has the single solution x = b ∗ a⁻¹). The converse is false: a "
              "Latin square need not be a group table, because associativity can fail. A repeated entry in a row or column "
              "proves at once that the set is not a group."),
        ("p", "Multiplication modulo 4 on {0, 1, 2, 3} shows what goes wrong. The rows for 0 and 2 contain repeats, and 0 and "
              "2 have no inverse (nothing multiplies them to 1), so this is not a group."),
        cayley("×₄", M4),

        ("h2", "7.4 The group axioms (Edexcel 1.1; OCR 8.03c; MEI Xa1)"),
        ("box", "Definition of a group", [
            "A group (G, ∗) is a set G with a binary operation ∗ such that:",
            "<b>G1 Closure</b>: a ∗ b ∈ G for all a, b ∈ G.",
            "<b>G2 Associativity</b>: (a ∗ b) ∗ c = a ∗ (b ∗ c) for all a, b, c ∈ G.",
            "<b>G3 Identity</b>: there is an element e ∈ G with e ∗ a = a ∗ e = a for all a ∈ G.",
            "<b>G4 Inverses</b>: for each a ∈ G there is a⁻¹ ∈ G with a ∗ a⁻¹ = a⁻¹ ∗ a = e.",
            "If also a ∗ b = b ∗ a for all a, b, the group is <b>abelian</b> (commutative). The group may be finite or infinite.",
        ]),
        ("bullets", [
            "From a Cayley table: closure means no entry is outside the set; the identity is the element whose row and column "
            "repeat the headings; the inverse of a is the element in a's row under which e appears; the group is abelian if "
            "the table is symmetric about the leading diagonal.",
            "Associativity cannot be seen from a table without checking every triple. In an exam, quote it: addition and "
            "multiplication of numbers (and so modular arithmetic), matrix multiplication and composition of functions are "
            "associative.",
            "The identity is unique: if e and f are both identities then e = e ∗ f = f. Each element has exactly one inverse: "
            "if b and c are inverses of a then b = b ∗ (a ∗ c) = (b ∗ a) ∗ c = c.",
            "(a ∗ b)⁻¹ = b⁻¹ ∗ a⁻¹ (note the order), because (a ∗ b) ∗ (b⁻¹ ∗ a⁻¹) = a ∗ e ∗ a⁻¹ = e. Also (a⁻¹)⁻¹ = a.",
            "Cancellation: if a ∗ x = a ∗ y then x = y (multiply on the left by a⁻¹). This is the reason for the Latin square property.",
        ]),
        ("p", "Example of an infinite group: ℝ \\ {−1} under a ∗ b = a + b + ab. Closure: a + b + ab = (1 + a)(1 + b) − 1, which is "
              "not −1 because (1 + a)(1 + b) ≠ 0. Associativity was shown in 7.2. Identity 0, since a ∗ 0 = a. Inverse: "
              "a + x + ax = 0 gives x = −a/(1 + a), which exists and is not −1. It is abelian because a ∗ b = b ∗ a."),

        ("h2", "7.5 Standard examples of groups (Edexcel 1.2; OCR 8.03c; MEI Xa2)"),
        ("table", ["Group", "Elements and operation", "Order", "Notes"], [
            ["(ℤₙ, +ₙ)", "{0, 1, …, n − 1}, addition modulo n", "n", "identity 0; inverse of a is n − a; cyclic, generated by 1"],
            ["Non-zero residues mod p", "{1, 2, …, p − 1}, multiplication modulo p, p prime", "p − 1",
             "identity 1; cyclic. Fails for composite n: 2 ×₄ 2 = 0"],
            ["Units modulo n", "numbers in {1, …, n − 1} with no common factor with n, ×ₙ", "varies", "e.g. {1, 3, 5, 7} under ×₈"],
            ["nth roots of unity", "{1, ω, ω², …, ωⁿ⁻¹}, ω = e^(2πi/n), multiplication", "n", "e.g. {1, i, −1, −i}; cyclic"],
            ["Symmetries of a regular n-gon (Dₙ)", "rotations and reflections, composition", "2n", "non-abelian for n ≥ 3"],
            ["Permutations Sₙ", "all rearrangements of {1, …, n}, composition", "n!", "S₃ has order 6"],
            ["Matrix groups", "non-singular matrices, matrix multiplication", "finite or infinite", "identity I; inverse M⁻¹; det ≠ 0"],
            ["Number groups", "(ℤ, +), (ℚ, +), (ℝ, +), (ℂ, +); (ℚ⁺, ×), (ℝ \\ {0}, ×), (ℂ \\ {0}, ×)", "infinite",
             "(ℤ, ×) is not a group: 2 has no inverse"],
        ]),
        ("p", "<b>Addition modulo 6.</b> The table of (ℤ₆, +₆) shifts one place along in each row, as every cyclic group's table "
              "does when the elements are listed in order of powers of a generator."),
        cayley("+₆", Z6),
        ("p", "<b>Symmetries of an equilateral triangle (D₃).</b> Label the corners A, B, C. The symmetries are the identity e, "
              "rotations r and r² through 120° and 240° anticlockwise about the centre, and reflections a, b, c in the three "
              "lines of symmetry, which stay fixed in the plane (the line a passes through the top corner position). "
              "x ∘ y means “do y, then do x”. The table is not symmetric: r ∘ a = c but a ∘ r = b, so D₃ is non-abelian. "
              "It is the smallest non-abelian group."),
        ("figure", "pc07_triangle.png", "The six symmetries of an equilateral triangle: rotations r (120°) and r² (240°) "
                   "about the centre O, and reflections in the fixed lines a, b and c.", 85),
        cayley("∘", D3),
        ("p", "<b>Permutations (Edexcel 1.2).</b> A permutation of {1, 2, 3} can be written in two-line form, top row 1 2 3 and "
              "bottom row the images, or as cycles: (1 2 3) sends 1 → 2, 2 → 3, 3 → 1, and (1 2) swaps 1 and 2 and fixes 3. "
              "Products are compositions, done right to left. For (1 2)(1 3): 1 → 3 → 3, 3 → 1 → 2 and 2 → 2 → 1, so "
              "(1 2)(1 3) = (1 3 2). The six permutations of {1, 2, 3} form S₃; the symmetries of the triangle permute its "
              "corners, so D₃ and S₃ have the same structure (Unit C8)."),
        ("p", "<b>Functions.</b> On ℝ \\ {0}, the functions x, −x, 1/x and −1/x form a group of order 4 under composition. Each "
              "is its own inverse, for example (−1/x) ∘ (−1/x) = −1/(−1/x) = x. <b>Matrices.</b> With A = (0 −1; 1 0), a rotation "
              "of 90° about O, the set {I, A, A², A³} is a group under matrix multiplication, because A⁴ = I. (Matrices are "
              "written row by row: (0 −1; 1 0) has rows 0, −1 and 1, 0.)"),

        ("h2", "7.6 The order of a group and of an element (Edexcel 1.3; OCR 8.03e; MEI Xa4)"),
        ("box", "Orders", [
            "The <b>order of a group</b> G, written |G|, is the number of elements it contains (possibly infinite).",
            "The <b>order of an element</b> a is the smallest positive integer n with aⁿ = e, where aⁿ = a ∗ a ∗ … ∗ a (n times). "
            "In additive notation this reads na = 0. If no such n exists, a has infinite order.",
            "The identity is the only element of order 1. An element of order 2 is <b>self-inverse</b>: a ∗ a = e, a ≠ e. "
            "Self-inverse elements show up as e on the leading diagonal of the table.",
            "In a finite group every element has finite order, and that order divides |G| (OCR 8.03e; proved in 7.9).",
        ]),
        ("p", "In {1, 2, 3, 4} under ×₅: 2¹ = 2, 2² = 4, 2³ = 3, 2⁴ = 1, so 2 has order 4. Similarly 3 has order 4, 4 has order 2 "
              "and 1 has order 1. In (ℤ₆, +₆): 2 + 2 + 2 = 0, so 2 has order 3. In D₃, r and r² have order 3 and a, b, c "
              "have order 2. In (ℝ \\ {0}, ×), −1 has order 2 and 2 has infinite order."),

        ("h2", "7.7 Cyclic groups and generators (Edexcel 1.2; OCR 8.03g, 8.03h; MEI Xa3)"),
        ("p", "The powers of one element g, namely e, g, g², …, always form a group, written ⟨g⟩. A group is <b>cyclic</b> if "
              "G = ⟨g⟩ for some g, which is then called a <b>generator</b>. A finite group of order n is cyclic exactly when it "
              "has an element of order n, and then G = {e, g, g², …, gⁿ⁻¹}."),
        ("bullets", [
            "Cyclic groups are abelian, since gᵐ ∗ gᵏ = gᵐ⁺ᵏ = gᵏ ∗ gᵐ. So a non-abelian group (such as D₃) is never cyclic.",
            "(ℤₙ, +ₙ) is cyclic, generated by 1. Its generators are the k with no common factor with n: in ℤ₆ they are 1 and 5.",
            "{1, 2, 3, 4} under ×₅ is cyclic with generators 2 and 3. {1, 3, 5, 7} under ×₈ is not cyclic: every non-identity "
            "element has order 2. (This is the <b>Klein four-group</b>.)",
            "If g generates G, so does g⁻¹. The fourth roots of unity are generated by i and by −i.",
            "A group that is not cyclic may still be <b>generated by two or more elements</b> (OCR 8.03h): every element is a "
            "product of them. D₃ is generated by r and a, since r ∘ a = c and a ∘ r = b. The Klein group {1, 3, 5, 7} is "
            "generated by 3 and 5, because 3 ×₈ 5 = 7.",
            "(ℤ, +) is an infinite cyclic group generated by 1 (or −1). [MEI excludes infinite cyclic groups; OCR A includes them.]",
        ]),

        ("h2", "7.8 Subgroups (Edexcel 1.3; OCR 8.03f; MEI Xa5)"),
        ("box", "Subgroups", [
            "H is a <b>subgroup</b> of (G, ∗) if H ⊆ G and H is itself a group under the same operation ∗.",
            "Every group G has the <b>trivial</b> subgroup {e} and G itself. A <b>proper</b> subgroup is any subgroup other than G; "
            "a <b>non-trivial</b> proper subgroup is one other than {e} and G.",
            "To show H is a subgroup: closure in H, e ∈ H, and the inverse of each element of H is in H. Associativity is "
            "inherited from G. For a finite non-empty H, closure alone is enough.",
            "For any a ∈ G, ⟨a⟩ is a subgroup, the cyclic subgroup generated by a; its order equals the order of a.",
        ]),
        ("p", "Subgroups of D₃: {e}, {e, a}, {e, b}, {e, c}, {e, r, r²} and D₃. Subgroups of (ℤ₆, +₆): {0}, {0, 3}, {0, 2, 4} "
              "and ℤ₆. A set such as {0, 1, 5} ⊂ ℤ₆ is not a subgroup: 1 +₆ 1 = 2 is outside it. Infinite groups have "
              "infinite subgroups: (2ℤ, +), the even integers, is a subgroup of (ℤ, +), which is a subgroup of (ℝ, +)."),
        ("p", "To find all subgroups of a finite group, list the cyclic subgroups ⟨a⟩ for each element, then look for "
              "non-cyclic ones made by joining them, using Lagrange's theorem (below) to limit the possible orders."),

        ("h2", "7.9 Lagrange's theorem (Edexcel 1.4; OCR 8.03k, A level; MEI Xa6)"),
        ("box", "Lagrange's theorem and its corollaries", [
            "<b>Lagrange's theorem.</b> If H is a subgroup of a finite group G, then |H| divides |G|.",
            "<b>Corollary 1.</b> The order of every element of G divides |G|, because the order of a equals |⟨a⟩|.",
            "<b>Corollary 2.</b> A group of prime order p is cyclic, and its only subgroups are {e} and G: any a ≠ e has order "
            "dividing p and greater than 1, so equal to p, and a generates G.",
            "<b>Corollary 3.</b> a^|G| = e for every a in a finite group G.",
        ]),
        ("p", "No board asks for a proof. The idea: the sets aH = {a ∗ h : h ∈ H} (the cosets of H) each contain |H| elements, "
              "and two cosets are either identical or have no element in common. So the cosets split G into pieces of equal "
              "size |H|, and |H| divides |G|."),
        ("p", "Lagrange tells you which orders are possible, not which occur. A group of order 6 can only have subgroups of "
              "order 1, 2, 3 or 6, and elements of order 1, 2, 3 or 6. The converse is false: the group of the 12 even "
              "permutations of {1, 2, 3, 4} has no subgroup of order 6, although 6 divides 12."),

        ("warn", "Common mistakes", [
            "Reading a Cayley table the wrong way round. The entry in row x and column y is x ∗ y. For symmetries, x ∘ y means "
            "do y first; state your convention.",
            "Not checking every axiom. Many candidates forget closure (e.g. {1, 2, 3} under ×₄ gives 2 × 2 = 0) or assume the "
            "identity is the first element listed (in {2, 4, 6, 8} under ×₁₀ the identity is 6).",
            "Claiming associativity “from the table”. Quote a reason (multiplication of numbers, matrix multiplication, "
            "composition of functions), or check it in general.",
            "Saying the order of an element is the power at which it “repeats”. It is the smallest n ≥ 1 with aⁿ = e.",
            "Using Lagrange backwards: a divisor of |G| need not be the order of a subgroup or of an element.",
            "Listing proper subgroups but forgetting {e}, or including G itself.",
            "Thinking (ℤₙ \\ {0}, ×ₙ) is always a group. It is a group only when n is prime.",
        ]),
        ("box", "Given or learn", [
            "Nothing in this unit is in any formula booklet. Learn the four axioms, the definitions of order, cyclic, abelian "
            "and subgroup, and the statement of Lagrange's theorem.",
        ]),
    ],

    "examples": [
        {
            "title": "Proving that an infinite set is a group",
            "question": "The binary operation ∗ is defined on ℝ by a ∗ b = a + b − 3. Show that (ℝ, ∗) is an abelian group.",
            "steps": [
                "Closure: a + b − 3 is a real number for all real a, b.",
                "Associativity: (a ∗ b) ∗ c = (a + b − 3) + c − 3 = a + b + c − 6, and a ∗ (b ∗ c) = a + (b + c − 3) − 3 = "
                "a + b + c − 6. These are equal.",
                "Identity: a ∗ e = a gives a + e − 3 = a, so e = 3. Check: 3 ∗ a = 3 + a − 3 = a too.",
                "Inverse: a ∗ x = 3 gives a + x − 3 = 3, so x = 6 − a, which is real. Check: (6 − a) ∗ a = 3.",
                "Commutative: a ∗ b = a + b − 3 = b + a − 3 = b ∗ a. So (ℝ, ∗) is an abelian group, with identity 3.",
            ],
        },
        {
            "title": "A group from modular arithmetic",
            "question": "Use the Cayley table of G = {1, 2, 3, 4} under ×₅ in Section 7.3. (a) Show that G is a group. "
                        "(b) Find the order of each element. (c) Show that G is cyclic and state its generators. "
                        "(d) Find a proper non-trivial subgroup.",
            "steps": [
                "(a) Closure: every entry is in {1, 2, 3, 4}. Associativity: multiplication of integers is associative, so "
                "multiplication modulo 5 is too. Identity: 1 (its row and column copy the headings).",
                "Inverses: 1 appears once in each row: 1⁻¹ = 1, 2⁻¹ = 3, 3⁻¹ = 2, 4⁻¹ = 4. So G is a group.",
                "(b) 2² = 4, 2³ = 3, 2⁴ = 1, so 2 has order 4. 3² = 4, 3³ = 2, 3⁴ = 1, so 3 has order 4. 4² = 1, so 4 has "
                "order 2. 1 has order 1.",
                "(c) G has order 4 and contains an element of order 4, so G is cyclic. Its generators are 2 and 3.",
                "(d) {1, 4}: closed (4 × 4 = 16 ≡ 1), contains 1, and 4 is self-inverse. Its order 2 divides 4, as Lagrange requires.",
            ],
        },
        {
            "title": "Symmetries of a triangle",
            "question": "Use the Cayley table of D₃ in Section 7.5. (a) Show that D₃ is not abelian. (b) State the order of "
                        "each element. (c) List all the subgroups of D₃. (d) Explain why D₃ is not cyclic, and show that it "
                        "is generated by r and a.",
            "steps": [
                "(a) From the table, r ∘ a = c (row r, column a) but a ∘ r = b. Since r ∘ a ≠ a ∘ r, D₃ is not abelian.",
                "(b) e has order 1. r ∘ r = r² and r ∘ r² = e, so r and r² have order 3. a ∘ a = b ∘ b = c ∘ c = e, so a, b, c "
                "have order 2.",
                "(c) By Lagrange the possible orders are 1, 2, 3, 6. Order 1: {e}. Order 2: {e, a}, {e, b}, {e, c}. "
                "Order 3: {e, r, r²}. Order 6: D₃. A subgroup containing two different reflections also contains their "
                "product (for example a ∘ b = r), a rotation of order 3, and its square, so it has at least 5 elements; its order divides 6, so it is D₃. "
                "There are therefore 6 subgroups.",
                "(d) No element has order 6, so D₃ is not cyclic (also, cyclic groups are abelian). From r and a: "
                "r² = r ∘ r, b = a ∘ r, c = r ∘ a, e = a ∘ a, so every element is a product of r and a.",
            ],
        },
        {
            "title": "Completing a group table",
            "question": "G = {e, a, b, c} is a group of order 4 with identity e, and a ∗ a = b. Complete the Cayley table "
                        "of G and show that G is cyclic.",
            "steps": [
                "The order of a divides 4 (Lagrange), and a ≠ e, a² = b ≠ e, so a has order 4. Then a³ is not e, a or b, "
                "so a³ = c and a⁴ = e. G = {e, a, a², a³} is cyclic, generated by a.",
                "Now every product follows from adding indices modulo 4. For example a ∗ c = a⁴ = e, b ∗ b = a⁴ = e, "
                "b ∗ c = a⁵ = a, c ∗ c = a⁶ = b.",
                "The completed table (rows e, a, b, c; columns e, a, b, c) is: row e: e a b c; row a: a b c e; "
                "row b: b c e a; row c: c e a b.",
                "Check: each row and column is a Latin square line, as it must be. The inverses are e, c, b, a respectively.",
            ],
        },
        {
            "title": "Lagrange's theorem in a group of order 8",
            "question": "G = {1, 3, 5, 7, 9, 11, 13, 15} under multiplication modulo 16 is a group. (a) Find the order of "
                        "each element. (b) Explain why G is not cyclic. (c) Find a cyclic subgroup of order 4 and a "
                        "non-cyclic subgroup of order 4. (d) Explain why G has no subgroup of order 3.",
            "steps": [
                "(a) 3² = 9, 3³ = 27 ≡ 11, 3⁴ = 33 ≡ 1, so 3 has order 4. 5² = 25 ≡ 9 and 9² = 81 ≡ 1, so 5 has order 4. "
                "7² = 49 ≡ 1, 9² ≡ 1 and 15² = 225 ≡ 1, so 7, 9, 15 have order 2. 11² = 121 ≡ 9 and 13² = 169 ≡ 9, so 11 "
                "and 13 have order 4. 1 has order 1.",
                "(b) G has order 8, but no element has order 8, so no element generates G.",
                "(c) ⟨3⟩ = {1, 3, 9, 11} is cyclic of order 4. {1, 7, 9, 15} is closed: 7 × 9 = 63 ≡ 15, 7 × 15 = 105 ≡ 9, "
                "9 × 15 = 135 ≡ 7, and each element is self-inverse. It is a subgroup of order 4 with no element of order 4, "
                "so it is not cyclic.",
                "(d) 3 does not divide |G| = 8, so by Lagrange's theorem there is no subgroup of order 3 (and no element of "
                "order 3).",
            ],
        },
    ],

    "practice": [
        "Let A = {x ∈ ℤ : −2 ≤ x < 3} and B = {x ∈ ℕ : x ≤ 4}. (a) List the elements of A and of B. (b) Find A ∩ B and A ∪ B. "
        "(c) State whether each is true or false: −3 ∈ ℕ₀, 0.5 ∈ ℚ, √2 ∈ ℚ, ℤ ⊂ ℚ.",
        "For each binary operation on ℤ, state whether it is closed, commutative and associative. (a) a ∗ b = a − b. "
        "(b) a ∗ b = a + b + 1. (c) a ∗ b = ab + 1.",
        "The binary operation ∘ is defined on ℝ by a ∘ b = |a − b|. Show that ∘ is commutative but not associative, and "
        "explain why (ℝ, ∘) has no identity element.",
        "Construct the Cayley table for {0, 2, 4, 6, 8} under addition modulo 10. Show that it is a group, state the "
        "inverse of each element and show that the group is cyclic.",
        "Show that {1, 5, 7, 11} under multiplication modulo 12 is a group. Find the order of each element and explain why "
        "the group is not cyclic.",
        "The set {2, 4, 6, 8} under multiplication modulo 10 is a group. (a) Construct its Cayley table. (b) State the "
        "identity and the inverse of each element. (c) Find all the generators.",
        "Explain why each of these is not a group. (a) {1, 2, 3} under ×₄. (b) {0, 1, 2, 3} under ×₄. (c) ℤ under ×. "
        "(d) ℕ under +.",
        "For (ℤ₈, +₈), find the order of each element and list all its subgroups.",
        "G = {1, 2, 3, 4, 5, 6} under multiplication modulo 7. (a) Find the order of each element. (b) State the generators "
        "of G. (c) Find the subgroups of order 2 and 3.",
        "ω = e^(2πi/3). (a) Show that {1, ω, ω²} is a group under multiplication of complex numbers. (b) For the group "
        "{1, i, −1, −i} under multiplication, find the order of each element and state the generators.",
        "A = (0 −1; 1 −1). (a) Find A² and A³. (b) Show that {I, A, A²} is a group under matrix multiplication and state "
        "the inverse of A. (c) Explain why the group is cyclic and state its generators.",
        "G is a group of order 21. (a) State the possible orders of elements of G. (b) Can G have a subgroup of order 6? "
        "(c) H is a subgroup of G that contains an element of order 7 and an element of order 3. Show that H = G. "
        "(d) Explain why every group of order 7 is cyclic.",
    ],
    "answers": [
        "(a) A = {−2, −1, 0, 1, 2}; B = {1, 2, 3, 4}. (b) A ∩ B = {1, 2}; A ∪ B = {−2, −1, 0, 1, 2, 3, 4}. "
        "(c) False, true, false, true.",
        "(a) Closed; not commutative (1 − 2 ≠ 2 − 1); not associative ((3 − 2) − 1 = 0, 3 − (2 − 1) = 2). "
        "(b) Closed, commutative, associative (both brackets give a + b + c + 2). "
        "(c) Closed, commutative; not associative: (1 ∗ 2) ∗ 3 = 3 ∗ 3 = 10 but 1 ∗ (2 ∗ 3) = 1 ∗ 7 = 8.",
        "|a − b| = |b − a|, so commutative. (1 ∘ 2) ∘ 3 = |1 − 3| = 2 but 1 ∘ (2 ∘ 3) = |1 − 1| = 0, so not associative. "
        "An identity e would need |a − e| = a for all a; for a = −1 this is impossible since |−1 − e| ≥ 0 > −1.",
        "Rows are cyclic shifts: row 2 is 2 4 6 8 0, etc. Closed, associative (addition), identity 0, inverses 0↔0, 2↔8, "
        "4↔6. 2 has order 5 (2, 4, 6, 8, 0), so it generates the group: cyclic of order 5 (every non-zero element generates it).",
        "Table: row 1: 1 5 7 11; row 5: 5 1 11 7; row 7: 7 11 1 5; row 11: 11 7 5 1. Closed, associative (multiplication), "
        "identity 1, each element self-inverse. Orders: 1 has order 1; 5, 7, 11 have order 2. No element of order 4, so not cyclic.",
        "(a) Row 2: 4 8 2 6; row 4: 8 6 4 2; row 6: 2 4 6 8; row 8: 6 2 8 4 (columns 2, 4, 6, 8). "
        "(b) Identity 6 (6 × 2 = 12 ≡ 2, etc.). Inverses: 2↔8 (16 ≡ 6), 4↔4 (16 ≡ 6), 6↔6. "
        "(c) 2: 2, 4, 8, 6 has order 4; 8: 8, 4, 2, 6 has order 4. Generators 2 and 8 (4 has order 2).",
        "(a) Not closed: 2 × 2 = 4 ≡ 0 ∉ {1, 2, 3}. (b) 0 (and 2) have no inverse: no x gives 0x ≡ 1. "
        "(c) 2 has no inverse in ℤ. (d) No identity (0 ∉ ℕ) and no inverses.",
        "Orders: 0 → 1; 4 → 2; 2, 6 → 4; 1, 3, 5, 7 → 8. Subgroups: {0}, {0, 4}, {0, 2, 4, 6}, ℤ₈.",
        "(a) 1: 1; 2: 3 (2, 4, 1); 3: 6 (3, 2, 6, 4, 5, 1); 4: 3; 5: 6; 6: 2. (b) Generators 3 and 5. "
        "(c) Order 2: {1, 6}. Order 3: {1, 2, 4}.",
        "(a) ω³ = 1 so ω·ω = ω², ω·ω² = 1, ω²·ω² = ω⁴ = ω: closed. Associative (complex multiplication), identity 1, "
        "inverses 1↔1, ω↔ω². (b) 1: order 1; −1: order 2; i and −i: order 4. Generators i and −i.",
        "(a) A² = (−1 1; −1 0), A³ = (1 0; 0 1) = I. (b) Products are powers of A with A³ = I, so closed; matrix "
        "multiplication is associative; identity I; inverses A⁻¹ = A², (A²)⁻¹ = A, I⁻¹ = I. "
        "(c) A has order 3, equal to the order of the group, so the group is ⟨A⟩ and is cyclic; generators A and A².",
        "(a) 1, 3, 7, 21. (b) No: 6 does not divide 21. (c) |H| divides 21 and is a multiple of both 7 and 3 (orders of "
        "elements of H divide |H|), so |H| = 21 and H = G. (d) 7 is prime: any a ≠ e has order dividing 7, so order 7, and generates G.",
    ],

    "exam": [
        "The set G = {1, 3, 7, 9} is combined under multiplication modulo 10.\n"
        "(a) Construct the Cayley table for G. [2]\n"
        "(b) Show that G is a group. You may assume that multiplication modulo 10 is associative. [3]\n"
        "(c) Find the order of each element of G. [2]\n"
        "(d) Explain why G is cyclic, stating all its generators. [2]\n"
        "(e) Write down the proper subgroups of G. [2]",
        "The binary operation ∗ is defined on S = ℝ \\ {−1} by a ∗ b = a + b + ab.\n"
        "(a) Show that S is closed under ∗. [3]\n"
        "(b) Show that ∗ is associative. [2]\n"
        "(c) Find the identity element and an expression for the inverse of a. [3]\n"
        "(d) State, with a reason, whether (S, ∗) is abelian. [1]\n"
        "(e) Find the element of order 2 in (S, ∗). [2]",
        "The group D₃ of symmetries of an equilateral triangle has the Cayley table given in Section 7.5 (x ∘ y means do y, "
        "then x).\n"
        "(a) Explain why D₃ has exactly six elements. [1]\n"
        "(b) Find the inverse of each element. [2]\n"
        "(c) Find a ∘ r ∘ a and hence describe a ∘ r ∘ a as a single symmetry. [2]\n"
        "(d) List all the subgroups of D₃. [3]\n"
        "(e) Use Lagrange's theorem to explain why D₃ has no subgroup of order 4, and why D₃ is not cyclic. [2]",
        "The group G is (ℤ₁₂, +₁₂).\n"
        "(a) Find the order of the element 8. [1]\n"
        "(b) Find all the generators of G. [2]\n"
        "(c) List all the subgroups of G. [4]\n"
        "(d) Show that {0, 4, 8} ∪ {0, 6} is not a subgroup of G. [1]\n"
        "(e) A group H has order 12. State, with a reason, whether H must contain an element of order 12, and whether it "
        "could contain an element of order 5. [2]",
    ],
    "exam_answers": [
        "(a) Row 1: 1 3 7 9; row 3: 3 9 1 7; row 7: 7 1 9 3; row 9: 9 7 3 1 (columns 1, 3, 7, 9). B2 (B1 for one error). "
        "(b) All entries in G: closed B1. Identity 1 B1. Inverses 1⁻¹ = 1, 3⁻¹ = 7, 7⁻¹ = 3, 9⁻¹ = 9, with associativity given, so "
        "G is a group B1. (c) 1: 1; 3: 4; 7: 4; 9: 2 B2. (d) 3 has order 4 = |G|, so G is cyclic B1; generators 3 and 7 B1. "
        "(e) {1} and {1, 9} B2 (B1 each).",
        "(a) a + b + ab = (1 + a)(1 + b) − 1 M1. Since a ≠ −1 and b ≠ −1, (1 + a)(1 + b) ≠ 0 A1, so a ∗ b ≠ −1 and a ∗ b ∈ S A1. "
        "(b) (a ∗ b) ∗ c = (a + b + ab) + c + (a + b + ab)c = a + b + c + ab + bc + ca + abc M1, and a ∗ (b ∗ c) gives the same, "
        "so associative A1. (c) a ∗ e = a ⇒ e(1 + a) = 0 ⇒ e = 0 B1. a + x + ax = 0 ⇒ x = −a/(1 + a) M1 A1 (and x ≠ −1 since "
        "that would need 0 = −1). (d) Abelian, since a + b + ab is symmetric in a and b B1. "
        "(e) a ∗ a = 0 ⇒ 2a + a² = 0 ⇒ a = 0 or −2 M1; a = −2 (a = 0 is the identity) A1.",
        "(a) 3 rotations (0°, 120°, 240°) and 3 reflections; any symmetry is fixed by where it sends corner A (3 choices) "
        "and whether it keeps or reverses the order of the corners (2 choices) B1. (b) e⁻¹ = e, r⁻¹ = r², (r²)⁻¹ = r, a, b, c "
        "self-inverse B2. (c) a ∘ r = b (row a, column r) M1, so a ∘ r ∘ a = b ∘ a = r², the 240° rotation A1. "
        "(d) {e}, {e, a}, {e, b}, {e, c}, {e, r, r²}, D₃ B3 (B2 for 5, B1 for 3–4). "
        "(e) 4 does not divide 6, so no subgroup of order 4 B1. No element of order 6 (orders are 1, 2, 3), so not cyclic B1.",
        "(a) 8, 4, 0: order 3 B1. (b) Generators are k with hcf(k, 12) = 1: 1, 5, 7, 11 B2. "
        "(c) {0}, {0, 6}, {0, 4, 8}, {0, 3, 6, 9}, {0, 2, 4, 6, 8, 10}, ℤ₁₂ B4 (B3 for five correct, B2 for four, B1 for three). "
        "(d) 4 + 6 = 10 is not in {0, 4, 6, 8}, so not closed B1. "
        "(e) Not necessarily: the symmetries of a regular hexagon form a non-abelian group of order 12, which is not cyclic B1; "
        "no element of order 5, since 5 does not divide 12 (Lagrange) B1.",
    ],
}
