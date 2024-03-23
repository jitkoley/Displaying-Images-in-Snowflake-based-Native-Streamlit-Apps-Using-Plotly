import streamlit as st
import pandas as pd
import plotly.express as px
from skimage import io



st.title("Displaying Images in Snowflake-based Native Streamlit Apps Using Plotly:snowflake:")
#...................................................
img = io.imread('snowflake_logo_icon_168808.png')
fig = px.imshow(img)
fig.update_traces(hovertemplate = None,hoverinfo = "skip")
fig.update_layout(width=300, height=100, margin=dict(l=10, r=10, b=10, t=10))
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)
fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

st.sidebar.plotly_chart(fig,config={'displayModeBar': False})
#...............................................






