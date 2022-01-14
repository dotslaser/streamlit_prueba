import streamlit as st
import pandas as pd

data = {
  'Series':[1,3,4,5,7],
  'Series2':[10,30,40,100,250]
}

df = pd.DataFrame(data)

st.title('App')
st.subheader('Introduction')
st.write('First App')

st.write(df)

st.line_chart(df)