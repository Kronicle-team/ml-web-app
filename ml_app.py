from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np
# Core Pkgs
import streamlit as st
import cv2
from PIL import Image, ImageEnhance
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


@st.cache
def load_image(img):
    im = Image.open(img)
    return im


face_cascade = cv2.CascadeClassifier('frecog/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('frecog/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('frecog/haarcascade_smile.xml')


def detect_faces(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img, faces


def detect_eyes(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    return img


def detect_smiles(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect Smiles
    smiles = smile_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the Smiles
    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img


def cartonize_image(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Edges
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Color
    color = cv2.bilateralFilter(img, 9, 300, 300)
    # Cartoon
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon


def cannize_image(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    canny = cv2.Canny(img, 100, 150)
    return canny


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

            our_image = Image.open(uploaded_file)
            st.text("Original Image")
            # st.write(type(our_image))
            st.image(our_image)

            enhance_type = st.sidebar.radio("Enhance Type",
                                            ["Original", "Gray-Scale", "Contrast", "Brightness", "Blurring"])
            if enhance_type == 'Gray-Scale':
                new_img = np.array(our_image.convert('RGB'))
                img = cv2.cvtColor(new_img, 1)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # st.write(new_img)
                st.image(gray)
            elif enhance_type == 'Contrast':
                c_rate = st.sidebar.slider("Contrast", 0.5, 3.5)
                enhancer = ImageEnhance.Contrast(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output)

            elif enhance_type == 'Brightness':
                c_rate = st.sidebar.slider("Brightness", 0.5, 3.5)
                enhancer = ImageEnhance.Brightness(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output)

            elif enhance_type == 'Blurring':
                new_img = np.array(our_image.convert('RGB'))
                blur_rate = st.sidebar.slider("Brightness", 0.5, 3.5)
                img = cv2.cvtColor(new_img, 1)
                blur_img = cv2.GaussianBlur(img, (11, 11), blur_rate)
                st.image(blur_img)
            elif enhance_type == 'Original':

                st.image(our_image, width=300)
            else:
                st.image(our_image, width=300)

        # Face Detection
        task = ["Faces", "Smiles", "Eyes", "Cannize", "Cartonize"]
        feature_choice = st.sidebar.selectbox("Find Features", task)
        if st.button("Process"):

            if feature_choice == 'Faces':
                result_img, result_faces = detect_faces(our_image)
                st.image(result_img)

                st.success("Found {} faces".format(len(result_faces)))
            elif feature_choice == 'Smiles':
                result_img = detect_smiles(our_image)
                st.image(result_img)


            elif feature_choice == 'Eyes':
                result_img = detect_eyes(our_image)
                st.image(result_img)

            elif feature_choice == 'Cartonize':
                result_img = cartonize_image(our_image)
                st.image(result_img)

            elif feature_choice == 'Cannize':
                result_canny = cannize_image(our_image)
                st.image(result_canny)
