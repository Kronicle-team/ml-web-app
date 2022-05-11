import streamlit as st

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

import streamlit.components.v1 as stc
from ml_app import run_ml_app
from identify_kpop_face import identify_kpop_face_app
from eda_app import run_edit_app

# add styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

html_temp = """
		<div style="background-color:#435892;padding:10px;border-radius:10px">
		<h1 style="color:#ffffff;subheader-align:center;subheader-shadow: 4px 4px 4px #FFA092">Kronicle - Kpop Idols and Photocards Classification</h1>
		<h4 style="color:#ffffff;subheader-align:center;">Deep Learning Web App</h4>
		</div>
		"""


def main():
    stc.html(html_temp)

    menu = ["HOME", "EDIT", "CLASSIFY CATEGORY", "IDENTIFY KPOP IDOL FACES", "ABOUT"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "HOME":
        st.subheader("Using CNN model to categorize, identify, and edit the photocard.")

        st.text_input('Project GitHub', 'https://github.com/Kronicle-team')
        st.text_input('CLASSIFY CATEGORY Section', 'Allows you to upload your own photocard and identify whether it is an album card or trading card.')
        st.text_input('IDENTIFY KPOP IDOL FACES Section', 'Allows you to upload your own photocard and identify whether it is an album card or trading card.')
        st.text_input('EDIT Section', 'Allows you to upload your own photocard and identify whether it is an album card or trading card.')
        st.text_input('ABOUT Section', 'About the creators and the whole project.')


    elif choice == "EDIT":
        run_edit_app()
    elif choice == "CLASSIFY CATEGORY":
        run_ml_app()
    elif choice == "IDENTIFY KPOP IDOL FACES":
        identify_kpop_face_app()
    else:
        st.subheader("About Kronicle")
        st.subheader("Group 5 Project - COSC2634 ")
        st.subheader("Building IT Systems")
        st.subheader("May, 2022\n")

        st.subheader("The authors of the whole project")
        modal = st.expander("THE TEAM")
        option_1 = modal.checkbox("Tran Ngoc Anh Thu")
        option_2 = modal.checkbox("Doan Yen Nhi")
        option_3 = modal.checkbox("Nguyen Hoang Linh")
        option_4 = modal.checkbox("Du Duc Manh")
        option_5 = modal.checkbox("Hua Minh Thu")

        if option_1:
            st.image(
                "https://i.ibb.co/zZKb9g9/Thu.jpg",
                width=300,  # Manually Adjust the width of the image as per requirement
            )
            st.subheader("Machine Learning Engineer, Full Stack Developer, and UI/UX Designer")

        if option_2:
            st.image(
                "https://i.ibb.co/r5yL27k/Nhi.jpg",
                width=300,  # Manually Adjust the width of the image as per requirement
            )
            st.subheader("Scrum Master, GitHub Admin, and Full Stack Developer")

        if option_3:
            st.image(
                "https://i.ibb.co/qCmg569/Linh.jpg",
                width=300,  # Manually Adjust the width of the image as per requirement
            )
            st.subheader("GitHub Admin and Full Stack Developer")

        if option_4:
            st.image(
                "https://i.ibb.co/LhzjHQC/manh.jpg",
                width=300,  # Manually Adjust the width of the image as per requirement
            )
            st.subheader("GitHub Admin and Full Stack Developer")

        if option_5:
            st.image(
                "https://i.ibb.co/sw1FF9V/Thu-Hua.jpg",
                width=300,  # Manually Adjust the width of the image as per requirement
            )
            st.subheader("UI/UX Designer, Full Stack Developer, and Meeting Minutes Taker", font="monospace")


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)  # hide streamlit style

if __name__ == '__main__':
    main()
