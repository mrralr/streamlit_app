import streamlit as st
import time as t

st.image("TransparentGraphicLogo.png")

st.title("oboboooaoo")

st.header("eesaesesa")

st.subheader("shush")

st.info("yuh")

st.warning("acousitc")

st.error("oopsie daisy")

st.success("Well done")

st.write("abdurahamna hasna")
st.write(range(50))

st.markdown("# hm")
st.markdown("## hmmm")
st.markdown("### hmmmmmm")
st.markdown(":rofl:")

st.text("EEEE")
st.caption("this is a caption")

st.latex(r''' a+b x^2+c''')

st.checkbox('no')

st.button("shuuuuush")

st.radio("Who let him cook", ["Me", "hasan (deffo not)", "rayan", "mr rashid"])

st.selectbox("dropdown", ["yuh", "nah", "immma do my own thing"])

st.multiselect("pick", ["kebab rolls", "chicken tikka", "butter chicken"])

st.select_slider("Rate abd hasan out of 10", ["0.2", "0", "-1", "0.1"])

st.slider("What is your Age?", 0, 100)

st.number_input("Number pls")

st.text_input("email address pls")

st.date_input("let me cook when?")

st.time_input("schedule the meeting")

st.text_area("big paragraph for explanatiosn")

st.file_uploader("upload ur passwords")

st.color_picker("whats your fav color mines blue")

st.progress(90)

with st.spinner("im cooking"):
  t.sleep(5)

st.balloons()

st.sidebar.title("this ismy sidbear")
st.sidebar.text_input("give your mail")
st.sidebar.text_input("passwordpls")
st.sidebar.button("Submit")
st.radio("Status",["Student", "Teacher", "None"])

import pandas as pd
import numpy as np

st.title("charts")
data = pd.DataFrame(np.random.randn(50,2),columns=["money","bishes"])
st.bar_chart(data)
