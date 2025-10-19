import streamlit as st
from fastai.vision.all import *

st.title("Cat vs Dog Classifier")
st.text("Built by Abigail Chang")

def is_cat(f):
    return f[0].isupper() # returns true or false

cat_vs_dog_mod1 = load_learner("cat-vs-dog.pkl")

def predict(image):
    img = PILImage.create(image)
    pred_class, pred_idx, outputs = cat_vs_dog_mod1.predict(img)
    print("pred_class = "+pred_class) # cat: true, dog: false
    print("pred_idx = "+str(pred_idx))
    print("output = "+str(outputs))
    if pred_class == "True":
        likehood = outputs[1].item()
        animal = "cat"
    else:
        likehood = outputs[0].item()
        animal = "dog"
    if likehood > 0.9:
        return f"I'm {round(likehood * 100, 2)}% confident this is a {animal.title()}!"
    else:
        return f"Not sure... but I'm {round(likehood * 100, 2)}% confident it's a {animal}."


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    prediction = predict(uploaded_file)
    st.subheader(prediction)
    st.image(uploaded_file,caption="Uploaded Image", use_container_width=True)


