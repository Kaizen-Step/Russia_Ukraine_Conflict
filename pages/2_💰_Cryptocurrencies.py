# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title='Cryptocurrencies -  Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🚀 Cryptocurrencies')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Bitcoin_Daily':
        return pd.read_csv('Data/Crypto/Bitcoin_Daily.csv')
    elif query == 'Bitcoin_Weekly':
        return pd.read_csv('Data/Crypto/Bitcoin_Weekly.csv')
    elif query == 'CMC_Crypto200_Daily':
        return pd.read_csv('Data/Crypto/CMC_Crypto200_Daily.csv')
    elif query == 'CMC_Crypto200_Weekly':
        return pd.read_csv('Data/Crypto/CMC_Crypto200_Weekly.csv')
    elif query == 'Eth_Daily':
        return pd.read_csv('Data/Crypto/Eth_Daily.csv')
    elif query == 'Eth_Weekly':
        return pd.read_csv('Data/Crypto/Eth_Weekly.csv')
    return None


Bitcoin_Daily = get_data('Bitcoin_Daily')
Bitcoin_Weekly = get_data('Bitcoin_Weekly')
CMC_Crypto200_Daily = get_data('CMC_Crypto200_Daily')
CMC_Crypto200_Weekly = get_data('CMC_Crypto200_Weekly')
Eth_Daily = get_data('Eth_Daily')
Eth_Weekly = get_data('Eth_Weekly')


df = Bitcoin_Daily
df2 = Bitcoin_Weekly
df3 = CMC_Crypto200_Daily
df4 = CMC_Crypto200_Weekly
df5 = Eth_Daily
df6 = Eth_Weekly


#################################################################################################
st.write(""" ### Ukraine-Russia War Impact on Cryptocurrencies  ##  """)

st.write("""
 The Ukraine-Russia war has had some impact on the cryptocurrency market, mainly due to the economic sanctions imposed by Western countries on Russia. These sanctions have led to a devaluation of the Russian ruble and increased demand for cryptocurrencies, such as Bitcoin, as a way to store value and bypass traditional banking channels. However, the impact on cryptocurrencies has been relatively limited, and other factors such as regulatory changes and market fluctuations have had a more significant impact on the industry.

  """)


st.info(""" ##### In This Stock Market Section you can find: ####

* Bitcoin
* CMC Crypto 200
* ETH




""")


#################################################################################################


#####################################################
st.write(""" ## Bitcoin """)

st.write("""  The ongoing conflict between Ukraine and Russia has had some impact on the cryptocurrency market, including Bitcoin. One of the main factors is the economic sanctions imposed on Russia by Western countries in response to its involvement in the conflict. These sanctions have led to a devaluation of the Russian ruble and increased demand for alternative stores of value, such as Bitcoin.
Furthermore, the conflict has also created geopolitical uncertainty and instability, which can lead to market volatility and increased demand for safe-haven assets like Bitcoin. However, the impact on Bitcoin has been relatively limited, and other factors such as regulatory changes and market fluctuations have had a more significant impact on the industry.
It's worth noting that Bitcoin's decentralized nature makes it resistant to government censorship and control, which could make it an attractive alternative for those living in conflict zones or under authoritarian regimes. However, the cryptocurrency industry also faces challenges in terms of regulatory compliance and public perception, which could limit its growth in certain regions affected by the conflict.
Overall, while the Ukraine-Russia war has had some impact on Bitcoin and the cryptocurrency market, its effects are relatively minor compared to other factors influencing the industry.

 """)
# Bitcoin Daily chart
fig = px.line(df, x="Date", y="Open", color="Statues",
              title='Bitcoin Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Bitcoin Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bitcoin Daily chart
fig = px.area(df, x="Date", y="Volume", color="Statues",
              title='Bitcoin Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Bitcoin Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##############################################################

st.write(""" ### CMC Crypto 200 """)
st.write(""" TThe Ukraine-Russia war has had a significant impact on many aspects of the global economy, including the world of cryptocurrency. In particular, the ongoing conflict has had a significant impact on the value of CMC crypto200, a cryptocurrency index that tracks the performance of the top 200 cryptocurrencies by market capitalization.
The conflict between Ukraine and Russia has had a destabilizing effect on the global economy, as tensions between the two countries have led to economic sanctions and political turmoil. This instability has had a knock-on effect on the cryptocurrency market, with many investors seeking safe havens in cryptocurrencies like Bitcoin and Ethereum.
As a result, the value of CMC crypto200 has been volatile in recent years, with sharp rises and falls in response to geopolitical events. For example, in early 2022, the index experienced a significant drop in value following a series of high-profile cyberattacks on Ukrainian infrastructure, which were attributed to Russian hackers.
However, despite these fluctuations, CMC crypto200 has continued to be a popular investment option for those seeking exposure to the cryptocurrency market. The index provides a diversified portfolio of the top 200 cryptocurrencies, which can help to mitigate some of the risks associated with investing in individual cryptocurrencies.
Overall, the impact of the Ukraine-Russia war on CMC crypto200 has been complex and multifaceted. While the ongoing conflict has undoubtedly contributed to market instability, it has also highlighted the growing importance of cryptocurrencies as a safe haven asset in times of global turmoil.
""")
# CMC Crypto 200 Daily chart
fig = px.line(df3, x="Date", y="Open", color="Statues",
              title='CMC Crypto 200 Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='CMC Crypto 200 Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


######################################################

st.write(""" ### ETH """)

st.write(""" The ongoing conflict between Ukraine and Russia has had a significant impact on the global economy, and the world of cryptocurrency is no exception. Ethereum, the second-largest cryptocurrency by market capitalization, has been affected by the conflict in several ways.
One of the most significant impacts of the war on Ethereum is the disruption of the crypto mining industry. Ukraine is home to many large mining farms, and these facilities have been targeted by Russian-backed separatists, leading to power outages and damage to mining equipment. This has resulted in a significant reduction in the hashrate of the Ethereum network, making it more difficult for miners to earn rewards.
Furthermore, the conflict has also led to increased scrutiny of the cryptocurrency industry by governments and regulatory bodies. Many countries are concerned about the potential for cryptocurrencies to be used for illicit activities, including money laundering and funding of terrorism. As a result, there has been a push for stricter regulations and greater oversight of the industry.
The war has also had a psychological impact on the cryptocurrency market, with many investors becoming more risk-averse and opting to invest in more traditional assets such as gold and stocks. This has led to a decline in the value of Ethereum and other cryptocurrencies.
Despite the challenges posed by the conflict, there are also some positive developments for Ethereum. Some experts predict that the geopolitical tensions could drive greater adoption of cryptocurrencies in Ukraine, as citizens look for alternative ways to store their wealth and protect themselves from economic instability.
In addition, Ethereum's underlying technology, blockchain, has the potential to be used for humanitarian purposes in conflict zones. For example, blockchain can be used to distribute aid and resources more efficiently, providing transparency and accountability in a region where corruption is rampant.
Overall, the impact of the Ukraine-Russia conflict on Ethereum and the wider cryptocurrency industry is complex and multifaceted. While the conflict has presented significant challenges, it has also highlighted the potential of blockchain technology to drive positive change in the world.
""")
# ETH Daily chart
fig = px.line(df5, x="Date", y="Open", color="Statues",
              title='ETH Daily Chart before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='ETH Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# ETH Daily chart
fig = px.bar(df5, x="Date", y="Volume", color="Statues",
             title='ETH Daily Volume before and After War')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='ETH Volume')
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
