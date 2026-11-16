# Pearson Edexcel Further Mathematics: Pure components (9FM0, 8FM0, IAL FP1–FP3)

Method note: these notes come from the official Pearson PDFs, downloaded and turned into text on 17 Nov 2026. Section numbers and wording are taken from the spec tables. Some mathematical symbols were lost in the text extraction, and those spots are marked. Primary sources:

- **A level Further Maths 9FM0 spec, Issue 4 (June 2023):** https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf
- **AS Further Maths 8FM0 spec, Issue 5 (July 2025):** https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf
- **AS/A level Maths and Further Maths formula booklet** ("Mathematical formulae and statistical tables", X54458A, © 2017): https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/X_18pt_A4_Formulae_Booklet_and_Statistical_Tables.pdf
- **IAL Mathematics, Further Mathematics and Pure Mathematics spec, Issue 3 (April 2019; first teaching Sept 2018):** https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf
- **IAL formula booklet, Issue 2 (January 2021):** https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/IAL-Mathematics-Formula-Book.pdf
- **IAL qualification page** (lists the same spec PDF, first teaching Sept 2018, first assessment 2019): https://qualifications.pearson.com/en/qualifications/edexcel-international-advanced-levels/mathematics-2018.html

## Q1. Full content list for each component, and what is AS (8FM0) versus A level only

### Takeaway
9FM0 Core Pure has 9 topics, sections 1–9, examined across two compulsory papers.

AS 8FM0 Core Pure is exactly the first part of that content: sections 1.1, 2.1–2.7, 3.1–3.8, 4.1–4.3, 5.1 and 6.1–6.5. These sub-points are worded identically in the two specs. The following are A level only:
- de Moivre and roots of unity (2.8–2.11)
- method of differences and Maclaurin (4.4–4.6)
- the rest of further calculus (5.2–5.6)
- polar coordinates (7), hyperbolic functions (8) and differential equations (9)

The AS FP1 and FP2 options are smaller versions of the A level FP1 (3A) and FP2 (4A) papers.

The IAL units divide the content differently:
- FP1 is AS-level: complex basics, quadratic roots, numerical root-finding, parabola and rectangular hyperbola, 2×2 matrices, Σ series, induction.
- FP2 covers inequalities, method of differences, de Moivre, loci and transformations, first and second order DEs, Maclaurin and Taylor, and polar.
- FP3 covers hyperbolics, conics, inverse trig and hyperbolic calculus, reduction formulae, arc length and surface area, vectors, 3×3 matrices and eigen.

IAL has no groups, no number theory, no recurrence relations, no Leibnitz or L'Hospital, no Weierstrass integration, no Simpson's rule, no SHM or coupled systems, and no mean value.

### Cited Findings

#### A. 9FM0 Papers 1 & 2: Core Pure Mathematics
Both papers may examine any of this content. Source: [9FM0 spec pp.9–19](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf).

In the lists below:
- "[AS]" means the sub-point is also in 8FM0 Core Pure, worded identically ([8FM0 spec pp.8–12](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf)).
- "[A only]" means the sub-point is not in 8FM0.

**1 Proof**
- **1.1 [AS]** Construct proofs using mathematical induction, for:
  - sums of series, e.g. Σr³ = ¼n²(n+1)², Σr(r+1) = n(n+1)(n+2)/3
  - divisibility, e.g. 3²ⁿ + 11 divisible by 4
  - powers of matrices, e.g. (3 −4; 1 −1)ⁿ = (2n+1 −4n; n 1−2n)

**2 Complex numbers**
- **2.1 [AS]** Solve any quadratic with real coefficients. Solve cubics or quartics with real coefficients, given a factor or root, e.g. f(z) = 2z³+5z²+7z+10 given z+2 is a factor.
- **2.2 [AS]** Add, subtract, multiply and divide in x+iy form. Know real part, imaginary part, modulus and argument.
- **2.3 [AS]** Complex conjugate. Non-real roots of real polynomials occur in conjugate pairs.
- **2.4 [AS]** Argand diagrams, including the sum or difference of two complex numbers.
- **2.5 [AS]** Convert between Cartesian and modulus-argument form (radians assumed).
- **2.6 [AS]** Multiply and divide in mod-arg form: |z₁z₂| = |z₁||z₂|, arg(z₁z₂) = arg z₁ + arg z₂, and so on.
- **2.7 [AS]** Simple loci and regions: |z−a| = b, |z−a| = |z−b|, arg(z−a) = β; regions |z−a| ≤ |z−b|, |z−a| ≤ b, α < arg(z−a) < β.
- **2.8 [A only]** de Moivre's theorem. Use it for multiple-angle formulae and sums of series:
  - z + 1/z = 2cosθ and z − 1/z = 2i sinθ
  - cos pθ, sin qθ and tan rθ in terms of powers, and powers in terms of multiple angles
  - e.g. 1 + z + … + zⁿ⁻¹ = 1 + i cot(π/2n) where z = cos(π/n) + i sin(π/n)
- **2.9 [A only]** e^{iθ} = cosθ + i sinθ and the form z = re^{iθ}. Also cosθ = ½(e^{iθ}+e^{−iθ}) and sinθ = (1/2i)(e^{iθ}−e^{−iθ}).
- **2.10 [A only]** The n distinct nth roots of re^{iθ}, which form the vertices of a regular n-gon.
- **2.11 [A only]** Complex roots of unity to solve geometric problems.

**3 Matrices** (all [AS])
- **3.1** Add, subtract and multiply conformable matrices; multiply by a scalar.
- **3.2** Zero and identity matrices.
- **3.3** Linear transformations:
  - In 2-D: reflections in the axes and in y = ±x, rotation about O, stretches parallel to the axes, enlargement about O.
  - AB means B followed by A.
  - In 3-D: reflection in x=0, y=0 or z=0, or rotation about a coordinate axis.
- **3.4** Invariant points and invariant lines.
- **3.5** 2×2 and 3×3 determinants as area or volume scale factors, including the effect on orientation.
- **3.6** Singular and non-singular matrices and properties of inverses. Inverse of 2×2 and 3×3 matrices (a calculator may be used, but the process must be understood).
- **3.7** Solve three linear simultaneous equations in three variables by inverse matrix.
- **3.8** Geometric interpretation of three planes: they meet in a point, form a sheaf, or form a prism or are otherwise inconsistent.

**4 Further algebra and functions**
- **4.1 [AS]** Roots and coefficients of polynomials up to quartic, e.g. α²+β²+γ², Σ1/α, (3+α)(3+β)(3+γ), α³+β³+γ³.
- **4.2 [AS]** Form a polynomial whose roots are a linear transformation of the roots of a given polynomial (at least cubic).
- **4.3 [AS]** Standard formulae for Σr, Σr² and Σr³, and their use for other series, e.g. Σr²(r+2).
- **4.4 [A only]** Method of differences, including partial fractions, e.g. Σ1/(r(r+1)).
- **4.5 [A only]** Maclaurin series of a function, including the general term.
- **4.6 [A only]** Maclaurin series for eˣ, ln(1+x), sin x, cos x and (1+x)ⁿ:
  - know the range of validity (proof not required)
  - includes series of compound functions

**5 Further calculus**
- **5.1 [AS]** Volumes of revolution, both π∫y²dx and π∫x²dy. The A level guidance adds Cartesian *or parametric* equations; the AS guidance says only that both are required.
- **5.2 [A only]** Improper integrals, both types: the integrand undefined in the range, or an infinite range. E.g. ∫₀^∞ e^{−x}dx and ∫₀² 1/√x dx.
- **5.3 [A only]** Mean value of a function, (1/(b−a))∫f(x)dx.
- **5.4 [A only]** Partial fractions integration, extended to quadratic factors ax²+c in the denominator.
- **5.5 [A only]** Differentiate inverse trig functions, e.g. arcsin x + x√(1−x²).
- **5.6 [A only]** Integrate (a²−x²)^{−½} and (a²+x²)^{−1}, and choose trig substitutions. The extracted text reads "(a² − x²)^−1"; the formula booklet's arctan entry for 1/(a²+x²) suggests a² + x² is meant. Check the PDF.

**6 Further vectors** (all [AS])
- **6.1** Vector and Cartesian equations of a line in 3-D. Intersection of two lines; skew and parallel lines.
- **6.2** Vector and Cartesian equations of a plane: r = a+λb+μc and ax+by+cz = d.
- **6.3** Scalar product. Plane in the form r·n = k. Angles between two lines, two planes, and a line and a plane.
- **6.4** Perpendicularity via a·b = 0.
- **6.5** Intersection of a line and a plane. Perpendicular distance between two lines, from a point to a line, and from a point to a plane, using |n₁α+n₂β+n₃γ+d|/√(n₁²+n₂²+n₃²).

**7 Polar coordinates** (all [A only])
- **7.1** Polar coordinates; convert to and from Cartesian.
- **7.2** Sketch curves such as r = p sec(α−θ), r = a, r = 2a cosθ, r = kθ, r = a(1±cosθ), r = a(3+2cosθ), r = a cos2θ, r² = a²cos2θ.
- **7.3** Area ½∫r²dθ. Tangents parallel or perpendicular to the initial line.

**8 Hyperbolic functions** (all [A only])
- **8.1** Definitions of sinh, cosh and tanh, with domains, ranges and graphs.
- **8.2** Differentiate and integrate hyperbolic functions.
- **8.3** Inverse hyperbolics, with their domains and ranges.
- **8.4** Derive and use the logarithmic forms.
- **8.5** Integrate (x²+a²)^{−½} and (x²−a²)^{−½}, and choose substitutions.

**9 Differential equations** (all [A only])
- **9.1** Integrating factor for dy/dx + P(x)y = Q(x). The factor e^{∫P dx} may be quoted without proof.
- **9.2** General and particular solutions; sketch families of solution curves.
- **9.3** Modelling in kinematics and other contexts.
- **9.4** y″+ay′+by = 0 by the auxiliary equation.
- **9.5** y″+ay′+by = f(x) by complementary function plus particular integral, where f(x) = ke^{px}, A+Bx, p+qx+cx², or m cos ωx + n sin ωx.
- **9.6** How the sign of the discriminant (positive, zero, negative) gives the form of the solution.
- **9.7** Simple harmonic motion, ẍ = −ω²x.
- **9.8** Damped oscillations, with resistance proportional to velocity. Forced vibration may be set.
- **9.9** Coupled first-order linear systems dx/dt = ax+by+f(t), dy/dt = cx+dy+g(t), e.g. predator–prey.

Source for all of section A: [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf). The 9FM0 spec says content shared with AS is marked in bold in the original; the [AS] tags above come from direct comparison with the [8FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf).

#### B. 9FM0 Paper 3A: Further Pure Mathematics 1
Source: [9FM0 spec pp.20–22](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf).

**1 Further trigonometry**
- **1.1** t-formulae: sinθ = 2t/(1+t²), cosθ = (1−t²)/(1+t²), tanθ = 2t/(1−t²), where t = tan(θ/2). Issue 4 corrected a typo in the cos formula.
- **1.2** Using them to prove identities.
- **1.3** Using them to solve equations, e.g. a cos x + b sin x = c.

**2 Further calculus**
- **2.1** Taylor series, e.g. sin x in powers of (x−π) up to (x−π)³.
- **2.2** Series expansions to find limits.
- **2.3** Leibnitz's theorem.
- **2.4** L'Hospital's rule, including repeated use or substitutions, e.g. lim (1+a/x)ˣ as x→∞.
- **2.5** Weierstrass (t = tan x/2) substitution for definite and indefinite integrals.

**3 Further differential equations**
- **3.1** Taylor series method for series solutions of DEs, e.g. y″ + xy′ + y = 0 up to x⁴.
- **3.2** DEs reducible by a given substitution to the Core Pure section 9 types.

**4 Coordinate systems**
- **4.1** Cartesian and parametric equations of:
  - the parabola, y² = 4ax with (at², 2at)
  - the rectangular hyperbola
  - the ellipse, with (a cos t, b sin t)
  - the hyperbola, with (a sec t, b tan t) and (a cosh t, b sinh t)
- **4.2** Focus–directrix properties and eccentricity, e.g. for the ellipse b² = a²(1−e²), foci (±ae, 0), directrices x = ±a/e.
- **4.3** Tangents and normals. The condition for y = mx+c to be a tangent is expected knowledge.
- **4.4** Loci problems.

**5 Further vectors**
- **5.1** Vector product; |a×b| as an area.
- **5.2** Scalar triple product; volumes of a tetrahedron and a parallelepiped.
- **5.3** 3-D geometry, including the line (r−a)×b = 0 and direction ratios and cosines.

**6 Further numerical methods**
- **6.1** Numerical solution of first and second order DEs using:
  - (dy/dx)ₙ ≈ (yₙ₊₁−yₙ)/h
  - (dy/dx)ₙ ≈ (yₙ₊₁−yₙ₋₁)/2h
  - (d²y/dx²)ₙ ≈ (yₙ₊₁−2yₙ+yₙ₋₁)/h²
- **6.2** Simpson's rule.

**7 Inequalities**
- **7.1** Algebraic inequalities, including the modulus, e.g. 1/(x−a) > x/(x−b) and |x²−1| > 2(x+1).

#### C. 9FM0 Paper 4A: Further Pure Mathematics 2
Source: [9FM0 spec pp.23–25](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf).

**1 Groups**
- **1.1** Axioms: binary operation, closure, associativity, identity, inverse.
- **1.2** Examples: symmetries, non-singular matrices, integers mod n, permutation groups. Cayley tables; cyclic groups.
- **1.3** Order of a group and of an element; subgroups.
- **1.4** Lagrange's theorem.
- **1.5** Isomorphism, for groups of order at most 8.

**2 Further calculus**
- **2.1** Reduction formulae, e.g. nIₙ = (n−1)Iₙ₋₂ for Iₙ = ∫₀^{π/2} sinⁿx dx, and Iₙ₊₂ = 2sin((n+1)x)/(n+1) + Iₙ for Iₙ = ∫ sin(nx)/sin x dx.
- **2.2** Arc length and area of a surface of revolution. The curve may be Cartesian, parametric *or polar*.

**3 Further matrix algebra**
- **3.1** Eigenvalues and eigenvectors of 2×2 and 3×3 matrices: characteristic equation, repeated and complex eigenvalues, normalised vectors.
- **3.2** Diagonalisation, P⁻¹AP; orthogonal diagonalisation of symmetric matrices.
- **3.3** Cayley–Hamilton theorem for 2×2 and 3×3 matrices.

**4 Further complex numbers**
- **4.1** Further loci and regions: |z−a| = k|z−b|, arg((z−a)/(z−b)) = β, α ≤ arg(z−z₁) ≤ β, p ≤ Re(z) ≤ q.
- **4.2** Transformations from the z-plane to the w-plane, e.g. w = z² and w = (az+b)/(cz+d).

**5 Number theory**
- **5.1** Division theorem, Euclidean algorithm (HCF) and congruences.
- **5.2** Bezout's identity, by back substitution.
- **5.3** Modular arithmetic: a ≡ b (mod n); reflexive, symmetric and transitive properties; addition, subtraction, multiplication and power laws.
- **5.4** Fermat's Little Theorem (no proof), e.g. 4²⁰ mod 7.
- **5.5** Divisibility tests for 2, 3, 4, 5, 6, 9, 10 and 11.
- **5.6** Solving congruence equations: conditions for existence, and Bezout for multiplicative inverses.
- **5.7** Combinatorics: multiplicative, addition and subtraction principles; number of subsets; ⁿPᵣ and ⁿCᵣ.

**6 Further sequences and series**
- **6.1** First and second order recurrence relations: uₙ₊₁ + f(n)uₙ = g(n) and uₙ₊₂ + f(n)uₙ₊₁ + g(n)uₙ = h(n).
- **6.2** Closed-form solutions using particular solution, complementary function and auxiliary equation, e.g. 2uₙ₊₂ + 7uₙ₊₁ − 15uₙ = 6. Modelling, e.g. population growth.
- **6.3** Proof by induction of closed forms.

#### D. 8FM0 Paper 2 option content: AS Further Pure Mathematics 1 (and AS FP2)
Source: [8FM0 spec pp.13–16](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf).

**AS Further Pure Mathematics 1**
- **1 Further trigonometry**
  - **1.1** t-formulae, plus knowledge of the definitions of sec, cosec and cot.
  - **1.2** Identities.
  - **1.3** Equations of the form a cos x + b sin x = c.
- **2 Coordinate systems**: parabola and rectangular hyperbola only.
  - **2.1** Cartesian equations y² = 4ax and xy = c².
  - **2.2** Parametric forms (at², 2at) and (ct, c/t).
  - **2.3** Focus–directrix property of the *parabola*.
  - **2.4** Tangents and normals. The condition for y = mx+c to be a tangent is known; dy/dx = 2a/y may be used.
  - **2.5** Simple loci problems.
- **3 Further vectors**
  - **3.1** Vector product; a vector perpendicular to two others.
  - **3.2** Area of a triangle and a parallelogram.
  - **3.3** Scalar triple product; volume of a tetrahedron and a parallelepiped.
- **4 Numerical methods**
  - **4.1** The same three DE approximations as A level FP1 6.1. There is no Simpson's rule.
- **5 Inequalities**
  - **5.1** Algebraic inequalities and inequations, e.g. 1/(x−a) > x/(x−b). The second example compares x/(x+a) with 1/(x+b); its symbol was lost in extraction.
  - There is no mention of the modulus sign, unlike A level FP1 7.1.

**What A level 3A adds beyond AS FP1**
- Taylor series, limits, Leibnitz, L'Hospital and the Weierstrass substitution
- Taylor-series solution of DEs, and DEs by substitution
- the ellipse and hyperbola, with eccentricity
- (r−a)×b = 0 and direction cosines
- Simpson's rule
- modulus inequalities

Source: comparison of the [8FM0](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf) and [9FM0](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf) specs.

**AS Further Pure Mathematics 2** (for completeness; only available in route 2A together with FP1)
- **1 Groups**: 1.1–1.4 as A level. There is no isomorphism.
- **2 Further matrix algebra**: 2.1–2.3 as A level, but for **2×2 matrices only**.
- **3 Further complex numbers**: 3.1 further loci and regions only. There are no z→w transformations.
- **4 Number theory**:
  - **4.1** Division theorem and Euclid.
  - **4.2** Bezout.
  - **4.3** Modular arithmetic.
  - **4.4** Divisibility tests.
  - There is no Fermat, no congruence equations and no combinatorics.
- **5 Further sequences and series**:
  - **5.1** First order recurrence relations only.
  - **5.2** Closed forms.
  - **5.3** Induction.

Source: [8FM0 spec pp.15–16](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf).

#### E. IAL Unit FP1 (WFM01)
- **Status:** compulsory for IAS and IAL Further Mathematics and for Pure Mathematics.
- **Prerequisites:** P1 and P2. Also locating roots by change of sign, rotation about O, and dividing a cubic or quartic by a quadratic.

Source: [IAL spec pp.30–35](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf).

**1 Complex numbers**
- **1.1** a+ib and r cosθ + i r sinθ forms; conjugate, modulus, argument and equality.
- **1.2** Sum, product and quotient; |z₁z₂| = |z₁||z₂|. Knowledge of arg(z₁z₂) = arg z₁ + arg z₂ is *not required*.
- **1.3** Argand diagram, including sums, products and quotients.
- **1.4** Complex roots of real quadratics.
- **1.5** Conjugate complex roots and a real root of a cubic with integer coefficients.
- **1.6** Roots of a quartic with real coefficients.

**2 Roots of quadratic equations**
- **2.1** α+β = −b/a and αβ = c/a.
- **2.2** Manipulating expressions, e.g. α³+β³ ≡ (α+β)³ − 3αβ(α+β).
- **2.3** New quadratics with roots such as α³, β³; 1/α, 1/β; α+2/β, …

**3 Numerical solution of equations**
- **3.1** Interval bisection, linear interpolation and Newton–Raphson, using functions from P1 and P2 only.

**4 Coordinate systems**
- **4.1** Parabola and rectangular hyperbola, y² = 4ax and xy = c².
- **4.2** Parametric idea: (at², 2at).
- **4.3** Focus–directrix property of the parabola.
- **4.4** Tangents and normals, by differentiating y = 2a^{½}x^{½} and y = c²/x. No parametric differentiation.

**5 Matrix algebra**
- **5.1–5.3** Addition, scalar multiple and products.
- **5.4** 2×2 determinants; singular matrices.
- **5.5** 2×2 inverse; (AB)⁻¹ = B⁻¹A⁻¹.

**6 Transformations using matrices** (2-D only)
- **6.1** Linear maps; AB means B then A.
- **6.2** Reflections, rotation, stretches and enlargement.
- **6.3** Combinations of transformations.
- **6.4** Inverse transformations; determinant as an area scale factor.

**7 Series**
- **7.1** Σr, Σr² and Σr(r²+2) style sums. "The method of differences is not required."

**8 Proof**
- **8.1** Induction for:
  - summation
  - divisibility
  - general terms of sequences, e.g. uₙ₊₁ = 3uₙ+4 gives uₙ = 3ⁿ−2
  - matrix products

#### F. IAL Unit FP2 (WFM02)
- **Status:** optional for IAS and IAL Further Mathematics and for IAL Pure Mathematics.
- **Prerequisites:** P1–P4 and FP1.

Source: [IAL spec pp.36–39](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf).

**1 Inequalities**
- **1.1** Including the modulus, e.g. 1/(x−a) > x/(x−b) and |x²−1| > 2(x+1).

**2 Series**
- **2.1** Method of differences with partial fractions.

**3 Further complex numbers**
- **3.1** Euler's relation e^{iθ} = cosθ + i sinθ.
- **3.2** de Moivre: cos nθ and sin mθ in powers, powers in multiple angles, and roots of a complex number. Students should be able to **prove de Moivre for any integer n**.
- **3.3** Loci and regions: |z−a| = b, |z−a| = k|z−b|, arg(z−a) = β, arg((z−a)/(z−b)) = β, and regions.
- **3.4** z→w transformations, e.g. w = z² and w = (az+b)/(cz+d).

**4 First order differential equations**
- **4.1** Separable variables, including forming the DE and sketching families of curves.
- **4.2** Integrating factor for dy/dx + Py = Q.
- **4.3** Reduction by a given substitution.

**5 Second order differential equations**
- **5.1** a y″ + b y′ + c y = f(x): CF + PI, with real distinct, equal or complex auxiliary-equation roots, and the same f(x) forms as 9FM0. E.g. y″ + 4y = sin 2x.
- **5.2** Reduction by a given substitution.

**6 Maclaurin and Taylor series**
- **6.1** Third and higher derivatives.
- **6.2** Maclaurin series.
- **6.3** Taylor series.
- **6.4** Taylor-series solution of DEs.

**7 Polar coordinates**
- **7.1** (r, θ) with r ≥ 0, and the same curve list as 9FM0 7.2, plus θ = α.
- Area ½∫r²dθ; tangents parallel or perpendicular to the initial line. The spec numbers both of these points "7.1".

#### G. IAL Unit FP3 (WFM03)
- **Status:** optional for IAS and IAL Further Mathematics and for IAL Pure Mathematics.
- **Prerequisites:** P1–P4 and FP1.

Source: [IAL spec pp.40–43](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf).

**1 Hyperbolic functions**
- **1.1** All six hyperbolic functions (including sech etc.), with graphs and identities such as cosh²x − sinh²x ≡ 1 and cosh²x + sinh²x ≡ cosh 2x. Solve a cosh x + b sinh x = c.
- **1.2** Inverse hyperbolics and their log forms. Students may be required to prove these.

**2 Further coordinate systems**
- **2.1** Ellipse and hyperbola: Cartesian and parametric forms, including (a cosh t, b sinh t).
- **2.2** Focus–directrix properties and eccentricity.
- **2.3** Tangents and normals; the condition for y = mx+c to be a tangent.
- **2.4** Simple loci.

**3 Differentiation**
- **3.1** Hyperbolic functions.
- **3.2** Inverse trig and inverse hyperbolic functions, e.g. artanh x².

**4 Integration**
- **4.1** Hyperbolic functions.
- **4.2** Inverse trig and inverse hyperbolic functions, e.g. ∫arsinh x dx and ∫arctan x dx.
- **4.3** Hyperbolic and trig substitutions for 1/√(a²−x²), 1/(a²+x²), 1/√(a²+x²) and 1/√(x²−a²).
- **4.4** Quadratic surds; substitutions are given in harder cases.
- **4.5** Reduction formulae; same examples as 9FM0 FP2 2.1.
- **4.6** Arc length and surface area of revolution, Cartesian or parametric only. "Equations in polar form will not be set."

**5 Vectors**
- **5.1** Vector product and triple scalar product, as area and volume.
- **5.2** Points, lines and planes; the line (r−a)×b = 0. Distance from a point to a plane, the line of intersection of two planes, and the shortest distance between skew lines.
- **5.3** Plane in the forms r·n = p and r = a+sb+tc.

**6 Further matrix algebra**
- **6.1** 2-D and 3-D linear maps.
- **6.2** Combinations of transformations.
- **6.3** Transpose; (AB)ᵀ = BᵀAᵀ.
- **6.4** 3×3 determinants.
- **6.5** 3×3 inverse.
- **6.6** Inverse transformations.
- **6.7** Eigenvalues and eigenvectors of 2×2 and 3×3 matrices; normalised vectors.
- **6.8** Orthogonal diagonalisation of symmetric matrices (PᵀAP).

### Inferences

**Where each topic sits in each course**

| Topic | 9FM0 | AS 8FM0 | IAL |
|---|---|---|---|
| Proof by induction | CP 1.1 | CP 1.1 | FP1 8.1, which adds sequence general terms |
| Complex basics, mod-arg, simple loci | CP 2.1–2.7 | same | FP1 1 (mod-arg multiplication rule not required), FP2 3.3 |
| de Moivre, e^{iθ}, nth roots, roots of unity | CP 2.8–2.11 | – | FP2 3.1–3.2. IAL requires a proof of de Moivre; 9FM0 states no geometric roots-of-unity point the way CP 2.11 does |
| Further loci, z→w transformations | FP2 (4A) 4.1–4.2 | AS FP2 3.1 (loci only) | FP2 3.3–3.4 |
| Matrices | CP 3 (2×2 and 3×3, 3-D transformations, three planes) | same | FP1 5–6 (2×2), FP3 6 (3×3 and transpose). IAL has no explicit invariant points or lines and no three-planes interpretation |
| Eigenvalues, diagonalisation, Cayley–Hamilton | FP2 3 | AS FP2 2 (2×2) | FP3 6.7–6.8 (no Cayley–Hamilton) |
| Roots of polynomials | CP 4.1–4.2 (up to quartic) | same | FP1 2, quadratics only. A gap relative to 9FM0 |
| Σr, Σr², Σr³ | CP 4.3 | same | FP1 7 |
| Method of differences | CP 4.4 | – | FP2 2 |
| Maclaurin | CP 4.5–4.6 | – | FP2 6.2 |
| Taylor | FP1 (3A) 2.1 | – | FP2 6.3 |
| Volumes of revolution | CP 5.1 | CP 5.1 | Not in FP1–FP3; appears in P4 (not checked in this note) |
| Improper integrals, mean value | CP 5.2–5.3 | – | not in IAL FP units |
| Partial fractions with ax²+c, inverse trig calculus | CP 5.4–5.6 | – | FP3 3.2, 4.2–4.3 |
| Vectors: lines and planes, scalar product, distances | CP 6 | same | FP3 5 |
| Vector product, triple product | FP1 5 | AS FP1 3 | FP3 5.1 |
| Polar | CP 7 | – | FP2 7 |
| Hyperbolic | CP 8 (sinh, cosh, tanh) | – | FP3 1, 3, 4 (all six functions) |
| First and second order DEs | CP 9.1–9.6 | – | FP2 4–5 |
| SHM, damping, coupled systems | CP 9.7–9.9 | – | not in IAL FP |
| t-formulae | FP1 1 | AS FP1 1 | not in IAL |
| Weierstrass, Leibnitz, L'Hospital, limits by series | FP1 2.2–2.5 | – | not in IAL |
| Conics | FP1 4 | AS FP1 2 (parabola and rectangular hyperbola) | FP1 4 (parabola and rectangular hyperbola), FP3 2 (ellipse and hyperbola) |
| Numerical DE approximations, Simpson | FP1 6 | AS FP1 4 (no Simpson) | not in IAL FP. FP1 has root-finding instead (bisection, linear interpolation, Newton–Raphson) |
| Inequalities | FP1 7 | AS FP1 5 | FP2 1 |
| Reduction formulae, arc length, surface area | FP2 2 (polar allowed) | – | FP3 4.5–4.6 (no polar) |
| Groups, number theory, recurrence relations | FP2 1, 5, 6 | AS FP2 (reduced) | not in IAL |

- **What is AS versus A level in 9FM0 Core Pure.** The AS part of Core Pure is exactly CP 1.1, 2.1–2.7, 3.1–3.8, 4.1–4.3, 5.1 and 6.1–6.5. These are the same as 8FM0 Core Pure, so the 9FM0 spec's bold "common content" corresponds to these points. Everything else in Core Pure is A level only.

### Gaps
- **AS FP1 inequality example.** The exact second example in AS FP1 5.1 (the comparison symbol between x/(x+a) and 1/(x+b)) did not survive text extraction.
- **CP 5.6 sign.** Whether the extracted "(a²−x²)^−1" is really "(a²+x²)^−1" should be checked in the PDF.
- **Bold common content.** The bold formatting in the 9FM0 spec cannot be seen in the text extract. The [AS] mapping comes from comparing the two specs, not from the bold itself.
- **Volumes of revolution in IAL.** IAL P4 content on volumes of revolution was not checked; it is outside the FP units.
- **Newer IAL spec.** The IAL qualification page lists Issue 3 (April 2019) as the current spec. No newer IAL spec issue was found as of Nov 2026.

## Q2. Which formulae are given in the booklet and which must be memorised

### Takeaway
**GCE (8FM0/9FM0):**
- **Must be recalled:** Appendix 1 of each spec lists the formulae students must remember. For pure, these include:
  - mod-arg and exponential multiplication and division of complex numbers
  - the meaning of the basic loci
  - e^{iθ} = cosθ + i sinθ
  - the 2×2 determinant and inverse, and (AB)⁻¹ = B⁻¹A⁻¹
  - Σr
  - root–coefficient sums for quadratics and cubics
  - definitions of cosh, sinh and tanh
  - standard derivatives and integrals, including sinh and cosh
  - volumes of revolution
  - the SHM equation
  - the scalar product, the vector line equation and the plane equation (r−a)·n = 0
- **Given in the booklet:** the "Further Mathematics" pages give:
  - Σr² and Σr³
  - rotation and reflection matrices
  - polar area
  - de Moivre and the roots of unity
  - Maclaurin and Taylor series
  - vector product, triple product, and the line and plane forms
  - point–plane distance
  - hyperbolic identities and inverse log forms
  - inverse trig and hyperbolic derivatives and integrals
  - (A level only) the conics table, arc length and surface area
- **Not in the booklet:**
  - the t-formulae
  - the numerical DE approximations
  - Simpson's rule

**IAL:**
- **Must be remembered:** only FP1 lists formulae: α+β, αβ and Σr.
- **Given in the booklet:** the unit-by-unit pages give the rest.

### Cited Findings
- **9FM0 Appendix 1** says these formulae "will not appear in the booklet" and must be known. Pure content listed:
  - quadratic formula, indices and logs, straight lines, AP and GP general terms, sine and cosine rules, triangle area
  - trig identities (Pythagorean, double angle), mensuration, arc and sector
  - **Complex numbers:**
    - z₁z₂ = r₁r₂e^{i(θ₁+θ₂)} and z₁/z₂ = (r₁/r₂)e^{i(θ₁−θ₂)}
    - |z−a| = r is a circle; arg(z−a) = θ is a half-line
    - e^{iθ} = cosθ + i sinθ
  - **Matrices:** 2×2 determinant ad−bc and inverse; AB means B then A; (AB)⁻¹ = B⁻¹A⁻¹
  - **Algebra:** Σr = ½n(n+1); for quadratics α+β = −b/a and αβ = c/a; for cubics Σα = −b/a, Σαβ = c/a, αβγ = −d/a
  - **Hyperbolic:** definitions of cosh, sinh and tanh
  - **Calculus:** derivatives of xⁿ, sin kx, cos kx, sinh kx, cosh kx, e^{kx} and ln x; sum, product and chain rules; the matching integrals; area under a curve
  - **Volumes of revolution:** Vₓ = π∫y²dx and V_y = π∫x²dy
  - **SHM:** ẍ = −ω²x
  - **Vectors:** magnitude; scalar product a·b = a₁b₁+a₂b₂+a₃b₃ = |a||b|cosθ; line r = a+tb; plane (r−a)·n = 0
  - plus statistics and mechanics items

  Source: [9FM0 spec Appendix 1, pp.61–67](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf).
- **8FM0 Appendix 1** has the same structure, with headings for quadratics, indices, logs, coordinate geometry, sequences, trigonometry, mensuration, complex numbers, matrices, algebra, hyperbolic functions, calculus and differential equations, vectors, statistics and mechanics. These must be known and are not in the booklet. Source: [8FM0 spec Appendix 1, p.41](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf).
- **Booklet, AS Further Mathematics pure section (pp.23–32).** It gives:
  - Σr² = n(n+1)(2n+1)/6 and Σr³ = n²(n+1)²/4
  - the anticlockwise rotation matrix, and reflection in y = (tanθ)x as (cos2θ sin2θ; sin2θ −cos2θ)
  - polar sector area ½∫r²dθ
  - de Moivre {r(cosθ+i sinθ)}ⁿ = rⁿ(cos nθ + i sin nθ), and the roots of zⁿ = 1 as e^{2πki/n}
  - the Maclaurin general formula and series for eˣ, ln(1+x), sin x, cos x and arctan x, with validity ranges
  - the vector product determinant and a×b = |a||b|sinθ n̂, the triple product a·(b×c), the Cartesian line, the plane n·r forms, the plane through three points, and the point–plane distance
  - hyperbolic identities: cosh²−sinh² = 1, sinh2x, cosh2x, and the log forms of arcosh, arsinh and artanh
  - derivatives of arcsin, arccos, arctan, sinh, cosh, tanh, arsinh, arcosh and artanh
  - integrals of sinh, cosh, tanh, 1/√(a²−x²), 1/(a²+x²), 1/√(x²−a²), 1/√(x²+a²), 1/(a²−x²) and 1/(x²−a²)

  The booklet's introduction says Further Maths students "may be required to use the formulae that were introduced in AS or A Level Mathematics papers." Source: [Formula booklet](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/X_18pt_A4_Formulae_Booklet_and_Statistical_Tables.pdf).
- **Booklet, A Level Further Mathematics pure section (pp.40–52).** It repeats all of the above and adds:
  - a **Conics** table for the ellipse, parabola, hyperbola and rectangular hyperbola: standard and parametric forms, eccentricity, b² relations, foci, directrices, asymptotes
  - **Arc length** in Cartesian, parametric and polar forms
  - **Surface area of revolution** Sₓ in Cartesian, parametric and polar forms

  The word "Simpson" does not appear anywhere in the booklet. The trapezium rule and Newton–Raphson appear only in the A Level Mathematics section. Source: [Formula booklet](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/X_18pt_A4_Formulae_Booklet_and_Statistical_Tables.pdf).
- **IAL FP1 memorise list:** "Roots of quadratic equations: α+β = −b/a, αβ = c/a" and "Series: Σr = ½n(n+1)". FP2 and FP3 have no separate memorise list. Source: [IAL spec FP1.2](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf).
- **IAL booklet, Issue 2 (Jan 2021):**
  - **FP1 page:** Σr² and Σr³; Newton–Raphson; conics for the parabola (focus (a, 0), directrix x = −a) and the rectangular hyperbola (foci and directrices "not required"); rotation and reflection matrices.
  - **FP2 page:** polar sector area; e^{iθ}; de Moivre; roots of unity; Maclaurin, the Taylor forms f(x) about a and f(a+x), and the standard series.
  - **FP3 page:** resolved part of a in the direction of b; ratio point; vector product and triple product; line and plane equations; point–plane distance; hyperbolic identities and log forms; full conics table; inverse trig and hyperbolic derivatives and integrals; arc length and surface area (Cartesian and parametric).
  - Each FP page says candidates may also need the P1–P4 (and FP1) formulae. Issue 2 corrected the ellipse standard form and the integration lines.

  Source: [IAL formula booklet](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/IAL-Mathematics-Formula-Book.pdf).

### Inferences
- **9FM0 FP1 must-learn items.** For 9FM0 FP1, students must memorise the t-formulae, the DE finite-difference approximations and Simpson's rule, because none of them is in the booklet. Leibnitz's theorem and the L'Hospital rule are also not printed.
- **Integrating factor.** The 9FM0 and IAL guidance say the integrating factor "may be quoted without proof". It is not in the booklet or the memorise list, so in practice it has to be memorised.
- **AS booklet section.** The AS Further Maths booklet section includes Maclaurin and hyperbolic formulae even though AS Core Pure and AS FP1 do not examine those topics. The AS section is evidently shared, so it should not be read as a guide to AS content.

### Gaps
- **Recall-only points not checked.** I did not check whether the guidance column for any sub-point (e.g. FP2 2.1 reduction formulae) states extra results that must be recalled, beyond Appendix 1.
- **Leibnitz.** I did not confirm whether Leibnitz's theorem appears in the A Level Maths section of the booklet; it was not seen in the Further Maths pure pages.

## Q3. Paper structure: length, marks, and compulsory versus optional papers

### Takeaway
- **9FM0:** four 1h30, 75-mark papers, each 25%. Core Pure 1 and 2 are compulsory. FP1 (3A) and FP2 (4A) are options.
- **8FM0:** two 1h40, 80-mark papers, each 50%. Paper 1 is Core Pure; Paper 2 is one of ten option pairs, and four of those include AS FP1.
- **IAL:** every unit is 1h30 and 75 marks. FP1 is compulsory for IAS and IAL Further Maths. IAL Further Maths needs FP1 plus FP2 or FP3, among six units.

### Cited Findings
- **9FM0 papers and weighting.** Students "must take Paper 1 and Paper 2, the two mandatory Core Pure papers, and two optional papers". Each paper is 1 hour 30 minutes, 75 marks and 25% of the qualification. Students may take more than two options. All assessments are in May/June of a single year. Source: [9FM0 spec pp.4–5](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf).
- **9FM0 Core Pure coverage.** "Paper 1 and Paper 2 may contain questions on any topics from the Pure Mathematics content". Calculators are allowed and the booklet is provided. The Core Pure papers were first assessed in May/June 2019. Source: [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf).
- **9FM0 options.** Option 1 papers are 3A FP1, 3B FS1, 3C FM1 and 3D D1. Option 2 papers are 4A FP2, 4B FS2, 4C FM2 and 4D D2. Students choose "any two Option 1 papers, or a matching pair of Option 1 and Option 2 papers", which gives ten option pairs. So FP2 (4A) can only be taken with FP1 (3A). Source: [9FM0 spec p.5 and Appendix 9](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf).
- **9FM0 AO weightings.** Each paper carries 23–27% of the AO weighting. Source: [9FM0 spec AO table](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf).
- **8FM0 Paper 1 (8FM0/01, Core Pure).** 1 hour 40 minutes, 80 marks, 50%. Content: Proof, Complex numbers, Matrices, Further algebra and functions, Further calculus, Further vectors. Source: [8FM0 spec p.3](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf).
- **8FM0 Paper 2 (8FM0/2A–2K, options).** 1 hour 40 minutes, 80 marks, 50%. Students take one of ten pairs:
  - 2A FP1 + FP2
  - 2B FP1 + FS1
  - 2C FP1 + FM1
  - 2D FP1 + D1
  - 2E FS1 + FM1
  - 2F FS1 + D1
  - 2G FS1 + FS2
  - 2H FM1 + D1
  - 2J FM1 + FM2
  - 2K D1 + D2

  First assessment was May/June 2018. Source: [8FM0 spec pp.4, 29](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf).
- **IAL units.** Each unit is externally assessed with "a written examination of 1 hour and 30 minutes" and 75 marks. FP1 to FP3 are worth 33⅓% of an IAS and 16⅔% of an IAL. FP1–FP3 are available in January and June. First assessments were June 2019 for FP1 and June 2020 for FP2 and FP3. Source: [IAL spec pp.7–8](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf).
- **IAL unit combinations.**
  - IAS Further Mathematics: FP1 compulsory, plus two from FP2, FP3, M1–M3, S1–S3 and D1.
  - IAL Further Mathematics: "FP1 and either FP2 or FP3" compulsory, with further options from FP2, FP3, M1–M3, S1–S3 and D1 (six units in total).
  - IAL Pure Mathematics: P1–P4 and FP1, plus FP2 or FP3.
  - A unit result used for one qualification cannot be reused for another (Maths plus Further Maths needs 12 different units).

  Source: [IAL spec p.10](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf).

### Inferences
- **IAL can skip one Further Pure unit.** An IAL Further Maths student can avoid either FP2 (complex/DEs/polar/Maclaurin) or FP3 (hyperbolics/conics/vectors/3×3 matrices). By contrast, every 9FM0 student covers all of Core Pure, which includes hyperbolics, polar, DEs and vectors.
- **AS mark split.** In 8FM0 Paper 2 the two halves of the option pair presumably share the 80 marks (about 40 each, about 50 minutes each), but the spec text extracted here does not say so explicitly.

### Gaps
- **AS option split.** The 40/40 split of 8FM0 Paper 2 between the two options, and the component codes for the AS FP1 section (e.g. 8FM0/21; a past paper URL "8fm0-23" suggests /23 = FS1), were not confirmed in the spec text.
- **IAL weighting.** The IAL spec does not state any further weighting between pure and applied units.
