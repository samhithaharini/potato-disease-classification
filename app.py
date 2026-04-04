import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("potato_model.keras")

class_names = [
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy"
]

st.title("Potato Disease Classification")
st.write("Upload a potato leaf image to predict disease")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

def preprocess_image(image):
    image = image.resize((256, 256))
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    processed_image = preprocess_image(image)

    predictions = model.predict(processed_image)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    if predicted_class == "Potato___Early_blight":
        st.error("Early Blight Detected")
    elif predicted_class == "Potato___Late_blight":
        st.warning("Late Blight Detected")
    else:
        st.success("Healthy Leaf")

    st.write("Confidence: {:.2f}%".format(confidence))