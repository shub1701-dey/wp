import streamlit as st
import pickle

st.subheader("weather Prediction App..")
pn=st.number_input("Enter Precipitation ")
maxt=st.number_input("Enter Maximun Temp")
mint=st.number_input("Enter minimun Temp")
wind=st.number_input("Eter Wind Speed")
button=st.button("Predict")
if button:
    lr=pickle.load(open("wp.pkl", "rb"))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"today weather situation,{res}")