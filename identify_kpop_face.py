from tensorflow import keras
from PIL import Image, ImageOps
# Core Pkgs
import streamlit as st
import cv2
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



def identify_kpop_face_app():
    st.title("SEVENTEEN Photocard Classification - Kronicle")
    st.header("SEVENTEEN")
    st.text("Upload a Photocard to Classify")
    # file upload and handling logic
    uploaded_file = st.file_uploader("Choose a photocard", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        # image = Image.open(img_name).convert('RGB')
        st.image(image, width=400, caption='Uploaded a photocard.')
        st.write("")
        st.write("Classifying your Photocard .........hold tight")
        label = photocard_classification(image, 'models/identify_idol_faces/keras_model.h5')
        if label == 0:
            st.write("This looks like a Rose from Blackpink")
        elif label == 1:
            st.write("This looks like Jennie from Blackpink")
        elif label == 2:
            st.write("This looks like Lisa from Blackpink")
        elif label == 3:
            st.write("This looks like Jisoo from Blackpink")
        elif label == 4:
            st.write("This looks like G-Dragon from Big Bang")
        elif label == 5:
            st.write("This looks like T.O.P from Big Bang")
        elif label == 6:
            st.write("This looks like Seungri from Big Bang")
        elif label == 7:
            st.write("This looks like Taeyang from Big Bang")
        elif label == 8:
            st.write("This looks like Daesung from Big Bang")
        elif label == 9:
            st.write("This looks like Seventeen from S.Coups")
        elif label == 10:
            st.write("This looks like Seventeen from Jeonghan")
        elif label == 11:
            st.write("This looks like Seventeen from Joshua")
        elif label == 12:
            st.write("This looks like Seventeen from Hoshi")
        elif label == 13:
            st.write("This looks like Seventeen from Wonwoo")
        else:
            st.write("This looks like a photocard from another group")
        st.write("")

