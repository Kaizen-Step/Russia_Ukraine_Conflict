# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='Agricultural_Prices- Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌾 Agricultural Price Index ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Agri_price_europe':
        return pd.read_csv('Data/Agricultural_Price/Agri_price_europe.csv')
    elif query == 'Agri_price_countires':
        return pd.read_csv('Data/Agricultural_Price/Agri_price_countires.csv')
    elif query == 'Agri_price_top10':
        return pd.read_csv('Data/Agricultural_Price/Agri_price_top10.csv')
    return None


Agri_price_europe = get_data('Agri_price_europe')
Agri_price_countires = get_data('Agri_price_countires')
Agri_price_top10 = get_data('Agri_price_top10')

df = Agri_price_europe
df2 = Agri_price_countires
df3 = Agri_price_top10
#################################################################################################
st.write(""" ### Agricultural Prices Index ##  """)

st.write("""The ongoing conflict between Russia and Ukraine has had a significant impact on the agricultural prices index in Europe. The war has disrupted the supply chain of agricultural products, leading to a decrease in the availability of certain commodities and an increase in their prices.
One of the main reasons for this is that Ukraine is a major exporter of agricultural products, including wheat, corn, and barley. With the conflict in the east of the country, the production and transportation of these goods have been severely affected. As a result, there has been a reduction in the supply of these products to the European market, leading to higher prices.
In addition to the disruption in supply, there is also a political aspect to the conflict that has affected the agricultural prices index in Europe. Following the annexation of Crimea by Russia, the European Union imposed economic sanctions on Russia. In retaliation, Russia banned imports of certain agricultural products from the EU, including fruits, vegetables, dairy, and meat. This has led to an oversupply of these products in the EU market, which has resulted in a drop in prices for these goods.
Overall, the impact of the Russia-Ukraine conflict on the agricultural prices index in Europe has been mixed. While some products have seen a price increase due to reduced supply, others have seen a price decrease due to oversupply. However, the long-term effects of the conflict on the agricultural industry in both countries and the wider European market remain uncertain.


  """)


st.info(""" ##### In This Genre Section you can find: ####

* Agricultural Prices Index in Europian Nations [Quarter] 
* Europian Countries Most effected




""")


#################################################################################################
st.write(""" ## Agricultural Prices Index in Europe [Quarterly]  """)

st.write(""" The Russian invasion of Ukraine has significantly disturbed global agricultural markets in 2022. Russia and Ukraine had been major exporters of grains, wheat, maize, oilseeds (particularly sunflowers) and fertilisers until the war started. Furthermore, the actions to phase out the EU’s dependency on Russian fossil fuels have driven up energy prices. This has all underpinned sharp price rises for key agricultural products and inputs, as new Eurostat data shows.
Between the third quarter of 2021 (Q3 2021) and the third quarter of 2022 (Q3 2022), the average EU price of agricultural products as a whole (output) rose sharply (+30%) for the same ‘basket’ of products. This represented a further acceleration in price rises (+25% between Q2 2021 and Q2 2022). There were particularly strong price increases noted for cereals (+52%), eggs (+49%) and milk (+42%).
Over the same period, the average price of goods and services currently consumed in agriculture (i.e. inputs not related to investment) for the EU as a whole increased by 35% for the same ‘basket’ of inputs, which was a similar rate of increase as between Q2 2021 and Q2 2022 (+36%). Within this basket, there were some considerable price hikes; the average EU price of fertilisers and soil improvers doubled (+101%), with sharp rises also for energy and lubricants (+60%) and for animal feeding stuffs (+35%).
    """)

# gricultural Prices Index in Europe
fig = px.bar(df, x="Date", y="Agricultural Price Index EU", color="Statues",
             title='Agricultural Prices Index in Europe ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Agricultural Prices Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#####################################################
st.write(""" ## Europian Countries Most effected """)

st.write("""  The ongoing conflict between Russia and Ukraine has had far-reaching effects on the global economy, with agricultural prices being particularly impacted. European countries, in particular, have been hit hard by the rise in agricultural price index as a result of this conflict.
One of the main reasons for this is the fact that Russia was a major importer of agricultural products from Europe before the conflict began. In response to Western sanctions imposed on Russia over its annexation of Crimea, Russia imposed its own sanctions on a range of European products, including agricultural goods. This led to a significant drop in demand for European produce in Russia, causing prices to fall.
In addition, the conflict has disrupted trade routes between Europe and Asia, making it more difficult and expensive for European countries to export their agricultural products to markets in Asia. This has led to a glut of produce on the European market, further driving down prices.
Countries such as Poland, which relied heavily on exports to Russia before the conflict, have been particularly hard hit by the drop in demand. Other countries such as Lithuania, Latvia, and Estonia, which are heavily dependent on agriculture for their economies, have also been significantly impacted by the rise in agricultural prices.
The impact of the conflict on agricultural prices has been felt across the continent, with farmers in countries such as France, Germany, and the Netherlands also reporting significant losses. The European Union has responded by introducing a range of measures to support farmers, including financial assistance and aid packages.
Despite these measures, the rise in agricultural prices caused by the Russia-Ukraine conflict is likely to continue to have an impact on European countries for some time to come. As the conflict shows no signs of abating, farmers and policymakers alike will need to continue to find ways to mitigate the effects of this ongoing crisis on the agricultural sector.	 """)

# gricultural Prices Index in Europe
fig = px.bar(df3.head(10), x="Countires", y="Recent Agriculture Index", color="Countires",
             title='Europian Countries Most effected ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Agricultural Prices Index')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.table(df2.head(10))


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* The adoption genre is currently the most profitable of all time, with gross sales of 74 billion dollars
* Foreign language and documentaries were the categories with the most number of releases
* The category deserving of attention is IMAX, with 153 million in average box office receipts per movie
* The average gross per release was insufficient because there weren't many releases in some genres
  

""")
