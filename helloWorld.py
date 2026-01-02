import streamlit as st
st.title("Hello, World!")
st.write("Welcome to my first Streamlit app.")
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"]
)

if genre == "Comedy":
    st.write("You selected: " + genre)
elif genre == "Drama":
    st.write("You selected: " + genre)
elif genre == "Documentary":
    st.write("You selected: " + genre)
else:
    st.write("You didn't select any.")