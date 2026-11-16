"""Unit C12: Surfaces and partial differentiation
(OCR A Additional Pure Y535/Y545 8.05a–g; OCR MEI Extra Pure Y435 Xc1–Xc7)."""

UNIT = {
    "number": "C12",
    "title": "Surfaces and partial differentiation",
    "tag": "Option · OCR A Additional Pure 8.05a, 8.05c, 8.05d, 8.05e (AS Y535), 8.05b, 8.05f, 8.05g (A level Y545) · "
           "OCR MEI Extra Pure Y435 Xc1–Xc7 (first-order partial derivatives only) · not on Edexcel, AQA, IAL or CAIE",
    "notes": [
        ("p", "So far every function you have differentiated had one input: y = f(x). Many quantities depend on two or more "
              "inputs. The height of a hillside depends on how far east (x) and how far north (y) you are; the volume of a "
              "cylinder depends on its radius and its height. This unit shows how to picture a function of two variables as a "
              "surface in three dimensions, how to differentiate it with respect to one variable at a time (partial "
              "differentiation), and how to use this to find and classify stationary points and to find tangent planes and "
              "normal lines. It uses the vector equations of lines and planes from Units A9 and A10."),
        ("p", "Notation: matrices are written row by row, so (a b; c d) has first row a, b and second row c, d. Vectors are "
              "written as column vectors (1, 2, −3)ᵀ or in i, j, k form."),

        ("h2", "12.1 Surfaces z = f(x, y) (OCR 8.05a, MEI Xc1)"),
        ("p", "A function of two variables, z = f(x, y), gives one value of z for each point (x, y) in its domain. Plotting "
              "the points (x, y, f(x, y)) in three dimensions gives a <b>surface</b>. Use right-handed axes: x towards you, "
              "y to the right, z up. The height of the surface above the point (x, y, 0) of the xy-plane is z."),
        ("table", ["Equation", "Surface", "What it looks like"], [
            ["z = 6 − 2x − 3y", "plane", "meets the axes at (3, 0, 0), (0, 2, 0), (0, 0, 6)"],
            ["z = x² + y²", "paraboloid (bowl)", "lowest point at the origin; circular contours"],
            ["z = x² − y²", "hyperbolic paraboloid (saddle)", "rises along the x-axis, falls along the y-axis"],
            ["z = √(x² + y²)", "cone", "z equals the distance from the z-axis"],
            ["z = 4 − x² − 2y²", "upside-down bowl", "highest point (0, 0, 4); elliptical contours"],
        ]),
        ("p", "You will normally sketch a surface by finding its <b>sections</b> and <b>contours</b> (Section 12.2), and use "
              "graphing software to see it in 3-D. The figures in this unit were drawn this way."),

        ("h2", "12.2 Sections and contours (OCR 8.05c, MEI Xc2)"),
        ("bullets", [
            "A <b>section</b> is the curve where the surface meets a vertical plane. The section x = a is the curve "
            "z = f(a, y) in the plane x = a. The section y = b is the curve z = f(x, b) in the plane y = b. "
            "Each section is an ordinary graph of one variable.",
            "A <b>contour</b> (level curve) is the curve f(x, y) = k: the points of the xy-plane where the surface has height k. "
            "It is the horizontal section z = k, projected down onto the xy-plane. A set of contours is a <b>contour map</b>, "
            "like the height lines on an Ordnance Survey map.",
            "Contours close together mean the surface is steep; far apart means it is gentle. Small closed loops round a point "
            "suggest a maximum or minimum there. Contours that cross (like an X) suggest a saddle point.",
        ]),
        ("figure", "pc12_paraboloid.png", "z = x² + y². Left: the surface with the section y = 0 (navy, the parabola z = x²) "
                   "and the horizontal sections z = 1, 2, 3 (red). Right: the contour map; the contour z = k is the circle "
                   "x² + y² = k of radius √k.", 150),
        ("p", "For the saddle z = x² − y², the section y = 0 is z = x² (a parabola with a minimum at the origin), but the "
              "section x = 0 is z = −y² (a parabola with a maximum at the origin). The contours x² − y² = k are rectangular "
              "hyperbolas, and the contour z = 0 is the pair of lines y = ±x, which cross at the saddle point."),
        ("figure", "pc12_saddle.png", "z = x² − y²: the surface with two sections through the origin, and its contour map. "
                   "The contours for k = 0 cross at the saddle point.", 150),

        ("h2", "12.3 Surfaces g(x, y, z) = c and more variables (OCR 8.05a, 8.05b; MEI Xc5)"),
        ("p", "Some surfaces are easier to write <b>implicitly</b> as g(x, y, z) = c, where g is a function of three variables. "
              "Any surface z = f(x, y) can be written this way, as f(x, y) − z = 0."),
        ("bullets", [
            "x² + y² + z² = r² is the sphere with centre O and radius r.",
            "x²/a² + y²/b² + z²/c² = 1 is an <b>ellipsoid</b>; its sections parallel to each coordinate plane are ellipses.",
            "ax + by + cz = d is a plane with normal vector (a, b, c)ᵀ.",
            "x² + y² − z² = 1 is a hyperboloid: each section z = k is a circle x² + y² = 1 + k².",
        ]),
        ("p", "(OCR A level, 8.05b) A function can depend on more than two variables, e.g. w = x²yz³ or w = e^(xy) cos z, "
              "and may involve trigonometric, exponential and logarithmic functions. You cannot draw the graph of w = f(x, y, z) "
              "(it needs four dimensions), but you can differentiate it partially in exactly the same way (Section 12.4)."),

        ("h2", "12.4 First-order partial derivatives (OCR 8.05d, MEI Xc3)"),
        ("p", "The <b>partial derivative of f with respect to x</b> is found by differentiating f with respect to x while "
              "treating y as a constant. It is written ∂f/∂x, ∂z/∂x or f<sub>x</sub>. Similarly ∂f/∂y = f<sub>y</sub> is "
              "found by holding x constant. The symbol ∂ (“partial d”, “del”) reminds you that the other variables are held fixed."),
        ("box", "First partial derivatives", [
            "f<sub>x</sub>(x, y) = ∂f/∂x = lim as h → 0 of [f(x + h, y) − f(x, y)] / h  (y held constant).",
            "f<sub>y</sub>(x, y) = ∂f/∂y = lim as h → 0 of [f(x, y + h) − f(x, y)] / h  (x held constant).",
            "Geometric meaning: f<sub>x</sub>(a, b) is the gradient of the section y = b at x = a, i.e. the slope of the "
            "surface at (a, b) in the x-direction. f<sub>y</sub>(a, b) is the slope in the y-direction.",
            "All the usual rules (product, quotient, chain) apply, with the other variable treated as a number.",
        ]),
        ("p", "For example, if f(x, y) = x³y² + 5y then f<sub>x</sub> = 3x²y² (5y is a constant, so its x-derivative is 0) and "
              "f<sub>y</sub> = 2x³y + 5. If z = e^(2x) sin 3y then ∂z/∂x = 2e^(2x) sin 3y and ∂z/∂y = 3e^(2x) cos 3y. "
              "For three variables, w = x²yz³ has w<sub>x</sub> = 2xyz³, w<sub>y</sub> = x²z³ and w<sub>z</sub> = 3x²yz²."),

        ("h2", "12.5 Second-order partial derivatives (OCR 8.05d only; not MEI)"),
        ("p", "Differentiating f<sub>x</sub> and f<sub>y</sub> again gives four second derivatives:"),
        ("bullets", [
            "f<sub>xx</sub> = ∂²f/∂x² = ∂/∂x (∂f/∂x) and f<sub>yy</sub> = ∂²f/∂y² = ∂/∂y (∂f/∂y).",
            "the <b>mixed</b> derivatives f<sub>xy</sub> = ∂/∂y (f<sub>x</sub>) = ∂²f/∂y∂x (differentiate with respect to x, "
            "then y) and f<sub>yx</sub> = ∂/∂x (f<sub>y</sub>) = ∂²f/∂x∂y.",
        ]),
        ("box", "Equality of mixed derivatives", [
            "For every function you will meet (any function whose second partial derivatives are continuous), "
            "f<sub>xy</sub> = f<sub>yx</sub>. So the order of differentiation does not matter, and finding both is a useful "
            "check on your algebra. The result is quoted, not proved.",
        ]),
        ("p", "Example: f = x²y³ + sin(xy). f<sub>x</sub> = 2xy³ + y cos(xy), f<sub>y</sub> = 3x²y² + x cos(xy). Then "
              "f<sub>xy</sub> = 6xy² + cos(xy) − xy sin(xy) = f<sub>yx</sub>, f<sub>xx</sub> = 2y³ − y² sin(xy) and "
              "f<sub>yy</sub> = 6x²y − x² sin(xy)."),

        ("h2", "12.6 Stationary points (OCR 8.05e, MEI Xc4)"),
        ("p", "At a <b>stationary point</b> (a, b, f(a, b)) the surface is flat: its slope is zero in every direction. "
              "In particular the slopes in the x- and y-directions are zero, so"),
        ("box", "Finding stationary points", [
            "Solve the simultaneous equations ∂f/∂x = 0 and ∂f/∂y = 0. Each solution (a, b) gives a stationary point "
            "(a, b, f(a, b)).",
            "There are three kinds: a local <b>maximum</b> (a hill top), a local <b>minimum</b> (the bottom of a bowl) and a "
            "<b>saddle point</b> (a mountain pass: a minimum along one section and a maximum along another).",
        ]),
        ("p", "The equations are usually non-linear. Factorise rather than divide, so that you do not lose solutions: from "
              "6xy − 12 = 0 you get xy = 2, but from 2xy − 2x = 0 you must write 2x(y − 1) = 0, so x = 0 <i>or</i> y = 1, "
              "and follow up both cases. At OCR AS level (Y535) you only need to find stationary points, not their nature."),
        ("p", "<b>Deciding the nature using sections (MEI method).</b> MEI does not require second derivatives: if you are asked "
              "for the nature, the question gives the method, usually “consider the sections …”. Look at the cross-sections "
              "through the stationary point. If some section has a maximum there and another has a minimum, it is a "
              "<b>saddle</b>. If every section has a minimum it is a minimum. Warning: the two sections x = a and y = b are "
              "not enough on their own; Worked example C12.4 has a saddle point where both of these sections have a minimum. "
              "Completing the square, or noting that f(x, y) ≥ f(a, b) for all x and y, can also settle the nature."),
        ("figure", "pc12_cubic_contours.png", "Contours of f(x, y) = x³ + y³ − 3xy (Worked example C12.3). Small closed loops "
                   "surround the minimum at (1, 1); two branches of the contour f = 0 cross at the saddle point (0, 0).", 115),

        ("h2", "12.7 Classifying stationary points with the Hessian (OCR A level 8.05f)"),
        ("p", "Near a stationary point the surface behaves like its second-order terms, so the second derivatives decide its "
              "nature. Collect them in the <b>Hessian matrix</b> and take its determinant:"),
        ("box", "The Hessian test (given in the OCR A formula booklet)", [
            "H = det(f<sub>xx</sub> f<sub>xy</sub>; f<sub>yx</sub> f<sub>yy</sub>) = f<sub>xx</sub>f<sub>yy</sub> − "
            "(f<sub>xy</sub>)², evaluated at the stationary point.",
            "H > 0 and f<sub>xx</sub> < 0: local maximum.    H > 0 and f<sub>xx</sub> > 0: local minimum.",
            "H < 0: saddle point.    H = 0: the test fails; investigate further (for example with sections).",
        ]),
        ("table", ["H at the point", "f<sub>xx</sub> at the point", "Nature", "Example at (0, 0)"], [
            ["H > 0", "f<sub>xx</sub> > 0", "minimum", "x² + y²: H = 4"],
            ["H > 0", "f<sub>xx</sub> < 0", "maximum", "4 − x² − 2y²: H = 8"],
            ["H < 0", "either", "saddle", "x² − y²: H = −4"],
            ["H = 0", "any", "test fails", "x⁴ + y⁴ (minimum), x⁴ − y⁴ (saddle), x³ + y² (neither max nor min)"],
        ]),
        ("p", "Why it works: if H > 0 then f<sub>xx</sub> and f<sub>yy</sub> have the same sign, so the surface curves the same "
              "way in every direction (a bowl or a dome). If H < 0 it curves up in some directions and down in others."),

        ("h2", "12.8 Tangent planes (OCR A level 8.05g, MEI Xc7)"),
        ("p", "The <b>tangent plane</b> to a surface at a point P is the plane that touches the surface at P; every curve on "
              "the surface through P has its tangent line in this plane. For z = f(x, y) at P(a, b, f(a, b)), the section "
              "y = b has direction (1, 0, f<sub>x</sub>)ᵀ at P and the section x = a has direction (0, 1, f<sub>y</sub>)ᵀ. "
              "Their vector product (1, 0, f<sub>x</sub>)ᵀ × (0, 1, f<sub>y</sub>)ᵀ = (−f<sub>x</sub>, −f<sub>y</sub>, 1)ᵀ "
              "is normal to the tangent plane, which gives"),
        ("box", "Tangent plane to z = f(x, y) at (a, b, f(a, b))", [
            "z = f(a, b) + (x − a) f<sub>x</sub>(a, b) + (y − b) f<sub>y</sub>(a, b)   (given in the OCR A booklet).",
            "A normal vector is (f<sub>x</sub>, f<sub>y</sub>, −1)ᵀ, evaluated at (a, b).",
            "Near P the surface is close to its tangent plane, so δz ≈ f<sub>x</sub> δx + f<sub>y</sub> δy for small "
            "changes δx and δy.",
        ]),
        ("figure", "pc12_tangent_plane.png", "The surface z = x²y + 3y² and its tangent plane z = 4x + 13y − 16 at (1, 2, 14) "
                   "(Worked example C12.5).", 95),

        ("h2", "12.9 Grad, normal vectors and normal lines (MEI Xc5–Xc7)"),
        ("p", "For a function g(x, y, z), the vector of its partial derivatives is called <b>grad g</b> (written ∇g, "
              "“del g”):"),
        ("box", "Grad and the normal to g(x, y, z) = c (given in the MEI formula booklet)", [
            "grad g = ∇g = (∂g/∂x, ∂g/∂y, ∂g/∂z)ᵀ.",
            "At a point A (position vector a) on the surface g(x, y, z) = c, grad g is a <b>normal vector</b> to the surface.",
            "Tangent plane at A: (r − a)·∇g = 0, where ∇g is evaluated at A.",
            "Normal line at A: r = a + λ∇g.",
            "For z = f(x, y), take g = f(x, y) − z: then grad g = (f<sub>x</sub>, f<sub>y</sub>, −1)ᵀ, matching Section 12.8.",
        ]),
        ("p", "Why grad g is normal: take any curve r(t) = (x(t), y(t), z(t)) lying on the surface, so g(x(t), y(t), z(t)) = c "
              "for all t. Differentiating with the chain rule gives g<sub>x</sub>x′ + g<sub>y</sub>y′ + g<sub>z</sub>z′ = 0, "
              "i.e. ∇g · r′(t) = 0. So ∇g is perpendicular to the tangent of every curve on the surface through the point: "
              "it is normal to the surface."),
        ("p", "For example, on the sphere x² + y² + z² = 9, ∇g = (2x, 2y, 2z)ᵀ = 2r, which points straight out from the centre, "
              "as you would expect. If ∇g = 0 at a point, the method gives no normal there (e.g. the vertex of a cone)."),
        ("figure", "pc12_ellipsoid_normal.png", "The ellipsoid x² + 2y² + 3z² = 9 and its normal line at (2, 1, 1), in the "
                   "direction of grad g = (4, 4, 6)ᵀ (Worked example C12.6).", 95),

        ("warn", "Common mistakes", [
            "Not holding the other variable constant: ∂/∂x (x²y³) = 2xy³, not 2xy³ + 3x²y². And ∂/∂x (5y) = 0.",
            "Losing stationary points by dividing by a variable that could be zero. Factorise each equation and follow every case.",
            "Giving only (a, b): a stationary point of a surface is (a, b, f(a, b)). Examiners often ask for all three coordinates.",
            "Deciding the nature from the sections x = a and y = b alone. Both can have minima at a saddle point.",
            "Reading H = 0 as “saddle” or “point of inflection”. H = 0 means the test gives no information.",
            "Using f<sub>yy</sub> instead of f<sub>xx</sub> for the sign when H > 0. (Either works when H > 0, but quote f<sub>xx</sub> as the booklet does.)",
            "Tangent planes: evaluating f<sub>x</sub> and f<sub>y</sub> at a general point instead of at (a, b), or dropping the −1 in (f<sub>x</sub>, f<sub>y</sub>, −1)ᵀ.",
            "MEI: second derivatives are not required; when asked for the nature, use exactly the method the question gives.",
        ]),
        ("box", "Given or learn", [
            "OCR A (Y545): the Hessian test and the tangent-plane formula are in the formula booklet. Learn how to find "
            "partial derivatives and stationary points.",
            "MEI (Y435): grad g and grad g = (f<sub>x</sub>, f<sub>y</sub>, −1)ᵀ for z = f(x, y) are in the booklet. Learn the "
            "tangent plane (r − a)·∇g = 0 and the normal line r = a + λ∇g.",
        ]),
    ],

    "examples": [
        {
            "title": "Sections and contours",
            "question": "A surface has equation z = 4 − x² − 2y². (a) Describe the contours z = 0, z = 2 and z = 4. "
                        "(b) Find the sections x = 0 and y = 1. (c) Describe the surface.",
            "steps": [
                "(a) z = k gives x² + 2y² = 4 − k. For k = 0: x²/4 + y²/2 = 1, an ellipse with semi-axes 2 (along x) and √2 (along y). "
                "For k = 2: x² + 2y² = 2, an ellipse with semi-axes √2 and 1. For k = 4: x² + 2y² = 0, the single point (0, 0). "
                "There are no points with z > 4.",
                "(b) x = 0: z = 4 − 2y², a ∩-shaped parabola in the yz-plane with vertex (0, 0, 4). "
                "y = 1: z = 2 − x², a ∩-shaped parabola in the plane y = 1 with vertex (0, 1, 2).",
                "(c) The contours are nested ellipses shrinking to a point as z increases to 4, and every vertical section is a "
                "∩-shaped parabola. The surface is an upside-down elliptical bowl with highest point (0, 0, 4), steeper in "
                "the y-direction than in the x-direction.",
            ],
        },
        {
            "title": "First and second partial derivatives",
            "question": "f(x, y) = x²e^(3y) + ln(x² + y²). (a) Find f<sub>x</sub> and f<sub>y</sub>. "
                        "(b) (OCR) Find f<sub>xx</sub>, f<sub>xy</sub> and f<sub>yx</sub>, and verify that f<sub>xy</sub> = f<sub>yx</sub>.",
            "steps": [
                "(a) Treat y as constant: f<sub>x</sub> = 2xe^(3y) + 2x/(x² + y²).",
                "Treat x as constant: f<sub>y</sub> = 3x²e^(3y) + 2y/(x² + y²).",
                "(b) f<sub>xx</sub> = 2e^(3y) + [2(x² + y²) − 2x·2x]/(x² + y²)² = 2e^(3y) + 2(y² − x²)/(x² + y²)².",
                "f<sub>xy</sub> = ∂/∂y (f<sub>x</sub>) = 6xe^(3y) − 4xy/(x² + y²)²  (chain rule on 2x(x² + y²)⁻¹).",
                "f<sub>yx</sub> = ∂/∂x (f<sub>y</sub>) = 6xe^(3y) − 4xy/(x² + y²)². The two agree, as expected.",
            ],
        },
        {
            "title": "Stationary points classified by the Hessian (OCR A level)",
            "question": "Find the stationary points of f(x, y) = x³ + y³ − 3xy and determine their nature.",
            "steps": [
                "f<sub>x</sub> = 3x² − 3y and f<sub>y</sub> = 3y² − 3x. Stationary points: y = x² and x = y².",
                "Substitute: x = x⁴, so x(x³ − 1) = 0, giving x = 0 or x = 1 (the only real root of x³ = 1). "
                "Then y = 0 or y = 1. Stationary points (0, 0, 0) and (1, 1, −1), since f(1, 1) = 1 + 1 − 3 = −1.",
                "f<sub>xx</sub> = 6x, f<sub>yy</sub> = 6y, f<sub>xy</sub> = −3, so H = 36xy − 9.",
                "At (0, 0): H = −9 < 0, so (0, 0, 0) is a saddle point.",
                "At (1, 1): H = 36 − 9 = 27 > 0 and f<sub>xx</sub> = 6 > 0, so (1, 1, −1) is a local minimum.",
                "The contour map in Section 12.6 confirms this: closed loops round (1, 1) and crossing contours at (0, 0).",
            ],
        },
        {
            "title": "Nature by sections: a saddle that looks like a minimum (MEI style)",
            "question": "z = x² − 4xy + y² − 6x + 6y. (a) Find the stationary point. (b) Show that the sections x = 1 and "
                        "y = −1 both have a minimum at the stationary point. (c) By considering the section of the surface by "
                        "the vertical plane x − y = 2, show that the stationary point is a saddle point.",
            "steps": [
                "(a) ∂z/∂x = 2x − 4y − 6 = 0 and ∂z/∂y = −4x + 2y + 6 = 0. From the first, x = 2y + 3; then "
                "−8y − 12 + 2y + 6 = 0, so y = −1 and x = 1. z = 1 + 4 + 1 − 6 − 6 = −6. Stationary point (1, −1, −6).",
                "(b) y = −1: z = x² + 4x + 1 − 6x − 6 = x² − 2x − 5 = (x − 1)² − 6, minimum −6 at x = 1. "
                "x = 1: z = 1 − 4y + y² − 6 + 6y = y² + 2y − 5 = (y + 1)² − 6, minimum −6 at y = −1.",
                "(c) The plane x − y = 2 passes through (1, −1). On it put x = 1 + t, y = −1 + t. Then "
                "z = (1 + t)² − 4(1 + t)(t − 1) + (t − 1)² − 6(1 + t) + 6(t − 1) = −2t² − 6.",
                "This section has a maximum −6 at t = 0. One section has a maximum and others a minimum at the same point, "
                "so (1, −1, −6) is a saddle point. (Check, OCR: H = 2 × 2 − (−4)² = −12 < 0.)",
            ],
        },
        {
            "title": "Tangent plane and normal to z = f(x, y)",
            "question": "The surface S has equation z = x²y + 3y². (a) Find the equation of the tangent plane to S at the point "
                        "where x = 1 and y = 2. (b) Find a vector equation of the normal line at this point.",
            "steps": [
                "(a) f(1, 2) = 2 + 12 = 14, so the point is (1, 2, 14).",
                "f<sub>x</sub> = 2xy = 4 and f<sub>y</sub> = x² + 6y = 13 at (1, 2).",
                "z = 14 + 4(x − 1) + 13(y − 2), i.e. z = 4x + 13y − 16 (or 4x + 13y − z = 16).",
                "Check: at (1, 2), 4 + 26 − 16 = 14.",
                "(b) Normal vector (f<sub>x</sub>, f<sub>y</sub>, −1)ᵀ = (4, 13, −1)ᵀ. Normal line: r = (1, 2, 14)ᵀ + λ(4, 13, −1)ᵀ.",
            ],
        },
        {
            "title": "Grad, tangent plane and normal line to g(x, y, z) = c (MEI)",
            "question": "The ellipsoid E has equation x² + 2y² + 3z² = 9. (a) Show that A(2, 1, 1) lies on E. (b) Find grad g "
                        "where g = x² + 2y² + 3z², and hence the equation of the tangent plane to E at A. (c) The normal line "
                        "to E at A meets the plane z = 0 at B. Find the coordinates of B.",
            "steps": [
                "(a) 4 + 2 + 3 = 9, so A lies on E.",
                "(b) grad g = (2x, 4y, 6z)ᵀ = (4, 4, 6)ᵀ at A, which is parallel to (2, 2, 3)ᵀ.",
                "Tangent plane: 2(x − 2) + 2(y − 1) + 3(z − 1) = 0, i.e. 2x + 2y + 3z = 9.",
                "(c) Normal line: r = (2, 1, 1)ᵀ + λ(2, 2, 3)ᵀ. z = 0 when 1 + 3λ = 0, λ = −1/3.",
                "B = (2 − 2/3, 1 − 2/3, 0) = (4/3, 1/3, 0).",
            ],
        },
    ],

    "practice": [
        "The surface S has equation z = x² + 4y². (a) Describe the contours z = 4 and z = 16. (b) Find the equation of the "
        "section x = 2 and describe its shape.",
        "Describe each surface, giving any intercepts with the axes: (a) z = 6 − 2x − 3y; (b) x² + y² + z² = 25; "
        "(c) z = √(x² + y²) (consider the contours).",
        "Find f<sub>x</sub> and f<sub>y</sub> for f(x, y) = x³ − 2x²y + 5y⁴.",
        "Find ∂z/∂x and ∂z/∂y for (a) z = e^(2x) sin 3y; (b) z = x/(x + y).",
        "z = ln(x² + y²). Show that x ∂z/∂x + y ∂z/∂y = 2.",
        "(OCR) f(x, y) = x²y³ + sin(xy). Find f<sub>xx</sub>, f<sub>yy</sub> and f<sub>xy</sub>, and verify that "
        "f<sub>xy</sub> = f<sub>yx</sub>.",
        "(OCR A level) w = x²yz³ + e^(xz). Find ∂w/∂x, ∂w/∂y and ∂w/∂z, and evaluate each at (1, 2, 0).",
        "Find the stationary point of z = x² + 2y² − 4x + 8y + 3. By completing the square, show that it is a minimum.",
        "f(x, y) = x³ − 12x + y² − 2y. (a) Find the two stationary points. (b) (OCR) Use the Hessian to classify them.",
        "Find the equation of the tangent plane to z = x² + y² at the point (1, 2, 5), in the form z = px + qy + r.",
        "(MEI) The surface S has equation xy + yz + zx = 11. (a) Show that P(1, 2, 3) lies on S. (b) Find grad g at P, "
        "where g = xy + yz + zx. (c) Find the equations of the tangent plane and the normal line to S at P.",
        "(OCR) (a) Show that f(x, y) = x⁴ + y⁴ and h(x, y) = x⁴ − y⁴ both have a stationary point at the origin with H = 0. "
        "(b) Determine the nature of each stationary point by another method.",
    ],
    "answers": [
        "(a) z = 4: x² + 4y² = 4, an ellipse x²/4 + y² = 1 with semi-axes 2 and 1. z = 16: x²/16 + y²/4 = 1, semi-axes 4 and 2. "
        "(b) z = 4 + 4y², a ∪-shaped parabola in the plane x = 2 with minimum point (2, 0, 4).",
        "(a) A plane through (3, 0, 0), (0, 2, 0), (0, 0, 6). (b) The sphere with centre O and radius 5; it meets the axes at "
        "(±5, 0, 0), (0, ±5, 0), (0, 0, ±5). (c) Contours x² + y² = k² are circles of radius k, growing evenly with k: a cone "
        "with vertex O, axis the z-axis, opening upwards (z ≥ 0), meeting the axes only at O.",
        "f<sub>x</sub> = 3x² − 4xy; f<sub>y</sub> = −2x² + 20y³.",
        "(a) ∂z/∂x = 2e^(2x) sin 3y, ∂z/∂y = 3e^(2x) cos 3y. (b) ∂z/∂x = y/(x + y)², ∂z/∂y = −x/(x + y)².",
        "∂z/∂x = 2x/(x² + y²), ∂z/∂y = 2y/(x² + y²), so x z<sub>x</sub> + y z<sub>y</sub> = (2x² + 2y²)/(x² + y²) = 2.",
        "f<sub>x</sub> = 2xy³ + y cos(xy), f<sub>y</sub> = 3x²y² + x cos(xy). f<sub>xx</sub> = 2y³ − y² sin(xy); "
        "f<sub>yy</sub> = 6x²y − x² sin(xy); f<sub>xy</sub> = f<sub>yx</sub> = 6xy² + cos(xy) − xy sin(xy).",
        "w<sub>x</sub> = 2xyz³ + ze^(xz), w<sub>y</sub> = x²z³, w<sub>z</sub> = 3x²yz² + xe^(xz). At (1, 2, 0): 0, 0 and 1.",
        "z<sub>x</sub> = 2x − 4 = 0, z<sub>y</sub> = 4y + 8 = 0: (2, −2, −9). z = (x − 2)² + 2(y + 2)² − 9 ≥ −9, with equality "
        "only at (2, −2), so it is a minimum.",
        "(a) f<sub>x</sub> = 3x² − 12 = 0, f<sub>y</sub> = 2y − 2 = 0: (2, 1, −17) and (−2, 1, 15). (b) f<sub>xx</sub> = 6x, "
        "f<sub>yy</sub> = 2, f<sub>xy</sub> = 0, H = 12x. At (2, 1): H = 24 > 0, f<sub>xx</sub> = 12 > 0, minimum. "
        "At (−2, 1): H = −24 < 0, saddle point.",
        "f<sub>x</sub> = 2x = 2, f<sub>y</sub> = 2y = 4. z = 5 + 2(x − 1) + 4(y − 2), i.e. z = 2x + 4y − 5.",
        "(a) 2 + 6 + 3 = 11. (b) grad g = (y + z, x + z, x + y)ᵀ = (5, 4, 3)ᵀ. (c) Tangent plane 5x + 4y + 3z = 22; "
        "normal line r = (1, 2, 3)ᵀ + λ(5, 4, 3)ᵀ.",
        "(a) f<sub>x</sub> = 4x³, f<sub>y</sub> = 4y³ are 0 at O; f<sub>xx</sub> = 12x², f<sub>yy</sub> = 12y², "
        "f<sub>xy</sub> = 0, so H = 0 at O. For h, h<sub>yy</sub> = −12y², so H = 0 too. (b) f ≥ 0 = f(0, 0) everywhere, so O is a "
        "minimum of f. For h, the section y = 0 is z = x⁴ (minimum at O) and the section x = 0 is z = −y⁴ (maximum at O), so O "
        "is a saddle point of h.",
    ],

    "exam": [
        "(OCR A level) The function f is defined by f(x, y) = x³ + 3xy² − 15x − 12y.\n"
        "(a) Show that at a stationary point x² + y² = 5 and xy = 2. [3]\n"
        "(b) Hence find the coordinates of the four stationary points of the surface z = f(x, y). [4]\n"
        "(c) Use the Hessian to determine the nature of each stationary point. [5]\n"
        "(d) Find the equation of the tangent plane to the surface at the point where x = 1 and y = 0. [3]",
        "(MEI) A surface S has equation z = 4xy − x⁴ − y⁴.\n"
        "(a) Find ∂z/∂x and ∂z/∂y. [2]\n"
        "(b) Find the coordinates of the three stationary points of S. [4]\n"
        "(c) By considering the sections of S by the planes y = x and y = −x, show that the stationary point at the origin "
        "is a saddle point. [3]\n"
        "(d) Find the equation of the tangent plane to S at the point where x = 1 and y = 2, and a vector equation of the "
        "normal line there. [4]",
        "(MEI) The surface H has equation x² + y² − z² = 4.\n"
        "(a) Describe the sections of H by the planes z = k, and the section by the plane x = 0. [3]\n"
        "(b) Show that A(2, 1, 1) lies on H, and find grad g at A, where g = x² + y² − z². [2]\n"
        "(c) Find the equation of the tangent plane to H at A in the form ax + by + cz = d. [2]\n"
        "(d) The normal line to H at A meets H again at B. Find the coordinates of B. [4]",
        "(OCR A level) The function f is defined by f(x, y) = (x² + y²)e^(−x).\n"
        "(a) Find f<sub>x</sub>, f<sub>y</sub> and f<sub>xy</sub>, and verify that f<sub>xy</sub> = f<sub>yx</sub>. [4]\n"
        "(b) Find the stationary points of the surface z = f(x, y). [3]\n"
        "(c) Determine the nature of each stationary point. [4]\n"
        "(d) Explain why the minimum value of f is 0. [1]",
    ],
    "exam_answers": [
        "(a) f<sub>x</sub> = 3x² + 3y² − 15 = 0 ⇒ x² + y² = 5 (M1 A1); f<sub>y</sub> = 6xy − 12 = 0 ⇒ xy = 2 (B1).\n"
        "(b) (x + y)² = 9 and (x − y)² = 1 (M1), giving (2, 1), (1, 2), (−2, −1), (−1, −2) (A1). "
        "z-values: f(2, 1) = −28, f(1, 2) = −26, f(−2, −1) = 28, f(−1, −2) = 26 (M1 A1).\n"
        "(c) f<sub>xx</sub> = 6x, f<sub>yy</sub> = 6x, f<sub>xy</sub> = 6y, H = 36(x² − y²) (M1 A1). (2, 1, −28): H = 108 > 0, "
        "f<sub>xx</sub> = 12 > 0, minimum (A1). (−2, −1, 28): H = 108 > 0, f<sub>xx</sub> = −12 < 0, maximum (A1). "
        "(1, 2, −26) and (−1, −2, 26): H = −108 < 0, saddle points (A1).\n"
        "(d) f(1, 0) = −14, f<sub>x</sub>(1, 0) = −12, f<sub>y</sub>(1, 0) = −12 (B1 B1). z = −14 − 12(x − 1) − 12y, "
        "i.e. z = −12x − 12y − 2 (A1).",
        "(a) ∂z/∂x = 4y − 4x³, ∂z/∂y = 4x − 4y³ (B1 B1).\n"
        "(b) y = x³ and x = y³ ⇒ x = x⁹ (M1), x(x⁸ − 1) = 0, x = 0, ±1 (A1). Points (0, 0, 0), (1, 1, 2), (−1, −1, 2) (A1 A1).\n"
        "(c) y = x: z = 4x² − 2x⁴, which has a minimum at x = 0 (z ≥ 0 near 0) (M1 A1). y = −x: z = −4x² − 2x⁴ ≤ 0, a maximum "
        "at x = 0. One section has a minimum and another a maximum, so it is a saddle point (A1).\n"
        "(d) At (1, 2): z = 8 − 1 − 16 = −9, ∂z/∂x = 4, ∂z/∂y = −28 (M1 A1). z = −9 + 4(x − 1) − 28(y − 2), i.e. "
        "z = 4x − 28y + 43 (A1). Normal line r = (1, 2, −9)ᵀ + λ(4, −28, −1)ᵀ (A1).",
        "(a) z = k: x² + y² = 4 + k², circles centre (0, 0, k) with radius √(4 + k²), smallest (radius 2) when k = 0 (B1 B1). "
        "x = 0: y² − z² = 4, a (rectangular) hyperbola in the yz-plane (B1). [H is a hyperboloid of one sheet.]\n"
        "(b) 4 + 1 − 1 = 4 (B1). grad g = (2x, 2y, −2z)ᵀ = (4, 2, −2)ᵀ (B1).\n"
        "(c) 4(x − 2) + 2(y − 1) − 2(z − 1) = 0 (M1), 2x + y − z = 4 (A1).\n"
        "(d) r = (2 + 2t, 1 + t, 1 − t) (M1). (2 + 2t)² + (1 + t)² − (1 − t)² = 4 ⇒ 4t² + 12t = 0 (M1 A1). t = −3 gives "
        "B(−4, −2, 4) (A1).",
        "(a) f<sub>x</sub> = (2x − x² − y²)e^(−x) (M1 A1), f<sub>y</sub> = 2ye^(−x) (B1). f<sub>xy</sub> = −2ye^(−x) and "
        "f<sub>yx</sub> = ∂/∂x (2ye^(−x)) = −2ye^(−x), equal (B1).\n"
        "(b) f<sub>y</sub> = 0 ⇒ y = 0 (e^(−x) ≠ 0); then 2x − x² = 0, x = 0 or 2 (M1 A1). Points (0, 0, 0) and (2, 0, 4e⁻²) (A1).\n"
        "(c) f<sub>xx</sub> = (x² + y² − 4x + 2)e^(−x), f<sub>yy</sub> = 2e^(−x) (M1). At (0, 0): f<sub>xx</sub> = 2, "
        "f<sub>yy</sub> = 2, f<sub>xy</sub> = 0, H = 4 > 0, f<sub>xx</sub> > 0, minimum (A1). At (2, 0): f<sub>xx</sub> = −2e⁻², "
        "f<sub>yy</sub> = 2e⁻², f<sub>xy</sub> = 0, H = −4e⁻⁴ < 0 (M1), saddle point (A1).\n"
        "(d) x² + y² ≥ 0 and e^(−x) > 0, so f ≥ 0, with f = 0 only at the origin (B1).",
    ],
}
