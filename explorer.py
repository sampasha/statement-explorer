import streamlit as st
import pandas as pd
from datetime import datetime
from babel.numbers import format_currency

st.set_page_config(
   page_title="Finance Explorer",
   layout="wide",
   initial_sidebar_state="expanded",
)


initial_date = st.sidebar.date_input("Start date", key='start')
final_date = st.sidebar.date_input("End date", key='end')
# st.write(initial_date)
transact_df = pd.read_csv('transactions(2017-2022).csv')
transact_df['Date'] = pd.to_datetime(transact_df['Date']).dt.date
transact_df['Value Dt'] = pd.to_datetime(transact_df['Value Dt']).dt.date

mask = (transact_df['Date'] > initial_date) & (transact_df['Date'] <= final_date)
transformed_df = transact_df.loc[mask]
# poi = st.selectbox("Select The Person of interest", list(transformed_df['Narration'].unique()))
name = st.text_input("Enter the name of the person")
search_df = transformed_df[transformed_df['Narration'].str.contains(name.upper())]
st.write(search_df)
st.subheader("Total Amount taken")
st.write("Total Amount taken : ", format_currency(search_df['Deposit Amt.'].sum(), 'INR', locale='en_IN'))
# st.write(search_df['Withdrawal Amt.'].sum())
# st.write()

