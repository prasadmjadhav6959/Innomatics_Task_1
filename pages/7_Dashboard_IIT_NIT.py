import streamlit as st
from matplotlib import image
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
file_directory1 = os.path.dirname(os.path.abspath(__file__))

# absolute path to this file's root directory
parent_directory1 = os.path.join(file_directory1, os.pardir)

# absolute path of directory of interest
dir_of_interest1 = os.path.join(parent_directory1,"resources")

image_path1 = os.path.join(dir_of_interest1, "images", "iit_nit.jpg")
data_path1 = os.path.join(dir_of_interest1, "data", "iit_nit.csv")


st.title("IIT & NIT")

img = image.imread(image_path1)
st.image(img)

df = pd.read_csv(data_path1)
st.dataframe(df)

institutes = st.selectbox("Select the Institutes:",df["institute_type"].unique())

fig_1 = px.histogram(df[df['institute_type'] == institutes], x="year")
st.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['institute_type'] == institutes], x="quota")
st.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.histogram(df[df['institute_type'] == institutes], x="opening_rank")
st.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.histogram(df[df['institute_type'] == institutes], x="closing_rank")
st.plotly_chart(fig_4, use_container_width=True)

fig_5 = px.histogram(df[df['institute_type'] == institutes], x="degree_short")
st.plotly_chart(fig_5, use_container_width=True)

fig_6 = px.histogram(df[df['institute_type'] == institutes], x="institute_short")
st.plotly_chart(fig_6, use_container_width=True)

fig_7 = px.histogram(df[df['institute_type'] == institutes], x="program_duration")
st.plotly_chart(fig_7, use_container_width=True)

fig_8 = px.histogram(df[df['institute_type'] == institutes], x="category")
st.plotly_chart(fig_8, use_container_width=True)