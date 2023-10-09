import streamlit as st
from calculate_reactivity import calculate_reactivity_indices

def welcome_message():
    st.sidebar.title("Welcome to the Reactivity Indices Calculator")
    st.sidebar.write("If you have any questions or suggestions, feel free to reach out to me at mahmoodmsaad9@gmail.com")

def main():
    # Display a welcome message
    welcome_message()

    # User inputs and calculations
    units = st.selectbox("Select input units:", ["eV", "Kcal/mol", "hetree"])
    homo_value = st.number_input("Enter HOMO value:")
    lumo_value = st.number_input("Enter LUMO value:")

    # Convert values to eV for calculations
    if units == "Kcal/mol":
        homo_ev = homo_value * 0.043364
        lumo_ev = lumo_value * 0.043364
    elif units == "hetree":
        homo_ev = homo_value * 27.2114
        lumo_ev = lumo_value * 27.2114
    else:
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
