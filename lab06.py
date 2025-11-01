#Programming in Science - October 21, 2025
#Presented to : Mr. Tiago Bortoletto Vaz
#Presented by: Neshama Gozlan & Marie-Ange Chhuon

#Part 3
#Import modules
import pandas as pd
import seaborn as sns

#1 (3 Questions)
# How does internet use vary with population size in different countries?
# Which region contains the most physicians?
# How many countries have a population greater than 10 million?

#2 (Import data)
df = pd.read_csv("wdi_wide.csv")
print(df)

#3
print(df.info()) #There are 10 empty values for the column "Physicians" and no empty value for the column "Population"

#4
print(df.nunique())

#5
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
#There are 66 countries where women can expect to live for more than 80 years.

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
#Yes, association varies by region. Europe shows a steeper curve than Africa, meaning life expectancy affects GNI more strongly there.

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
#We can’t see standard deviation since there’s only one data point per country, so no variability to measure.

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
#(1)relationship between life expectancy and tertiary education of males & females corresponding to different regions
sns.relplot(data=df,
            x="Tertiary education, female",
            y="Life expectancy, female",
            col= "Region",)
sns.relplot(data=df,
            x="Tertiary education, male",
            y="Life expectancy, male",
            col= "Region",)
#In Asia and Oceania, life expectancy increases linearly with tertiary education.
#In Africa, it follows a positive logarithmic curve.
#In Europe and America, the relationship is weak.
#Also, female data is more spread out: greater variability between countries. 

#(2)relationship between tertiary education of males/females and GNI per capita corresponding to the different regions
sns.relplot(data=df,
            x="Tertiary education, male",
            y="GNI per capita",
            col= "Region",)
sns.relplot(data=df,
            x="Tertiary education, female",
            y="GNI per capita",
            col= "Region",)
#Europe and Oceania show income growth with higher education.
#Asia and America show a weaker trend with some outliers.
#Africa shows almost no relationship: low education and low GNI. 

#(3) relationship between women in national parliament and life expectancy of female corresponding to the regions
sns.relplot(data=df,
            x="Women in national parliament",
            y="Life expectancy, female",
            col= "Region",)
#In Europe and America, more women in parliament = higher life expectancy.
#In Asia, there’s more spread, so no clear link.
#In Africa, a small positive trend exists.
#Oceania shows a similar trend, but with few countries.

#(4) Relationship between international tourism and high income economy
sns.relplot(data=df,
            x="International tourism",
            y="High Income Economy",
            col= "Region",)
#More tourism is generally linked to higher income economies.
#Africa lacks countries with high income, so less tourism is seen.

#(5) Relationship between population and greenhouse gas emissions
sns.relplot(data=df,
            x="Population",
            y="Greenhouse gas emissions",
            col= "Region",)
#Most regions show a positive relationship: more population leads to more emissions.
#In Africa, emissions stay low regardless of population (likely due to less industrialization).

#6
#a
emissions_per_capita = df["Emissions per capita"] = (df["Greenhouse gas emissions"] / df["Population"]).round(2)
sns.lmplot(data=df,
           x="Internet use",
           y="Emissions per capita")
#There is an association between internet use and emissions per capita but it's very weak (the points are spread out around the trendline).

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
#Yes, there is variation by region. Asia has the highest emissions per capita. Europe and America are moderate. Africa and Oceania are lowest.

#d
sns.lmplot(data=df,
           x="High Income Economy",
           y="Greenhouse gas emissions")
#No, not all high income economies have high emissions. Some do but many don't.