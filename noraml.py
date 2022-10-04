from turtle import color
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from keras.models import load_model
import math
classifier = load_model('Genetic_model.h5')
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(Number_of_Vehicles,Vehicle_Speed,Light_Conditions,Weather_Conditions,Road_Surface_Conditions,Chainage_km):  
   
    prediction=classifier.predict(
        [[int(Number_of_Vehicles),
          int(Vehicle_Speed),
          int(Light_Conditions),
          int(Weather_Conditions),
          int(Road_Surface_Conditions),
          int(Chainage_km)]])
    prediction=math.ceil(prediction)
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.set_page_config(layout="wide")
    st.title("PREDICTION OF ACCIDENTS USING ARTIFICIAL INTELIGENCE ")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-White:LavenderBlush;padding:13px">
    <h1 style ="color:brown;">Accident  Prediction Using Genetic Algorithm </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    st.date_input("Select Future date")
    Number_of_Vehicles = st.text_input("Number_of_Vehicles")
    Vehicle_Speed=st.slider("Vehicle_Speed",0,180)
    
    Light_Conditions1= st.selectbox("Lighting_Conditions:",['Darkness - lighting unknown',
                                                                'Darkness - lights lit',
                                                                'Darkness - lights unlit',
                                                                'Darkness - no lighting',
                                                                'Daylight'])
    if Light_Conditions1=="Darkness - lighting unknown":
        Light_Conditions=0
    elif Light_Conditions1=="Darkness - lights lit":
        Light_Conditions=1
    elif Light_Conditions1=="Darkness - lights unlit":
        Light_Conditions=2   
    elif Light_Conditions1=="Darkness - no lighting":
        Light_Conditions=3
    elif Light_Conditions1=="Daylight":
        Light_Conditions=4


    Weather_Conditions1 = st.selectbox("Weather_Conditions:",['Fine + high winds',
                                                              'Fine no high winds',
                                                              'Fog or mist',
                                                              'Other',
                                                              'Raining + high winds',
                                                              'Raining no high winds',
                                                              'Snowing + high winds',
                                                              'Snowing no high winds'])
    if Weather_Conditions1=="Fine + high winds":
        Weather_Conditions=0
    elif Weather_Conditions1=="Fine no high winds":
        Weather_Conditions=1
    elif Weather_Conditions1=="Fog or mist":
        Weather_Conditions=2   
    elif Weather_Conditions1=="Other":
        Weather_Conditions=3
    elif Weather_Conditions1=="Raining + high winds":
        Weather_Conditions=4
    elif Weather_Conditions1=="Raining no high winds":
        Weather_Conditions=5
    elif Weather_Conditions1=="Snowing + high winds":
        Weather_Conditions=6
    elif Weather_Conditions1=="Snowing no high winds":
        Weather_Conditions=7
    
    Road_Surface_Conditions1 = st.selectbox("Road_Surface_Conditions:",['Dry',
                                                 'Flood_over_3cm_deep',
                                                 'Frost or ice',
                                                 'Snow',
                                                 'Wet or damp'])
    if Road_Surface_Conditions1=="Dry":
        Road_Surface_Conditions=0
    elif Road_Surface_Conditions1=="Flood_over_3cm_deep":
        Road_Surface_Conditions=1
    elif Road_Surface_Conditions1=="Frost or ice":
        Road_Surface_Conditions=2   
    elif Road_Surface_Conditions1=="Snow":
        Road_Surface_Conditions=3
    elif Road_Surface_Conditions1=="Wet or damp":
        Road_Surface_Conditions=4

    Chainage_km=st.slider("Distance In Km from Pun To bangalore",0,50)
    
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result=prediction(Number_of_Vehicles,Vehicle_Speed,Light_Conditions,Weather_Conditions,Road_Surface_Conditions,Chainage_km) 
  
    st.success(st.title('Predicted No Of Accidents ------->>{}'.format(result)))
    if Chainage_km==15:
        dist="This is black Spot"
    elif Chainage_km==2:
        dist="This is black Spot"
    elif Chainage_km==13:
        dist="This is black Spot"
    elif Chainage_km==14:
        dist="This is black Spot"
    elif Chainage_km==17:
        dist="This is black Spot"
    else :
        dist="This Is Not black spot"
    st.success(st.title(dist))
    
    
    if Vehicle_Speed>=70:
        distance="This Is High Speed" 
    else:
        distance="This is No High Speed"
        
    st.success(st.title(distance))
   
    st.title("Light Condition Analysis")
    st.image("Images\Light con.png")
    st.image("Images\light pie.png")
    st.title("Vehicle Speed Analysis")
    st.image("Images\Vehicle Speed.png")
    st.image("Images\Vehicle pie.png")
    st.title("Wheather condition Analysis")
    st.image("Images\Wheather con.png")
    st.image("Images\Whea pie.png")
    st.title("Road Surface Condition Analysis")
    st.image("Images\Road_surf.png")
if __name__=='__main__':
    main()
