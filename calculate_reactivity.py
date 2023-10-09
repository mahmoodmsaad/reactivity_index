def calculate_reactivity_indices(homo_ev, lumo_ev):
    # Calculate delta_E in eV
    delta_e = lumo_ev - homo_ev

    if delta_e == 0:
        # Handle the case where delta_e is zero to avoid division by zero
        return {
            "HOMO (eV)": homo_ev,
            "LUMO (eV)": lumo_ev,
            "ΔE (eV)": delta_e,
            "Electronegativity (χ)": float('nan'),
            "Chemical Potential (µ)": float('nan'),
            "Hardness (η)": float('nan'),
            "Electrophilicity (ɷ)": float('nan'),
            "Softness (S)": float('nan'),
            "Total amount of charge transfer (δN)": float('nan'),
        }

    # Calculate electronegativity, chemical potential, hardness, electrophilicity, and softness
    electronegativity = (homo_ev + lumo_ev) / 2
    chemical_potential = -electronegativity
    hardness = delta_e / 2
    electrophilicity = (chemical_potential ** 2) / (2 * hardness)
    softness = 1 / (2 * hardness)

    # Calculate delta_N (Total amount of charge transfer) in eV
    delta_N = -(chemical_potential / hardness)

    return {
        "HOMO (eV)": homo_ev,
        "LUMO (eV)": lumo_ev,
        "ΔE (eV)": delta_e,
        "Electronegativity (χ)": electronegativity,
        "Chemical Potential (µ)": chemical_potential,
        "Hardness (η)": hardness,
        "Electrophilicity (ɷ)": electrophilicity,
        "Softness (S)": softness,
        "Total amount of charge transfer (δN)": delta_N,
    }
