import sqlite3
import streamlit as st
import pandas as pd
import plotly.express as px


connection = sqlite3.connect('scraper-app10.db')
cursor = connection.cursor()

sqlrequest = cursor.execute("Select date, temperature from temps")
df = sqlrequest.fetchall()

df = pd.DataFrame(df, columns=['date', 'temperature'])

# date = [temp[1] for temp in df]
# temperature = [temp[2] for temp in df]
# df = ([{'date': temp[1], 'temperature': float(temp[2])} for temp in df])

# df = {'date': date, 'temperature': temperature}
figure = px.line(x=df['date'], y=df['temperature'], labels={'x': 'Date', 'y': 'Temperature'})

st.write('Temperatures plot')
st.plotly_chart(figure)