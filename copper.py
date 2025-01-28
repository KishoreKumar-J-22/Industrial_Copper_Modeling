import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import pymongo as py
import json as js
import time
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.keyboard_url import keyboard_to_url


# Functions
def predict_status(ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,slgplg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)
    #modelfile of the classification
    with open("D:/Capstone_5/Classification_model.pkl","rb") as f:
        model_class=pickle.load(f)

    user_data= np.array([[ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       slgplg,itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0

def predict_selling_price(ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,
                   tknslg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)
    #modelfile of the classification
    with open("D:/Capstone_5/Regression_Model.pkl","rb") as f:
        model_regg=pickle.load(f)

    user_data= np.array([[ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_regg.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred


st.set_page_config(layout= "wide")

st.markdown(
                    "<h1 style='font-size: 65px;'><span style='color:#B87333;'>INDUSTRIAL</span> <span style='color: #B87333 ;'> COPPER </span> <span style='color: cyan ;'>MODELING </span> </h1>",
                    unsafe_allow_html=True)


with st.sidebar:
    option = option_menu('Kishore Kumar', options=["PREDICT SELLING PRICE", "PREDICT STATUS", "FEEDBACK"],
                         icons=['calculator-fill', 'graph-up-arrow','envelope-paper-heart-fill',],
                         menu_icon='alexa')

if option == "PREDICT STATUS":
    

    st.markdown(
                    '''<h1 style='font-size: 50px;'><span style='color:white;'>PREDICT </span> <span style='color: cyan;'> STATUS </span> 
                    <span style='color: white;'> ( </span> <span style='color: cyan;'>Won</span> <span style='color: white;'>/</span>
                    <span style='color: cyan;'>Lose</span> <span style='color: white;'>)</span> </h1>''',
                    unsafe_allow_html=True)

    st.header("")
    st.info("The values in the form are in default values. Please change the values to get the accurate prediction.")

    col1,col2= st.columns(2)

    with col1:


        # Custom CSS to change the font color to copper
        st.markdown("""
            <style>
                .stNumberInput label {
                    font-family: 'Arial', sans-serif;
                    font-size: 16px;
                    color: #B87333;  /* Copper color */
                }
            </style>
        """, unsafe_allow_html=True)

        # Number inputs with the copper-colored labels
        country = st.number_input(label="**Enter the Value for COUNTRY**", min_value=25.0, max_value=113.0)
        item_type = st.number_input(label="**Enter the Value for ITEM TYPE**", min_value=0.0, max_value=6.0)
        application = st.number_input(label="**Enter the Value for APPLICATION**", min_value=2.0, max_value=87.5)
        width = st.number_input(label="**Enter the Value for WIDTH**", min_value=700.0, max_value=1980.0)
        product_ref = st.number_input(label="**Enter the Value for PRODUCT_REF**", min_value=611728, max_value=1722207579)
        quantity_tons_log = st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**", format="%0.15f")
        customer_log = st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**", format="%0.15f")
        thickness_log = st.number_input(label="**Enter the Value for THICKNESS (Log Value)**", format="%0.15f")


       
    
    with col2:

        # Custom CSS to change the font color to copper
        st.markdown("""
            <style>
                .stSelectbox label,.stNumberInput label {
                    font-family: 'comic sans ms', sans-serif;
                    font-size: 16px;
                    color: #B87333;  /* Copper color */
                }
            </style>
        """, unsafe_allow_html=True)

        selling_price_log= st.number_input(label="**Enter the Value for SELLING PRICE (Log Value)**/ Min:5.97503, Max:7.39036",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button(":violet[***PREDICT THE STATUS***]",use_container_width=True)

    if button:
        status= predict_status(country,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,selling_price_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        if status == 1:
            st.write("## :green[**The Status is WON**]")
        else:
            st.write("## :red[**The Status is LOSE**]")

if option == "PREDICT SELLING PRICE":

    st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:white;'>PREDICT</span> <span style='color: cyan;'> SELLING PRICE </span> </h1>",
                    unsafe_allow_html=True)

    st.header("")
    st.write(" ")
    st.info("The values in the form are in minimum default values. Please change the values to get the accurate prediction.")

    col1,col2= st.columns(2)

    with col1:

        # Custom CSS to change the font color to copper
        st.markdown("""
            <style>
                .stNumberInput label {
                    font-family: 'comic sans ms', sans-serif;
                    font-size: 16px;
                    color: #B87333;  /* Copper color */
                }
            </style>
        """, unsafe_allow_html=True)
        country= st.number_input(label="**Enter the Value for COUNTRY**", min_value=25.0, max_value=113.0)
        status= st.number_input(label="**Enter the Value for STATUS**", min_value=0.0, max_value=8.0)
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**", min_value=0.0, max_value=6.0)
        application= st.number_input(label="**Enter the Value for APPLICATION**", min_value=2.0, max_value=87.5)
        width= st.number_input(label="**Enter the Value for WIDTH**", min_value=700.0, max_value=1980.0)
        product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**", min_value=611728, max_value=1722207579)
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**",
                                           format="%0.15f", min_value=-0.3223343801166147, max_value=6.924734324081348)
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**",
                                    format="%0.15f", min_value=17.21910565821408, max_value=17.230155364880137)
        
    
    with col2:
        # Custom CSS to change the font color to copper
        st.markdown("""
            <style>
                .stSelectbox label,.stNumberInput label {
                    font-family: 'comic sans ms', sans-serif;
                    font-size: 16px;
                    color: #B87333;  /* Copper color */
                }
            </style>
        """, unsafe_allow_html=True)
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**",
                                        format="%0.15f", min_value=-1.7147984280919266, max_value=3.281543137578373)
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button(":violet[***PREDICT THE SELLING PRICE***]",use_container_width=True)

    if button:
        price= predict_selling_price(country,status,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        
        st.write("## :green[**The Selling Price is :**]",price)

if option == "FEEDBACK":
    
    if option == "FEEDBACK":
        kishore_1 = py.MongoClient("mongodb+srv://Kishore:mongodb123@cluster-kishore.kznavjg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Kishore")
        db = kishore_1["Feedback_copper"]
        collection = db["comment"]

        st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)
        col1, col2, col3, = st.columns([3, 8, 3])

        with col2:
            selected_1 = option_menu(
                menu_title="OPINION BOX",
                options=['Choose Option', 'Your Feedback', "Explore User Thoughts"],
                icons=['arrow-down-circle-fill', 'envelope-plus-fill', 'people-fill'],
                menu_icon="person",
                default_index=0)
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")

        if selected_1 == 'Choose Option':
            kishore_1 = py.MongoClient("mongodb+srv://Kishore:mongodb123@cluster-kishore.kznavjg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Kishore")
            db = kishore_1["Feedback_copper"]
            collection = db["Reaction_emoji"]
            # Animation
            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)
            # Layout for emoji options
            st.write("Choose your mood:")
            col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

            # Emoji animations
            emoji_files = {
                "Angry": "D:/Air_BnB/angry_emoji.json",
                "Smile": "D:/Air_BnB/smile_emoji.json",
                "Calm": "D:/Air_BnB/calm_emoji.json",
                "Love": "D:/Air_BnB/love_emoji.json",
            }

            # Render Lottie animations in columns
            selected_emoji = None
            with col1:
                if st.button("Angry"):
                    selected_emoji = "Angry"
                file = lottie("D:/Air_BnB/angry_emoji.json")
                st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=200,
                        width=200,
                        key=None
                    )
            with col2:
                if st.button("Smile"):
                    selected_emoji = "Smile"
                file = lottie("D:/Air_BnB/smile_emoji.json")
                st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=200,
                        width=200,
                        key=None
                    )
            with col3:
                if st.button("Calm"):
                    selected_emoji = "Calm"
                file = lottie("D:/Air_BnB/calm_emoji.json")
                st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=200,
                        width=200,
                        key=None
                    )
            with col4:
                if st.button("Love"):
                    selected_emoji = "Love"
                file = lottie("D:/Air_BnB/love_emoji.json")
                st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=200,
                        width=200,
                        key=None
                    )

            # Save selection to MongoDB
            if selected_emoji:
                collection.insert_one({"emoji": selected_emoji})
                st.success(f"Your selection ({selected_emoji}) has been saved!")
                
        elif selected_1 == 'Your Feedback':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])
                col2.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:white;'>Your</span> <span style='color:cyan;'>Feedback</span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                # animation

                st.write("")

                st.write("")

                st.write("")
                col1, col2, col3 = st.columns([10, 15, 5])
                with col2:
                    file = lottie("D:/Air_BnB/star_before_fb.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=600,
                        key=None
                    )
                col1, col2, col3, = st.columns([3, 8, 3])

                with col2:
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:white;'>Enter</span> <span style='color:cyan;'>Comment</span> <span style='color: white;'>Here ⬇️</span> </h1>",
                        unsafe_allow_html=True)
                    Comment = st.text_input('   ')
                    st.write(Comment)
                    if st.button('Save Comment'):
                        collection.insert_one({'comment of user': Comment})
                        st.write("")
                        st.write("")
                        col1, col2, col3, = st.columns([5, 8, 5])
                        st.success('Your Valuable Comment Saved Thankyou!', icon="✅")
                        col1, col2, col3 = st.columns([10, 30, 10])
                        with col2:
                            file = lottie("D:/Air_BnB/star.json")
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                # renderer='svg',
                                height=100,
                                width=500,
                                key=None
                            )
                col1, col2, col3, = st.columns([3, 8, 3])
                with col2:
                        colored_header(
                            label="",
                            description="",
                            color_name="blue-green-70", )
                
        elif selected_1 == 'Explore User Thoughts':

            def lottie(filepath):
                with open(filepath, 'r') as file:
                    return js.load(file)

            col1, col2, col3 = st.columns([10, 30, 5])

            with col2:

                file = lottie("D:/Air_BnB/down_arrow.json")
                st_lottie(
                    file,
                    speed=2,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=300,
                    width=800,
                    key=None
                )
            col2.markdown(
                        "<h1 style='font-size: 70px;'><span style='color:white;'>Explore</span> <span style='color:cyan;'>User Thoughts </span> <span style='color: white;'>Here </span> </h1>",
                        unsafe_allow_html=True)
            col2.write("")
            col2.write("")
            with col2:

                file = lottie("D:/Air_BnB/thoughts.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=800,
                    key=None
                )
            st.write("")
            st.write("")
            st.write("")
            col1, col2, col3, = st.columns([3.6, 10, 3])
            with col2:
                # if st.button("Click Me!"):
                res = [i['comment of user'] for i in collection.find()]
                st.write("")
                with st.spinner('Wait for it...'):
                    time.sleep(5)

                colored_header(
                    label="Comments By Users ⬇",
                    description="",
                    color_name="blue-green-70", )
                for i in res:
                    print(st.code(i))

                col1, col2, col3 = st.columns([1, 10, 1])
                col2.write("")
                col2.write('')
                col2.markdown(
                    "<h1 style='font-size: 35px;'><span style='color:cyan;'>Press</span> <span style='color:white;'>'G'</span> <span style='color:cyan;'>On Keyboard To Explore More Project</span> </h1>",
                    unsafe_allow_html=True)
                with col2:
                    keyboard_to_url(key="G", url="https://github.com/KishoreKumar-J-22")
                def lottie(filepath):
                            with open(filepath, 'r') as file:  # 'G' On Keyboard To Explore More Project
                                return js.load(file)

                with col2:
                    file = lottie("D:/Air_BnB/click2.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        height=100,
                        width=700,
                        key=None
                    )

                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70", )




