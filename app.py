import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("vehicles_us.csv")


st.title("Vehicle Price Explorer")


if st.checkbox("Show raw data"):
    st.write(df.head())


st.subheader("Box Plot: Price by Vehicle Condition")
fig = px.box(
    df,
    x="condition",
    y="price",
    color="condition",
    title="Price Distribution by Condition"
)
st.plotly_chart(fig)


st.subheader("Histogram: Price Distribution")
hist = px.histogram(df, x="price", nbins=50, title="Histogram of Car Prices")
st.plotly_chart(hist)


st.subheader("Scatter Plot: Odometer vs Price")
scatter = px.scatter(df, x="odometer", y="price", color="type", title="Odometer vs Price by Vehicle Type")
st.plotly_chart(scatter)