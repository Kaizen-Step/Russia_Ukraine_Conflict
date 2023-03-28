# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='Inflation - Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔥 Inflation')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'CPI_EU':
        return pd.read_csv('Data/Inflation/CPI_EU.csv')
    elif query == 'CPI_US_Monthly':
        return pd.read_csv('Data/Inflation/CPI_US_Monthly.csv')
    elif query == 'STC_US':
        return pd.read_csv('Data/Inflation/STC_US.csv')
    return None


CPI_US_Monthly = get_data('CPI_US_Monthly')
CPI_EU = get_data('CPI_EU')
STC_US = get_data('STC_US')

df = CPI_EU
df2 = CPI_US_Monthly
df3 = STC_US
#################################################################################################
st.write(""" ### Ukraine-Russia War Impact On Inflation ##  """)

st.write("""
One of the key ways this conflict has affected the world economy is through inflation in Europe and the United States.
The increase in energy prices has had a ripple effect throughout the European economy, leading to higher prices for goods and services across the board. The European Central Bank has struggled to keep inflation under control, and the conflict has added to the challenges it faces in achieving its inflation target.
In the United States, the impact of the Ukraine-Russia conflict has been less direct, but still significant. The US economy is heavily dependent on global trade, and disruptions in the European economy have had a knock-on effect on US businesses that export to Europe. This has led to higher prices for goods and services in the US as well.
Furthermore, the sanctions imposed on Russia by the US and European Union in response to the conflict have had an impact on global oil prices. Russia is a major oil producer, and the sanctions have reduced its ability to export oil to the global market. This has led to a tighter global oil supply and contributed to higher oil prices, which in turn has contributed to inflation in the US and other countries.


   

  """)


st.info(""" ##### In This Inflation Section you can find: ####

* Consumer Price Index (CPI) Europian Region
* CPI United State
* Sticky Price Consumer Price Index less Food and Energy United State



""")


#################################################################################################
st.write(""" ## Consumer Price Index (CPI) Europian Region """)

st.write(""" CPI is a measure of the average price level of a basket of goods and services consumed by households, and it is a key indicator of inflation.
Ukraine is a key transit country for Russian gas exports to Europe, and the conflict has led to disruptions in the flow of natural gas through pipelines. As a result, European countries have had to look for alternative sources of energy, which has led to higher energy prices and contributed to inflation.
The rise in energy prices has had a ripple effect throughout the European economy, leading to higher prices for goods and services across the board. The CPI has increased as a result, and many European countries have struggled to keep inflation under control.    
The conflict has also led to trade restrictions and sanctions imposed on Russia by the European Union. These measures have reduced the availability of certain goods in the European market, which has contributed to higher prices.
The impact of the conflict on the CPI has been particularly pronounced in countries that are heavily reliant on Russian energy supplies, such as Hungary, Slovakia, and Bulgaria. These countries have been hit hard by the disruption of natural gas supplies and have experienced higher inflation rates than other European countries.
The European Central Bank (ECB) has been monitoring the impact of the conflict on inflation in the region and has taken steps to mitigate its effects. The ECB has implemented a number of measures, including interest rate cuts and quantitative easing, to support the economy and keep inflation under control. """)


# Customer Price Index in Europe Before and After War
fig = px.bar(df, x="Date", y="CPI_Europe", color="Statues",
             title='Customer Price Index in Europe Before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='CPI')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#####################################################
st.write(""" ## Consumer Price Index In United Estate """)

st.write("""
The CPI is influenced by a variety of factors, including changes in demand, supply, and production costs. The Ukraine-Russia war has affected the CPI through its impact on global oil and gas prices, as both countries are major producers and exporters of these commodities.
In addition to energy prices, the Ukraine-Russia war has also impacted the CPI through its impact on global trade. The conflict have disrupted global trade flows and led to higher prices for imported goods in the United States. This has been particularly true for goods that are heavily dependent on imports from Russia, such as steel and aluminum.
The impact of the Ukraine-Russia war on the CPI in the United States has been moderate but significant. The monthly CPI index fell to negative figures in July 2022, indicating that the conflict has not significantly increased inflation. However, it has resulted in higher pricing for some goods and services, particularly those that are highly dependent on energy and imported items. The influence on the CPI will probably last as long as the conflict does, albeit how much longer and more intense the conflict lasts will determine how much of an impact it has. """)

# Customer Price Index in United Estate Before and After War
fig = px.bar(df2, x="Date", y="CPI_US", color="Statues",
             title='Customer Price Index in United Estate Before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='CPI')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# ######################################################
st.write(""" ##  Sticky Price Consumer Price Index less Food and Energy United State """)

st.write(""" The Sticky Price Consumer Price Index less Food and Energy is a measure of inflation in the United States that excludes the prices of food and energy and focuses on prices that tend to be more stable or "sticky" over time.
This index is calculated by the Bureau of Labor Statistics (BLS) and is part of the Consumer Price Index (CPI), which is a widely used measure of inflation that tracks the changes in the prices of goods and services that consumers buy.
The Sticky Price CPI less Food and energy are considered a more stable measure of underlying inflation because they exclude the prices of goods and services that can be volatile, such as food and energy, which are subject to sudden changes in supply and demand. As you can see in the data below, the russia-ukraine war had a greater impact on sticky pricing.""")

# Customer Price Index in United Estate Before and After War
fig = px.bar(df3, x="DATE", y="CORESTICKM159SFRBATL", color="Statues",
             title='Customer Price Index in United Estate Before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Sticky CPI')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* CPI is a measure of the average price level of a basket of goods and services consumed by households, and it is a key indicator of inflation  
* The rise in energy prices has had a ripple effect throughout the European economy, leading to higher prices for goods and services across the board  
* The CPI has increased as a result, and many European countries have struggled to keep inflation under control  
* The impact of the conflict on the CPI has been particularly pronounced in countries that are heavily reliant on Russian energy supplies, such as Hungary, Slovakia, and Bulgaria
* The US monthly CPI index fell to negative figures in July 2022, indicating that the conflict has not significantly increased inflation in US  
* The russia-ukraine war had a greater impact on sticky pricing  

""")
