import streamlit as st 
view = [100,150,30]
st.write("# My Interest points")
st.write("## raw")
view
st.write("## scatter chart")
st.scatter_chart(view)

import pandas as pd 
sview = pd.Series(view)
sview