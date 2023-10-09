def calculate_reactivity_indices(homo_value, lumo_value, units='eV'):
    # Convert HOMO and LUMO values to eV for calculations
    if units == 'Kcal/mol':
        # Conversion factor: 1 Kcal/mol = 0.043364 eV
        homo_ev = homo_value * 0.043364
        lumo_ev = lumo_value * 0.043364
    elif units == 'hetree':
        # Conversion factor: 1 hetree = 27.2114 eV
        homo_ev = homo_value * 27.2114
        lumo_ev = lumo_value * 27.2114
    else:
        # eV input
        homo_ev = homo_value
        lumo_ev = lumo_value

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

# Example usage
homo_value = -0.225  # Replace with your HOMO value
lumo_value = 0.112   # Replace with your LUMO value
units = 'hetree'  # Replace with the desired input unit (eV, Kcal/mol, hetree)

reactivity_indices = calculate_reactivity_indices(homo_value, lumo_value, units)

# Print the results
for key, value in reactivity_indices.items():
    print(f"{key}: {value:.4f} eV")
