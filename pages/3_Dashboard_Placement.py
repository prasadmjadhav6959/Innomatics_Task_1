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

image_path1 = os.path.join(dir_of_interest1, "images", "placement.jpg")
data_path1 = os.path.join(dir_of_interest1, "data", "placement.csv")


st.title("Placement")

img = image.imread(image_path1)
st.image(img)

df = pd.read_csv(data_path1)
st.dataframe(df)

placement = st.selectbox("Select the Status:",df["status"].unique())

col1, col2, col3, col4  = st.columns(4)

fig_1 = px.histogram(df[df['status'] == placement], x="salary")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['status'] == placement], y="degree_p")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.scatter(df[df['status'] == placement], y="hsc_p")
col3.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.scatter(df[df['status'] == placement], y="ssc_p")
col4.plotly_chart(fig_4, use_container_width=True)