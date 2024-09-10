import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import pickle

cars_df=pd.read_csv('car_price.csv')
st.header('Cars24 Used cars price prediction')
st.dataframe(cars_df.head())

col1,col2=st.columns(2)

fuel_type=col1.selectbox('Fuel type',(cars_df['fuel_type'].unique()))
transmission_type=col1.selectbox('Transmission type',(cars_df['transmission_type'].unique()))
seats=col2.selectbox('Seats',(4,6,7,9,11))
engine_power=col2.slider('Engine power',500,5000,step=100)

encode_dict={
    'fuel_type':{'Diesel':1,'Petrol':2,'CNG':3,'LPG':4,'Electric':5},
    'seller_type':{'Individual':1,'Dealer':2,'Trustmark Dealer':3},
    'transmission_type':{'Manual':1,'Automatic':2}
}

fuel_type=encode_dict['fuel_type'][fuel_type]
transmission_type=encode_dict['transmission_type'][transmission_type]

def model_pred(fuel_type,transmission_type,seats,engine_power):
    with open('car_pred','rb') as file:
        model=pickle.load(file)
        input_features=[[2018.0,1,4000,fuel_type,transmission_type,19.70,engine_power,86.30,seats]]
        return np.round(model.predict(input_features),2)

if st.button('Predict price'):
    price=model_pred(fuel_type,transmission_type,seats,engine_power)
    st.text(f'The estimated selling price of the car is {price[0]} lakhs')

