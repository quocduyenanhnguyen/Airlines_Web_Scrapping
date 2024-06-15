import pandas as pd
import wikipedia as wp
html = wp.page("Largest_airlines_in_the_world").html().encode("UTF-8")

try:
    df1_ = pd.read_html(html)[7]
except IndexError:
    df1_ = pd.read_html(html)[0]

try:
    df2 = pd.read_html(html)[8]
except IndexError:
    df2 = pd.read_html(html)[0]

df = pd.DataFrame(df)
#df = df.to_string()
#print(df)

df1 = pd.DataFrame(df1)
#print(df1)

df1_ = pd.DataFrame(df1_)
#print(df1_)

df2 = pd.DataFrame(df2)
#print(df2)


df1_.to_csv("/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Individual_Airlines_Scheduled_passenger_kilometers_flown.csv", index=False)

df2.to_csv("/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Scheduled_freight_tonne_kilometers.csv", index=False)
