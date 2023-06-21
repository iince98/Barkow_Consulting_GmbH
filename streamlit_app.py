import streamlit as st
import matplotlib.pyplot as plt
a=[1,2,3,4,5]
b=[12,16,3,15,4,87
st.header ("Section Start")
st.text ("Bugün bayramdir1")
fig, ax = plt.subplots(1,1)
ax.scatter (x=a, y=b)
ax.set_xlabel("x ekseni")
ax.set_ylabel("y ekseni")
st.pyplot(fig)
