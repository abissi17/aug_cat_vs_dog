import streamlit as st

st.title("Cat vs Dog Classifier")
st.text("Built by Abi")

uploaded_file = st.file_uploader("Choose as image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, use_container_width=True)

st.video("https://www.ayclogic.com/wp-content/uploads/2025/07/Crossing-Street.mp4")

def is_cat(f):
    return f[0].isupper()