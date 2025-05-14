import streamlit as st
import pandas as pd

st.write("MVP Predictions 2025")

st.write("Below should be a dataframe")

st.write(pd.DataFrame({
    "column one" : [1, 2, 3, 4],
    "column two" : ['a', 'b', 'c', 'd'] 
}))

st.write("Here is some new text")