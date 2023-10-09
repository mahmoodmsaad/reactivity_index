import streamlit as st
from calculate_reactivity import calculate_reactivity_indices

def main():
    st.title("Reactivity Indices Calculator")

    # User inputs
    homo_ev = st.number_input("Enter HOMO value in eV:", value=0.0, step=0.01)
    lumo_ev = st.number_input("Enter LUMO value in eV:", value=0.0, step=0.01)

    if homo_ev < 0 or lumo_ev < 0:
        st.warning("Negative values are ignored. Please enter positive values for HOMO and LUMO.")

    # Calculate reactivity indices
    reactivity_indices = calculate_reactivity_indices(homo_ev, lumo_ev)

    # Display the results
    st.header("Reactivity Indices:")
    for key, value in reactivity_indices.items():
        st.write(f"{key}: {value:.4f} eV")

if __name__ == "__main__":
    main()
