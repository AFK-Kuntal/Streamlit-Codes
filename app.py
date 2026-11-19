import streamlit as st

st.title("Streamlit App")
st.subheader("Secondary Header")
st.text("Streamlit Text")
st.write("Streamlit write")

# Streamlit Widgets
# Dropdown menu
lang = st.selectbox(
    "Choose Your Favourite Language", ["Python", "C++", "Java", "JavaScript"]
)
st.write(f"You have chosen {lang}")

# Button
if st.button("Streamlit Button"):
    st.success("Button Pressed")

# checkbox
cbox = st.checkbox("Streamlit")
if cbox:
    st.write(f"You have chosen {cbox}")

# radio
framework = st.radio("Choose your Framework", ["React", "Numpy", "Tensorflow"])
if framework:
    st.write(f"You have chosen {framework}")

# slider
prof = st.slider("Proficiency", 0, 10, 5)
st.write(f"Your Proficiency level {prof}")

# number input
hours = st.number_input("How many hours you practice", min_value=0, max_value=6, step=1)
st.write(f"total practice hours {hours}")

# text_input
name = st.text_input("Enter Your Name")
if name:
    st.write(f"Welcome {name}")

# date field

dob = st.date_input("Select Your DOB")
st.write(f"{name}'s dob is {dob}")