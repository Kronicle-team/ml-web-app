<h1 align="center" style="color:#FD8477;font-size:70px;font-family:Georgia;text-align:center;">
    Kronicle Deep Learning Web App on Streamlit
</h1>

<p align="center">
  <strong>Tensorflow + OpenCV web application</strong>
</p>

<p align="center">
<a href="https://youtu.be/xatEzD7jfxM" target="blank">Demo on YouTube <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="tnathu-ai" height="30" width="40" /></a> 
</p>



----------

## Main Purpose 
The web app support the listing function on the organization's [Official trading photocard website](https://kronicle.netlify.app) by helping seller to classifying their products into appropriate category

-------------

## 📌 Features
The app contains a few key features:

+ Classifying most of SEVENTEEN photocards into provided categories
+ Identifying K-pop group members' faces from these groups: Blackpink, SEVENTEEN, Big Bang
+ Identify photocard's faces, smile, eyes
+ Adjust photocard colors grading


----------------------------

#### 📱 Basic Screen shots

|<a href="#"><img src="https://i.ibb.co/DQqyw58/classify-category.jpg" alt="classify category" width="700px"/></a>|<a href="#"><img src="https://i.ibb.co/k3r0G2X/identify-face.jpg" alt="identify faces" width="700px"/></a>|<a href="#"><img src="https://i.ibb.co/ZW0s0Bd/edit.jpg" alt="edit" width="700px"/></a>|
|:--:|:--:|:--:|
|Classify photocards category|Identify Idol face and group|Edit photocard image|

-------------------

## 🎉 Local Environment Setup
We used Python 3.8 or conda using Python 3.8, Pycharm as an IDE installed on our system. No other software or libraries required.

 1. Clone the *forked* repo to your local machine using the IDE of your interest (we used Pycharm here).

 ```bash
 git clone https://github.com/Kronicle-team/ml-web-app.git
 ```  

 2. Ensure that you have the prerequisite Python libraries installed on your local machine:

 ```bash
 pip install -r requirements.txt
```

 3. Navigate to the base of the cloned repo, and start the Streamlit app.

 ```bash
 cd ml-web-app/
 streamlit run app.py
 ```

 4. If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

```
  You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
```

You should also be automatically directed to the base page of your web app. This should look something like:

![Streamlit base page](https://i.ibb.co/hdqRwgG/CNN-web-app.jpg)


--------------------

## Folder Structure & Architecture

```
ml-web-app
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
│
└── requirements.txt
│
└── test
    ├── test_app.py
 ```


## License

Our app was built with Streamlit - a completely free and open-source and licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.
