import streamlit as st
import time as t

st.sidebar.image("TransparentGraphicLogo.png", use_column_width=True)
st.sidebar.title("Stuck On Saturn")

# Button Session States

if 'home_btn' not in st.session_state:
  st.session_state.home_btn = True

if 'la_btn' not in st.session_state:
  st.session_state.la_btn = False

def click_homebtn():
  st.session_state.home_btn = True
  st.session_state.la_btn = False
  st.experimental_rerun()

def click_labtn():
  st.session_state.la_btn = True
  st.session_state.home_btn = False
  st.experimental_rerun()

import pandas as pd
import numpy as np

supermarket_data = pd.read_excel(
  io='superstore.xlsm',
  engine='openpyxl',
  sheet_name='Superstore',
  usecols='O:P',
  nrows=1000,
)

# Home Button

photo = "TransparentGraphicLogo.png"

global home_btn
  
if st.session_state.home_btn:
  home_btn = st.sidebar.button("Home", type="primary", use_container_width=True)

  st.header("Home", divider="gray")
  
  tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
  
  data = pd.DataFrame(supermarket_data)

  tab1.subheader("A tab with a chart")
  tab1.line_chart(data)

  tab2.subheader("A tab with the data")
  tab2.write(data)

else:
  home_btn = st.sidebar.button("Home", type="secondary", use_container_width=True)

if home_btn:
  click_homebtn()

# Location Analysis Button

global la_btn

if st.session_state.la_btn:
  la_btn = st.sidebar.button("Location Analysis", type="primary", use_container_width=True)

  st.header("Location Analaysis", divider="gray")

  tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
  
  data = pd.DataFrame(supermarket_data)

  tab1.subheader("A tab with a chart")
  tab1.line_chart(data)

  tab2.subheader("A tab with the data")
  tab2.write(data)
else:
  la_btn = st.sidebar.button("Location Analysis", type="secondary", use_container_width=True)

if la_btn:
  click_labtn()
