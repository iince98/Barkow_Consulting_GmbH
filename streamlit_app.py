import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('son.csv', delimiter=';')
#df['birlesik']=df['Year']+df['Quarter']
print(df['Period'])

x_ekseni='Year'
a=df[x_ekseni]
b=df['mortgage_rates']
st.text(df.columns)
st.text (df.info(verbose = False))
st.header ("Section Start")


fig, ax = plt.subplots(1,1)
fig = plt.figure(figsize=(12, 5))
plt.plot(df['Year'],b)
plt.xticks(a, a, rotation='horizontal')


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
