import streamlit as st
from calculate_reactivity import calculate_reactivity_indices

def main():
    st.title("Reactivity Indices Calculator")

    # User inputs
    units = st.selectbox("Select input units:", ["eV", "Kcal/mol", "hetree"])
    homo_value = st.number_input("Enter HOMO value:")
    lumo_value = st.number_input("Enter LUMO value:")

    # Convert values to eV for calculations
    if units == "Kcal/mol":
        # Conversion factor: 1 Kcal/mol = 0.043364 eV
        homo_ev = homo_value * 0.043364
        lumo_ev = lumo_value * 0.043364
    elif units == "hetree":
        # Conversion factor: 1 hetree = 27.2114 eV
        homo_ev = homo_value * 27.2114
        lumo_ev = lumo_value * 27.2114
    else:
        # eV input
        homo_ev = homo_value
        lumo_ev = lumo_value

    # Calculate reactivity indices
    reactivity_indices = calculate_reactivity_indices(homo_ev, lumo_ev)

    # Display the results
    st.header("Reactivity Indices:")
    for key, value in reactivity_indices.items():
        st.write(f"{key}: {value:.4f} eV")

    # Reference
    st.markdown("Reference: [DOI: 10.1021/acsomega.1c05504](https://doi.org/10.1021/acsomega.1c05504)")

if __name__ == "__main__":
    main()
