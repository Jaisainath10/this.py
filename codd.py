import streamlit as st

def largest_number(a, b, c):
    """Returns the largest of three numbers."""
    return max(a, b, c)

# Streamlit interface
st.title("Find the largest number")
a = st.number_input("Enter the first number:", value=0, step=1)
b = st.number_input("Enter the second number:", value=0, step=1)
c = st.number_input("Enter the third number:", value=0, step=1)

if st.button("Find largest number"):
    result = largest_number(a, b, c)
    st.write(f"The largest number is {result}")
