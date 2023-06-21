import streamlit as st
import matplotlib.pyplot as plt
a=[1,2,3,4,5,14,12]
b=[1,2,3,4,5,14,12]
st.header ("Section Start")
st.text ("Bugün bayramdir1")
fig, ax = plt.subplots(1,1)
ax.scatter (x=a, y=b)
ax.set_xlabel("x ekseni")
ax.set_ylabel("y ekseni")
st.pyplot(fig)

possible_platforms = ["Carousell", "Foo", "Bar"]

for pfm in possible_platforms:
    st.markdown(
        f"""
    <style>
    span[data-baseweb="tag"]:has(span[title="{pfm}"]) {{
    background-color: blue !important;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )
