import streamlit as st
# Set the app title and add some color using markdown
st.markdown("<h1 style='color: purple;'>Fun Adding App for Toddlers </h1>",🎉
unsafe_allow_html=True)
st.markdown("<h3 style='color: teal;'>Let's add two numbers together! </h3>",🤗
unsafe_allow_html=True)
# Get user input for the first number
first_number = st.number_input("Enter the first number:", min_value=0, step=1)
# Get user input for the second number
second_number = st.number_input("Enter the second number:", min_value=0, step=1)
# Calculate the sum when the button is pressed
if st.button("Calculate Sum"):
result = first_number + second_number
st.markdown(f"<h2 style='color: green;'>The sum is: {result}</h2>",
unsafe_allow_html=True)
else:
st.write("Enter numbers above and click 'Calculate Sum' to see the result!")
# Footer for fun styling
st.markdown("<p style='color: grey; font-style: italic;'>Made with for little❤️
mathematicians!</p>", unsafe_allow_html=True)
