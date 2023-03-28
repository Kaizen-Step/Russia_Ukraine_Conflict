# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit


# Layout
st.set_page_config(page_title=' Real_Estate -  Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🏛️ Real Estate')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'HousePriceIndex_EU':
        return pd.read_csv('Data/Real_Estate/HousePriceIndex_EU.csv')
    elif query == 'Imigration_Europe':
        return pd.read_csv('Data/Real_Estate/Imigration_Europe.csv')
    elif query == 'Construction_Cost':
        return pd.read_csv('Data/Real_Estate/Construction_Cost.csv')
    return None


HousePriceIndex_EU = get_data('HousePriceIndex_EU')
Imigration_Europe = get_data('Imigration_Europe')
Construction_Cost = get_data('Construction_Cost')

df = HousePriceIndex_EU
df2 = Imigration_Europe
df3 = Construction_Cost
#################################################################################################
st.write(""" ### Russia Ukraine war impact on real estate ##  """)

st.write(""" The impact of the Russia-Ukraine war on real estate is not limited to the affected regions alone. The conflict has had global implications that have affected the real estate market worldwide. This is due to the interconnectedness of the global economy and the ripple effect that the war has had on various industries, including real estate.
One of the primary ways in which the conflict has impacted real estate globally is through the geopolitical risks it has introduced. The uncertainty and instability caused by the conflict have led to an increase in geopolitical risk perception, which has affected investment decisions in real estate.
  """)


st.info(""" ##### In This Real Estate Section you can find: ####


* Europian House Price Index
* Imigration Impact on Real Estate Prices
* Higher Construction Costs All Around the World
* U.S. Real Estate Being Used as a Safe-Haven Asset


""")


#################################################################################################
st.write(""" ### Europian House Price Index """)
st.write("""  Investors are now more cautious and selective in their investments, preferring stable and secure markets over risky ones. Another way in which the war has impacted the European real estate market is through the impact on commodity prices. The conflict has led to an increase in oil prices, which has a direct impact on real estate markets. The rise in oil prices has led to an increase in transportation and construction costs, which has affected the cost of building and maintaining real estate properties. We go into greater depth about this issue in the sections that follow.   
The war has also slowed economic growth. This has affected the demand for real estate, as businesses are less likely to invest in property during times of economic uncertainty. One of the primary ways in which the conflict has affected the housing market is through a decrease in foreign investment. Many international buyers have been hesitant to invest in the European region due to political instability and uncertainty. This has led to a decrease in demand for real estate, which in turn has resulted in a decline in prices. The eurozone house price index decreased from 10.2 in the fourth quarter of 2021 to 7.4 in the third quarter of 2022, as seen in the following chart.
Additionally, the conflict has also led to a decrease in tourism, which has had a significant impact on the housing market in areas that rely heavily on tourism. Many tourists have been hesitant to travel to the region due to safety concerns, which has resulted in a decrease in demand for homes and properties.
Countries such as Poland, Hungary, and Slovakia have all experienced a decline in prices, although the impact has been less pronounced than in Ukraine.
""")
# Europian House Price Index
fig = px.bar(df, x="Date", y="House Price Index_European", color="Statues",
             title='Europian House Price Index ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='House Price Index ')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#####################################################
st.write(""" ### Imigration Impact on Real Estate Prices """)

st.write(""" The war in Ukraine is a tragedy. In view of the suffering that this attack, which cannot be justified by anything, is bringing upon millions of people, all economic questions recede into the background.
Nevertheless, we would like to address the legitimate question of market participants about the impact of this war on the real estate market .
Millions of people have already fled Ukraine. These people need housing, and possibly for a long time. This will noticeably exacerbate the housing shortage that already exists.
The war in Ukraine is also causing further disruption to supply chains. The already existing procurement bottlenecks for certain materials for the construction industry will thus be further exacerbated. On the one hand this is exerting additional upward pressure on construction costs, while on the other construction activity is likely to decline further due to supply chain problems - despite high demand. The number of persons given temporary refuge during a war is examined in the chart below, along with how this rise in demand may affect future real estate values. Poland, with 1.5 million, is the first major destination for Ukrainian refugees.
""")


c1, c2 = st.columns(2)
with c1:
    # Ukrainians granted temporary protection After War In Different Europian Countries
    fig = px.bar(df2.head(15), x="Country", y="Total Imigration", color="Country",
                 title='Ukrainians granted temporary protection After War In Different Europian Countries [Log Value]')
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_type="log",
                      yaxis_title=' granted temporary protection')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.pie(df2, values='Total Imigration', names='Country', hole=0.4,
                 title='Share of Each Destination')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#####################################################################


##############################################################
st.write(""" ## Higher Construction Costs  """)

st.write("""As mentioned previously, the war in Ukraine has pushed energy prices higher. Construction is an energy-intense industry. This is because it takes an incredible amount of energy to transport all of the supplies to construction sites and build structures. This is not even to mention the energy it takes to obtain lumber from forests or extract metals from the earth and convert them into suitable building materials. It is a safe bet that building new homes and new multifamily properties will get more expensive due to the increased energy prices around the world. This means that there is a good chance that housing could actually get more expensive, even with temporarily reduced competition from Russian buyers. This is because construction companies, real estate developers, and home builders will most likely increase their prices to adjust for rising energy costs. The longer the war goes on, the higher the prices will likely rise. The following table displays the rise in construction costs across various nations following the conflict between Ukraine and Russia.
""")

st.table(df3.head(20))
##############################################################

st.write(""" ## U.S. Real Estate Being Used as a Safe-Haven Asset """)
st.write("""  Investors based in the US are more likely to seek out tangible assets during uncertain times, such as real estate. History has demonstrated the general resilience of multifamily properties during challenging economic times, and investors' appetite for lesser risk is growing.
Also, a lot of individuals look to American real estate as a haven asset. Hence, even if Russian purchasers are less competitive, there may be an increase in purchases from international investors seeking added protection. Also, the United States will take in at least 100,000 Ukrainian refugees. These refugees will all require housing.
Also, there are probably a lot of people in Europe who want to own land because they are concerned that the war may expand.
""")


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The war has slowed economic growth which has affected the demand for real estate, as businesses are less likely to invest in property during times of economic uncertainty   
* The eurozone house price index decreased from 10.2 in the fourth quarter of 2021 to 7.4 in the third quarter of 202   
* Millions of people have already fled Ukraine. These people need housing, and possibly for a long time. This will noticeably exacerbate the housing shortage that already exists  
* Poland, with 1.5 million, is the first major destination for Ukrainian refugees   
* The conflict has led to an increase in oil prices, which has led to an increase in transportation and construction costs  
* Housing could actually get more expensive, even with temporarily reduced competition from Russian buyers
* Many people flock to U.S. real estate as a safe-haven asset

""")
