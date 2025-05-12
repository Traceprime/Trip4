import pandas
import streamlit
import plotly.express as px
import altair as alt

print("All packages imported successfully!")
import pandas as pd

df = pd.read_csv("vehicles_us.csv")

print("✅ CSV loaded successfully!")
print("🔍 Preview of the data:")
print(df.head())