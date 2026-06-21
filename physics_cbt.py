#!/usr/bin/env python3
# ============================================================
# PHYSICS 102 CBT - 100 COMPLEX QUESTIONS
# Standalone Version - No external dependencies needed
# ============================================================
# Topics Covered:
# 1. Coulomb's Law & Electric Force
# 2. Electric Field & Field Lines
# 3. Gauss's Law & Applications
# 4. Electric Potential & Potential Energy
# 5. Electric Dipoles & Torque
# 6. Conductors, Insulators & Semiconductors
# 7. Electrostatic Induction & Shielding
# 8. Continuous Charge Distributions
# 9. Fundamental Forces of Nature
# 10. Superposition Principle
# ============================================================

import random

# ============================================================
# ALL 100 QUESTIONS WITH ANSWERS AND EXPLANATIONS
# ============================================================

QUESTIONS = [
    # === COULOMB'S LAW (1-15) ===
    {
        "question": "Two point charges q₁ = 2μC and q₂ = -3μC are placed 10 cm apart in air. Calculate the magnitude of the electrostatic force between them. (Take k = 9×10⁹ N·m²/C²)",
        "options": ["5.40 N", "4.50 N", "6.20 N", "3.80 N"],
        "answer": 0,
        "explanation": "Using Coulomb's Law: F = k|q₁q₂|/r² = (9×10⁹)(2×10⁻⁶)(3×10⁻⁶)/(0.1)² = (9×10⁹)(6×10⁻¹²)/0.01 = 54×10⁻³/0.01 = 5.40 N. The force is attractive since the charges are opposite."
    },
    {
        "question": "Compare the electric and gravitational forces between the electron and proton in a hydrogen atom. Given: mₑ = 9.1×10⁻³¹ kg, mₚ = 1.7×10⁻²⁷ kg, e = 1.6×10⁻¹⁹ C, G = 6.67×10⁻¹¹ N·m²/kg², r = 5.3×10⁻¹¹ m. What is the ratio Fₑ/Fg?",
        "options": ["2.2×10³⁹", "1.1×10³⁹", "2.2×10³⁸", "3.3×10³⁹"],
        "answer": 0,
        "explanation": "Fₑ = k(e²)/r² = (9×10⁹)(1.6×10⁻¹⁹)²/(5.3×10⁻¹¹)² = 8.2×10⁻⁸ N. Fg = G(mₑmₚ)/r² = (6.67×10⁻¹¹)(9.1×10⁻³¹)(1.7×10⁻²⁷)/(5.3×10⁻¹¹)² = 3.7×10⁻⁴⁷ N. Ratio Fₑ/Fg = 8.2×10⁻⁸/3.7×10⁻⁴⁷ ≈ 2.2×10³⁹. Electrical force is vastly stronger than gravity."
    },
    {
        "question": "Two charges q₁ = 1.0×10⁻⁶ C and q₂ = 2.3×10⁻² C are separated by 0.05 mm in vacuum. Calculate the force. If placed in a medium with dielectric constant 9, what is the new force?",
        "options": ["8.28×10² N, 9.2×10¹ N", "9.2×10² N, 1.03×10² N", "8.28×10³ N, 9.2×10² N", "7.5×10² N, 8.3×10¹ N"],
        "answer": 0,
        "explanation": "In vacuum: F = k(q₁q₂)/r² = (9×10⁹)(1×10⁻⁶)(2.3×10⁻²)/(5×10⁻⁵)² = 8.28×10² N. In medium: F' = F/εr = 8.28×10²/9 = 9.2×10¹ N. The dielectric constant reduces the force by factor εr."
    },
    {
        "question": "In a right-angle triangle, q₁ = -1.0μC at origin, q₂ = +2.0μC at (0, 10cm), and q₃ = +4.0μC at (20cm, 0). Find the magnitude of the net force on q₁.",
        "options": ["2.01 N", "1.80 N", "2.50 N", "1.44 N"],
        "answer": 0,
        "explanation": "F₁₂ = k|q₁q₂|/r₁₂² = (9×10⁹)(1×10⁻⁶)(2×10⁻⁶)/(0.1)² = 1.8 N (attractive, +y). F₁₃ = k|q₁q₃|/r₁₃² = (9×10⁹)(1×10⁻⁶)(4×10⁻⁶)/(0.2)² = 0.9 N (attractive, +x). F_net = √(1.8² + 0.9²) = √(3.24+0.81) = √4.05 ≈ 2.01 N."
    },
    {
        "question": "What is the electric field at 1 meter from a point charge of 20μC?",
        "options": ["1.8×10⁵ N/C", "2.0×10⁵ N/C", "1.5×10⁵ N/C", "2.5×10⁵ N/C"],
        "answer": 0,
        "explanation": "E = kQ/r² = (9×10⁹)(20×10⁻⁶)/(1)² = 1.8×10⁵ N/C. Direction is away from the positive charge."
    },
    {
        "question": "Determine the electric field magnitude at a point 22 cm to the left of a point charge of -2.4 nC.",
        "options": ["4.46×10⁴ N/C", "5.4×10² N/C", "6.2×10⁴ N/C", "3.6×10⁴ N/C"],
        "answer": 0,
        "explanation": "E = k|Q|/r² = (9×10⁹)(2.4×10⁻⁹)/(0.022)² = 21.6/4.84×10⁻⁴ = 4.46×10⁴ N/C. Direction is TOWARD the negative charge."
    },
    {
        "question": "Two point charges of 4μC and -3.2μC are separated by 4 cm. What is the net electric field at the midpoint?",
        "options": ["1.62×10⁸ N/C toward negative charge", "1.62×10⁷ N/C toward negative charge", "1.62×10⁶ N/C toward negative charge", "1.62×10⁵ N/C toward negative charge"],
        "answer": 0,
        "explanation": "At midpoint, d = 2 cm. E₄ = k(4×10⁻⁶)/(0.02)² = 9×10⁷ N/C (right, away from +). E₋₃.₂ = k(3.2×10⁻⁶)/(0.02)² = 7.2×10⁷ N/C (right, toward -). Both point right. E_net = (9+7.2)×10⁷ = 1.62×10⁸ N/C toward negative charge."
    },
    {
        "question": "A dipole has charges +2.0μC and -2.0μC separated by 0.1 m. Find the electric field at 0.5 m along its axis.",
        "options": ["28.8×10³ N/C", "14.4×10³ N/C", "57.6×10³ N/C", "7.2×10³ N/C"],
        "answer": 0,
        "explanation": "p = q×2a = (2×10⁻⁶)(0.1) = 2×10⁻⁷ C·m. E_axial = (1/4πε₀)(2p/r³) = (9×10⁹)(4×10⁻⁷)/(0.125) = 28.8×10³ N/C."
    },
    {
        "question": "An electric dipole with p = 2 C·pm is in uniform field E = 5 N/C at 60°. Calculate the torque.",
        "options": ["8.66 N·pm", "10.0 N·pm", "5.0 N·pm", "7.5 N·pm"],
        "answer": 0,
        "explanation": "τ = pE sinθ = (2)(5)sin(60°) = 10×0.866 = 8.66 N·pm. Torque aligns the dipole with the field."
    },
    {
        "question": "HCl gas in E = 3×10⁴ N/C has molecular dipole moment 3.4×10⁻³⁰ C·m. Calculate maximum torque.",
        "options": ["10.2×10⁻²⁶ N·m", "5.1×10⁻²⁶ N·m", "20.4×10⁻²⁶ N·m", "8.5×10⁻²⁶ N·m"],
        "answer": 0,
        "explanation": "Maximum torque at θ = 90°: τ_max = pE = (3.4×10⁻³⁰)(3×10⁴) = 10.2×10⁻²⁶ N·m."
    },
    {
        "question": "Find the force of repulsion between two protons (e = 1.6×10⁻¹⁹ C) separated by 5.3×10⁻¹¹ m.",
        "options": ["8.2×10⁻⁸ N", "4.1×10⁻⁸ N", "1.6×10⁻⁸ N", "2.0×10⁻⁷ N"],
        "answer": 0,
        "explanation": "F = k(e²)/r² = (9×10⁹)(1.6×10⁻¹⁹)²/(5.3×10⁻¹¹)² = (9×10⁹)(2.56×10⁻³⁸)/(2.809×10⁻²¹) = 8.2×10⁻⁸ N."
    },
    {
        "question": "What is the force between an α-particle (+2e) and an electron 10⁻¹³ m apart?",
        "options": ["4.6×10⁻² N", "2.3×10⁻² N", "9.2×10⁻² N", "1.2×10⁻² N"],
        "answer": 0,
        "explanation": "F = k(2e)(e)/r² = (9×10⁹)(2)(1.6×10⁻¹⁹)²/(10⁻¹³)² = 46.08×10⁻³ = 4.6×10⁻² N. Attractive."
    },
    {
        "question": "Find the electric field at 20 cm from a charge of 20μC. What force on a 5μC charge there?",
        "options": ["E = 4.5×10⁶ N/C, F = 22.5 N", "E = 9×10⁶ N/C, F = 45 N", "E = 2.25×10⁶ N/C, F = 11.25 N", "E = 4.5×10⁵ N/C, F = 2.25 N"],
        "answer": 0,
        "explanation": "E = kQ/r² = (9×10⁹)(20×10⁻⁶)/(0.2)² = 4.5×10⁶ N/C. F = qE = (5×10⁻⁶)(4.5×10⁶) = 22.5 N."
    },
    {
        "question": "Two charges q₁ = 1.0×10⁻⁶ C and q₂ = 2.3×10⁻² C in a medium with εr = 9. What is the force?",
        "options": ["9.2×10¹ N", "8.28×10² N", "7.4×10¹ N", "1.0×10² N"],
        "answer": 0,
        "explanation": "In vacuum: F = (9×10⁹)(1×10⁻⁶)(2.3×10⁻²)/(5×10⁻⁵)² = 8.28×10² N. In medium: F' = F/εr = 8.28×10²/9 = 9.2×10¹ N."
    },
    {
        "question": "What is the permittivity of free space ε₀?",
        "options": ["8.85×10⁻¹² F/m", "9×10⁹ N·m²/C²", "1.6×10⁻¹⁹ C", "6.67×10⁻¹¹ N·m²/kg²"],
        "answer": 0,
        "explanation": "ε₀ = 8.85×10⁻¹² F/m (or C²/N·m²). k = 1/(4πε₀) ≈ 9×10⁹ N·m²/C²."
    },

    # === GAUSS'S LAW (16-30) ===
    {
        "question": "A uniform electric field E = 400 N/C is incident on a plane surface A = 10 m² at 30° with the normal. Calculate the electric flux.",
        "options": ["3464 N·m²/C", "4000 N·m²/C", "2000 N·m²/C", "6928 N·m²/C"],
        "answer": 0,
        "explanation": "Φ = EA cosθ = (400)(10)cos(30°) = 4000×0.866 = 3464 N·m²/C. Flux depends on the angle between E and the normal."
    },
    {
        "question": "A flat square of area 10 m² is in a uniform field of 8000 N/C perpendicular to it. What is the flux?",
        "options": ["80000 N·m²/C", "40000 N·m²/C", "160000 N·m²/C", "0 N·m²/C"],
        "answer": 0,
        "explanation": "Φ = EA cosθ = (8000)(10)cos(0°) = 80000 N·m²/C. Perpendicular gives maximum flux (cos0° = 1)."
    },
    {
        "question": "State Gauss's Law mathematically for a closed surface.",
        "options": ["∮E·dA = Q_enc/ε₀", "∮E·dA = 0", "E = kQ/r²", "F = qE"],
        "answer": 0,
        "explanation": "Gauss's Law: ∮E·dA = Q_enc/ε₀. Net electric flux through any closed surface equals total charge enclosed divided by ε₀."
    },
    {
        "question": "For an infinite line charge with linear density λ, what is E at distance r?",
        "options": ["E = λ/(2πε₀r)", "E = λ/(4πε₀r²)", "E = λ/(2πε₀r²)", "E = λ/(πε₀r)"],
        "answer": 0,
        "explanation": "Using cylindrical Gaussian surface: E(2πrl) = λl/ε₀, so E = λ/(2πε₀r). Field decreases as 1/r (not 1/r²)."
    },
    {
        "question": "For an infinite charged plane sheet with surface density σ, what is E?",
        "options": ["E = σ/(2ε₀)", "E = σ/ε₀", "E = σ/(4πε₀)", "E = σ/(πε₀)"],
        "answer": 0,
        "explanation": "Using pillbox Gaussian surface: 2EA = σA/ε₀, so E = σ/(2ε₀). Field is uniform and independent of distance."
    },
    {
        "question": "Two infinite parallel sheets have +σ and -σ. What is E between them?",
        "options": ["E = σ/ε₀", "E = σ/(2ε₀)", "E = 2σ/ε₀", "E = 0"],
        "answer": 0,
        "explanation": "Between sheets, fields add: E = σ/(2ε₀) + σ/(2ε₀) = σ/ε₀. Outside, they cancel. Principle of parallel plate capacitors."
    },
    {
        "question": "For a uniformly charged spherical shell (radius R, charge q), what is E at r > R?",
        "options": ["E = kq/r²", "E = 0", "E = kq/R²", "E = kq/r"],
        "answer": 0,
        "explanation": "E = kq/r² = (1/4πε₀)(q/r²). Outside a spherical shell, field is identical to a point charge at the center."
    },
    {
        "question": "What is E inside a uniformly charged spherical shell?",
        "options": ["E = 0", "E = kq/r²", "E = kq/R²", "E = ρr/(3ε₀)"],
        "answer": 0,
        "explanation": "E = 0 inside a charged spherical shell. By Gauss's law, no charge is enclosed inside, so flux and field are zero."
    },
    {
        "question": "For a uniformly charged solid sphere (density ρ, radius R), what is E at r < R?",
        "options": ["E = ρr/(3ε₀)", "E = ρR/(3ε₀)", "E = kQ/r²", "E = 0"],
        "answer": 0,
        "explanation": "E = ρr/(3ε₀). Inside a uniform sphere, field increases linearly with r. Q_enc = ρ(4/3)πr³. By Gauss's law: E(4πr²) = ρ(4/3)πr³/ε₀."
    },
    {
        "question": "What is electrostatic shielding?",
        "options": ["A conducting surface prevents external static E-field from penetrating", "A method to increase field inside conductor", "Charging by induction", "Measuring electric potential"],
        "answer": 0,
        "explanation": "Electrostatic shielding: a conducting surface redistributes charges to cancel external fields inside. E=0 inside a conductor. Safe in a car during lightning."
    },
    {
        "question": "What is a Faraday cage?",
        "options": ["A conducting enclosure that blocks external electric fields", "A device to store charge", "A type of capacitor", "A high voltage generator"],
        "answer": 0,
        "explanation": "A Faraday cage is a conducting enclosure/mesh that blocks external electric fields. Fields within conductor cancel external fields, making E=0 inside."
    },
    {
        "question": "What is the electric flux through a closed surface with no enclosed charge?",
        "options": ["Zero", "Infinite", "Maximum", "Depends on area"],
        "answer": 0,
        "explanation": "By Gauss's law, if Q_enc = 0, then Φ_E = 0. Charges outside the surface do not contribute to net flux through a closed surface."
    },
    {
        "question": "A Gaussian surface is chosen based on:",
        "options": ["Symmetry of charge distribution", "Size of charges", "Color of material", "Temperature"],
        "answer": 0,
        "explanation": "Gaussian surface is chosen based on symmetry (spherical, cylindrical, planar) to simplify flux and field calculations."
    },
    {
        "question": "For a spherical Gaussian surface around a point charge, E is:",
        "options": ["Perpendicular to surface and constant in magnitude", "Parallel to surface", "Zero everywhere", "Varying in magnitude"],
        "answer": 0,
        "explanation": "For spherical Gaussian surface around point charge, E is radial (perpendicular to surface) and constant in magnitude at all points due to symmetry."
    },
    {
        "question": "What is the differential form of Gauss's Law?",
        "options": ["∇·E = ρ/ε₀", "∇×E = 0", "∇·E = 0", "∇×E = ρ/ε₀"],
        "answer": 0,
        "explanation": "∇·E = ρ/ε₀. Divergence of E equals charge density divided by ε₀. Relates local field behavior to charge density."
    },

    # === ELECTRIC POTENTIAL (31-50) ===
    {
        "question": "Two charges q₁ = +2μC and q₂ = -3μC are 0.5 m apart in vacuum. Calculate potential energy.",
        "options": ["-0.108 J", "+0.108 J", "-0.054 J", "+0.216 J"],
        "answer": 0,
        "explanation": "U = k(q₁q₂)/r = (8.987×10⁹)(2×10⁻⁶)(-3×10⁻⁶)/0.5 = -0.108 J. Negative means attraction; work needed to separate them."
    },
    {
        "question": "For q₁ = 4.0×10⁻⁴ C and q₂ = 3.4×10⁻² C at 0.34 mm, calculate potential energy.",
        "options": ["3.6×10⁸ J", "1.8×10⁸ J", "7.2×10⁸ J", "0.9×10⁸ J"],
        "answer": 0,
        "explanation": "U = kq₁q₂/r = (9×10⁹)(4.0×10⁻⁴)(3.4×10⁻²)/(3.4×10⁻⁴) = (9×10⁹)(4.0×10⁻⁴)(100) = 3.6×10⁸ J."
    },
    {
        "question": "A charge q = 2μC is at 0.4 m from a point. What is the electric potential?",
        "options": ["4.49×10⁴ V", "2.25×10⁴ V", "8.98×10⁴ V", "1.12×10⁴ V"],
        "answer": 0,
        "explanation": "V = kq/r = (8.987×10⁹)(2×10⁻⁶)/0.4 = 4.49×10⁴ V ≈ 44,900 V."
    },
    {
        "question": "For q₁ = 4.0×10⁻⁴ C and q₂ = 3.4×10⁻² C at 0.34 mm, what is potential at A due to q₂?",
        "options": ["9.0×10¹¹ V", "1.06×10¹⁰ V", "4.5×10¹¹ V", "2.0×10¹¹ V"],
        "answer": 0,
        "explanation": "V_A = kq₂/r = (9×10⁹)(3.4×10⁻²)/(3.4×10⁻⁴) = (9×10⁹)(100) = 9.0×10¹¹ V."
    },
    {
        "question": "A charge q = +3μC moves from A (12 V) to B (5 V). Calculate work done.",
        "options": ["-21 μJ", "+21 μJ", "-36 μJ", "+36 μJ"],
        "answer": 0,
        "explanation": "ΔV = 5 - 12 = -7 V. W = qΔV = (3×10⁻⁶)(-7) = -21×10⁻⁶ J = -21 μJ. Negative means field does work on the charge."
    },
    {
        "question": "Two positive charges 12×10⁻¹⁰ C and 8×10⁻¹⁰ C are 10 cm apart. What is the potential difference between points 10 cm and 6 cm from the first charge?",
        "options": ["72 V", "108 V", "180 V", "36 V"],
        "answer": 0,
        "explanation": "V at 10 cm = k(12×10⁻¹⁰)/0.1 = 108 V. V at 6 cm = k(12×10⁻¹⁰)/0.06 = 180 V. ΔV = 180 - 108 = 72 V."
    },
    {
        "question": "If potential changes from 100 V to 40 V over 2 meters, what is the electric field?",
        "options": ["30 V/m", "-30 V/m", "60 V/m", "-60 V/m"],
        "answer": 0,
        "explanation": "E = -dV/dx = -(40-100)/2 = 30 V/m. The negative sign in E = -dV/dx means E points in direction of decreasing potential."
    },
    {
        "question": "Given V = 6x + 3y, find the electric field.",
        "options": ["-6i - 3j", "6i + 3j", "-3i - 6j", "3i + 6j"],
        "answer": 0,
        "explanation": "E = -∇V = -(∂V/∂x i + ∂V/∂y j) = -(6i + 3j) = -6i - 3j. E is the negative gradient of potential."
    },
    {
        "question": "For V = 6x + 3y, what is |E| at (0,0)?",
        "options": ["6.71 N/C", "9.00 N/C", "3.00 N/C", "15.0 N/C"],
        "answer": 0,
        "explanation": "E = -6i - 3j. |E| = √(6² + 3²) = √45 = 6.71 N/C. Direction: tanθ = 3/6 = 0.5, θ = 26.56°."
    },
    {
        "question": "Find the potential difference to give a helium nucleus (q = 3.2×10⁻¹⁹ C) 48000 eV energy.",
        "options": ["2.4×10⁴ V", "4.8×10⁴ V", "1.2×10⁴ V", "9.6×10⁴ V"],
        "answer": 0,
        "explanation": "W = qΔV. 48000 eV = 48000×1.6×10⁻¹⁹ J = 7.68×10⁻¹⁵ J. ΔV = W/q = 7.68×10⁻¹⁵/3.2×10⁻¹⁹ = 2.4×10⁴ V."
    },
    {
        "question": "Calculate E at 5 m from a point charge of 10 nC.",
        "options": ["3.6 N/C", "7.2 N/C", "1.8 N/C", "14.4 N/C"],
        "answer": 0,
        "explanation": "E = kQ/r² = (9×10⁹)(10×10⁻⁹)/25 = 90/25 = 3.6 N/C."
    },
    {
        "question": "The potential difference in a thunderstorm is 2.0×10⁹ V. What is ΔU for an electron?",
        "options": ["3.2×10⁻¹⁰ J", "1.6×10⁻¹⁰ J", "6.4×10⁻¹⁰ J", "2.0×10⁻¹⁰ J"],
        "answer": 0,
        "explanation": "ΔU = qΔV = (1.6×10⁻¹⁹)(2.0×10⁹) = 3.2×10⁻¹⁰ J. Energy gained by electron accelerated through this potential."
    },
    {
        "question": "If V(y) = ay/(b²+y²), what is E?",
        "options": ["E = -dV/dy (requires differentiation)", "E = ay/(b²+y²)", "E = a/(b²+y²)", "E = 0"],
        "answer": 0,
        "explanation": "E = -dV/dy = -d/dy[ay/(b²+y²)] = -[a(b²+y²)-ay(2y)]/(b²+y²)² = a(y²-b²)/(b²+y²)²."
    },
    {
        "question": "For a point charge Q, the electric potential V at distance r is:",
        "options": ["V = kQ/r", "V = kQ/r²", "V = kQr", "V = Q/(4πε₀r²)"],
        "answer": 0,
        "explanation": "V = kQ/r = Q/(4πε₀r). Potential decreases as 1/r (not 1/r² like field). Positive Q gives positive V; negative Q gives negative V."
    },
    {
        "question": "What is the electric field inside a conductor in electrostatic equilibrium?",
        "options": ["Zero", "Maximum", "Equal to surface field", "Depends on charge"],
        "answer": 0,
        "explanation": "E = 0 inside a conductor in electrostatic equilibrium. External fields cause charge redistribution until internal field cancels it. Basis of electrostatic shielding."
    },
    {
        "question": "What is the potential gradient?",
        "options": ["Rate of change of potential with distance: dV/dx", "Electric field magnitude", "Charge density", "Current per unit area"],
        "answer": 0,
        "explanation": "Potential gradient = dV/dx. Electric field E = -dV/dx (negative of potential gradient). E points in direction of steepest potential decrease."
    },
    {
        "question": "For a uniform electric field E and displacement d along the field, what is ΔV?",
        "options": ["ΔV = -Ed", "ΔV = Ed", "ΔV = E/d", "ΔV = 0"],
        "answer": 0,
        "explanation": "ΔV = -Ed. The negative sign indicates potential decreases in the direction of the electric field. Moving with the field means moving to lower potential."
    },
    {
        "question": "The potential difference between two points A and B due to point charge Q is:",
        "options": ["ΔV = kQ(1/r_B - 1/r_A)", "ΔV = kQ(r_B - r_A)", "ΔV = kQ/r", "ΔV = 0"],
        "answer": 0,
        "explanation": "ΔV = V_B - V_A = kQ(1/r_B - 1/r_A) = (Q/4πε₀)(1/r_B - 1/r_A). Potential difference depends only on positions, not on test charge."
    },
    {
        "question": "For the potential V = 2x²yz³ + 3xy³z², what is Ex?",
        "options": ["Ex = -(4xyz³ + 3y³z²)", "Ex = 4xyz³ + 3y³z²", "Ex = -(2x²z³ + 9xy²z²)", "Ex = -(6x²yz² + 6xy³z)"],
        "answer": 0,
        "explanation": "Ex = -∂V/∂x = -(4xyz³ + 3y³z²). E component is the negative partial derivative of potential with respect to that coordinate."
    },
    {
        "question": "For V = 2x²yz³ + 3xy³z², what is Ey?",
        "options": ["Ey = -(2x²z³ + 9xy²z²)", "Ey = 2x²z³ + 9xy²z²", "Ey = -(4xyz³ + 3y³z²)", "Ey = -(6x²yz² + 6xy³z)"],
        "answer": 0,
        "explanation": "Ey = -∂V/∂y = -(2x²z³ + 9xy²z²). At (1,-1,2): Ey = -(16 + 36) = -52."
    },
    {
        "question": "For V = 2x²yz³ + 3xy³z², what is Ez?",
        "options": ["Ez = -(6x²yz² + 6xy³z)", "Ez = 6x²yz² + 6xy³z", "Ez = -(4xyz³ + 3y³z²)", "Ez = -(2x²z³ + 9xy²z²)"],
        "answer": 0,
        "explanation": "Ez = -∂V/∂z = -(6x²yz² + 6xy³z). At (1,-1,2): Ez = -(6(1)(-1)(4) + 6(1)(-1)(2)) = -(-24-12) = 36."
    },

    # === ELECTRIC CHARGE FUNDAMENTALS (51-65) ===
    {
        "question": "State the Law of Conservation of Charge.",
        "options": ["Charges can neither be created nor destroyed, only transferred", "Like charges repel and unlike charges attract", "Charge is quantized in units of e", "Total charge in isolated system is always zero"],
        "answer": 0,
        "explanation": "Law of Conservation of Charge: charges can neither be created nor destroyed, only transferred from one body to another. Total charge in an isolated system remains constant."
    },
    {
        "question": "State the Law of Electrostatics.",
        "options": ["Like charges repel while unlike charges attract", "Opposite charges repel", "Charges are always conserved", "Electric field lines never cross"],
        "answer": 0,
        "explanation": "Law of Electrostatics: like charges repel while unlike charges attract. This is the fundamental principle of electrostatic interactions."
    },
    {
        "question": "What happens when glass is rubbed with silk?",
        "options": ["Glass becomes positively charged", "Glass becomes negatively charged", "Silk becomes positively charged", "No charge is transferred"],
        "answer": 0,
        "explanation": "Glass rubbed with silk becomes positively charged. Electrons transfer from glass to silk, leaving glass with electron deficit (positive) and silk with excess electrons (negative)."
    },
    {
        "question": "What happens when ebonite is rubbed with fur?",
        "options": ["Ebonite becomes negatively charged", "Ebonite becomes positively charged", "Fur becomes negatively charged", "No charge transfer occurs"],
        "answer": 0,
        "explanation": "Ebonite rubbed with fur becomes negatively charged. Electrons transfer from fur to ebonite, giving ebonite excess electrons."
    },
    {
        "question": "When a polythene strip is rubbed with wool, what happens?",
        "options": ["Polythene becomes negatively charged", "Polythene becomes positively charged", "Wool becomes negatively charged", "Both become positively charged"],
        "answer": 0,
        "explanation": "Polythene becomes negatively charged. Loosely held electrons in wool transfer to polythene. Wool, having lost electrons, becomes positively charged."
    },
    {
        "question": "What is the structure of an atom?",
        "options": ["Central nucleus with protons and neutrons, electrons orbiting", "Uniformly distributed positive charge with embedded electrons", "Solid sphere of positive charge", "Electrons and protons mixed uniformly"],
        "answer": 0,
        "explanation": "Atom has central nucleus with protons (+) and neutrons (0), electrons (-) orbiting. Atom is neutral when proton number equals electron number."
    },
    {
        "question": "What happens when a neutral atom gains an electron?",
        "options": ["It becomes negatively charged", "It becomes positively charged", "It remains neutral", "It becomes radioactive"],
        "answer": 0,
        "explanation": "When a neutral atom gains an electron, it has more negative charges than positive, so it becomes negatively charged (anion)."
    },
    {
        "question": "What happens when a neutral atom loses an electron?",
        "options": ["It becomes positively charged", "It becomes negatively charged", "It remains neutral", "It disintegrates"],
        "answer": 0,
        "explanation": "When a neutral atom loses an electron, it has more positive charges (protons) than negative, so it becomes positively charged (cation)."
    },
    {
        "question": "What is electrostatic induction?",
        "options": ["Charging a neutral body by placing a charged body near it without contact", "Charging by rubbing two materials", "Transfer of charge by direct contact", "Flow of charge through a conductor"],
        "answer": 0,
        "explanation": "Electrostatic induction: charging a neutral body by bringing a charged body near it (no contact). Charges redistribute: opposite charges attracted to near side, like charges repel to far side."
    },
    {
        "question": "What are the four fundamental forces of nature?",
        "options": ["Gravity, Electromagnetism, Strong force, Weak force", "Gravity, Friction, Magnetism, Electricity", "Nuclear, Chemical, Mechanical, Thermal", "Pull, Push, Twist, Lift"],
        "answer": 0,
        "explanation": "Four fundamental forces: Gravity (mass attraction), Electromagnetism (charge interactions), Strong force (binds quarks/nucleons), Weak force (beta decay)."
    },
    {
        "question": "Which force binds quarks together?",
        "options": ["Strong force", "Weak force", "Electromagnetism", "Gravity"],
        "answer": 0,
        "explanation": "Strong force (mediated by gluons) binds quarks into protons and neutrons, and holds protons and neutrons in the nucleus."
    },
    {
        "question": "Which force is responsible for beta decay?",
        "options": ["Weak force", "Strong force", "Electromagnetism", "Gravity"],
        "answer": 0,
        "explanation": "Weak force is responsible for beta decay (neutron → proton + electron + antineutrino). Mediated by W⁻, W⁺, and Z⁰ bosons."
    },
    {
        "question": "What particle mediates the electromagnetic force?",
        "options": ["Photon", "Gluon", "Graviton", "W boson"],
        "answer": 0,
        "explanation": "Electromagnetic force is mediated by photons. Photons are massless particles carrying electromagnetic interaction between charged particles."
    },
    {
        "question": "What particle is theorized to mediate gravity?",
        "options": ["Graviton", "Photon", "Gluon", "Higgs boson"],
        "answer": 0,
        "explanation": "Graviton is the theorized force carrier for gravity. Unlike other force carriers, it has not yet been experimentally detected."
    },
    {
        "question": "Which force governs an apple falling from a tree?",
        "options": ["Gravity", "Electromagnetism", "Strong force", "Weak force"],
        "answer": 0,
        "explanation": "Gravity governs the motion of an apple falling from a tree. It is the attractive force between masses (Newton's law of universal gravitation)."
    },

    # === CONDUCTORS & INSULATORS (66-75) ===
    {
        "question": "Which is a good conductor of electricity?",
        "options": ["Silver", "Plastic", "Rubber", "Glass"],
        "answer": 0,
        "explanation": "Silver is an excellent conductor. Good conductors have many free electrons. Insulators like plastic, rubber, and glass have no free electrons."
    },
    {
        "question": "Which material is a semiconductor?",
        "options": ["Silicon", "Copper", "Glass", "Paper"],
        "answer": 0,
        "explanation": "Silicon is a semiconductor. Semiconductors have conductivity between conductors and insulators. Other examples: Germanium, Carbon."
    },
    {
        "question": "Why are metals good conductors?",
        "options": ["They have free electrons that move throughout the material", "Their atoms are tightly packed", "They have high melting points", "They are magnetic"],
        "answer": 0,
        "explanation": "Metals are good conductors because they have free electrons (delocalized) not bound to any particular atom, moving freely through the material."
    },
    {
        "question": "What characterizes an electrical insulator?",
        "options": ["Electrons are tightly held and not free to move", "It has many free electrons", "It conducts electricity easily", "It has metallic bonds"],
        "answer": 0,
        "explanation": "In insulators, electrons are tightly bound to atoms and not free to move. This prevents electric current flow. Examples: plastic, rubber, glass, paper, nylon."
    },
    {
        "question": "The human body is classified as:",
        "options": ["Poor conductor", "Good conductor", "Insulator", "Semiconductor"],
        "answer": 0,
        "explanation": "Human body is a poor conductor (but still conducts due to water and ions). Conducts better than insulators but much worse than metals."
    },
    {
        "question": "Water is classified as:",
        "options": ["Poor conductor", "Good conductor", "Insulator", "Semiconductor"],
        "answer": 0,
        "explanation": "Pure water is a poor conductor. Tap water conducts due to dissolved ions. In classification tables, water is listed as a poor conductor."
    },
    {
        "question": "Which is NOT an insulator?",
        "options": ["Aluminum", "Plastic", "Rubber", "Nylon"],
        "answer": 0,
        "explanation": "Aluminum is a metal and good conductor. Plastic, rubber, and nylon are all insulators."
    },
    {
        "question": "In charging an electroscope by induction, what is the first step?",
        "options": ["Bring a charged rod near the cap", "Touch the cap with a finger", "Remove the finger", "Remove the rod"],
        "answer": 0,
        "explanation": "Step 1: Bring charged rod near cap. This induces charge separation - free electrons repelled to leaf (if rod negative), causing leaf to diverge."
    },
    {
        "question": "In induction charging, what happens when you touch the cap with a finger while rod is nearby?",
        "options": ["Electrons flow to earth through the hand", "Electrons flow from earth to the cap", "Nothing happens", "The leaf diverges more"],
        "answer": 0,
        "explanation": "Step 2: Touch cap with finger. Electrons repelled toward earth through hand (grounding). Leaf closes as electrons leave."
    },
    {
        "question": "After removing the finger (but before removing rod) in induction charging, what is left on the cap?",
        "options": ["A net positive charge", "A net negative charge", "No charge", "Equal positive and negative charges"],
        "answer": 0,
        "explanation": "Step 3: Remove finger. Net positive charge remains on cap (electrons escaped to earth). Rod still holds induced charges in place."
    },

    # === ELECTRIC FIELD PROPERTIES (76-85) ===
    {
        "question": "Electric field lines begin from ___ and end on ___.",
        "options": ["Positive charge, negative charge", "Negative charge, positive charge", "North pole, south pole", "Any charge, infinity"],
        "answer": 0,
        "explanation": "Electric field lines begin from positive charges and end on negative charges. For isolated charge, they extend to infinity (outward for +, inward for -)."
    },
    {
        "question": "Do electric field lines ever cross?",
        "options": ["No, that would imply two field directions at one point", "Yes, between opposite charges", "Only for like charges", "Only in non-uniform fields"],
        "answer": 0,
        "explanation": "Electric field lines never cross. Crossing would mean two different directions for E at one point, which is physically impossible."
    },
    {
        "question": "What does the density of electric field lines represent?",
        "options": ["Strength of the electric field", "Direction of the field", "Potential difference", "Charge magnitude"],
        "answer": 0,
        "explanation": "Density of field lines represents field strength. More lines per unit area = stronger field. Fewer lines = weaker field."
    },
    {
        "question": "In a uniform electric field, field lines are:",
        "options": ["Parallel and equally spaced", "Converging to a point", "Diverging from a point", "Forming closed loops"],
        "answer": 0,
        "explanation": "In uniform electric field, field lines are parallel and equally spaced. Field has same magnitude and direction everywhere. Example: between parallel charged plates."
    },
    {
        "question": "What is the direction of E at any point?",
        "options": ["Tangent to the electric field line at that point", "Perpendicular to the field line", "Toward the nearest charge", "Away from all charges"],
        "answer": 0,
        "explanation": "Direction of E at any point is tangent to the electric field line at that point. This gives direction of force on a positive test charge."
    },
    {
        "question": "What is the SI unit of electric field intensity?",
        "options": ["N/C or V/m", "J/C", "N·m", "C/m²"],
        "answer": 0,
        "explanation": "E = F/q, so unit is N/C. Also E = -dV/dx, so unit is V/m. Both are equivalent: 1 N/C = 1 V/m."
    },
    {
        "question": "What is the relationship between E and V?",
        "options": ["E = -dV/dx", "E = dV/dx", "E = V/x", "E = V²/x"],
        "answer": 0,
        "explanation": "E = -dV/dx. Electric field is the negative gradient of potential. Negative sign indicates E points in direction of decreasing potential."
    },
    {
        "question": "What is E inside a conductor in electrostatic equilibrium?",
        "options": ["Zero", "Maximum", "Equal to surface field", "Depends on charge"],
        "answer": 0,
        "explanation": "E = 0 inside a conductor in electrostatic equilibrium. External fields cause charge redistribution until internal field cancels it. Basis of electrostatic shielding."
    },
    {
        "question": "What is an electric dipole?",
        "options": ["Two equal and opposite charges separated by small distance", "Two like charges close together", "A single charged particle", "A charged conducting sphere"],
        "answer": 0,
        "explanation": "Electric dipole: two equal and opposite charges (+q and -q) separated by small distance (2a). Examples: water, ammonia, HCl molecules."
    },
    {
        "question": "What is the unit of electric dipole moment?",
        "options": ["C·m (Coulomb-meter)", "N/C", "V/m", "J/C"],
        "answer": 0,
        "explanation": "Dipole moment p = q×2a, so unit is C·m. It is a vector pointing from -q to +q."
    },

    # === DIPOLE ADVANCED (86-95) ===
    {
        "question": "On the equatorial line of a dipole, the electric field is:",
        "options": ["Opposite to the dipole moment direction", "In the same direction as dipole moment", "Zero", "Perpendicular to the dipole axis"],
        "answer": 0,
        "explanation": "On equatorial line, E = (1/4πε₀)(p/r³), directed opposite to dipole moment p. Field is parallel to axis but opposite to p direction."
    },
    {
        "question": "At any point at distance r from a dipole, E depends on:",
        "options": ["Angle θ with the dipole axis", "Only distance r", "Only dipole moment p", "Charge magnitude q"],
        "answer": 0,
        "explanation": "E = (1/4πε₀)(p/r³)√(1+3cos²θ). Field depends on both distance r and angle θ with dipole axis. Maximum at θ=0° (axial), minimum at θ=90° (equatorial)."
    },
    {
        "question": "What is the potential energy of a dipole in an electric field?",
        "options": ["U = -pE cosθ", "U = pE sinθ", "U = pE", "U = p/E"],
        "answer": 0,
        "explanation": "U = -p·E = -pE cosθ. Minimum energy (most stable) when p aligns with E (θ=0°). Maximum when anti-parallel (θ=180°)."
    },
    {
        "question": "The potential due to a dipole at distance r is:",
        "options": ["V = (p cosθ)/(4πε₀r²)", "V = p/(4πε₀r²)", "V = p/(4πε₀r³)", "V = 0"],
        "answer": 0,
        "explanation": "V = (p cosθ)/(4πε₀r²). Potential falls as 1/r² (faster than 1/r for point charge). At θ=90° (equatorial), V=0."
    },
    {
        "question": "On the axial line of a dipole, the electric field is:",
        "options": ["E = (1/4πε₀)(2p/r³)", "E = (1/4πε₀)(p/r³)", "E = 0", "E = (1/4πε₀)(p/r²)"],
        "answer": 0,
        "explanation": "On axial line: E = (1/4πε₀)(2p/r³). Twice the magnitude of the equatorial field at the same distance. Direction is same as p (away from dipole)."
    },
    {
        "question": "For a dipole with q = 3μC and separation 0.1 m, what is the dipole moment?",
        "options": ["3×10⁻⁷ C·m", "6×10⁻⁷ C·m", "3×10⁻⁶ C·m", "6×10⁻⁶ C·m"],
        "answer": 0,
        "explanation": "p = q×2a = (3×10⁻⁶)(0.1) = 3×10⁻⁷ C·m. Dipole moment is the product of charge magnitude and separation distance."
    },
    {
        "question": "What is the torque on a dipole in a uniform electric field?",
        "options": ["τ = pE sinθ", "τ = pE cosθ", "τ = p/E", "τ = p + E"],
        "answer": 0,
        "explanation": "τ = pE sinθ = p × E (cross product). Torque tends to align dipole moment p with the electric field E direction."
    },
    {
        "question": "When is the torque on a dipole maximum?",
        "options": ["When θ = 90° (perpendicular to field)", "When θ = 0° (parallel to field)", "When θ = 180° (anti-parallel)", "When θ = 45°"],
        "answer": 0,
        "explanation": "Maximum torque when θ = 90°: τ_max = pE sin(90°) = pE. At this angle, the dipole is perpendicular to the field and experiences maximum twisting force."
    },
    {
        "question": "When is the potential energy of a dipole minimum?",
        "options": ["When θ = 0° (aligned with field)", "When θ = 90°", "When θ = 180°", "When θ = 45°"],
        "answer": 0,
        "explanation": "U = -pE cosθ. Minimum when cosθ = 1 (θ = 0°), so U_min = -pE. This is the most stable configuration where dipole is aligned with the field."
    },
    {
        "question": "What is the electric field at the center of a dipole (midpoint between charges)?",
        "options": ["Zero (fields from +q and -q cancel)", "Maximum", "Equal to axial field", "Undefined"],
        "answer": 0,
        "explanation": "At the center of a dipole, the electric fields from +q and -q are equal and opposite, so they cancel exactly. E = 0 at the midpoint."
    },

    # === CONTINUOUS CHARGE & SUPERPOSITION (96-100) ===
    {
        "question": "What is linear charge density λ?",
        "options": ["Charge per unit length", "Charge per unit area", "Charge per unit volume", "Total charge"],
        "answer": 0,
        "explanation": "Linear charge density λ = ΔQ/ΔL. For small element, dQ = λdL. Unit: C/m. Used for charged wires, rods."
    },
    {
        "question": "What is surface charge density σ?",
        "options": ["Charge per unit area", "Charge per unit length", "Charge per unit volume", "Total charge divided by radius"],
        "answer": 0,
        "explanation": "Surface charge density σ = ΔQ/ΔA. For small element, dQ = σdA. Unit: C/m². Used for charged sheets, plates, shells."
    },
    {
        "question": "What is volume charge density ρ?",
        "options": ["Charge per unit volume", "Charge per unit area", "Charge per unit length", "Mass per unit volume"],
        "answer": 0,
        "explanation": "Volume charge density ρ = ΔQ/ΔV. For small element, dQ = ρdV. Unit: C/m³. Used for uniformly charged spheres, cylinders."
    },
    {
        "question": "State the Principle of Superposition for electric fields.",
        "options": ["Net E is the vector sum of all individual E fields at that point", "Net E is the scalar sum of all E fields", "Only the strongest E field matters", "E fields cancel each other always"],
        "answer": 0,
        "explanation": "Superposition Principle: when multiple E fields are present at a point, the net E is the vector sum of all individual E fields at that point. E_net = E₁ + E₂ + E₃ + ..."
    },
    {
        "question": "For a continuous charge distribution, the total electric field is found by:",
        "options": ["Integrating contributions from all infinitesimal charge elements", "Adding charges algebraically", "Multiplying charge densities", "Using only Gauss's law"],
        "answer": 0,
        "explanation": "For continuous distributions, E = (1/4πε₀)∫(dq/r²)r̂. Integrate contributions from all infinitesimal elements dq, taking the limit as Δq → 0 (summation becomes integration)."
    },
]


# ============================================================
# CBT APPLICATION CLASS
# ============================================================

class PhysicsCBT:
    """Computer-Based Testing System for Physics 102"""

    def __init__(self, shuffle=True):
        self.questions = QUESTIONS.copy()
        if shuffle:
            random.shuffle(self.questions)
        self.current_index = 0
        self.score = 0
        self.answered = 0
        self.wrong_answers = []
        self.total_questions = len(self.questions)

    def display_question(self, idx):
        """Display a question with formatted options"""
        q = self.questions[idx]
        print("\n" + "="*70)
        print(f"QUESTION {idx + 1} OF {self.total_questions}")
        print("="*70)
        print(f"\n{q['question']}\n")

        for i, opt in enumerate(q['options']):
            letter = chr(65 + i)  # A, B, C, D
            print(f"  {letter}. {opt}")
        print()

    def get_user_answer(self):
        """Get and validate user input"""
        while True:
            user_input = input("Your answer (A/B/C/D or Q to quit): ").strip().upper()

            if user_input == 'Q':
                return 'QUIT'

            if user_input in ['A', 'B', 'C', 'D']:
                return ord(user_input) - 65  # Convert to 0, 1, 2, 3

            print("Invalid input! Please enter A, B, C, D, or Q.")

    def check_answer(self, q_idx, user_ans):
        """Check if answer is correct and display feedback"""
        q = self.questions[q_idx]
        correct_ans = q['answer']
        correct_letter = chr(65 + correct_ans)

        if user_ans == correct_ans:
            print("\n" + "✓"*35)
            print("✓✓✓  CORRECT!  ✓✓✓")
            print("✓"*35)
            self.score += 1
            return True
        else:
            user_letter = chr(65 + user_ans)
            print("\n" + "✗"*35)
            print(f"✗✗✗  WRONG! You chose {user_letter}  ✗✗✗")
            print("✗"*35)
            print(f"\n>>> CORRECT ANSWER: {correct_letter}. {q['options'][correct_ans]}")
            print(f"\n📚 EXPLANATION:")
            print(f"{q['explanation']}")

            self.wrong_answers.append({
                'question_num': q_idx + 1,
                'question': q['question'],
                'your_answer': q['options'][user_ans],
                'correct_answer': q['options'][correct_ans],
                'explanation': q['explanation']
            })
            return False

    def show_progress(self):
        """Display current progress"""
        print(f"\n{'─'*70}")
        print(f"Progress: {self.answered}/{self.total_questions} | Score: {self.score}/{self.answered}")
        print(f"{'─'*70}")

    def show_final_results(self):
        """Display comprehensive final results"""
        print("\n")
        print("╔" + "="*68 + "╗")
        print("║" + " "*20 + "FINAL RESULTS" + " "*35 + "║")
        print("╚" + "="*68 + "╝")

        print(f"\n📊 TOTAL QUESTIONS: {self.total_questions}")
        print(f"✅ CORRECT ANSWERS: {self.score}")
        print(f"❌ WRONG ANSWERS: {self.total_questions - self.score}")

        percentage = (self.score / self.total_questions) * 100
        print(f"\n📈 PERCENTAGE: {percentage:.2f}%")

        # Grade
        if percentage >= 70:
            grade = "A - EXCELLENT! 🏆"
        elif percentage >= 60:
            grade = "B - VERY GOOD! 🌟"
        elif percentage >= 50:
            grade = "C - GOOD! 👍"
        elif percentage >= 40:
            grade = "D - FAIR 📚"
        else:
            grade = "F - NEEDS MORE STUDY 📖"

        print(f"\n🎓 GRADE: {grade}")

        # Show wrong answers review
        if self.wrong_answers:
            print("\n" + "─"*70)
            print("📋 REVIEW OF WRONG ANSWERS:")
            print("─"*70)
            for i, wa in enumerate(self.wrong_answers, 1):
                print(f"\n{i}. Q{wa['question_num']}: {wa['question'][:80]}...")
                print(f"   Your answer: {wa['your_answer']}")
                print(f"   Correct: {wa['correct_answer']}")

        print("\n" + "="*70)
        print("Thank you for taking the Physics 102 CBT!")
        print("="*70)

    def run(self):
        """Main CBT execution loop"""
        print("\n")
        print("╔" + "="*68 + "╗")
        print("║" + " "*15 + "PHYSICS 102 CBT EXAM" + " "*33 + "║")
        print("║" + " "*10 + "Coulomb's Law, Electric Field, Gauss's Law" + " "*16 + "║")
        print("║" + " "*18 + "Electric Potential & Dipoles" + " "*22 + "║")
        print("╚" + "="*68 + "╝")
        print(f"\nTotal Questions: {self.total_questions}")
        print("Instructions: Answer each question. If wrong, you'll see the")
        print("explanation before moving to the next question.")
        print("Type Q anytime to quit.\n")
        input("Press ENTER to start...")

        while self.current_index < self.total_questions:
            self.display_question(self.current_index)
            user_ans = self.get_user_answer()

            if user_ans == 'QUIT':
                print("\n⚠️  Exam terminated early.")
                break

            self.check_answer(self.current_index, user_ans)
            self.answered += 1
            self.current_index += 1

            if self.current_index < self.total_questions:
                self.show_progress()
                input("\nPress ENTER for next question...")

        self.show_final_results()
        return self.score, self.total_questions


# ============================================================
# MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    # Create and run the CBT
    cbt = PhysicsCBT(shuffle=True)  # Set shuffle=False for fixed order
    cbt.run()
