# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# Judul
st.title('Prediksi Kualitas Air')

# Deskripsi
st.write('Aplikasi ini memprediksi kualitas air (Potability) berdasarkan parameter yang diinputkan')
# Parameter
ph = st.number_input('pH', min_value=0.0, max_value=14.0, value=7.0)
Hardness = st.number_input('Hardness', min_value=0.0, max_value=500.0, value=150.0)
Solids = st.number_input('Solids (Total dissolved solids)', min_value=0.0, max_value=50000.0, value=20000.0)
Chloramines = st.number_input('Chloramines', min_value=0.0, max_value=20.0, value=4.0)
Sulfate = st.number_input('Sulfate', min_value=0.0, max_value=500.0, value=250.0)
Conductivity = st.number_input('Conductivity', min_value=0.0, max_value=1000.0, value=400.0)
Organic_carbon = st.number_input('Organic_carbon', min_value=0.0, max_value=50.0, value=10.0)
Trihalomethanes = st.number_input('Trihalomethanes', min_value=0.0, max_value=200.0, value=80.0)
Turbidity = st.number_input('Turbidity', min_value=0.0, max_value=10.0, value=5.0)

# DataFrame dari input
input_data = pd.DataFrame({
        'ph': [ph],
        'Hardness': [Hardness],
        'Solids': [Solids],
        'Chloramines': [Chloramines],
        'Sulfate': [Sulfate],
        'Conductivity': [Conductivity],
        'Organic_carbon': [Organic_carbon],
        'Trihalomethanes': [Trihalomethanes],
        'Turbidity': [Turbidity]
    })
# Bagi train test
# Bagi data 70:30 latih dan uji
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.30, random_state=42)
# Load model
model = RandomForestClassifier(criterion='entropy', max_depth=11, max_features='sqrt', min_samples_leaf=2, min_samples_split=3)
model.fit(X_train, y_train)
# Prediksi
prediction = model.predict(input_data)[0]

# Hasil
if st.button('Prediksi'):
    if prediction == 1:
        st.success('Air **Layak Minum**')
    else:
        st.error('Air **Tidak Layak Minum**')
