import streamlit as st
import streamlit.components.v1 as stc
from ml_app import run_ml_app
from eda_app import run_eda_app

# config function
st.set_page_config(
    page_title="Kronicle",
    page_icon='assets/logo.png',
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Kronicle-team/Kpop-Idol-Photocard-Classification',
        'Report a bug': "https://github.com/Kronicle-team/Kpop-Idol-Photocard-Classification",
        'About': "# > Creator: Tran Ngoc Anh Thu  ·  Kronicle  ·  ",
    }
)


html_temp = """
		<div style="background-color:#FEDBCD;padding:10px;border-radius:10px">
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
        modal = st.expander("Advanced options")

        option_1 = modal.checkbox("Option 1")
        option_2 = modal.checkbox("Option 2")
        option_3 = modal.checkbox("Option 3")
        option_4 = modal.checkbox("Option 4")

        if option_1:
            st.write("Hello world 1")

        if option_2:
            st.write("Hello world 2")

        if option_3:
            st.write("Hello world 3")

        if option_4:
            st.write("Hello world 4")


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)  # hide streamlit style

if __name__ == '__main__':
    main()
