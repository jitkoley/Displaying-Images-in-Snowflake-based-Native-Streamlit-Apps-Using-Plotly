# Displaying-Images-in-Snowflake-based-Native-Streamlit-Apps-Using-Plotly
Overview:
In the realm of data applications, one often encounters intriguing challenges. Recently, I found myself grappling with the task of integrating image display functionality into a Streamlit app built on Snowflake, a cloud-based data platform. This journey led me to explore innovative solutions and uncover new possibilities. Here's a glimpse into my adventure.

A Challenge Unveiled:
As I embarked on the development journey, I encountered a hurdle - Snowflake's lack of native support for displaying images using Streamlit's built-in function, st.image(). This limitation sparked my curiosity and ignited a quest for a workaround.

Innovative Solutions:
Amidst the challenge, I stumbled upon a creative workaround using Plotly Express, a versatile visualization library. This approach involved harnessing the power of Plotly to seamlessly incorporate image display functionality into the Streamlit app.

Crafting the Solution:
With determination fueling my efforts, I set out to implement the solution step by step. First, I imported the necessary libraries, including Streamlit, Plotly Express, and skimage for image processing. Then, I meticulously crafted the code to load the image data, create a Plotly figure, and customize it to suit my needs. Finally, I integrated the Plotly figure into the Streamlit interface, thereby overcoming the challenge with finesse.
...................................................................................................
A Glimpse into the Code:

# Importing Libraries
import streamlit as st
import plotly.express as px
from skimage import io

# Loading Image Data
img = io.imread('image.png')

# Creating Plotly Figure
fig = px.imshow(img)

# Customizing Plotly Figure
fig.update_traces(hovertemplate=None, hoverinfo="skip")
fig.update_layout(width=300, height=100, margin=dict(l=10, r=10, b=10, t=10))
fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False)
fig.update_yaxes(showticklabels=False, showgrid=False, zeroline=False)

# Displaying Plotly Figure in Streamlit
st.sidebar.plotly_chart(fig, config={'displayModeBar': False})
...........................................................................................................................
A Triumph of Innovation:
Through perseverance and ingenuity, I successfully navigated the challenge posed by Snowflake's limitations. The integration of Plotly Express into the Streamlit app not only resolved the issue but also opened doors to a myriad of possibilities for enhancing interactivity and visual appeal.


Conclusion:
As I reflect on this journey, I'm reminded of the power of innovation in overcoming obstacles. What began as a challenge evolved into an opportunity for exploration and discovery. By embracing creativity and leveraging the strengths of different libraries, I was able to elevate the functionality of my Streamlit app and embark on new adventures in the world of data applications.

Embark on Your Journey:
As you navigate your own development endeavors, remember to embrace challenges as opportunities for growth. With innovation as your compass and determination as your guide, there's no limit to what you can achieve in the ever-evolving landscape of data applications.


note: read the complete blog on Medium link given below
https://medium.com/@jitkoley7/displaying-images-in-snowflake-based-native-streamlit-apps-using-plotly-bb8efdc091c7



