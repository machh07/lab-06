#Programming in Science - October 21, 2025
#Presented to : Mr. Tiago Bortoletto Vaz
#Presented by: Neshama Gozlan & Marie-Ange Chhuon

#Import modules
import pandas as pd
import seaborn as sns

#Questions
#1. Do a scatter plot of internet use in different countries
#2. Do a histogram of number of physicians in different countries
#3. Do a scatter plot of female life expectancy in different countries

#Import data
df = pd.read_csv("wdi_wide.csv")
print(df)
print(df.info()) #10 empty values for the column "Physicians" and no empty value for the column "Population"
print(df.nunique())
print(df.describe())

#6
GNI_per_capita = df["GNI per capita"] = (df["GNI"] / df["Population"]).round(2)

#7a
count_r = df["Region"].value_counts()
print(count_r)
#7b
count_HIE = df["High Income Economy"].value_counts()
print(count_HIE)

#8
print(pd.crosstab(df["Region"], df["High Income Economy"]))

#9