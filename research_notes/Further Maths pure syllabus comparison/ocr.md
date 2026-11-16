# OCR Further Mathematics: pure components (OCR A H245/H235 and OCR B MEI H645/H635)

Method: the current specification PDFs and formulae booklets were downloaded straight from ocr.org.uk on 17 Nov 2026 and converted to text with pdftotext. Every code and statement below is taken from those PDFs. Statement wording is shortened. Notes in square brackets are OCR's own exclusions.

**Source documents (exact URLs)**
- OCR A, A Level H245 specification, Version 2 (October 2025): https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf
- OCR A, AS H235 specification, Version 2 (October 2025): https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf
- OCR B (MEI), A Level H645 specification, Version 2.1 (March 2026): https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf
- OCR B (MEI), AS H635 specification, Version 2 (October 2025): https://www.ocr.org.uk/Images/308764-specification-accredited-as-level-gce-further-mathematics-b-mei-h635.pdf
- H245 Formulae Booklet, latest copy on the assessment page (CST322, © OCR 2022): https://www.ocr.org.uk/Images/752529-formulae-booklet-a-level-further-mathematics-a.pdf (the same booklet is also at https://www.ocr.org.uk/Images/308765-a-level-further-mathematics-a-formulae-booklet.pdf)
- H235 AS Formulae Booklet (© OCR 2020): https://www.ocr.org.uk/Images/752815-formulae-booklet.pdf
- Qualification pages: https://www.ocr.org.uk/qualifications/as-and-a-level/further-mathematics-a-h235-h245-from-2017/ and https://www.ocr.org.uk/qualifications/as-and-a-level/further-mathematics-b-mei-h635-h645-from-2017/

---

## Every spec reference/sub-point for each pure component

### Takeaway
OCR A uses one Pure Core (codes 4.01a–4.10h), examined by both Y540 and Y541. AS Y531 is the "Stage 1" subset of that same core. The optional Additional Pure (Y545) uses codes 8.01a–8.06b. MEI Core Pure (Y420) uses codes P*, and its "(a)" sections make up AS Core Pure Y410. MEI Extra Pure (Y435) uses codes X* and covers recurrence relations, groups, eigenvalues/eigenvectors and multivariable calculus. Unlike OCR A Y545, it has no number theory, no further vectors and no arc length or surface area.

### Cited Findings

#### A. OCR A H245: Pure Core (Y540 and Y541) — codes 4.01–4.10
- Both papers "assess content from the whole of the Pure Core". The content table has a "Stage 1" column, which is the content shared with AS H235, and a "Stage 2" column, which is A Level only. In each section OCR lists the Stage 1 statements first. — [H245 spec](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- How AS/A Level status was found: AS = the codes that appear in the H235 Y531 table. The H235 Y531 codes are: 4.01a; 4.02a, b, c, e, f, g, h, i, j, k, l, o, p; 4.03a–4.03r; 4.04a, c, e, g; 4.05a, b. Every other 4.xx code is A Level only (Stage 2). — [H235 spec](https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf); [H245 spec](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)

Status key: **AS** = in Y531 and H245 (Stage 1); **A** = H245 only (Stage 2). All statements are from the [H245 spec](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf), pp.15–35.

**4.01 Proof**
- 4.01a (AS): construct proofs by mathematical induction, e.g. divisibility, powers of matrices, results on powers, exponentials and factorials.
- 4.01b (A): more demanding induction proofs, including conjecture followed by proof, and sums of series and inequalities (e.g. n! < nⁿ; nth derivative of x²eˣ).

**4.02 Complex Numbers**
- 4.02a (AS): language of complex numbers: real part, imaginary part, conjugate, modulus, argument.
- 4.02b (AS): cartesian form x+iy and modulus-argument form r(cosθ+i sinθ) = [r,θ] = r cis θ.
- 4.02c (AS): notation z, z*, Re, Im, arg, |z|. A complex number is zero iff both parts are zero. The principal argument may lie in [0,2π) or (−π,π].
- 4.02d (A): exponential form re^{iθ}.
- 4.02e (AS): arithmetic (+, −, ×, ÷) in cartesian and modulus-argument forms.
- 4.02f (AS): convert between cartesian and modulus-argument forms.
- 4.02g (AS): complex roots of real polynomials occur in conjugate pairs.
- 4.02h (AS): find the two square roots of a complex number algebraically.
- 4.02i (AS): solve real quadratics that have complex roots.
- 4.02j (AS): use conjugate pairs and the factor theorem to solve or factorise real cubics and quartics. Enough information is given to find a root or quadratic factor.
- 4.02k (AS): use and interpret Argand diagrams (real axis, imaginary axis).
- 4.02l (AS): geometric effect of conjugation, addition and subtraction.
- 4.02m (A): geometric effect of multiplication and division, including positive integer powers.
- 4.02n (A): Euler's formula e^{iθ} = cosθ + i sinθ.
- 4.02o (AS): loci and regions on an Argand diagram: |z−a| = k, arg(z−a) = β, Re(z) = k, Im(z) = k, |z−a| = |z−b|, and the inequalities based on these. Dashed lines exclude a boundary, solid lines include it.
- 4.02p (AS): set notation for loci.
- 4.02q (A): de Moivre's theorem. Use it for multiple-angle formulae (e.g. sin3θ), for powers of sin and cos written in terms of multiple angles, for sums of trigonometric or exponential series, and with sinθ = (e^{iθ}−e^{−iθ})/2i.
- 4.02r (A): the n distinct nth roots of re^{iθ} form the vertices of a regular n-gon.
- 4.02s (A): use roots of unity to solve geometric problems, including sums of roots of unity.

**4.03 Matrices**
- 4.03a (AS): language: conformable, equal, square, m×n, determinant, zero/null, transpose, identity. Real and complex matrices.
- 4.03b (AS): add, subtract and multiply matrices, including scalar multiplication and positive integer powers. Numerical work may be done on a calculator.
- 4.03c (AS): multiplication is associative but not commutative.
- 4.03d (AS): 2-D linear transformations: reflection in the axes and in y = ±x, rotation about O, enlargement centre O, stretch parallel to an axis, shear parallel to an axis.
- 4.03e (AS): successive transformations. AB means B first, then A.
- 4.03f (AS): 3-D transformations, limited to reflection in x = 0, y = 0 or z = 0 and rotation about a coordinate axis.
- 4.03g (AS): invariant points and lines, and the difference between an invariant line and a line of invariant points. [3-D excluded]
- 4.03h (AS): 2×2 determinant, with and without a calculator.
- 4.03i (AS): the 2×2 determinant is the area scale factor, and its sign shows orientation.
- 4.03j (AS): 3×3 determinant, with and without a calculator.
- 4.03k (AS): the 3×3 determinant is the volume scale factor, and its sign shows orientation.
- 4.03l (AS): singular and non-singular matrices.
- 4.03m (AS): det(AB) = det A × det B.
- 4.03n (AS): inverse of a 2×2 matrix, with and without a calculator.
- 4.03o (AS): inverse of a 3×3 matrix, with and without a calculator.
- 4.03p (AS): properties of inverses, e.g. (AB)⁻¹ = B⁻¹A⁻¹.
- 4.03q (AS): inverse matrices correspond to inverse transformations.
- 4.03r (AS): solve 2 or 3 linear simultaneous equations with an inverse matrix when there is a unique solution.
- 4.03s (A): when there is no unique solution, decide between consistent (infinitely many solutions) and inconsistent (no solutions). [Finding the infinite solution set excluded]
- 4.03t (A): interpret the solution, or lack of one, as the arrangement of three planes, including parallel cases. [Line of intersection excluded]

**4.04 Further Vectors**
- 4.04a (AS): line equations in 2-D and 3-D, cartesian and vector form, r = a + λb.
- 4.04b (A): plane equations: ax+by+cz = d, r = a+λb+μc, (r−a)·n = 0, r·n = p.
- 4.04c (AS): scalar product; angle between vectors or lines; test for perpendicularity.
- 4.04d (A): angle between two planes, and between a line and a plane.
- 4.04e (AS): point of intersection of two lines; decide whether lines intersect, are parallel or are skew.
- 4.04f (A): intersection of a line and a plane.
- 4.04g (AS): vector product, used to find a vector perpendicular to two given vectors. A calculator or the given formula may be used. [Magnitude of the vector product excluded]
- 4.04h (A): distance between parallel lines; shortest distance between skew lines (formula given).
- 4.04i (A): shortest distance from a point to a line (2-D formula given).
- 4.04j (A): shortest distance from a point to a plane (formula given).

**4.05 Further Algebra**
- 4.05a (AS): symmetric functions of roots and coefficients, up to quartics.
- 4.05b (AS): use a substitution to get an equation with related roots (cubic or higher).
- 4.05c (A): partial fractions with ax²+c factors (c > 0) in the denominator and improper fractions.

**4.06 Series** (all A)
- 4.06a: standard formulae for Σr, Σr², Σr³. The Σr² and Σr³ formulae are given, but proofs may be asked for.
- 4.06b: method of differences for finite and infinite series, including with partial fractions.

**4.07 Hyperbolic Functions** (all A)
- 4.07a: definitions of sinh, cosh, tanh in terms of exponentials, with domain and range.
- 4.07b: graphs.
- 4.07c: cosh²x − sinh²x ≡ 1. [Prior knowledge of other identities excluded]
- 4.07d: differentiate and integrate hyperbolic functions.
- 4.07e: inverse hyperbolic functions, with domains and ranges.
- 4.07f: derive and use the logarithmic forms (sinh⁻¹, arsinh notation).

**4.08 Further Calculus** (all A)
- 4.08a: Maclaurin series, including the general term.
- 4.08b: standard series for eˣ, sin x, cos x, ln(1+x), (1+x)ⁿ and functions built from them, with their intervals of validity. [Proof of validity and complex x excluded]
- 4.08c: improper integrals, where the integrand is undefined in the interval or the range is infinite.
- 4.08d: volumes of revolution about either axis, including between two curves and for parametric curves.
- 4.08e: mean value of a function.
- 4.08f: integration by partial fractions.
- 4.08g: derive and use the derivatives of sin⁻¹, cos⁻¹, tan⁻¹, sinh⁻¹, cosh⁻¹, tanh⁻¹.
- 4.08h: integrate 1/√(a²−x²), 1/(a²+x²), 1/√(x²+a²), 1/√(x²−a²) and use trigonometric or hyperbolic substitutions.

**4.09 Polar Coordinates** (all A)
- 4.09a: polar coordinates (r ≥ 0) and conversion to and from cartesian.
- 4.09b: sketch r = f(θ), showing symmetry and least and greatest r.
- 4.09c: area ½∫r² dθ.

**4.10 Differential Equations** (all A)
- 4.10a: general and particular solutions.
- 4.10b: modelling in kinematics and other contexts, including Newton's second law and variable force. [Variable mass and a = v dv/dx excluded]
- 4.10c: integrating factor e^{∫P dx} for dy/dx + P(x)y = Q(x).
- 4.10d: y'' + ay' + by = 0 by the auxiliary equation, covering distinct real, repeated and complex roots.
- 4.10e: non-homogeneous equations: complementary function plus particular integral, for polynomial, exponential or trigonometric f(x), including when the CF affects the trial PI.
- 4.10f: SHM ẍ = −ω²x; x = A cos ωt + B sin ωt and x = R sin(ωt+φ).
- 4.10g: damped oscillations: under-, over- and critical damping.
- 4.10h: coupled first-order linear systems dx/dt = ax+by+f(t), dy/dt = cx+dy+g(t), solved by elimination (e.g. predator–prey).

#### B. OCR A H235: AS Pure Core (Y531)
- Y531 contains exactly the Stage 1 codes listed above: proof 4.01a; complex numbers (no exponential form, de Moivre or roots of unity); all of matrices 4.03a–r; vectors 4.04a, c, e, g (lines, scalar product, line–line intersection, vector product); roots of polynomials 4.05a, b. There are no series, hyperbolic functions, calculus, polar coordinates or differential equations at AS. — [H235 spec](https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf)
- AS H235 also has an Additional Pure option (Y535), using a Stage 1 subset of the 8.xx codes: 8.01a–f, h; 8.02a–f, i–k; 8.03a–i; 8.04a–d; 8.05a, c, d, e. — [H235 spec](https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf)

#### C. OCR A H245: Additional Pure Mathematics (Y545) — codes 8.01–8.06
Status shows whether the statement is also in AS Y535 (Stage 1). Source: [H245 spec](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf), pp.77–87. Assumed knowledge is all of Pure Core Y540/Y541.

**8.01 Sequences and Series**
- 8.01a: sequences given by recurrence relations or closed form uₙ = f(n).
- 8.01b: induction proofs for sequences and series.
- 8.01c: behaviour of sequences: periodic, convergent, divergent, oscillating, monotonic.
- 8.01d: limits as n → ∞ and steady states. [Rates of convergence excluded]
- 8.01e: Fibonacci, Lucas and similar sequences; properties of φ.
- 8.01f (AS): solve first-order linear recurrences uₙ₊₁ = auₙ + f(n), where f is a polynomial or dkⁿ, using the auxiliary equation and CF.
- 8.01g (A): solve second-order linear recurrences, with distinct, repeated or complex roots, homogeneous or non-homogeneous.
- 8.01h (AS): modelling with recurrences (birth and death rates, INT(x)).
- 8.01i (A): second-order recurrence modelling.

**8.02 Number Theory**
- 8.02a: number bases.
- 8.02b: divisibility tests for 2, 3, 4, 5, 8, 9, 11.
- 8.02c: build tests for other primes below 50.
- 8.02d: division algorithm a = bq + r.
- 8.02e (AS): modular arithmetic.
- 8.02f (AS): single linear congruences ax ≡ b (mod n).
- 8.02g (A): quadratic residues.
- 8.02h (A): simultaneous linear congruences, at most 3 (Chinese remainder theorem allowed but not required).
- 8.02i (AS): primes, composites, hcf, coprimality; fundamental theorem of arithmetic (no proof).
- 8.02j (AS): a|b and a|c ⇒ a|(bx+cy).
- 8.02k (AS): Euclid's lemma.
- 8.02l (A): Fermat's little theorem in both forms, and pseudo-primes. [Proof and Carmichael numbers excluded]
- 8.02m, 8.02n (A): order of a modulo p, which divides p−1.
- 8.02o (A): (a+b)^p ≡ a^p + b^p (mod p) by the binomial theorem.

**8.03 Groups**
- 8.03a: binary operations, associativity, commutativity.
- 8.03b: Cayley tables.
- 8.03c: group definition (integers mod n, functions, matrices, transformations, symmetries, complex numbers); identity, closure, abelian.
- 8.03d: Latin square property.
- 8.03e: order of a group and of an element; the order of an element divides the order of the group.
- 8.03f: subgroups and proper subgroups.
- 8.03g: cyclic groups.
- 8.03h: generators, including non-cyclic groups generated by two or more elements.
- 8.03i (AS): structure of finite groups up to order 7.
- 8.03j (A): groups of higher finite order or of infinite order.
- 8.03k (A): Lagrange's theorem (statement, no proof).
- 8.03l (A): isomorphism by informal methods.
- 8.03m (A): abstract groups defined by their algebraic properties.

**8.04 Further Vectors**
- 8.04a (AS): vector product defined geometrically, |a||b| sinθ n̂ (right-handed triple), and in components.
- 8.04b (AS): anti-commutative and distributive.
- 8.04c (AS): areas of triangles and parallelograms.
- 8.04d (AS): significance of a×b = 0, and the line (r−a)×d = 0.
- 8.04e (A): scalar triple product a·(b×c); volumes of tetrahedra and parallelepipeds; meaning of a·(b×c) = 0.

**8.05 Surfaces and Partial Differentiation**
- 8.05a (AS): z = f(x,y) and g(x,y,z) = c as 3-D surfaces.
- 8.05b (A): more than two variables, and trigonometric, logarithmic and exponential functions.
- 8.05c (AS): sections and contours.
- 8.05d (AS): first and second partial derivatives, mixed derivatives, f_xy = f_yx.
- 8.05e (AS): stationary points where f_x = f_y = 0. Find them only; their nature is not required at AS.
- 8.05f (A): classify stationary points with the Hessian determinant.
- 8.05g (A): tangent plane z = f(a,b) + (x−a)f_x + (y−b)f_y.

**8.06 Further Calculus** (A)
- 8.06a: reduction formulae.
- 8.06b: arc lengths and surface areas of revolution, cartesian and parametric.

#### D. MEI H645: Core Pure (Y420)
- In the content table, sections labelled "(a)" are the same content as AS Core Pure Y410, and sections labelled "(b)" are A Level only. Y420 adds the vector product (Pv7, Pv8) to the DfE content. Statements marked "*" are unnumbered. — [H645 spec](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf), pp.18–34
- How the codes work: only the first code on each page carries the "P" prefix (e.g. Pj1, then j2, j3…). Read j2 as Pj2. — [H645 spec](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)

Status: (a) = AS Y410 and A Level Y420; (b) = Y420 only.
- **Proof (a)**: * proof by deduction and exhaustion, and disproof by counter-example. Pp4: induction for given results on the nth term of a sequence, the sum of a series, or the nth power of a matrix.
- **Proof (b)**: * proof by contradiction. Pp5: induction in general, e.g. divisibility or de Moivre.
- **Complex Numbers (a)**:
  - Pj1: language of complex numbers.
  - Pj2: solve any real quadratic.
  - Pj3: conjugate roots; solve real cubics and quartics.
  - Pj4: arithmetic in x+yi.
  - Pj5: zero iff both parts are zero.
  - Pj6: radians.
  - Pj7: modulus-argument form, zz* = |z|², principal argument in (−π, π].
  - Pj8: multiply and divide in modulus-argument form.
  - Pj9: Argand diagram and conjugates.
  - Pj10: sum, difference, product and quotient on an Argand diagram.
  - Pj11: loci |z−a| = r, arg(z−a) = θ, |z−a| = |z−b|, regions, and their intersections and unions. [Exclusion: |z−a| = k|z−b|, k ≠ 1]
- **Complex Numbers (b)**:
  - Pj12: de Moivre.
  - Pj13: multiple angles (e.g. tan4θ) and series such as ΣⁿCᵣ cos rθ.
  - Pj14: e^{iθ} and re^{iθ}.
  - Pj15–Pj17: nth roots form a regular n-gon; formula for the roots; why the roots sum to zero.
  - Pj18: multiplication as enlargement plus rotation.
  - Pj19: roots of unity.
  - Pj20: geometric problems.
- **Matrices and transformations (a)**:
  - Pm1: matrix arithmetic up to 3×3, with and without a calculator.
  - Pm2: zero and identity matrices.
  - Pm3: associative but not commutative.
  - Pm4: 2-D transformations (reflection, rotation, enlargement, stretch, shear); 3-D reflections in x = 0, y = 0, z = 0, and rotations by multiples of 90° about an axis.
  - Pm5: successive 2-D transformations.
  - Pm6: invariant points and lines (2-D).
  - Pm7: 2×2 and 3×3 determinants (3×3 with a calculator); singular and non-singular.
  - Pm8: 2×2 determinant as area scale factor, with orientation.
  - Pm9: 3×3 determinant as volume scale factor, with orientation.
  - Pm10: det(MN) = det M det N.
  - Pm11–Pm14: inverses (3×3 with a calculator), inverse transformations, (AB)⁻¹ = B⁻¹A⁻¹.
  - Also an unnumbered statement (*) on the language of vectors in 2-D and 3-D.
- **Matrices and transformations (b)**: Pm15: 3×3 determinant and inverse without a calculator, possibly with algebraic terms.
- **Vectors and 3-D space (a)**:
  - Pv1: scalar product and angles.
  - Pv2: plane equations (r−a)·n = 0 and n₁x+n₂y+n₃z+d = 0. [The form r = a+λb+μc is excluded]
  - Pv3: a normal is perpendicular to every vector in the plane.
  - Pv4: arrangements of three planes (sheaf, prism, etc.).
  - Pv5: solve 3×3 linear systems with an inverse matrix and interpret them geometrically. [Finding the line of intersection excluded]
  - Pv6: angle between two planes.
- **Vectors and 3-D space (b)**:
  - Pv7: vector product in components (formula given).
  - Pv8: |a||b| sinθ n̂; meaning of a×b = 0.
  - Pv9: line equations in 2-D and 3-D.
  - Pv10: angle between two lines.
  - Pv11–Pv12: intersecting, parallel or skew lines, and the point of intersection.
  - Pv13: distance between parallel lines; skew-line distance (formula given).
  - Pv14: intersection of a line and a plane.
  - Pv15: angle between a line and a plane.
  - Pv16: point-to-line distance, 2-D or 3-D (2-D formula given).
  - Pv17: point-to-plane distance (formula given).
- **Algebra (a)**: Pa1: roots and coefficients for quadratics, cubics and quartics. Pa2: new equation by a linear transformation of the roots (cubic or quartic). [Non-linear transformations of roots excluded]
- **Series (a)**: Ps1: Σr, Σr², Σr³ and the method of differences.
- **Series (b)**:
  - * sequence vs series; meaning of convergence.
  - Ps2: summation with partial fractions.
  - Ps3: Maclaurin series with general term; approximation error.
  - Ps4: limited range of convergence.
  - Ps5: standard series for eˣ, ln(1+x), sin, cos, (1+x)ⁿ with their validity. [Proof of convergence and complex x excluded]
- **Calculus (b)**:
  - Pc1: improper integrals.
  - Pc2: volumes of revolution about the x- or y-axis. [Other axes excluded]
  - Pc3: mean value.
  - Pc4: partial fractions in integration, with an ax²+c factor and one linear term.
  - * definitions of the inverse trigonometric functions.
  - Pc5: differentiate the inverse trigonometric functions.
  - Pc6: integrals of (a²−x²)^−½ and (a²+x²)⁻¹ by trigonometric substitution (formulae given).
- **Polar coordinates (b)**: PP1: polar coordinates and conversion. PP2: sketch curves, e.g. r = a(1+cosθ), r = a cos2θ. PP3: area ½∫r² dθ.
- **Hyperbolic functions (b)**:
  - Pa3: definitions, domains, ranges, graphs.
  - Pa4: cosh²x − sinh²x = 1. [Other identities excluded]
  - Pa5: differentiate and integrate.
  - Pa6: inverse hyperbolic functions.
  - Pa7: derive and use the logarithmic forms.
  - Pa8: integrals of (x²+a²)^−½ and (x²−a²)^−½.
- **Differential equations (b)**:
  - Pp19–Pp22: modelling. Define variables, form equations from verbal descriptions, kinematics language including a = v dv/dx, * Newton's second law F = ma. [Variable mass excluded]
  - Pc7: general and particular solutions.
  - Pc8–Pc10: integrating factor.
  - Pc11–Pc12: second-order homogeneous equations by the auxiliary equation (discriminant >0, =0, <0).
  - Pc13–Pc14: non-homogeneous equations with CF + PI (polynomial, trigonometric, exponential f(x)).
  - Pc15: SHM.
  - Pc16–Pc17: damped oscillations (over, critical, under).
  - Pc18: coupled first-order simultaneous linear equations (predator–prey).

#### E. MEI H635: AS Core Pure (Y410)
- Y410 "is the same as one third of the Core Pure (Y420) content", namely the "(a)" sections: Pp4; Pj1–Pj11; Pm1–Pm14; Pv1–Pv6; Pa1–Pa2; Ps1. Assumed knowledge is AS Level Mathematics. — [H635 spec](https://www.ocr.org.uk/Images/308764-specification-accredited-as-level-gce-further-mathematics-b-mei-h635.pdf); [H645 spec](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- **Correction to the brief:** in H635, **Y411 is Mechanics a**, not a pure paper. The AS options are Y411 Mechanics a, Y412 Statistics a, Y413 Modelling with Algorithms and Y414 Numerical Methods. MEI AS has **no** pure option equivalent to Extra Pure. — [H635 spec](https://www.ocr.org.uk/Images/308764-specification-accredited-as-level-gce-further-mathematics-b-mei-h635.pdf)

#### F. MEI H645: Extra Pure (Y435), a minor option
Source: [H645 spec](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf), pp.113–121. Assumed knowledge is A Level Mathematics plus Core Pure Y420. This paper is A Level only.
- **Recurrence relations**:
  - Xs1: modelling with recurrence relations.
  - Xs2: language: limit, convergent, divergent, periodic, oscillating, linear/non-linear, homogeneous, general and particular solution.
  - Xs3: investigate long-run behaviour, possibly non-linear. [Rates of convergence excluded]
  - Xs4: verify a given solution.
  - Xs5: first-order homogeneous.
  - Xs6: first-order non-homogeneous, where f(n) is constant, linear, quadratic or dkⁿ.
  - Xs7: second-order homogeneous, with distinct, repeated or complex roots.
  - Xs8: second-order non-homogeneous.
  - Xs9: properties of solutions, e.g. proving a limit. [Generating functions excluded]
- **Groups**:
  - XS1–XS2: set language and number-set notation (N, Z, Q, R, C, N₀, Q⁺, R⁺₀).
  - Xa1: group axioms, finite or infinite.
  - Xa2: examples (symmetries, modular arithmetic, matrices, complex numbers, integers under +) and group tables.
  - Xa3: cyclic groups and generators. [Infinite cyclic groups excluded]
  - Xa4: order of a group and of an element.
  - Xa5: subgroups, including proper and non-trivial.
  - Xa6: Lagrange's theorem and its corollary. [Proof excluded]
  - Xa7–Xa8: isomorphism, e.g. groups of order 6; cyclic groups of the same order are isomorphic.
- **Matrices**:
  - Xm1: eigenvalues and eigenvectors for 2×2 and 3×3 matrices (real eigenvalues).
  - Xm2: characteristic equation det(M−λI) = 0.
  - Xm3: diagonalisation (distinct real eigenvalues).
  - Xm4: powers through the diagonal form.
  - Xm5: Cayley–Hamilton theorem, e.g. for powers or the inverse. [Proof excluded]
  - Xm6: eigenvalues and eigenvectors in 2-D and 3-D transformations, e.g. finding the plane of a reflection.
- **Multivariable calculus**:
  - Xc1: z = f(x,y) as a surface.
  - Xc2: contours and sections.
  - Xc3: first-order partial derivatives. [Second and higher order excluded]
  - Xc4: stationary points from ∂z/∂x = ∂z/∂y = 0. If their nature is asked for, the method is given.
  - Xc5: g(x,y,z) = c as a surface.
  - Xc6: grad g as a normal vector.
  - Xc7: normal line and tangent plane.
- Also note: the MEI minor option Further Pure with Technology (Y436) is being withdrawn. The final first teaching date is September 2026, the final assessment is Summer 2028, and there is no resit. — [H645 spec v2.1](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)

### Inferences
- **Main structural differences.** OCR A puts all A Level core pure into two equal 75-mark papers. MEI puts it into one 144-mark paper.
- **Vectors.** Both boards include the vector product in the core. OCR A puts it at AS (4.04g). MEI puts it only in the (b) part (Pv7–Pv8), so MEI AS has no vector product and no line equations.
- **OCR A Y545 vs MEI Y435.** They share recurrence relations, groups and partial differentiation and surfaces. Y545 alone has number theory, the scalar triple product, the Hessian classification, reduction formulae and arc length and surface area. Y435 alone has eigenvalues and eigenvectors, diagonalisation, Cayley–Hamilton and grad/normal lines.
- **Depth of partial differentiation.** Y435 excludes second-order partial derivatives (Xc3), while Y545 requires them (8.05d, 8.05f).
- **Weight.** Y545 is a full 25% option. Y435 is a 16⅔% minor option.

### Gaps
- Mathematical symbols in the PDF text extraction were partly garbled (symbol fonts). Statements were paraphrased from the readable text. Exact typography should be checked against the PDFs.
- Stage 1 vs Stage 2 status for OCR A was found by comparing code lists between H235 and H245, not by reading column positions (the layout is lost in text extraction). The results are consistent with the H245 rule that Stage 1 statements are listed first.

---

## Which formulae are in the OCR formula booklets, and what must be memorised

### Takeaway
Both boards publish an identical list in the specification of formulae candidates must know without being given them. For pure topics it covers: basic complex-number multiplication and division in exponential form, the |z−a| = r and arg loci, Euler's form, the 2×2 determinant and inverse, AB ordering, (AB)⁻¹, Σr, roots–coefficients relations for quadratics and cubics, definitions of cosh, sinh and tanh, derivatives and integrals of sinh kx and cosh kx, volumes of revolution, the SHM equation, the scalar product and the line and plane vector equations. The booklets give de Moivre, roots of unity, Σr² and Σr³, the Maclaurin series, the inverse trigonometric and hyperbolic derivatives and integrals, the logarithmic forms of the inverse hyperbolic functions, the vector product, the distance formulae and the polar area formula. The OCR A booklet also has an Additional Pure section (Hessian test, tangent plane, arc length and surface area).

### Cited Findings
- **Must be memorised (OCR A, H245 section 5d).** "Learners must be able to use the following formulae and identities … without these formulae and identities being provided". Pure items listed:
  - Complex numbers: for z₁ = r₁e^{iθ₁} and z₂ = r₂e^{iθ₂}, z₁z₂ = r₁r₂e^{i(θ₁+θ₂)} and z₁/z₂ = (r₁/r₂)e^{i(θ₁−θ₂)}; loci |z−a| = r (circle) and arg(z−a) = θ (half line); e^{iθ} = cosθ + i sinθ.
  - Matrices: 2×2 determinant ad−bc and inverse; AB means B then A; (AB)⁻¹ = B⁻¹A⁻¹.
  - Algebra: Σr = ½n(n+1); sum and product of roots for quadratics, and Σα, Σαβ, αβγ for cubics.
  - Hyperbolic functions: definitions of cosh, sinh and tanh.
  - Calculus: derivatives and integrals including sinh kx and cosh kx; Vx = π∫y² dx and Vy = π∫x² dy; SHM ẍ = −ω²x.
  - Vectors: magnitude, scalar product a·b = |a||b|cosθ, r = a + tb, (r−a)·n = 0.
  - Also the A Level Maths basics (quadratic formula, indices, logarithms, trigonometric identities, mensuration). Formulae "may only be provided where they are the starting point for a proof or as a result to be proved."
  - — [H245 spec §5d](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- **Must be memorised (MEI, H645 §5d).** The list is the same, item for item (complex numbers, matrices, algebra, hyperbolic definitions, calculus table, volumes of revolution, SHM, vectors). — [H645 spec §5d](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf). H235 has the equivalent list in its §5d. — [H235 spec](https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf)
- **OCR A H245 booklet, pure contents.** The booklet gives:
  - Series: arithmetic, geometric, binomial; Σr² = ⅙n(n+1)(2n+1); Σr³ = ¼n²(n+1)²; the Maclaurin general form plus eˣ, ln(1+x), sin x, cos x, (1+x)ⁿ with validity.
  - Matrix transformations: reflection in y = ±x; rotation through θ; Rx, Ry, Rz.
  - Calculus: derivatives of tan kx, sec, cot, cosec, arcsin, arccos, arctan; quotient rule; first principles; standard integrals; integration by parts; mean value; polar sector area ½∫r² dθ; integrals giving sin⁻¹, tan⁻¹, sinh⁻¹, cosh⁻¹ (with ln forms).
  - Numerical methods: trapezium rule, Newton–Raphson.
  - Complex numbers: the loci |z−a| = k, arg(z−a) = α, |z−a| = |z−b|; de Moivre; roots of unity.
  - Vectors: cartesian line and plane equations; vector product determinant; distance formulas for skew lines, point–line and point–plane.
  - Other: small-angle approximations; compound-angle identities; cosh²−sinh² = 1 and the logarithmic forms of sinh⁻¹, cosh⁻¹, tanh⁻¹; SHM solutions x = A cos ωt + B sin ωt and x = R sin(ωt+φ).
  - **Additional Pure section:** a×b = |a||b| sinθ n̂; Hessian H and the 4-case stationary-point test; tangent-plane formula; arc length (cartesian and parametric); surface area of revolution about x and y (cartesian and parametric).
  - — [H245 Formulae Booklet](https://www.ocr.org.uk/Images/752529-formulae-booklet-a-level-further-mathematics-a.pdf)
- **H235 AS booklet, pure contents.** It gives only: the binomial series; matrix transformations (reflection in y = ±x, rotation, Rx, Ry, Rz); first principles; the three complex loci; the cartesian line in 3-D; the vector product determinant. Its Additional Pure section gives a×b = |a||b| sinθ n̂. — [H235 Formulae Booklet](https://www.ocr.org.uk/Images/752815-formulae-booklet.pdf)
- **MEI booklet, Core Pure section** (reproduced in the spec, which states "the same formula booklet will be used for AS and A Level Further Mathematics B (MEI)"):
  - Complex numbers: de Moivre; roots of unity.
  - Vectors: cartesian plane and 3-D line; vector product (component form and |a||b| sinθ n̂); distances for skew lines, point–line (ax+by+c = 0 form) and point–plane (n₁x+n₂y+n₃z+d = 0 form).
  - Hyperbolic functions: cosh²−sinh² = 1 and the logarithmic forms of arsinh, arcosh, artanh.
  - Calculus: derivatives of arcsin, arccos, arctan; integrals giving arcsin, arctan, arsinh, arcosh; mean value; polar sector area.
  - Series: Σr², Σr³; Maclaurin general form and standard series.
  - **Extra Pure section:** grad g, and grad g = (f_x, f_y, −1) when z = f(x,y).
  - Further Pure with Technology section: Euler, modified Euler, RK4, and the polar tangent gradient.
  - — [H645 spec §5d](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- Spec content statements also say which formulae are "given":
  - OCR A: Σr² and Σr³ (proof may be required, 4.06a); vector product formula (4.04g); skew-line, point–line and point–plane distances (4.04h–j); tangent plane (8.05g, as stated in the statement itself). — [H245 spec](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
  - MEI: Ps1, Ps5, Pc6, Pv7, Pv8, Pv13, Pv16 (2-D case only), Pv17, Xc6; for Xc4 "the method will be given". — [H645 spec](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)

### Inferences
- **Memorise at OCR A, but given at MEI.** OCR A candidates must remember the scalar triple product and the reduction-formula method (8.04e, 8.06a). These are not in the booklet.
- **Given at OCR A, but memorise at MEI.** The Hessian test is in the OCR A booklet. MEI Y435 excludes classifying stationary points unless the method is given in the question.
- **Point-to-line distance in 3-D (MEI Pv16).** No formula is given, so the method must be known.
- **Inverse hyperbolic forms.** Both specs require candidates to derive the logarithmic forms (4.07f, Pa7), even though the booklets print them.

### Gaps
- **MEI booklet download.** On 17 Nov 2026 every "formulae-booklet.pdf" link on the MEI H635/H645 assessment page (e.g. https://www.ocr.org.uk/Images/752530-formulae-booklet.pdf) served the OCR **Physics A** (H156/H556) Data, Formulae and Relationships booklet. This looks like a site linking error. The MEI booklet contents above therefore come from spec §5d, which reproduces the booklet. A standalone MEI booklet PDF URL could not be confirmed.

---

## Paper structure (marks, time, weighting)

### Takeaway
- **OCR A H245:** Y540 and Y541 are each 75 marks, 1 h 30 min, 25%. Y545 is the same format (75 marks, 1 h 30 min, 25%). Candidates take Y540 + Y541 + any two options.
- **OCR A H235:** Y531 is 60 marks, 1 h 15 min, 33⅓%.
- **MEI H645:** Y420 is 144 marks (180 scaled), 2 h 40 min, 50%. Y435 is 60 marks, 1 h 15 min, 16⅔%.
- **MEI H635:** Y410 is 60 marks, 1 h 15 min, 33⅓%.

### Cited Findings
- **H245 papers.**
  - Learners take Y540 and Y541 plus any two of Y542 Statistics, Y543 Mechanics, Y544 Discrete Mathematics and Y545 Additional Pure. Each paper is 75 marks, a 90-minute written paper and 25% of the total.
  - All questions are compulsory. Each paper has "an increasing gradient of difficulty" and a mix of short and long questions.
  - Optional papers also assess Pure Core synoptically. Learners may take more than two optional papers.
  - — [H245 spec](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- **H245 assessment objective (AO) targets, in marks (AO1/AO2/AO3).** Y540: 37–38/18–19/18–19. Y541: 37–38/18–19/18–19. Y545: 37–38/22–23/14–15. — [H245 spec §3b](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- **H235 papers.** Y531 Pure Core is mandatory, plus two of Y532–Y535 (Y535 is Additional Pure). Each paper is 60 marks, 75 minutes and 33⅓%. AO targets: Y531 35–37/14–16/8–10; Y535 35–37/14–16/8–10. — [H235 spec](https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf)
- **H645 Core Pure (Y420).**
  - 2 hours 40 minutes, 144 marks (180 scaled), 50% of H645.
  - Section A has 30–40 marks of more straightforward questions. Section B has 104–114 marks of mixed questions.
  - Major options (Y421 Mechanics Major, Y422 Statistics Major): 120 marks, 2 h 15 min, 33⅓%. Minor options: 60 marks, 1 h 15 min (Y436: 1 h 45 min), 16⅔%.
  - Routes: A = Core Pure + Mechanics Major + one minor (not Mechanics Minor); B = Core Pure + Statistics Major + one minor (not Statistics Minor); C = Core Pure + three minors.
  - — [H645 spec](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- **H645 Extra Pure (Y435).** 1 hour 15 minutes, 60 marks, no sections, 16⅔% of H645. — [H645 spec](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- **H635 Core Pure (Y410).** 1 hour 15 minutes, 60 marks, 33⅓% of H635. Learners take Y410 plus any two of Y411–Y414, each 60 marks, 1 h 15 min, 33⅓%. — [H635 spec](https://www.ocr.org.uk/Images/308764-specification-accredited-as-level-gce-further-mathematics-b-mei-h635.pdf)
- **Calculators (OCR A).** Calculators are allowed on all papers and are expected to include an iterative (ANS) function, matrix operations including inversion up to at least 3×3, and statistical functions. — [H245 spec](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- **Specification versions.** H245 and H235 are at Version 2 (Oct 2025): rebranding to Cambridge OCR only, no content change. Earlier, v1.5 (Aug 2022) removed options Y415 and Y416. H645 is at v2.1 (March 2026): adds the Y436 withdrawal notice. — [H245 spec](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf); [H645 spec](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)

### Inferences
- **Share of the qualification that is pure.** In OCR A H245, the compulsory pure content is 50% (Y540 + Y541), rising to 75% with Y545. In MEI H645, Core Pure alone is 50%, rising to a maximum of 50% + 16⅔% + 16⅔% if a candidate takes Extra Pure and Further Pure with Technology on Route C. FPT is only available until 2028.
- **Time per mark.** About 1.2 min/mark on OCR A papers (90 min / 75), about 1.1 min/mark on MEI Y420 (160 min / 144), and 1.25 min/mark on the 60-mark papers.

### Gaps
- The "(a)" (AS-common) content of MEI Y420 is shown in the specification as unshaded sections. The text extraction cannot show shading, but the "(a)"/"(b)" labels in the section headings carry the same information.
- Weighting by pure topic within a paper is not published.
