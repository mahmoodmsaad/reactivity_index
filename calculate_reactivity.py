# calculate_reactivity.py
def calculate_reactivity_indices(homo_ev, lumo_ev):
    # Calculate delta_E in eV
    delta_e = lumo_ev - homo_ev

    # Calculate electronegativity, chemical potential, hardness, electrophilicity, and softness
    electronegativity = (homo_ev + lumo_ev) / 2
    chemical_potential = -electronegativity
    hardness = delta_e / 2
    electrophilicity = (chemical_potential ** 2) / (2 * hardness)
    softness = 1 / (2 * hardness)

    return {
        "HOMO (eV)": homo_ev,
        "LUMO (eV)": lumo_ev,
        "ΔE (eV)": delta_e,
        "Electronegativity (χ)": electronegativity,
        "Chemical Potential (µ)": chemical_potential,
        "Hardness (η)": hardness,
        "Electrophilicity (ɷ)": electrophilicity,
        "Softness (S)": softness,
    }
