#CODE BY PRINCE PILLE
#COVID'19 DATA VISUALISATION


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


dataset_url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
df = pd.read_csv(dataset_url)

print(df)
df.head()
df.tail()
print(df.shape)

#when it started confirmed case
Df = df[df.Confirmed > 0]
print(Df.head())

#when some of the country we have to find?
Df= Df[Df.Country == "Italy"]
print(Df)


#Global spread of covid19
fig = px.choropleth(Df, locations = "Country", locationmode = "country names", color="Confirmed", animation_frame="Date")
fig.update_layout(title_text = "Global Spread of Covid-19")
fig.show()

#Global deaths of covid19
fig = px.choropleth(Df, locations = "Country", locationmode = "country names", color="Deaths", animation_frame="Date")
fig.update_layout(title_text = "Global Deaths of Covid-19")
fig.show()

#intensive the covid19 Transmission has been in each of the country
Df_India = Df[Df.Country == "India"]
print(Df_India.head())

#just two coloums
Df_India = Df_India[["Date","Confirmed"]]
print(Df_India.head())

#calculating the first derivation of confrimed column
Df_India["Infection Rate"]= Df_India["Confirmed"].diff()
print(Df_India.head())

#In graph to show this rate
fig1=px.line(Df_India, x = "Date", y = ["Confirmed","Infection Rate"])
fig1.show()
#max rate
print(Df_India["Infection Rate"].max())

#cal of different countries
countries= list(Df["Country"].unique())
max_infection_rates = []
for c in countries:
    MIR = Df[Df.Country == c].Confirmed.diff().max()
    max_infection_rates.append(MIR)

print(max_infection_rates)
Df_MIR = pd.DataFrame()
Df_MIR["Country"] = countries
Df_MIR["Max Infection Rate"] = max_infection_rates
print(Df_MIR.head())

#plot barchart
fig= px.bar(df_MIR, x="Country", y="Max Infection Rate", color = "Country", title = "Global maximum infection rate", log_y= True)
fig.show()


###################National Lockdown Impacts covid19 transmission in India################################
#24-03-2020 lockdown started
India_lockdown_start_date = "2020-03-24"
India_lockdown_a_mounth_date = "2020-04-24"
print(df.head())

Df_india = Df[Df.Country== "India"]

#Infection rate
Df_india["Infection Rate"] = Df_india.Confirmed.diff()
print(df_india.head())

#visualisation
fig = px.line(df_india, x="Date", y = "Infection Rate", title= "Before and after lockdown in INDIA")

fig.add_shape(
    dict(
    type="path",
    x0=India_lockdown_start_date,
    y0=0,
    x1=India_lockdown_start_date,
    y1= df_india["Infection Rate"].max(),
    line = dict(color="yellow",width=2) 
    )
)
fig.add_annotation(
    dict(
    x= India_lockdown_start_date,
    y= df_india["Infection Rate"].max(),
    text= "starting date of the lockdown"
    )
)


##################death rate before and after lockdown##################

#dataframe
#print(Df_india.head())

#let's calculate the deaths rate
Df_india["Deaths Rate"]= Df_india.Deaths.diff()
#print(Df_india.head())
Df_india["Infection Rate"] = Df_india.Confirmed.diff()

#show the difference by line graph

#fig = px.line(Df_india, x= "Date" , y= ["Infection Rate","Deaths Rate"])
#fig.show()


#normalize the columns
Df_india["Infection Rate"] = Df_india["Infection Rate"]/Df_india["Infection Rate"].max()
Df_india["Deaths Rate"] = Df_india["Deaths Rate"]/Df_india["Deaths Rate"].max()

fig = px.line(Df_india, x= "Date" , y= ["Infection Rate","Deaths Rate"],title= "death and infected start of lockdown in INDIA")
fig.add_shape(
    dict(
    type="line",
    x0=India_lockdown_start_date,
    y0=0,
    x1=India_lockdown_start_date,
    y1= Df_india["Infection Rate"].max(),
    line = dict(color="red",width=2) 
    )
)
fig.add_annotation(
    dict(
    x= India_lockdown_start_date,
    y= Df_india["Infection Rate"].max(),
    text= "starting date of the lockdown"
    )
)
fig.show()