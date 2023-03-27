# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title=' Stock Markets - Hollywood-Box Office',
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
 The ongoing Ukraine-Russia war has had a significant impact on the global stock market, with a particular focus on the stock market of Ukraine and Russia. The instability caused by the conflict has led to a decrease in investor confidence, resulting in a decline in the stock prices of companies in both countries. The sanctions imposed by Western countries on Russia have also had a significant impact on the Russian stock market, with many investors pulling out of the market due to the uncertainty surrounding the conflict. Additionally, the global oil market has also been affected, as Russia is a major oil producer and any disruption in their supply can lead to increased volatility in the stock market. Overall, the ongoing conflict has created a challenging economic environment for both Ukraine and Russia, with the impact being felt across the global stock market.   

  """)


st.info(""" ##### In This Stock Market Section you can find: ####

* S&P500
* NASDAQ
* Gold
* Crude Oil  
* USD/Rub
* EUR/USD



""")


#################################################################################################


#####################################################
st.write(""" ## S&P500 """)

st.write("""  The Ukraine-Russia war has had a limited direct impact on the S&P 500, which is a stock market index of 500 large companies listed on US stock exchanges. However, the conflict has created a ripple effect on the global economy, which indirectly affects the S&P 500. The ongoing instability has led to a decrease in investor confidence, resulting in increased volatility in the global stock market, including the S&P 500. Additionally, the sanctions imposed by Western countries on Russia have had a broader impact on the global economy, including the US economy, which can affect the performance of the S&P 500. Overall, while the direct impact of the Ukraine-Russia war on the S&P 500 may be limited, the indirect impact on the global economy can create uncertainty and volatility in the market.

 """)
# S&P500 Daily chart
fig = px.line(df, x="Date", y="Open", color="Statues",
              title='S&P500 Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='S&P500 Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# S&P500 Daily chart
fig = px.area(df, x="Date", y="Volume", color="Statues",
              title='S&P500 Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='S&P500 Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##############################################################

st.write(""" ### NASDAQ """)
st.write(""" The Ukraine-Russia war has had a limited direct impact on the NASDAQ, which is a stock market index that tracks the performance of technology and growth-oriented companies listed on US stock exchanges. However, the indirect impact of the conflict on the global economy can affect the performance of companies listed on the NASDAQ.
The ongoing instability has created uncertainty in the global market, which can lead to decreased investor confidence and increased volatility in the stock market, including the NASDAQ. Additionally, the sanctions imposed on Russia by Western countries can have an impact on the global economy, which can ultimately affect the performance of companies listed on the NASDAQ.
Furthermore, the conflict has created potential risks for technology companies that rely on global supply chains. Any disruption to these supply chains can lead to increased costs and decreased profitability, which can negatively impact the performance of these companies on the NASDAQ. 
""")
# NASDAQ Daily chart
fig = px.line(df3, x="Date", y="Open", color="Statues",
              title='NASDAQ Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='NASDAQ Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NASDAQ Daily chart
fig = px.area(df3, x="Date", y="Volume", color="Statues",
              title='NASDAQ Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='NASDAQ Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
######################################################

st.write(""" ### Gold """)

st.write(""" The Ukraine-Russia war has had a significant impact on the price of gold, which is often seen as a safe-haven asset during times of geopolitical uncertainty. As tensions escalated between Ukraine and Russia, the demand for gold as a safe-haven asset increased, leading to a rise in its price.
Additionally, the conflict has led to increased economic uncertainty, with many investors seeking refuge in safe-haven assets like gold. The sanctions imposed by Western countries on Russia have also contributed to the rise in gold prices, as investors seek to hedge against the potential impact of these sanctions on the global economy.
Moreover, the conflict has led to a decrease in the value of the Russian ruble, which has caused investors in Russia to seek refuge in gold as a store of value. This has further contributed to the rise in the price of gold.
Overall, the Ukraine-Russia war has had a significant impact on the price of gold, with the ongoing instability and uncertainty driving up demand for the precious metal as a safe-haven asset.
""")
# Gold Daily chart
fig = px.line(df5, x="Date", y="Open", color="Statues",
              title='Gold Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Gold Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Gold Daily chart
fig = px.bar(df5, x="Date", y="Volume", color="Statues",
             title='Gold Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Gold Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


############################################################
st.write(""" ## Crude Oil """)
st.write(""" Energy prices: Russia is one of the world's largest oil and gas producers and exporters, and the conflict has disrupted the global energy market. The sanctions imposed on Russia have led to a decrease in oil and gas production and exports, causing energy prices to increase. This has had a significant impact on the global economy, particularly on energy-dependent countries.  
The ongoing Ukraine-Russia war has had a significant impact on global financial markets, including the prices of crude oil. The conflict has caused instability and uncertainty in the region, which has affected the oil market in several ways.
Firstly, the threat of disruption to oil supplies has caused oil prices to increase. Ukraine is an important transit route for Russian gas exports to Europe, and any disruption to this transit could lead to a reduction in gas supplies to Europe. This has caused some investors to become concerned about the potential impact on oil prices, which has resulted in increased demand for crude oil and subsequently higher prices.
Secondly, the conflict has affected the value of the Russian ruble, which is the currency used to sell Russian oil. The ruble has been under pressure since the start of the war, with many investors selling their ruble-denominated assets in favor of safer currencies such as the US dollar. This has caused the ruble to weaken, making Russian oil cheaper for buyers who use other currencies. This has resulted in an increase in demand for Russian oil, which has also contributed to higher crude oil prices.
Lastly, the Ukraine-Russia war has raised concerns about the potential for wider geopolitical tensions and instability in the region. This has caused some investors to become more risk-averse and to seek safe-haven assets such as gold and oil. As a result, crude oil prices have been supported by the geopolitical tensions, with investors buying oil as a hedge against uncertainty in the region.
In conclusion, the ongoing Ukraine-Russia war has had a significant impact on crude oil prices. The threat of disruption to oil supplies, the weakening of the ruble, and the wider geopolitical tensions in the region have all contributed to higher crude oil prices. As the conflict continues, it is likely that the impact on the oil market will continue to be felt.
""")
# Crude Oil Daily chart
fig = px.line(df7, x="Date", y="Open", color="Statues",
              title='Crude Oil Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Crude Oil Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Crude Oil Daily chart
fig = px.bar(df7, x="Date", y="Volume", color="Statues",
             title='Crude Oil Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Crude Oil Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
###################################################################
st.write(""" ## Euro/USD  """)
st.write(""" The ongoing Ukraine-Russia war has had a significant impact on the Euro/USD exchange rate. The conflict has caused instability and uncertainty in the region, which has affected the value of the Euro and the US dollar in different ways.
Firstly, the Euro has been under pressure since the start of the war due to its close trade and economic ties with Russia. The European Union (EU) is heavily dependent on Russian gas exports, and any disruption to this supply chain could lead to higher energy prices and slower economic growth. This has caused some investors to become more risk-averse, leading to a decline in demand for the Euro and subsequently lower exchange rates against the US dollar.
Secondly, the US dollar has benefited from its status as a safe-haven currency during times of geopolitical uncertainty. The US economy is relatively insulated from the Ukraine-Russia conflict, and investors have sought refuge in the US dollar as a hedge against the riskier Euro. This has led to an increase in demand for US dollars and subsequently higher exchange rates against the Euro.
Lastly, the Ukraine-Russia conflict has raised concerns about the potential for wider geopolitical tensions and instability in the region. This has caused some investors to become more risk-averse and to seek safe-haven assets such as the US dollar. As a result, the Euro has been further weakened by the geopolitical tensions, with investors selling Euro-denominated assets in favor of safer currencies.
In conclusion, the ongoing Ukraine-Russia war has had a significant impact on the Euro/USD exchange rate. The Euro has been under pressure due to its close ties with Russia, while the US dollar has benefited from its status as a safe-haven currency. As the conflict continues, it is likely that the impact on the exchange rate will continue to be felt.
""")
# Euro/USD Daily chart
fig = px.line(df11, x="Date", y="Open", color="Statues",
              title='Euro/USD Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Euro/USD Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* As a result of the COVID-19 pandemic, the Hollywood annual gross dropped from \$11.36 billion in 2019 to \$2.11 billion in 2020
* Annual gross has steadily increased, reaching nearly \$7.36 billion in 2022—a more than 112% increase in a single year.
* Since 2000, the number of movies released has continuously risen, with 2018 seeing a record-breaking 993 movies released in a single year
* The total gross fell by 82% in 2020 while the number of movies released fell by 44%.
* Each movie's average gross revenue rose from \$12 million in 2019 to \$14.84 million in 2022.

""")
