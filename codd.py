import streamlit as st

def largest_number(a, b, c):
    """Returns the largest of three numbers."""
    return max(a, b, c)

# Streamlit interface
st.title("Find the largest number among three")
a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

if st.button("largest number"):
    result = largest_number(a, b, c)
    st.write(f"The largest number is {result}")
