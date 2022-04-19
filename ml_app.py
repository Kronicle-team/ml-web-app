import streamlit as st
from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np


# add styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def photocard_classification(img, file):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = keras.models.load_model(file)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = img
    # image = Image.open(img_name).convert('RGB')
    # image = cv2.imread(image)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    # print(prediction)
    return np.argmax(prediction)


def run_ml_app():
    st.title("SEVENTEEN Photocard Classification - Kronicle")
    st.header("SEVENTEEN")
    st.text("Upload a photocard to classify")
    # file upload and handling logic
    uploaded_file = st.file_uploader("Choose a photocard", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        # image = Image.open(img_name).convert('RGB')
        st.image(image, caption='Uploaded a photocard.', use_column_width=True)
        st.write("")
        st.write("Classifying a photocard .........hold tight")
        label = photocard_classification(image, 'keras_model.h5')
        if label == 0:
            st.write("This photocard looks like SEVENTEEN Attacca Album photocards.")
        elif label == 1:
            st.write("This photocard looks like SEVENTEEN Heng Garæ Album photocards.")
        elif label == 2:
            st.write("This photocard looks like SEVENTEEN Caratland trading cards.")
        elif label == 3:
            st.write("This photocard looks like SEVENTEEN Haru Tour trading cards.")
        elif label == 4:
            st.write("This photocard looks like SEVENTEEN Incomplete 2021 trading cards.")
        elif label == 5:
            st.write("Oops! This is not a SEVENTEEN trading cards.")
