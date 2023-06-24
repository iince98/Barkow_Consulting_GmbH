import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import mpld3
import streamlit.components.v1 as components

pd.set_option('display.max_columns', None)
df = pd.read_csv('son.csv', delimiter=';')
#df['birlesik']=df['Year']+df['Quarter']


const = df['Construction_costs']
material = df['Material_costs']
labour = df['Labour_costs']

st.header("Task description: Comparison of house prices, (construction prices - optional), and mortgage rates/volumes. The period of the time series is quarterly between 2003-2023.")

st.header ("Missing values1")

st.text(df.isnull().sum())

st.header("Columns")
st.text(df.columns)

st.header("Describe")
st.text (df.describe())

st.header ("Section Start")

print(type(df['Year']))


fig, ax = plt.subplots(1,1)
plt.plot(df['Year'],const)
plt.plot(df['Year'],material)
plt.plot(df['Year'],labour)

#st.pyplot(fig)
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)

possible_platforms = ["Carousell", "Foo", "Bar1"]


with open ('style.css') as file1:
    st.markdown(f'<style>{file1.read()}</style>',unsafe_allow_html=True)
    st.text (file1.read())


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
