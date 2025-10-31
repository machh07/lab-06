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
print(df.describe()) #This function provides a statistical analysis of the dataset (mean, std, min, max and confidence intervals) 

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
filtered_women_expectancy = df[df["Life expectancy, female"] > 80]
print(filtered_women_expectancy)

for i in filtered_women_expectancy["Country Name"]:
    print(i)
    
#Part 4
#1
sns.relplot(data=df,
            x="Life expectancy, female",
            y="GNI per capita")
sns.relplot(data=df,
            x="Life expectancy, male",
            y="GNI per capita")
#Yes, there is an association between life expectancy and GNI per capita. We can observe that when life expectancy increases, the GNI per capita grows exponentially.
#2
sns.relplot(data=df,
            x="Life expectancy, female",
            y="GNI per capita",
            hue="Region",)  
sns.relplot(data=df,
            x="Life expectancy, male",
            y="GNI per capita",
            hue="Region",)  
#3
sns.relplot(data=df,
            kind="line",
            x="Life expectancy, female",
            y="GNI per capita",
            errorbar="sd",
            hue="Region",)     
sns.relplot(data=df,
            kind="line",
            x="Life expectancy, male",
            y="GNI per capita",
            errorbar="sd",
            hue="Region",)
#4
sns.lmplot(data=df,
           x="Life expectancy, female",
           y="GNI per capita",
           hue="Region",)
sns.lmplot(data=df,
           x="Life expectancy, male",
           y="GNI per capita",
           hue="Region",)
#5
#(1)relationship between life expectancy, female and population corresponding to the regions
sns.relplot(data=df,
            x="Life expectancy, female",
            y="Physicians",
            col= "Region",)
#(2)relationship between tertiary education of males and GNI per capita corresponding to the regions
sns.relplot(data=df,
            x="Tertiary education, male",
            y="GNI per capita",
            col= "Region",)
#africa and Oceana dont have alot of income 
#(3) relationship between women in national parliament and life expectancy of female corresponding to the regions
sns.relplot(data=df,
            x="Women in national parliament",
            y="Life expectancy, female",
            col= "Region",)
#(4)
sns.relplot(data=df,
            x="International tourism",
            y="High Income Economy",
            col= "Region",)


#6
#a
emissions_per_capita = df["Emissions per capita"] = (df["Greenhouse gas emissions"] / df["Population"]).round(2)
sns.lmplot(data=df,
           x="Internet use",
           y="Emissions per capita")
#There is an association between internet use and emissions per capita but it's very weak.

#b
filtered_emissions_per_capita = df[df["Emissions per capita"] > 0.03]
print(filtered_emissions_per_capita)

for i in filtered_emissions_per_capita["Country Name"]:
    print(i)
#Only Brunei Darussalam produces emissions higher than 0.03

#c
sns.relplot(data=df,
            x="Internet use",
            y="Emissions per capita",
            col= "Region",)
#Yes. We can observe higher emissions in the regions of Asia and America (especially) compared to Oceania and Africa which have much lower emissions and internet use.
#d
sns.lmplot(data=df,
           x="High Income Economy",
           y="Greenhouse gas emissions")
#No, not all high income economies have high emissions. 