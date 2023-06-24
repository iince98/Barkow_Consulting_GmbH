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

st.header ("Missing values1")
st.text(df.isnull().sum())
st.text(df.columns)
st.text (df.describe())
st.header ("Section Start")


""" fig, ax = plt.subplots(1,1)
fig = plt.figure(figsize=(12, 5))
plt.plot(df['Year'],b) """
fig, ax = plt.subplots(1,1)
plt.plot(df['Year'],const)
plt.plot(df['Year'],material)
plt.plot(df['Year'],labour)

st.pyplot(fig)
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)

possible_platforms = ["Carousell", "Foo", "Bar1"]

for pfm in possible_platforms:
    st.markdown(
        f"""
    <style>
    span[data-baseweb="tag"]:has(span[title="{pfm}"]) {{
    background-color: green !important;
    color:red;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

st.markdown("Report Category Specific Parameters")

st.multiselect("Platform", possible_platforms)
with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    st.text (f.read())


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
