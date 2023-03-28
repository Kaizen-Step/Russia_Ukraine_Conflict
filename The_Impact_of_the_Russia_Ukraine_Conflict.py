# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title=' The Impact of the Russia Ukraine Conflict',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' The Impact of the Russia Ukraine Conflict ')
st.text(" \n")
# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/russia2.webp'))

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/russia4.jpg'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/russia6.webp'))


st.write("""


### Russo-Ukrainian War ###
The Russo-Ukrainian War is an ongoing international conflict between Russia and Russian-backed separatists, against Ukraine, which began in February 2014. Following Ukraine's Revolution of Dignity, Russia annexed Crimea from Ukraine and supported pro-Russian separatists fighting the Ukrainian military in the Donbas war. The first eight years of conflict also included naval incidents, cyberwarfare, and heightened political tensions. In February 2022, Russia launched a full-scale invasion of Ukraine.    
In early 2014, the Euromaidan protests led to the Revolution of Dignity and the ousting of Ukraine's pro-Russian president Viktor Yanukovych. Shortly after, pro-Russian unrest erupted in eastern and southern Ukraine. Simultaneously, unmarked Russian troops moved into Ukraine's Crimea and took over government buildings, strategic sites and infrastructure. Russia soon annexed Crimea after a highly-disputed referendum. In April 2014, armed pro-Russian separatists seized government buildings in Ukraine's eastern Donbas region and proclaimed the Donetsk People's Republic (DPR) and Luhansk People's Republic (LPR) as independent states, starting the Donbas war. The separatists received considerable but covert support from Russia, and Ukrainian attempts to fully retake separatist-held areas failed. Although Russia denied involvement, Russian troops took part in the fighting. In February 2015, Russia and Ukraine signed the Minsk II agreements to end the conflict, but the agreements were never fully implemented in the years that followed. The Donbas war settled into a violent but static conflict between Ukraine and Russian proxies, with many brief ceasefires but no lasting peace and few changes in territorial control.    
Beginning in 2021, Russia built up a large military presence near its border with Ukraine, including within neighbouring Belarus. Russian officials repeatedly denied plans to attack Ukraine. Russian president Vladimir Putin criticized the enlargement of NATO and demanded that Ukraine be barred from ever joining the military alliance. He also expressed irredentist views and questioned Ukraine's right to exist. Russia recognized the DPR and LPR as independent states in February 2022, with Putin announcing a "special military operation" in Ukraine and subsequently invading the region. The invasion was internationally condemned; many countries imposed sanctions against Russia and increased existing sanctions. Russia abandoned an attempt to take Kyiv in early April 2022 amid fierce resistance. From August, Ukrainian forces began recapturing territories in the north-east and south as a result of counter-offensives. In late September, Russia declared the annexation of four partially-occupied regions in southern and eastern Ukraine, which was internationally unrecognized. The war has resulted in a refugee crisis and tens of thousands of deaths.[[1]](https://en.wikipedia.org/wiki/Russo-Ukrainian_War)

### The economic consequences of the war in Ukraine ###
Over the past decade intensifying geopolitical risk has been a constant feature of world politics, yet the world economy and financial markets have shrugged it off. From the contest between China and America to the rise of populist rulers in Latin America and tensions in the Middle East, firms and investors have carried on regardless, judging that the economic consequences will be contained.
Russia’s invasion of Ukraine is likely to break this pattern, because it will result in the isolation of the world’s 11th-largest economy and one of its largest commodity producers. The immediate global implications will be higher inflation, lower growth and some disruption to financial markets as deeper sanctions take hold. The longer-term fallout will be a further debilitation of the system of globalised supply chains and integrated financial markets that has dominated the world economy since the Soviet Union collapsed in 1991. As well as being the dominant supplier of gas to Europe, Russia is one of the world’s largest oil producers and a key supplier of industrial metals such as nickel, aluminium and palladium. Both Russia and Ukraine are major wheat exporters, while Russia and Belarus (a Russian proxy) are big in potash, an input into fertilisers. The prices of these commodities have been rising this year and are now likely to rise further. Amid reports of explosions across Ukraine, the price of Brent oil breached $100 per barrel on the morning of February 24th and European gas prices rose by 30%.[[2]](https://www.economist.com/finance-and-economics/2022/02/26/the-economic-consequences-of-the-war-in-ukraine?utm_medium=cpc.adword.pd&utm_source=google&ppccampaignID=18151738051&ppcadID=&utm_campaign=a.22brand_pmax&utm_content=conversion.direct-response.anonymous&gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY1Q_aVMYVb4go2f7SYCepwuzRgvia6V-sF6YrICMl284wh4OO6nz_waAo6yEALw_wcB&gclsrc=aw.ds)


""")


st.write("""
## Methodology ##  

The Russia-Ukraine war has had several impacts on the global economy. One of the most significant impacts is the disruption of energy supplies. Ukraine is a major transit country for Russian gas exports to Europe, and the conflict has raised concerns about the security and reliability of energy supplies to the region. We attempted to track the impact of the Russian invasion (Ukraine-Russia War), which took place on February 24, 2022, on several facets of the world economy in this dashboard. We were able to compare the the stock market before and after the invasion as well as cryptocurrency, real estate prices, agricultural prices, and inflation. Unfortunately, due to incomplete and outdated information regarding Russia's economy after the war(which might be a policy for war situations), the majority of studies concentrated on European countries as a region near to the war and the United States as a country that was influenced by the war but was not directly participating in it. 
We tooke two-year spans from the year before and the year following the war for the majority of the charts. The time frame was increased in certain instances to five years in order to better comprehend the perspective. Eight different databases were used to create in-depth analyses for each section of this dashboard. Below is a list of the databases and the parts they were used in:


* [Federal Reserve Economic DataBase ](https://www.federalreserve.gov/data.htm) (US Inflation, Employment)
* [Euro Stat Economic DataBase ](https://ec.europa.eu/eurostat/web/main/data/database) (Euro Inflation, Unemployment Rate)
* [U.S. BUREAU OF LABOR STATISTICS ](https://www.bls.gov/data/) (Employment)
* [Yahoo Finance ](https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC) (Stock Market , Cryptocurrencies)
* [International Construction Cost Report ](https://www.arcadis.com/en/knowledge-hub/perspectives/global/international-construction-costs) (Construction Costs)
* [International Cost Engineering Council) ](https://www.icoste.org) (Real Estate)
* [World Bank Open Data ](https://data.worldbank.org/) (Real Estate, Agricultral Price)
* [Euro Stat Ukraine War ](https://ec.europa.eu/eurostat/web/ukraine) (Ukraine Refugee Granted temporary protection)

""")


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://en.wikipedia.org/wiki/Russo-Ukrainian_War      
        2.https://www.economist.com/finance-and-economics/2022/02/26/the-economic-consequences-of-the-war-in-ukraine      

            """)


st.text(" \n")
c1, c2, c3 = st.columns(3)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")


with c2:
    st.info(
        '**Project Github:  [Russia Ukraine Conflict](https://github.com/Kaizen-Step/Russia_Ukraine_Conflict)**', icon="💻")


with c3:
    st.info(
        '**Data Set:  [Federal Reserve Economic DataBase and ....](https://www.federalreserve.gov/data.htm)**', icon="🧠")
