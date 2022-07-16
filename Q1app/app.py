import streamlit as st
from pathlib import Path
import joblib
import numpy as np



def load_model(model):
    filename = model+".sav"
    model_path = Path(__file__).parents[0] / filename
    joblib_model = joblib.load(model_path)
    return joblib_model


st.title("Faulty Check Prediction")

models = ("RandomForest", "XGBoost","MLP")
modelname = st.selectbox("Model :",models)

st.write("""### Input Sensors Data""")
col1, col2 = st.columns(2)
with col1:
  CH1Temp1 = st.number_input("CH1Temp1")
  CH1Temp2 = st.number_input("CH1Temp2")
  CHP1Vib1 = st.number_input("CHP1Vib1")
  CHP1Vib2 = st.number_input("CHP1Vib2")
with col2:
  CH2Temp1 = st.number_input("CH2Temp1")
  CH2Temp2 = st.number_input("CH2Temp2")
  CHP2Vib1 = st.number_input("CHP2Vib1")
  CHP2Vib2 = st.number_input("CHP2Vib2")
ok = st.button("Check")
if ok:
  model = load_model(modelname)
  X = np.array([CH1Temp1,CH1Temp2,CH2Temp1,CH2Temp2,
  CHP1Vib1,CHP1Vib2,CHP2Vib1,CHP2Vib2])
  X = X.reshape(-1,8)
  ypred = model.predict(X)
  if ypred[0] == 0:
    ans = 'Not Faulty'
  else:
    ans = 'Faulty'
  st.subheader(f"The result is {ans}")

