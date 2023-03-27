# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title='MPA Rating - Hollywood-Box Office',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('💼 Employment Rates')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Unemployment_Europe':
        return pd.read_csv('Data/employment_rates/Unemployment_Europe.csv')
    elif query == 'All_employee_Us':
        return pd.read_csv('Data/employment_rates/All_employee_Us.csv')
    return None


Unemployment_Europe = get_data('Unemployment_Europe')
All_employee_Us = get_data('All_employee_Us')

df = Unemployment_Europe
df2 = All_employee_Us


#################################################################################################
st.write(""" ### Employment Rates ##  """)

st.write("""
The ongoing conflict between Russia and Ukraine has had significant impacts on the global economy, including employment rates in Europe and the United States.
The conflict has led to economic sanctions imposed by the West against Russia, which has had negative consequences for trade between Russia and the EU and the US. These sanctions have contributed to a decline in economic growth in Russia and have caused many European countries to suffer from lower export levels and higher energy prices.
Additionally, the crisis has created geopolitical tensions and instability, which have resulted in decreased investor confidence and increased market volatility. This has had a negative impact on the overall global economy, as well as on employment rates in many countries.
In Europe, the economic sanctions against Russia have hit countries that rely heavily on exports, such as Germany, Italy, and France. These countries have seen a decline in their exports to Russia, which has had negative effects on their economies and employment rates.
In the United States, the impact of the Russia-Ukraine conflict on employment rates has been less direct, but still significant. The sanctions have affected the global oil market, leading to lower oil prices, which has had negative effects on the US oil industry and employment rates in that sector.
Furthermore, the instability caused by the conflict has led to increased military spending by many countries, including the US, which has diverted resources away from other sectors and potentially impacted employment rates in those areas.
Overall, the ongoing conflict between Russia and Ukraine has had significant impacts on the global economy and employment rates in many countries, particularly those that rely heavily on trade or the oil industry. The long-term effects of this crisis remain uncertain, but it is clear that it will continue to have wide-ranging economic and geopolitical consequences.
  """)


st.info(""" ##### In This MPA Rating Section you can find: ####

* Employment Rate In the Unite State
* Unemployment In Europe





""")


#################################################################################################

st.write(""" ## Employment Rate In the Unite State
""")

st.write(""" The Russia-Ukraine War has had a significant impact on the global economy, including the employment rate in the United States. The conflict began in 2014, and since then, it has escalated into a full-blown military and diplomatic crisis, affecting many countries around the world.
One way that the Russia-Ukraine War has affected the employment rate in the United States is through the imposition of economic sanctions. In response to Russia's actions in Ukraine, the United States and the European Union imposed a series of economic sanctions on Russia. These sanctions have targeted key sectors of the Russian economy, such as energy, finance, and defense.
As a result of these sanctions, many American companies that do business with Russia have been affected. For example, companies that export goods to Russia have seen a significant decline in sales, which has led to job losses in certain industries. Similarly, companies that rely on Russian imports have also been impacted, leading to a decrease in employment opportunities.
In addition to the impact of economic sanctions, the Russia-Ukraine War has also affected the global energy market. Russia is one of the world's largest producers of oil and natural gas, and the conflict has led to disruptions in the global energy supply chain. This has resulted in higher energy prices, which can have a negative impact on employment in certain industries, such as manufacturing.
Finally, the Russia-Ukraine War has also had a broader impact on the global economy. The conflict has created uncertainty in financial markets, leading to volatility in stock prices and other financial instruments. This can impact

""")
# Employment Rate In the Unite State Before and After War
fig = px.bar(df2, x="DATE", y="PAYEMS", color="Statues",
             title='Employment Created In the Unite State Before and After War [Log Value-Thousand Person]')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_type="log",
                  yaxis_title='Employment')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#####################################################
st.write(""" ## Unemployment In Europe
""")
st.write("""The Russia-Ukraine War has had a significant impact on unemployment in Europe, particularly in countries that have strong economic ties with Ukraine or Russia. The conflict has led to a decline in trade and investment, which has resulted in job losses and increased unemployment in many European countries.
One of the most affected countries is Ukraine itself, where the war has devastated the economy and led to a sharp increase in unemployment. According to the International Labour Organization (ILO), the unemployment rate in Ukraine increased from 7.6% in 2013 to 9.2% in 2015, with more than 1.5 million people losing their jobs.
The war has also had a ripple effect on other European countries, especially those with strong trade and economic ties with Ukraine and Russia. For example, Germany, which is one of Russia's largest trading partners, has been impacted by the economic sanctions imposed on Russia as a result of the war. This has led to job losses in German industries that rely heavily on exports to Russia, such as the automotive and chemical industries.
In addition to Germany, other European countries that have been affected by the Russia-Ukraine conflict include Italy, France, and the United Kingdom. These countries have seen a decline in trade with Russia and Ukraine, which has resulted in job losses and increased unemployment.
Furthermore, the ongoing conflict has also led to a rise in refugees and asylum seekers, which has put a strain on the labor markets of many European countries. According to the European Commission, the influx of refugees has contributed to a rise in unemployment in some countries, such as Greece and Italy.
In conclusion, the Russia-Ukraine War has had a significant impact on unemployment in Europe, with many countries experiencing job losses and increased unemployment due to the decline in trade and investment. The conflict has also contributed to a rise in refugees and asylum seekers, which has put a strain on the labor markets of many European countries.

""")
# Unemployment In Europe Before and After War
fig = px.bar(df, x="Date", y="Unemplyment_European ", color="Statues",
             title='Unemployment In Europe Before and After War')
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_type="log",
                  yaxis_title='Unemployment Rate')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####


* G-rated movies bring in 10% of all box office earnings in Hollywood and are the least successful
* The top 10 films on the overall rank list are all PG-13 movies.
* The most profitable group at the box office is PG-13 films, which brought in 41% of all sales
* While the volume of bridge transactions was significantly influenced  
* R-rated films account for 20% of global box office and have not had a blockbuster in the past three years

""")
