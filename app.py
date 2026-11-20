import streamlit as st
import pandas as pd

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

# streamlit columns
col1, col2 = st.columns(2)
with col1:
    st.write("Vote for Python")
    st.image(
        "https://images.unsplash.com/photo-1649180556628-9ba704115795?q=80&w=2324&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        width=200,
    )
    vote1 = st.button(
        "Vote", key="python"
    )  # if content inside two button is same then we have to pass a key of unique id otherwise streamlit throws error
with col2:
    st.write("Vote for C++")
    st.image(
        "https://images.unsplash.com/photo-1743090661056-e51700546169?q=80&w=2340&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
        width=200,
    )
    vote2 = st.button("Vote", key="C++")


# streamlit sidebar
sidebar_name = st.sidebar.text_input("Enter Your Name")
if sidebar_name:
    st.sidebar.title(f"hello {sidebar_name}")
sidebar_selectbox = st.sidebar.selectbox(
    "Enter Your Favourite", ["Python", "C++", "JavaScript"]
)

# streamlit expander
with st.expander("Programming Instructions"):
    st.write("""
        1.Write Clean Code

        2.Try to follow indentation

        3.Keep Variable names unique
    """)

#Markdowns 
st.markdown("### Streamlit Markdown")
st.markdown("> Blockquote")


# Uploading Files and using Pandas with streamlit(we can use any others library too like matplotlib...)
file = st.file_uploader("Upload Your File",type="csv")
if file:
    df = pd.read_csv(file)
    st.subheader("pandas Data Frame Preview")
    st.dataframe(df)
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    crops = df["label"].unique()
    crop=st.selectbox("Select Crop", crops) 
    filtered_crop = df[df["label"] == crop]
    st.dataframe(filtered_crop)
