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
st.title('🌡️ Inflation')

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
st.write(""" ### Inflation ##  """)

st.write("""
The ongoing conflict between Ukraine and Russia has had significant impacts not only on the region but also on the global economy. One of the key ways this conflict has affected the world economy is through inflation in Europe and the United States.
The conflict has led to a disruption in the supply of natural gas and other energy resources to Europe, which has caused a spike in energy prices. Ukraine is a major transit route for Russian gas exports to Europe, and the conflict has led to disruptions in the flow of natural gas through pipelines. This has forced European countries to look for alternative sources of energy, which has driven up the cost of natural gas and other fuels.
The increase in energy prices has had a ripple effect throughout the European economy, leading to higher prices for goods and services across the board. The European Central Bank has struggled to keep inflation under control, and the conflict has added to the challenges it faces in achieving its inflation target.
In the United States, the impact of the Ukraine-Russia conflict has been less direct, but still significant. The US economy is heavily dependent on global trade, and disruptions in the European economy have had a knock-on effect on US businesses that export to Europe. This has led to higher prices for goods and services in the US as well.
Furthermore, the sanctions imposed on Russia by the US and European Union in response to the conflict have had an impact on global oil prices. Russia is a major oil producer, and the sanctions have reduced its ability to export oil to the global market. This has led to a tighter global oil supply and contributed to higher oil prices, which in turn has contributed to inflation in the US and other countries.
Overall, the ongoing conflict between Ukraine and Russia has had far-reaching impacts on the global economy, including contributing to inflation in Europe and the US. As long as the conflict persists, it is likely that these economic impacts will continue to be felt.     


   

  """)


st.info(""" ##### In This Studio Section you can find: ####

* Consumer Price Index (CPI) Europian Region
* CPI United State
* Sticky Price Consumer Price Index less Food and Energy United State
* Reccession 



""")


#################################################################################################
st.write(""" ## Consumer Price Index (CPI) Europian Region """)

st.write(""" The ongoing conflict between Ukraine and Russia has had a significant impact on the Consumer Price Index (CPI) in the European region. CPI is a measure of the average price level of a basket of goods and services consumed by households, and it is a key indicator of inflation.
The conflict has led to disruptions in the supply of natural gas, which is a major source of energy for many European countries. Ukraine is a key transit country for Russian gas exports to Europe, and the conflict has led to disruptions in the flow of natural gas through pipelines. As a result, European countries have had to look for alternative sources of energy, which has led to higher energy prices and contributed to inflation.
The rise in energy prices has had a ripple effect throughout the European economy, leading to higher prices for goods and services across the board. The CPI has increased as a result, and many European countries have struggled to keep inflation under control.
In addition to the disruption of natural gas supplies, the conflict has also led to trade restrictions and sanctions imposed on Russia by the European Union. These measures have reduced the availability of certain goods in the European market, which has contributed to higher prices.
The impact of the conflict on the CPI has been particularly pronounced in countries that are heavily reliant on Russian energy supplies, such as Hungary, Slovakia, and Bulgaria. These countries have been hit hard by the disruption of natural gas supplies and have experienced higher inflation rates than other European countries.
The European Central Bank (ECB) has been monitoring the impact of the conflict on inflation in the region and has taken steps to mitigate its effects. The ECB has implemented a number of measures, including interest rate cuts and quantitative easing, to support the economy and keep inflation under control.
In conclusion, the ongoing conflict between Ukraine and Russia has had a significant impact on the Consumer Price Index in the European region. The disruption of natural gas supplies and trade restrictions have led to higher energy and commodity prices, contributing to inflation. As the conflict continues, it is likely that these economic impacts will persist, and the ECB will need to continue to take measures to support the economy and keep inflation under control. """)


# Customer Price Index in Europe Before and After War
fig = px.bar(df, x="Date", y="CPI_Europe", color="Statues",
             title='Customer Price Index in Europe Before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='CPI')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#####################################################
st.write(""" ## Consumer Price Index In United Estate """)

st.write("""  "The Ukraine-Russia war has had a significant impact on the global economy, and the United States has not been immune to its effects. One area that has been impacted is the Consumer Price Index (CPI), which measures the average change in prices of goods and services purchased by households in the United States.
The CPI is influenced by a variety of factors, including changes in demand, supply, and production costs. The Ukraine-Russia war has affected the CPI through its impact on global oil and gas prices, as both countries are major producers and exporters of these commodities. The conflict has led to disruptions in supply chains and trade flows, which have increased the cost of oil and gas, and ultimately affected the price of goods and services in the United States.
In addition to energy prices, the Ukraine-Russia war has also impacted the CPI through its impact on global trade. The conflict has led to economic sanctions and trade restrictions between the two countries, which have disrupted global trade flows and led to higher prices for imported goods in the United States. This has been particularly true for goods that are heavily dependent on imports from Russia, such as steel and aluminum.
Overall, the impact of the Ukraine-Russia war on the CPI in the United States has been moderate but significant. While the conflict has not caused a dramatic increase in inflation, it has led to higher prices for certain goods and services, particularly those that are heavily dependent on energy and imported goods. As the conflict continues, it is likely that the impact on the CPI will continue to be felt, although the extent of the impact will depend on the duration and intensity of the conflict. """)

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
The Sticky Price CPI less Food and Energy is considered a more stable measure of underlying inflation because it excludes the prices of goods and services that can be volatile, such as food and energy, which are subject to sudden changes in supply and demand. """)

# Customer Price Index in United Estate Before and After War
fig = px.bar(df3, x="DATE", y="CORESTICKM159SFRBATL", color="Statues",
             title='Customer Price Index in United Estate Before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Sticky CPI')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* In all three ranking lists, "Marvel Comics" came in first, well surpassing the runner-up
* With 53 films released, "Stephen King," which is best renowned for producing horror movies, came in fourth place among all studios in number of release
* With 28 films and an average revenue of $217 million, "Pixar" came in second on the list of highest average box office receipts per release
* "Bad Robot" did well, earning an average of 205 million dollars

""")
