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

image_path1 = os.path.join(dir_of_interest1, "images", "layoffs.jpg")
data_path1 = os.path.join(dir_of_interest1, "data", "layoffs.csv")


st.title("Layoffs")

img = image.imread(image_path1)
st.image(img)

df = pd.read_csv(data_path1)
st.dataframe(df)

country = st.selectbox("Select the Status:",df["country"].unique())

col1, col2, col3  = st.columns(3)

fig_1 = px.histogram(df[df['country'] == country], x="total_laid_off")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df[df['country'] == country], x="industry")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.scatter(df[df['country'] == country], x="total_laid_off")
col3.plotly_chart(fig_3, use_container_width=True)