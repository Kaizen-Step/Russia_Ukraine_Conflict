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
One of the primary ways in which the conflict has impacted real estate globally is through the geopolitical risks it has introduced. The uncertainty and instability caused by the conflict have led to an increase in geopolitical risk perception, which has affected investment decisions in real estate. Investors are now more cautious and selective in their investments, preferring stable and secure markets over risky ones.
Another way in which the war has impacted the global real estate market is through the impact on commodity prices. The conflict has led to an increase in oil prices, which has a direct impact on real estate markets worldwide. The rise in oil prices has led to an increase in transportation and construction costs, which has affected the cost of building and maintaining real estate properties.
Moreover, the war has also impacted the global economy, leading to economic sanctions, trade restrictions, and a slowdown in economic growth. This has affected the demand for real estate, as businesses are less likely to invest in property during times of economic uncertainty.
Overall, the Russia-Ukraine war has had far-reaching implications on the global real estate market, affecting investment decisions, commodity prices, and economic growth.
    

   

  """)


st.info(""" ##### In This Real Estate Section you can find: ####


* Europian House Price Index
* Imigration Impact on Real Estate Prices
* Higher Construction Costs All Around the World
* U.S. Real Estate Being Used as a Safe-Haven Asset


""")


#################################################################################################
st.write(""" ### Europian House Price Index """)
st.write(""" In the fall, there was a conflict between the number of films released and the overall box office; as we saw in the previous graph, the total box office fell precipitously after the summer, but the number of films released rose by 40%. This comparison demonstrates that more movies, regardless of their quality, do not increase market revenue.
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
Nevertheless, we would like to address the legitimate question of market participants about the impact of this war on the real estate market in Germany and in Berlin. Because in fact there are a number of implications, even if the real estate industry is less affected by this crisis than some other industries.
Millions of people have already fled Ukraine, and many are coming to Germany - including Berlin. These people need housing, and possibly for a long time. This will noticeably exacerbate the housing shortage that already exists in the capital.
The war in Ukraine is also causing further disruption to supply chains. The already existing procurement bottlenecks for certain materials for the construction industry will thus be further exacerbated. On the one hand this is exerting additional upward pressure on construction costs, while on the other construction activity is likely to decline further due to supply chain problems - despite high demand.
The sanctions against Russia are already driving up energy prices, and no reversal of this trend is in sight. As a result, energy costs are further fueling inflation, which is already elevated, and central banks are likely to be forced to take countermeasures. Even if the European Central Bank is likely to act very cautiously with interest rate hikes due to the risks to the economy, the moderate rise in interest rates is likely to continue.
Inflation, rising interest rates and uncertainty are likely to cause a slowdown in price increases on the real estate market - including in Berlin. However, we do not expect a trend reversal in the form of falling prices. Domestic and foreign investors see German and Berlin real estate as a safe haven, especially in the current environment of growing uncertainty. So far, there has been no sign of a slowdown in market activity, unlike at the beginning of the Corona pandemic, when the market went into a state of shock.
Sellers therefore continue to face high demand. Buyers should keep an eye on interest rate developments: With a view to the expectation of rising interest rates, they should consider bringing forward planned acquisitions in order to take advantage of the still favorable borrowing conditions.
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

st.write(""" As mentioned previously, the war in Ukraine has pushed energy prices higher. Construction is an energy-intense industry. This is because it takes an incredible amount of energy to transport all of the supplies to construction sites and build structures. This is not even to mention the energy it takes to obtain lumber from forests or extract metals from the earth and convert them into suitable building materials. It is a safe bet that building new homes and new multifamily properties will get more expensive due to the increased energy prices around the world.
This means that there is a good chance that housing could actually get more expensive even with temporarily reduced competition from Russian buyers. This is because construction companies, real estate developers, and home builders will most likely increase their prices to adjust for rising energy costs. The longer the war goes on, the higher the prices will likely rise.
""")

st.table(df3.head(20))
##############################################################

st.write(""" ## U.S. Real Estate Being Used as a Safe-Haven Asset """)
st.write("""  In times of uncertainty, US-based investors are looking more for hard assets, like real estate. The overall resiliency of multifamily properties throughout difficult economic times has been proven historically and investors’ appetite for lower risk is rising.
In addition to this, many people flock to U.S. real estate as a safe-haven asset. So, even if there is less competition from Russian buyers, it is possible that there could be a buying increase from foreign investors who want extra security. The U.S. is also set to welcome at least 100,000 Ukrainian refugees. All of these refugees will need housing as well.
There are also likely to be many people in Europe who are afraid that the war might spread and who want to have property in the U.S., in case they need somewhere to go to escape danger. So, it is possible that there could be a significant influx of buyers for U.S. real estate as a direct result of the war.
""")


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The highest top-10 grossing day in 2022 was only 99 million, falling short of 2021's record of 128 million
* In 2022, there were seven days with top 10 grossings of more than 50 million
* The amount of films released during the World Cup in Qatar decreased, but the overall box office didn't alter significantly 
* After the summer, overall gross fell sharply, from a peak of 334 million on July 8–14 to a low of 58.7 million on September 9–15
* The quantity of movies released and the overall box office conflicted in the fall

""")
