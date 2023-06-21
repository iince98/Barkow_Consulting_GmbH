import streamlit as st
import matplotlib.pyplot as plt
a=[1,2,3,4,5]
b=[12,16,3,15,4]
st.header ("Section Start")
for i in range (1,15):
  st.write (i, " Hello world")
fig, ax = plt.subplots(1,1)
ax.scatter (x=a, y=b)
st.pyplot(fig)
