import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

st.write("what's up guys")

st.write("Below should be a dataframe")

st.write(pd.DataFrame({
    "column one" : [1, 2, 3, 4],
    "column two" : ['a', 'b', 'c', 'd'] 
}))
