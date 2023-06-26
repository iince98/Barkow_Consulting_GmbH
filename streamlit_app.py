import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import mpld3
import streamlit.components.v1 as components
import seaborn as sns
from PIL import Image
import numpy as np
import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels)

# Plot!
st.plotly_chart(fig, use_container_width=True)










pd.set_option('display.max_columns', None)
df = pd.read_csv('son.csv', delimiter=';')
#df['birlesik']=df['Year']+df['Quarter']


df['Quarter'] = df['Quarter'].apply(lambda x: str(int(x.split()[1])*3)) 

for i in range (len(df['Year'])):
    df['Year'][i] = str(df['Year'][i]) + df['Quarter'][i]


df['Year'] = df['Year'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m'))

year = df['Year']
const = df['Construction_costs']
material = df['Material_costs']
labour = df['Labour_costs']
house_price = df['House_price_index']
new_residential = df['New_residential_property']
existing_residential = df['Existing_residential_property']
mortgage = df['mortgage_rates']


st.markdown(f'<img src="https://www.barkowconsulting.com/img/barkow_consulting_logo.svg" alt="W3Schools.com">',unsafe_allow_html=True)
#image = Image.open('imza_copy.png')
#st.image(image, caption='Barkow Consulting GmbH')

st.header ("Task")

st.text("Task description: Comparison of house prices, (construction prices - optional), \nand mortgage rates/volumes. The period of the time series is quarterly between \n2003-2023.")

st.text("Steps:")
st.text("1- Get data (Some reference links are provided below.")
st.text("2- Create interactive plotly charts (EDA)")
st.text("3- Explain general insights gained from basic EDA summary statistics mean, min,\n max , negative/positive correlated etc.,")
st.text("4- Explain insights related to the last quarter eg. the change in the \ncurrent quarter is ..., etc.")
st.text("5- Show results on a preferably on a Streamlit  app.")


st.header ("Introduction")
st.markdown ("Data pre-processing, Feature Engineering, and Exploratory Data Analysis (EDA) are fundamental early steps after data collection. Still, they are not limited to where the data is simply visualized, plotted, and manipulated, without any assumptions, to assess thequality of the data and building models.")

st.header ("Missing values")
st.markdown ("Finding 'missing values' is widely been in all pre-processing steps to identify null values in the data. With this, we get the number of missing records in each column")

st.text(df.isnull().sum())

st.header("Columns")
st.text(df.columns)

st.header("Describe")
st.markdown ("The information gives a quick and simple description of the data. It can include Count, Mean, Standard Deviation, median, mode, minimum value, maximum value, range, standard deviation, etc. Statistics summary gives a high-level idea to identify whether the data has any outliers, data entry error, distribution of data such as the data is normally distributed or left/right skewed.")
st.text (df.describe(include="all"))

st.header("Data set")
st.dataframe(df)
st.markdown ("Source: https://www.destatis.de/EN/Themes/Economy/Prices/Construction-Prices-And-Real-Property-Prices/_node.html#267504")
st.markdown ("https://www.destatis.de/en/Themes/Economy/Prices/Construction-Prices-And-Real-Property-Prices/_node.html")
st.markdown ("https://www.bundesbank.de/dynamic/action/en/statistics/time-series-databases/time-series-databases/745582/745582?tsId=BBK01.SUD131&dateSelect=2023")

st.header ("EDA Multivariate Analysis (Heatmap)")
st.markdown ("As the name suggests, Multivariate analysis looks at more than two variables. Multivariate analysis is one of the most useful methods to determine relationships and analyze patterns for any dataset. A heat map is widely been used for Multivariate Analysis. Heat Map gives the correlation between the variables, whether it has a positive or negative correlation. In our example heat map shows the correlation between the variables.")
fig1, ax1 = plt.subplots()
sns.heatmap(df.drop(['Year', 'Quarter'], axis=1).corr(), ax=ax1)
st.write(fig1)


st.header ("Graphics")

fig1, ax1 = plt.subplots(1,1)
plt.plot(year,mortgage,marker=".", markersize="5",color="k", label="mortgage")
plt.legend(loc="upper left")
fig_html1 = mpld3.fig_to_html(fig1)
components.html(fig_html1, height=600)


fig, ax = plt.subplots(1,1)
plt.plot(year,const,marker=".", markersize="5",color="r", label="construction")
plt.plot(year,material,marker=".", markersize="5",color="b", label="material" )
plt.plot(year,labour,marker=".", markersize="5",color="g", label="labour")
plt.plot(year,house_price,marker=".", markersize="5",color="c", label="house_price")
plt.plot(year,new_residential,marker=".", markersize="5",color="m", label="new_residential")
plt.plot(year,existing_residential,marker=".", markersize="5",color="y", label="existing_residential")
plt.legend(loc="upper left")
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)


st.write("Explanation on the last quarter of 2023")
st.markdown ("Although the index values of 'Labour, Material and Construction' shows a rising trend, 'House Prices' decreses. And also it very clear that the percentage of change is also different. It is advised to have a deep look into other factor which effects 'House Prices'. An officiail state explanation may have an impact on 'House Prices'. It would be better to have and use more features having possible effect on 'House Prices'.")




with open ('style.css') as file1:
    st.markdown(f'<style>{file1.read()}</style>',unsafe_allow_html=True)
    st.text (file1.read())