# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image


# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Aknowledgement - Insight of the Week',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 References')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# SQL Codes
st.write(""" ## Acknowledgement ## """)

st.write("""
We are grateful to all who helped us develop this project specially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And also all Economic Data providers with massive databases and last but not least ****MetricsDao**** that is the reason behind this project.


""")

st.text(" \n")
st.text(" \n")

# Sources
st.write(""" ## Sources ## """)

st.write("""
Here are the reference numbers for all of the sources used in this project:
  


""")

st.write("""  
  1.https://en.wikipedia.org/wiki/Russo-Ukrainian_War        
        2.https://www.economist.com/finance-and-economics/2022/02/26/the-economic-consequences-of-the-war-in-ukraine?              
3. [Federal Reserve Economic DataBase ](https://www.federalreserve.gov/data.htm) (US Inflation, Employment)  
4. [Euro Stat Economic DataBase ](https://ec.europa.eu/eurostat/web/main/data/database) (Euro Inflation, Unemployment Rate)  
5. [U.S. BUREAU OF LABOR STATISTICS (](https://www.bls.gov/data/) (Employment)   
    

""")
