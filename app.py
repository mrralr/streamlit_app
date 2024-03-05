import streamlit as st
import time as t

st.sidebar.image("TransparentGraphicLogo.png", use_column_width=True)
st.sidebar.title("Stuck On Saturn")

st.sidebar.button("Home", type="primary", use_container_width=True)

# Button Session States

if 'home_btn' not in st.session_state:
  st.session_state.home_btn = True

if 'la_btn' not in st.session_state:
  st.session_state.la_btn = False

def click_homebtn():
  st.session_state.home_btn = True
  st.session_state.la_btn = False

def click_labtn():
  st.session_state.la_btn = True
  st.session_state.home_btn = False

home_btn = st.session_state.home_btn
la_btn = st.session_state.la_btn

# Home Button

if home_btn:
  click_homebtn()

if st.session_state.home_btn:
  st.sidebar.button("Home", type="primary", use_container_width=True)
else:
  st.sidebar.button("Home", type="secondary", use_container_width=True)

# Location Analysis Button

if la_btn:
  click_labtn()

if st.session_state.la_btn:
  st.sidebar.button("Location Analysis", type="primary", use_container_width=True)
else:
  st.sidebar.button("Location Analysis", type="secondary", use_container_width=True)
