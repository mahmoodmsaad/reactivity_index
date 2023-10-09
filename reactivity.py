import streamlit as st
from calculate_reactivity import calculate_reactivity_indices

def main():
    st.title("Reactivity Indices Calculator")

    # User inputs in hetree units
    homo_hetree = st.number_input("Enter HOMO value in hetree:")
    lumo_hetree = st.number_input("Enter LUMO value in hetree:")

    # Calculate reactivity indices
    reactivity_indices = calculate_reactivity_indices(homo_hetree, lumo_hetree)

    # Display the results
    st.header("Reactivity Indices:")
    for key, value in reactivity_indices.items():
        st.write(f"{key}: {value:.4f} eV")

if __name__ == "__main__":
    main()
