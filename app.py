import streamlit as st

st.title("Streamlit App")
st.subheader("Secondary Header")
st.text("Streamlit Text")
st.write("Streamlit write")

# Streamlit Select Options
lang = st.selectbox(
    "Choose Your Favourite Language", ["Python", "C++", "Java", "JavaScript"]
)
st.write(f"You have chosen {lang}")
st.success("You have chosen succesfully")
