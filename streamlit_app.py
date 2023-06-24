import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import mpld3
import streamlit.components.v1 as components

pd.set_option('display.max_columns', None)
df = pd.read_csv('son.csv', delimiter=';')
#df['birlesik']=df['Year']+df['Quarter']

# = df['Year'].astype(str) + "_" + df['Quarter']
st.text(df['Quarter'][6])

df['Quarter'] = df['Quarter'].apply(lambda x: if len(x.split()[1])==1 "0"+str(int(x.split()[1])*3) else str(int(x.split()[1])*3)) 

for i in range (len(df['Year'])):
    df['Year'][i] = str(df['Year'][i]) + df['Quarter'][0]

st.text(df['Year'])

#df['Year'] = df['Year'].apply(lambda x: pd.to_datetime(str(x), format='%Y%MM'))

year = df['Year']
const = df['Construction_costs']
material = df['Material_costs']
labour = df['Labour_costs']

st.text("Task description: Comparison of house prices, (construction prices - optional), \nand mortgage rates/volumes. The period of the time series is quarterly between \n2003-2023.")

st.text("Steps:")
st.text("1- Get data (Some reference links are provided below.")
st.text("2- Create interactive plotly charts (EDA)")
st.text("3- Explain general insights gained from basic EDA summary statistics mean, min, max , negative/positive correlated etc.,")
st.text("4- Explain insights related to the last quarter eg. the change in the current quarter is ..., etc.")
st.text("5- Show results on a preferably on a Streamlit  app.")




st.header ("Missing values1")

st.text(df.isnull().sum())

st.header("Columns")
st.text(df.columns)

st.header("Describe")
st.text (df.describe())

st.header ("Section Start")



fig, ax = plt.subplots(1,1)
plt.plot(year,const)
#plt.plot(df['Year'],material)
#plt.plot(df['Year'],labour)



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
