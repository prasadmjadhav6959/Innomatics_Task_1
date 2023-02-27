import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
file_directory1 = os.path.dirname(os.path.abspath(__file__))

# absolute path to this file's root directory
parent_directory1 = os.path.join(file_directory1, os.pardir)

# absolute path of directory of interest
dir_of_interest1 = os.path.join(parent_directory1,"resources")

image_path1 = os.path.join(dir_of_interest1, "images", "titanic.jpg")
data_path1 = os.path.join(dir_of_interest1, "data", "titanic.csv")


st.title("Titanic")

img = image.imread(image_path1)
st.image(img)

df = pd.read_csv(data_path1)
st.dataframe(df)

sex = st.selectbox("Select the Gender:",df["Sex"].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Sex'] == sex], x="Survived")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Sex'] == sex], y="Survived")
col2.plotly_chart(fig_2, use_container_width=True)
