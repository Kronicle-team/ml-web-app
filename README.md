# Welcome to Kronicle Deep Learning Web App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](#)


## 🎉Local Environment Setup

```bash
pip install streamlit
```

 1. Ensure that you have the prerequisite Python libraries installed on your local machine:

 ```bash
pip install -r requirements.txt
 conda install -c conda-forge scikit-surprise
 ```

 2. Clone the *forked* repo to your local machine.

 ```bash
 git clone https://github.com/Kronicle-team/ml-web-app.git
 ```  

 3. Navigate to the base of the cloned repo, and start the Streamlit app.

 ```bash
 cd ml-web-app/
 streamlit run app.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
```

You should also be automatically directed to the base page of your web app. This should look something like:

![Streamlit base page](#)


--------------------

```
demo-web-app
│
├── .streamlit
│   └── config.toml
│
├── app
│   ├── main.py
│   └── utils.py
│
├── assets
│   ├── background.png
│   └── icon.png
│
├── data
│   └── olympiad-problems.csv
│
└── requirements.txt
│
└── requirements.txt
    ├── test_app.py
 ```


## License

Our app was built with Streamlit - a completely free and open-source and licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.
