import streamlit as st
import streamlit.components.v1 as stc
from ml_app import run_ml_app
from eda_app import run_eda_app

html_temp = """
		<div style="background-color:pink;padding:10px;border-radius:10px">
		<h1 style="color:black;text-align:center;">Kronicle - K-pop Idols and Photocards Classification</h1>
		<h4 style="color:black;text-align:center;">Deep Learning Web App</h4>
		</div>
		"""


def main():
    stc.html(html_temp)

    menu = ["Home", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("""
			### Data Exploration: Analyze K-pop Idols and their Photocards
			The scanning app that uses the CNN model to categorize, verify, and authenticate the photocard.
			#### Project GitHub: 
				- https://github.com/Kronicle-team/Kpop-Idol-Photocard-Classification
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App
				""")

    elif choice == "EDA":
        run_eda_app()
    elif choice == "ML":
        run_ml_app()
    else:
        st.subheader("About Kronicle")
        st.text("Group 5 Project - COSC2634 ")
        st.text("Building IT Systems")
        st.text("May, 2022")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)  # hide streamlit style

if __name__ == '__main__':
    main()
