import streamlit as st  
import pandas as pd     # Used to work with tabular data
import plotly.data as pldata
import plotly.express as px  

df = pldata.gapminder(return_type='pandas')

st.sidebar.header('Choose Country')


# clean data to display unique country name
countries=pd.Series(df['country']).unique()
default_index=list(countries).index('Canada')
# st.write(default_index)
selected_country = st.sidebar.selectbox('Select Country', countries, index=default_index) 

filtered_by_country_df = df[df['country'] == selected_country] 
st.title('Country information')

st.markdown(':blue[visualization by country]')

st.subheader('Gross Domestic Product by year')  

st.line_chart(filtered_by_country_df, x='year', y='gdpPercap')

st.subheader('Population by year')
st.bar_chart(filtered_by_country_df, x='year', y='pop')

st.markdown(':red[raw data first 50 rows]')

# raw dataset
st.dataframe(df.head(50))

st.markdown(':green[data includes follow countries]')
st.dataframe(countries)

