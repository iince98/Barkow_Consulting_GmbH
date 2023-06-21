import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('son.csv')

a=[1,2,3,4,5,14,12]
b=[1,2,3,4,5,14,12]
st.text (df[0])
st.header ("Section Start")
st.text ("Bugün bayramdir2")
fig, ax = plt.subplots(1,1)
ax.scatter (x=a, y=b)
ax.set_xlabel("x ekseni")
ax.set_ylabel("y ekseni")
st.pyplot(fig)

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
