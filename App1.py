mport streamlit as st

# Set up the title and description with emojis and a bright background color
st.markdown(
    """
    <style>
    .app-title {
        color: #FF6347; 
        font-size: 50px; 
        text-align: center; 
        font-weight: bold;
    }
    .instruction {
        color: #4682B4; 
        font-size: 25px; 
        text-align: center;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# App title
st.markdown("<p class='app-title'>🎉 Fun Adding App for Toddlers 🎉</p>", unsafe_allow_html=True)
st.markdown("<p class='instruction'>Let's add two numbers together!</p>", unsafe_allow_html=True)

# Number inputs
first_number = st.number_input("Enter the first number:", min_value=0, max_value=100)
second_number = st.number_input("Enter the second number:", min_value=0, max_value=100)

# Calculate and display result with a button
if st.button("Add Them Up!"):
    result = first_number + second_number
    st.markdown(f"<h3 style='color: #32CD32; text-align: center;'>The sum is: {result} 🎈</h3>", unsafe_allow_html=True)
