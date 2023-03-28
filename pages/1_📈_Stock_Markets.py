# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title=' Stock Markets - Russia Ukraine Conflict',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('📈 Stock Markets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'SP500D':
        return pd.read_csv('Data/Stock Market/SP500_Daily.csv')
    elif query == 'SP500W':
        return pd.read_csv('Data/Stock Market/SP500_Weekly.csv')
    elif query == 'NASDAQ_D':
        return pd.read_csv('Data/Stock Market/NASDAQ_Daily.csv')
    elif query == 'NASDAQ_W':
        return pd.read_csv('Data/Stock Market/NASDAQ_Weekly.csv')
    elif query == 'Gold_D':
        return pd.read_csv('Data/Stock Market/Gold_Daily.csv')
    elif query == 'Gold_W':
        return pd.read_csv('Data/Stock Market/Gold_Weekly.csv')
    elif query == 'Crude_Oil_D':
        return pd.read_csv('Data/Stock Market/Crude_Oil_Daily.csv')
    elif query == 'Crude_Oil_W':
        return pd.read_csv('Data/Stock Market/Crude_Oil_Weekly.csv')
    elif query == 'USD_Rub_D':
        return pd.read_csv('Data/Stock Market/Ruble-USD_Daily.csv')
    elif query == 'USD_Rub_W':
        return pd.read_csv('Data/Stock Market/Ruble-USD_Weekly.csv')
    elif query == 'EUR_USD_D':
        return pd.read_csv('Data/Stock Market/EUR-USD_Daily.csv')
    elif query == 'EUR_USD_W':
        return pd.read_csv('Data/Stock Market/EUR-USD_Weekly.csv')
    return None


SP500D = get_data('SP500D')
SP500W = get_data('SP500W')
NASDAQ_D = get_data('NASDAQ_D')
NASDAQ_W = get_data('NASDAQ_W')
Gold_D = get_data('Gold_D')
Gold_W = get_data('Gold_W')
Crude_Oil_D = get_data('Crude_Oil_D')
Crude_Oil_W = get_data('Crude_Oil_W')
USD_Rub_D = get_data('USD_Rub_D')
USD_Rub_W = get_data('USD_Rub_W')
EUR_USD_D = get_data('EUR_USD_D')
EUR_USD_W = get_data('EUR_USD_W')


df = SP500D
df2 = SP500W
df3 = NASDAQ_D
df4 = NASDAQ_W
df5 = Gold_D
df6 = Gold_W
df7 = Crude_Oil_D
df8 = Crude_Oil_W
df9 = USD_Rub_D
df10 = USD_Rub_W
df11 = EUR_USD_D
df12 = EUR_USD_W


#################################################################################################
st.write(""" ### Ukraine-Russia War Impact on Stock Market  ##  """)

st.write("""
 The ongoing Ukraine-Russia war has had a significant impact on the global stock market, with a particular focus on the stock market of Ukraine and Russia. The instability caused by the conflict has led to a decrease in investor confidence, resulting in a decline in the stock prices of companies in both countries. The sanctions imposed by Western countries on Russia have also had a significant impact on the Russian stock market, with many investors pulling out of the market due to the uncertainty surrounding the conflict. Additionally, the global oil market has also been affected, as Russia is a major oil producer and any disruption in their supply can lead to increased volatility in the stock market. The ongoing conflict has created a challenging economic environment for both Ukraine and Russia, with the impact being felt across the global stock market. In this section, as we explained in the methodology, we focused on US stock market indexes, gold, and crude oil to represent the global economy and then compared EUR/USD and USD/Rub to better understand the effects because we had limited or outdated data about the Russian stock market after the war.

  """)


st.info(""" ##### In This Stock Market Section you can find: ####

* S&P500 - The Ukraine-Russia indirect Impact on Index
* NASDAQ - The War Will Significantly Affect the NASDAQ in the Long Run
* Gold - A Safe-Haven Asset
* Crude Oil - The Threat of Disruption To Oil Supplies     
* EUR/USD - Hedge Against The Riskier Euro  
* USD/Rub - The Future of Ruble




""")


#################################################################################################


#####################################################
st.write(""" ## The Ukraine-Russia indirect Impact on S&P500 Index """)

st.write("""  The Ukraine-Russia war has had a limited direct impact on the S&P 500, which is a stock market index of 500 large companies listed on US stock exchanges. However, the conflict has created a ripple effect on the global economy, which indirectly affects the S&P 500. The ongoing instability has led to a decrease in investor confidence, resulting in increased volatility in the global stock market, including the S&P 500. The S&P 500 index saw a significant decline after February 24, 2022, as shown in the figure below, but was unable to surpass its 2021 high.   
 Additionally, the sanctions imposed by Western countries on Russia have had a broader impact on the global economy, including the US economy, which affect the performance of the S&P 500. The conflict between Ukraine and Russia may not have had much of a direct impact on the S&P 500, but it did have a significant indirect effect on the US economy, which caused market concern and volatility.

 """)
# S&P500 Daily chart
fig = px.line(df, x="Date", y="Open", color="Statues",
              title='S&P500 Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='S&P500 Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# S&P500 Daily chart
fig = px.bar(df, x="Date", y="Volume", color="Statues",
             title='S&P500 Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='S&P500 Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


################################################################################################################

st.write(""" ## The War Will Significantly Affect the NASDAQ in the Long Run """)
st.write(""" Like S&P500 Index the Ukraine-Russia war has had a limited direct impact on the NASDAQ, which is a stock market index that tracks the performance of technology and growth-oriented companies listed on US stock exchanges. However, the indirect impact of the conflict on the global economy can affect the performance of companies listed on the NASDAQ.    
The ongoing instability has created uncertainty in the global market, and the sanctions imposed on Russia by Western countries ultimately affect the performance of companies listed on the NASDAQ. The magnitude of this effect can be seen in a sharp dip on February 24, 2022 (the day Russia invaded Ukraine's border). This battle had a greater impact on the NASDAQ than the S&P 500, as seen by a mild decline that is currently ongoing.    
Furthermore, the conflict has created potential risks for technology companies that rely on global supply chains. Any disruption to these supply chains can lead to increased costs and decreased profitability, which can negatively impact the performance of these companies on the NASDAQ in the long term. 
""")
# NASDAQ Daily chart
fig = px.line(df3, x="Date", y="Open", color="Statues",
              title='NASDAQ Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='NASDAQ Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NASDAQ Daily chart
fig = px.bar(df3, x="Date", y="Volume", color="Statues",
             title='NASDAQ Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='NASDAQ Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
######################################################

st.write(""" ##  Gold A Safe-Haven Asset """)

st.write(""" The Ukraine-Russia war has had a significant impact on the price of gold, which is often seen as a safe-haven asset during times of geopolitical uncertainty. As tensions escalated between Ukraine and Russia, the demand for gold as a safe-haven asset increased, leading to a rise in its price. On March 22, 2022, it reached the record of 2053, and after declining in 2022, it began to rise once more in 2023, The conflict  have heightened economic uncertainty, which has driven many investors to seek safety in safe-haven assets like gold. As investors look to insure against the potential effects of these sanctions on the global economy, the Western nations' sanctions against Russia have also pushed up the price of gold. Also, the fighting has caused the value of the Russian ruble to drop, forcing Russian investors to turn to gold as a store of wealth. This has further fueled the increase in the cost of gold.
""")
# Gold Daily chart
fig = px.line(df5, x="Date", y="Open", color="Statues",
              title='Gold Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Gold Price [USD]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Gold Daily chart
fig = px.area(df5, x="Date", y="Volume", color="Statues",
              title='Gold Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,  yaxis_type="log",
                  yaxis_title='Gold Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


############################################################
st.write(""" ## Crude Oil And The Threat of Disruption To Oil Supplies """)
st.write(""" Russia is one of the world's largest oil and gas producers and exporters, and the conflict has disrupted the global energy market. The sanctions imposed on Russia have led to a decrease in oil and gas production and exports, causing energy prices to increase. This has had a significant impact, particularly on energy-dependent countries. The ongoing Ukraine-Russia war has had a significant impact on the prices of crude oil. The conflict has caused instability and uncertainty in the region, which has affected the oil market in several ways. The threat of disruption to oil supplies has caused oil prices to increase. Ukraine is an important transit route for Russian gas exports to Europe, and any disruption to this transit could lead to a reduction in gas supplies to Europe. This has caused some investors to become concerned about the potential impact on oil prices, which has resulted in increased demand for crude oil and subsequently higher prices. The figure below shows that the price of crude oil peaked at \$124 in the month following the invasion and then fluctuated within that range for almost four months.  
On the other hand, the conflict has affected the value of the Russian ruble, which is the currency used to sell Russian oil. The ruble has been under pressure since the start of the war, with many investors selling their ruble-denominated assets in favor of safer currencies such as the US dollar. This has caused the ruble to weaken, making Russian oil cheaper for buyers who use other currencies. This might be a reason for the drop in the crude oil price after the hype in the market.     

""")
# Crude Oil Daily chart
fig = px.line(df7, x="Date", y="Open", color="Statues",
              title='Crude Oil Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Crude Oil Price')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Crude Oil Daily chart
fig = px.area(df7, x="Date", y="Volume", color="Statues",
              title='Crude Oil Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Crude Oil Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
###################################################################
st.write(""" ## **EUR/USD** Hedge Against The Riskier Euro    """)
st.write(""" The euro has been under pressure since the start of the war due to its close trade and economic ties with Russia. The European Union (EU) is heavily dependent on Russian gas exports, and any disruption to this supply chain could lead to higher energy prices and slower economic growth. This has caused some investors to become more risk-averse, leading to a decline in demand for the euro and subsequently lower exchange rates against the US dollar. You can observe the significant decline in the value of the euro following the conflict in the following graph.     
The US dollar has benefited from its status as a safe-haven currency during times of geopolitical uncertainty. The US economy is relatively insulated from the Ukraine-Russia conflict, and investors have sought refuge in the US dollar as a hedge against the riskier Euro. This has led to an increase in demand for US dollars and subsequently higher exchange rates against the Euro.
The Ukraine-Russia conflict has raised concerns about the potential for wider geopolitical tensions and instability in the region. This has caused some investors to become more risk-averse and to seek safe-haven assets such as the US dollar. As a result, the Euro has been further weakened with investors selling Euro-denominated assets in favor of safer currencies.
""")
# Euro/USD Daily chart
fig = px.line(df11, x="Date", y="Open", color="Statues",
              title='Euro/USD Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Euro/USD ')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
############################################################################
st.write(""" ##  USD/Rub The Future of Ruble """)
st.write(""" The initial impact of the conflict was a sharp depreciation of the ruble, as investors fled the Russian market amid concerns about the stability of the region. The Russian economy relies heavily on oil exports, and the sanctions imposed by Western countries as a result of the conflict have further weakened the ruble.
The sanctions have also limited Russia's ability to access international markets, which has led to a decrease in foreign investment and increased capital flight. This has put further pressure on the ruble, which has struggled to maintain its value against the US dollar.   
However, the ruble has also shown some resilience in the face of the conflict. The Russian Central Bank has implemented a number of measures to stabilize the currency, including raising interest rates and intervening in the foreign exchange market.    
Overall, the impact of the Russia-Ukraine conflict on the USD/RUB exchange rate has been significant, with both short-term fluctuations and longer-term trends. The ongoing conflict, combined with economic sanctions and geopolitical tensions, make it difficult to predict how the exchange rate will evolve in the future.
""")
# USD/Rub Daily chart
fig = px.line(df9, x="Date", y="Open", color="Statues",
              title='USD/Rub Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='USD/Rub')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####



* The S&P 500 index saw a significant decline after February 24, 2022, but was unable to surpass its 2021 high      
* The ongoing instability has led to a decrease in investor confidence, resulting in increased volatility in the global stock market, including the S&P 500      
* The NASDAQ experienced a sharp dip on February 24, 2022, and this battle had a greater impact on the NASDAQ than the S&P 500      
* Disruption to supply chains can lead to increased costs and decreased profitability, which will negatively impact the performance of companies on the NASDAQ in the long term     
* On March 22, 2022, the gold price reached a record of 2053, and after declining in 2022, it began to rise once more in 2023     
* The ruble weakening, making Russian oil cheaper for buyers who use other currencies, might be a reason for the drop in the crude oil price after the hype in the market       
* The US economy is relatively insulated from the Ukraine-Russia conflict, and investors have sought refuge in the US dollar as a hedge against the riskier Euro  
* The Russian economy relies heavily on oil exports, and the sanctions imposed by Western countries as a result of the conflict have further weakened the ruble  


""")
