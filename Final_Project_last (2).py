#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 00:55:26 2018

@author: demaggis
"""

#Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.ticker as mtick 
import matplotlib.pyplot as plt

sns.set(style = 'white')

########################################################################################
#                         EXPLORATORY DATA ANALYSIS (EDA)
########################################################################################

# --------------------------------------------------------------------------------------
#                            1. Dataset Examination
# --------------------------------------------------------------------------------------

Telecom = pd.read_csv("~/Desktop/WA_Fn-UseC_-Telco-Customer-Churn.csv")
Telecom.head()


print(str(len(Telecom.columns)) + " columns")
print()
for i in Telecom.columns:
    print(Telecom.loc[:,i].head())

# Looking at attributes' type    
Telecom.info()
Telecom.describe() 

# Let's convert 'Total Charges' to numerical (just as Monthly Charges are):
Telecom['TotalCharges'] = pd.to_numeric(Telecom['TotalCharges'], errors='coerce') 
Telecom['TotalCharges'].head() # converted!
# Let's convert 'Senior Citizen' to object type (being it categorical):
Telecom['SeniorCitizen'].replace(to_replace=1, value='Yes', inplace=True)
Telecom['SeniorCitizen'].replace(to_replace=0, value='No', inplace=True)
Telecom.info()
Telecom.describe()

# after converting 'Total Charges' to numerical, we can see that suddenly entries
# became 7032 (from Telecom.info()), this may be ought to missing values.

# --------------------------------------------------------------------------------------
#                             2. Missing Values
# --------------------------------------------------------------------------------------

Telecom.info() # 11 missing values in 'TotalCharges'

# let's verify it:
Telecom[Telecom['TotalCharges'].isnull()==True]

# since 11 values are not a big issue, we decided to simply drop these rows:
Telecom.drop(Telecom[Telecom['TotalCharges'].isnull()==True].index,axis=0,inplace=True)
Telecom.shape

# check
Telecom[Telecom['TotalCharges'].isnull()==True] # ok
Telecom.info() # ok

# Since the 'CustomerID' column tells us nothing (customer-specific), we decided to drop it:
Telecom = Telecom.iloc[:,1:]
Telecom.head(), Telecom.shape

# Now we can figure out what sample we are analysing:

# number of entries in the dataset
Telecom.shape
# number of unique entries per column
Telecom.nunique()

# Overall, we are analysing a sample of 7032 customers featuring a series of attributes (20 without 
# customerID). Of these, some are numerical (Monthly Charges, Total Charges and tenure), the others are categorical.

# --------------------------------------------------------------------------------------
#           3. Univariate Analysis: Categorical & Numerical variables
# --------------------------------------------------------------------------------------

#                                   Gender Demographics

# Plot
gender = Telecom['gender'].value_counts()*100.0 /len(Telecom)
gender_distribution = gender.plot(kind='bar', stacked = True, rot = 0, color = ['blue','pink'])

# Labels  
gender_distribution.yaxis.set_major_formatter(mtick.PercentFormatter())
gender_distribution.set_ylabel('% Customers')
gender_distribution.set_xlabel('Gender')
gender_distribution.set_ylabel('% Customers')
gender_distribution.set_title('Gender Distribution')
print()
print(gender)
                                                                         
# Comments
# There is an even cut off of 50.5% Male and 49.5% Female

# /////////////////////

#                                   Age Demographics

senior_distribution = (Telecom['SeniorCitizen'].value_counts()*100.0 /len(Telecom))\
                    .plot(kind='pie',autopct='%.1f%%', labels = ['No', 'Yes'], figsize = (7,7)\
                    , colors = ['turquoise','grey'], fontsize = 15)
# Labels 
senior_distribution.set_title('Percent of Seniors')
senior_distribution.legend(labels=['Not Senior','Senior'],loc="best")
senior_distribution.yaxis.set_major_formatter(mtick.PercentFormatter())

# Comments
# The overwhelming majority of the clients are non-senior citizens giving us a younger customer base. 
# 83.8% of our clients are not senior citizens. 

# /////////////////////

#                                Partner Distribution

partner = Telecom['Partner'].value_counts()*100.0 /len(Telecom)
partner_distribution = partner.plot(kind='bar', stacked = True, rot = 0, color = ['blue','pink'])

# Labels  
partner_distribution.set_ylabel('% Customers')
partner_distribution.set_xlabel('Partner')
partner_distribution.set_title('Partner Distribution')
print()
print(partner)

# Comments
# it is a close 51% - 48% split between customers without partners and those with partners. 

# /////////////////////

#                                Dependent Distribution

dependent = Telecom['Dependents'].value_counts()*100.0 /len(Telecom)
dependent_distribution = dependent.plot(kind='bar', stacked = True, rot = 0, color = ['blue','pink'])

# Labels  
dependent_distribution.set_ylabel('% Customers')
dependent_distribution.set_xlabel('Does the customer has dependents?')
dependent_distribution.set_title('Dependents Distribution')
print()
print(dependent)

# Comments
# Those with dependents are much rarer with only 30% of our customer base

# /////////////////////

#                               Contract Specification

Contracts_count = Telecom.Contract.value_counts()

contracts = Contracts_count.plot(kind='bar', stacked = True, rot = 0, width = .5)
contracts.set_xlabel('Contract Type')
contracts.set_ylabel('# of Customers')
contracts.set_title('Contract Distribution')
print()
print(Contracts_count/Telecom.Contract.value_counts().sum())

# Comments
# The majority of the customers work with a month-to-month contract (55% vis à vis 24% for 2Y and 21% for 1Y)

# /////////////////////

##                              Services Provided Info


#  Phone Services

PhoneService = Telecom['PhoneService'].value_counts()*100.0 /len(Telecom)
PhoneserviceDistribution = PhoneService.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])

# Labels  
PhoneserviceDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
PhoneserviceDistribution.set_xlabel('PhoneService')
PhoneserviceDistribution.set_ylabel('% Customers')
PhoneserviceDistribution.set_title('PhoneService')
print()
print(PhoneService)

#  Multiple Lines

MultipleLines = Telecom['MultipleLines'].value_counts()*100.0 /len(Telecom)
MultipleLinesDistribution = MultipleLines.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])

# Labels  
PhoneserviceDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
MultipleLinesDistribution.set_ylabel('% Customers')
MultipleLinesDistribution.set_xlabel('MultipleLines')
MultipleLinesDistribution.set_ylabel('% Customers')
MultipleLinesDistribution.set_title('MultipleLines')
print()
print(MultipleLines)



# Internet Service
    
InternetService = Telecom['InternetService'].value_counts()*100.0 /len(Telecom)
InternetServiceDistribution = InternetService.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])
# Labels  
InternetServiceDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
InternetServiceDistribution.set_ylabel('% Customers')
InternetServiceDistribution.set_xlabel('InternetService')
InternetServiceDistribution.set_title('Internet Service Distribution')
print()
print(InternetService)


# /////////////////////
#                                     Tenure

size = (8, 6)
fig, ax = plt.subplots(figsize=size)

tenure = sns.distplot(Telecom['tenure'], hist=True, kde = False,\
                      color = 'blue',\
                      hist_kws={'edgecolor':'black'}, ax=ax)

tenure.set_ylabel('Number of Customers')
tenure.set_xlabel('Tenure (months)')
tenure.set_title('Customers by their tenure')

first10_per_tenure, last10_per_tenure = Telecom.groupby('tenure').count()['Churn'].sort_values()[-10:
    ], Telecom.groupby('tenure').count()['Churn'].sort_values()[:11]

print(first10_per_tenure, last10_per_tenure)

# Comments
# This graph features a U-shape, representing a customerbase which is widely concentrated in 
# correspondence with one-month (or in general very short-term) contracts or with very large size contract
# (full 72 months or so). 

# /////////////////////

#                             Additional services distribution

#                                OnlineSecurity

OnlineSecurity = Telecom['OnlineSecurity'].value_counts()*100.0 /len(Telecom)
OnlineSecurityDistribution = OnlineSecurity.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])
# Labels  
OnlineSecurityDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
OnlineSecurityDistribution.set_ylabel('% Customers')
OnlineSecurityDistribution.set_xlabel('OnlineSecurity')
OnlineSecurityDistribution.set_title('OnlineSecurityDistribution')
print()
print(OnlineSecurity)

#                                  Online Backup

OnlineBackup = Telecom['OnlineBackup'].value_counts()*100.0 /len(Telecom)
OnlineBackupDistribution = OnlineBackup.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])
# Labels  
OnlineBackupDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
OnlineBackupDistribution.set_ylabel('% Customers')
OnlineBackupDistribution.set_xlabel('OnlineBackup')
OnlineBackupDistribution.set_title('OnlineBackup Distribution')
print()
print(OnlineBackup)

#                               Device Protection

DeviceProtection = Telecom['DeviceProtection'].value_counts()*100.0 /len(Telecom)
DeviceProtectionDistribution = DeviceProtection.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])
# Labels  
DeviceProtectionDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
DeviceProtectionDistribution.set_ylabel('% Customers')
DeviceProtectionDistribution.set_xlabel('DeviceProtection')
DeviceProtectionDistribution.set_title('DeviceProtection Distribution')
print()
print(DeviceProtection)

#                           TechSupport

TechSupport = Telecom['TechSupport'].value_counts()*100.0 /len(Telecom)
TechSupportDistribution = TechSupport.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])
# Labels  
TechSupportDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
TechSupportDistribution.set_ylabel('% Customers')
TechSupportDistribution.set_xlabel('TechSupport')
TechSupportDistribution.set_title('TechSupport Distribution')
print()
print(TechSupport)

#                                  StreamingTV

StreamingTV = Telecom['StreamingTV'].value_counts()*100.0 /len(Telecom)
StreamingTVDistribution = StreamingTV.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])
# Labels  
StreamingTVDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
StreamingTVDistribution.set_ylabel('% Customers')
StreamingTVDistribution.set_xlabel('StreamingTV')
StreamingTVDistribution.set_title('StreamingTV Distribution')
print()
print(StreamingTV)

#                              Streaming Movies

StreamingMovies = Telecom['StreamingMovies'].value_counts()*100.0 /len(Telecom)
StreamingMoviesDistribution = StreamingMovies.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])
# Labels  
StreamingMoviesDistribution.yaxis.set_major_formatter(mtick.PercentFormatter())
StreamingMoviesDistribution.set_ylabel('% Customers')
StreamingMoviesDistribution.set_xlabel('StreamingMovies')
StreamingMoviesDistribution.set_title('StreamingMovies Distribution')
print()
print(StreamingMovies)

# Comment
# the additional services above-analysed are mainly not owned by the customers,
# in particular Online Security and Tech Support. Streaming TV and Streaming Movies,
# on the other hand, feature 50-50 distribution of ownership and non-ownership
# in the analysed sample

# /////////////////////
    
#                               Paperless Billing
    
PaperlessBilling = Telecom['PaperlessBilling'].value_counts()*100.0 /len(Telecom)
Billing_distribution = PaperlessBilling.plot(kind='bar', stacked = True, rot = 0, color = ['blue','green'])

# Labels  
Billing_distribution.yaxis.set_major_formatter(mtick.PercentFormatter())
Billing_distribution.set_ylabel('% Customers')
Billing_distribution.set_xlabel('PaperlessBilling')
Billing_distribution.set_ylabel('% Customers')
Billing_distribution.set_title('PaperlessBilling Distribution')
print()
print(PaperlessBilling)

# Comment
# The variable PaperlessBilling is a Dummy Variable taking value 1 in case billing is done online and 
# 0 otherwise.     
# The majority of respondents has paperless billing (59.27%), while the 40% of respondents
# has paper billing. The magnitude of the difference is therefore significant yet not overwhelming
    
# /////////////////////

#                                       PaymentMethod
    
payment = Telecom['PaymentMethod'].value_counts()*100.0 /len(Telecom)
payment_distribution = payment.plot(kind='bar', stacked = True, rot = 0, color = ['blue','pink', 'green','red'])

# Labels  
payment_distribution.yaxis.set_major_formatter(mtick.PercentFormatter())
payment_distribution.set_ylabel('% Customers')
payment_distribution.set_xlabel('Payment Method')
payment_distribution.set_title('PaymentMethod Distribution')
print()
print(payment)

# Comment
# The variable Payment Method is a categorical variable with four levels: Electronic Check,
# Mail check, Bank Transfer, Credit Card. The 33.63% of respondents makes use of electronic checks, 
# which is the most used payment method.
# The remaining payment methods are evenly used by respondents, as they all show an avereage 
# usage of 21%.
    
# /////////////////////
    
#                                       MonthlyCharges
    
size = (8, 6)
fig, ax = plt.subplots(figsize=size)

MonthlyCharges = sns.distplot(Telecom['MonthlyCharges'], hist=True, kde = False,\
                      color = 'blue',\
                      hist_kws={'edgecolor':'black'}, ax=ax)

MonthlyCharges.set_ylabel('Number of Customers')
MonthlyCharges.set_xlabel('Monthly Charges')
MonthlyCharges.set_title('Monthly Charges Distribution')

# Comment
#the variable monthly charges is a numerical variable showing the amount of charges payed by each 
# customer per month.
# As evidenced in the graph above, a rough 20% of our sample spends approximately 20 euros per month. 
# The remaing part of the sample is mostly concentrated in the range between 70 euroes and 90 euroes 
# paid per month.
    
# /////////////////////

#                                       TotalCharges
    
size = (8, 6)
fig, ax = plt.subplots(figsize=size)

TotalCharges = sns.distplot(Telecom['TotalCharges'], hist=True, kde = False,\
                      color = 'blue',\
                      hist_kws={'edgecolor':'black'}, ax=ax)

TotalCharges.set_ylabel('Number of Customers')
TotalCharges.set_xlabel('Total Charges')
TotalCharges.set_title('Total Charges Distribution') 

# Comment
# The variable total charges is a numerical variable showing the amount of charges paid by to the customer.
# The 65% of respondents pays charges in the range from 0 to 2500. the rest of the sample is decreasingly 
# distributed with 8000 being the minimum of our distribution.
    
# /////////////////////

#                                        Churn Ratio

Churn = Telecom.Churn.value_counts().plot(kind='pie',autopct='%.1f%%', labels = ['No', 'Yes'], figsize = (7,7)\
                    , colors = ['lightblue','lightgrey'], fontsize = 15)

Churn.set_title('Churn Rate')
Churn.legend(labels=['No Churn','Churn'],loc="best")
Churn.yaxis.set_major_formatter(mtick.PercentFormatter())

Telecom.Churn.value_counts()

# Comments
# 26.6 % of customers are churning out of our services.

# --------------------------------------------------------------------------------------
#           4. Bivariate Analysis: Categorical & Numerical variables
# --------------------------------------------------------------------------------------

#                                   Churn - gender
    
gender = Telecom.groupby(['Churn','gender']).size().unstack()

table = (gender.T*100.0 / gender.T.sum()).T.plot(kind='bar',width = 0.5,
         stacked = True, rot = 0,figsize = (10,8),color = ['pink','brown'])
table.yaxis.set_major_formatter(mtick.PercentFormatter())
table.set_ylabel('Percent Customers')
table.set_title('Churn by Gender')
table.legend(loc='center',prop={'size':12},title = 'Gender')

# Comments
# Female and Male customers equally distributed among those who churn and those who don't.

# /////////////////////   
    
#                                   Churn - Senior Citizen

senior = Telecom.groupby(['Churn','SeniorCitizen']).size().unstack()

table = (senior.T*100.0 / senior.T.sum()).T.plot(kind='bar',width = 0.5,
         stacked = True, rot = 0,figsize = (10,8),color = ['turquoise','grey'])
table.yaxis.set_major_formatter(mtick.PercentFormatter())
table.set_ylabel('Percent Customers')
table.set_title('Churn by Seniority')
table.legend(loc='center',prop={'size':12},title = 'Senior Citizen')


# Comments
# In correspondence with the pie chart above, the majority of the clients are non senior citizens.
# The distribution of churn based on age does not reveal much. Senior citizens are marginally
# more likely to churn than non-senior citizens. 

# /////////////////////

#                                   Churn - Partner

values = Telecom.groupby('Churn')['Partner'].value_counts()

values_noChurn = values.values[:2]
values_yesChurn = values.values[2:]

names = 'No Partner', 'Yes Partner'
my_circle=plt.Circle( (0,0), 0.7, color='white')
# color names
plt.pie(values_yesChurn, labels=values_yesChurn.round(2), colors=['red','brown'])
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(names)
plt.title('Yes Churn')
plt.show()

names2 = 'Yes Partner', 'No Partner'
my_circle=plt.Circle( (0,0), 0.7, color='white')
# color names
plt.pie(values_noChurn, labels=values_noChurn.round(2), colors=['red','brown'])
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(names2)
plt.title('No Churn')
plt.show()

# Comments
# among those who churn, the great majority is made up of customers without a partner.
# We grouped by 'Churn' since the amount of those with and without partners is comparable.

# /////////////////////

#                                   Churn - Dependents

values = Telecom.groupby('Dependents')['Churn'].value_counts()

values_yesDep = values.values[2:]
values_noDep = values.values[:2]

names = 'No Churn', 'Yes Churn'
my_circle=plt.Circle( (0,0), 0.7, color='white')
# color names
plt.pie(values_yesDep, labels=values_yesDep.round(2), colors=['green','grey'])
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(names)
plt.title('Yes Dependents')
plt.show()

names2 = 'No Churn', 'Yes Churn'
my_circle=plt.Circle( (0,0), 0.7, color='white')
# color names
plt.pie(values_noDep, labels=values_noDep.round(2), colors=['green','grey'])
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(names2)
plt.title('No Dependents')
plt.show()

# Comments
# customers with and without dependents are likely not to churn. But those with dependents
# are more likely to churn.

# /////////////////////
    
#                                   Churn - tenure 

size = (4, 8)
fig, ax = plt.subplots(figsize=size)

sns.boxplot(x = Telecom.Churn, y = Telecom.tenure, ax=ax)

# Comments
# Customers that don't churn are the ones with higher value of tenure, they are more fidelize.
# Although we can see that between customers that churn there are some outliers in the upper
# part of the distribution.

# /////////////////////

#                                   Churn - PhoneService 

PhoneService = Telecom.groupby(['Churn','PhoneService']).size().unstack()

table = (PhoneService.T*100.0 / PhoneService.T.sum()).T.plot(kind='bar',width = 0.5,
         stacked = True, rot = 0,figsize = (10,8),color = ['pink','brown'])
table.yaxis.set_major_formatter(mtick.PercentFormatter())
table.set_ylabel('Percent Customers')
table.set_title('Churn by PhoneService')
table.legend(loc='center',prop={'size':12},title = 'PhoneService')
print()
print( 'Yes Phone Service: No Churn is ',str(PhoneService.values[0,1]/PhoneService.values[1,1]), ' times the Yes Churn')
print( 'No Phone Service: No Churn is ',str((PhoneService.values[0,0]/PhoneService.values[1,0]).round(1)), ' times the Yes Churn')

# Comments
# Both the customers with and without Phone Service, tend not to churn (no_Churn/yes_Churn ratio 
# is 3 for both the customers' types.

# /////////////////////

#                                   Churn - MultipleLines 

MultipleLines = Telecom.groupby(['Churn','MultipleLines']).size().unstack()

table = (MultipleLines.T*100.0 / MultipleLines.T.sum()).T.plot(kind='bar',width = 0.5,
         stacked = True, rot = 0,figsize = (10,8),color = ['pink','red','brown'])
table.yaxis.set_major_formatter(mtick.PercentFormatter())
table.set_ylabel('Percent Customers')
table.set_title('Churn by MultipleLines')
table.legend(loc='center',prop={'size':12},title = 'MultipleLines')
print()
print( 'Yes MultipleLines: No Churn is ',str((MultipleLines.values[0,2]/MultipleLines.values[1,2]).round(1)), ' times the Yes Churn')
print( 'No MultipleLines: No Churn is ',str((MultipleLines.values[0,0]/MultipleLines.values[1,0]).round(1)), ' times the Yes Churn')
print( 'No phone service: No Churn is ',str((MultipleLines.values[0,1]/MultipleLines.values[1,1]).round(1)), ' times the Yes Churn')

# Comments
# The customers with and without MultipleLines, tend not to churn (no_Churn/yes_Churn ratio 
# is close to 3 for both the customers' types. Info on 'No phone service' is redundant.

# /////////////////////

#                                   Churn - InternetService 

InternetService = Telecom.groupby(['Churn','InternetService']).size().unstack()

table = (InternetService.T*100.0 / InternetService.T.sum()).T.plot(kind='bar',width = 0.5,
         stacked = True, rot = 0,figsize = (10,8),color = ['black','grey','brown'])
table.yaxis.set_major_formatter(mtick.PercentFormatter())
table.set_ylabel('Percent Customers')
table.set_title('Churn by InternetService')
table.legend(loc='center',prop={'size':12},title = 'InternetService')
print()
print(InternetService)

# Comments
# Customers with DSL tend not to churn just like those with no Internet service
# vis à vis customers with Fiber optic, who are more likely to churn

# /////////////////////

#                              Churn - Additional Services

cols = ["OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"]
df = Telecom[(Telecom.InternetService != "No")& (Telecom.Churn == "Yes")]
df = pd.melt(df[cols]).rename({'value': 'Has service'}, axis=1)
plt.figure(figsize=(15, 4.5))
ax = sns.countplot(data=df, x='variable', color = 'blue', hue='Has service')

ax.set_xlabel('Additional services')
ax.set_ylabel('Customers With Churn')
plt.show()

# Comments
# Generally, those that refrain from additional services like Online Security, Online Backup and Device Protection
# are those that churn most.

# /////////////////////

#                                Churn - Contract Type

contract = Telecom.groupby('Churn')['Contract'].value_counts()

table = (contract.T*100.0 / contract.T.sum()).T.plot(kind='bar',width = 0.5,\
                                                     stacked = True,\
                                                     rot = 0,\
                                                     figsize = (10,8))
         

table.yaxis.set_major_formatter(mtick.PercentFormatter())
table.set_ylabel('Percent Customers')
table.set_title('Churn by Contract Type')

print(contract.T*100.0 / contract.T.sum())

# Comments
# Those that do churn are almost always in month-to-month contracts.

# /////////////////////

#                                Churn - Paperless Billing

values = Telecom.groupby('PaperlessBilling')['Churn'].value_counts()

values_yesPaperless = values.values[2:]
values_noPaperless = values.values[:2]

names = 'No Churn', 'Yes Churn'
my_circle=plt.Circle( (0,0), 0.7, color='white')
# color names
plt.pie(values_yesPaperless, labels=values_yesPaperless.round(2), colors=['black','orange'])
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(names)
plt.title('Yes PaperlessBilling')
plt.show()

names2 = 'No Churn', 'Yes Churn'
my_circle=plt.Circle( (0,0), 0.7, color='white')
# color names
plt.pie(values_noPaperless, labels=values_noPaperless.round(2), colors=['black','orange'])
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.legend(names2)
plt.title('No PaperlessBilling')
plt.show()

# Comments
# both customers with and without paperless billing are likely not to churn, but those
# without paperless billing are more likely not to churn.

# /////////////////////

#                                Churn - Payment Method

PaymentMethod = Telecom.groupby(['Churn','PaymentMethod']).size().unstack()

table = (PaymentMethod.T*100.0 / PaymentMethod.T.sum()).T.plot(kind='bar',width = 0.5,
         stacked = True, rot = 0,figsize = (10,8),color = ['black','grey','pink','purple'])
table.yaxis.set_major_formatter(mtick.PercentFormatter())
table.set_ylabel('Percent Customers')
table.set_title('Churn by PaymentMethod')
table.legend(loc='center',prop={'size':12},title = 'PaymentMethod')
print()
for i in PaymentMethod.columns:
    print(PaymentMethod[i])

# Comments
# All customers are more likely not to churn, than to churn, but less for Customers 
# with Electronich check, which are the ones we expect more to churn when compared to 
# other customers (those whose payment method is bank transfer, credit card or mailed check).

# /////////////////////

#                                Churn - Monthly Charges

size = (4, 8)
fig, ax = plt.subplots(figsize=size)

sns.boxplot(x = Telecom.Churn, y = Telecom.MonthlyCharges, ax=ax)


# Comments
# Those who churn tend to have higher value of Monthly Charges, both
# in mean and overall distribution, than the ones who remain with the company. 

# /////////////////////

#                                Churn - Total Charges

size = (4, 8)
fig, ax = plt.subplots(figsize=size)

sns.boxplot(x = Telecom.Churn, y = Telecom.TotalCharges, ax=ax)


# Comments
# The no-churn customers have a higher total expense than the yes-churn customers.
# However, we need to consider the high number of outliers on the upper part of the distribution. 

# /////////////////////

##                            Tenure per type of Contract

fig, (MtM, One, Two) = plt.subplots(nrows=1, ncols=3, sharey = True, figsize = (20,4))

MtM = sns.distplot(Telecom[Telecom['Contract']=='Month-to-month']['tenure'],hist=True, kde = False,\
                      color = 'blue',\
                      hist_kws={'edgecolor':'black'},
                  ax=MtM)

MtM.set_ylabel('Number of Customers')
MtM.set_xlabel('Tenure (months)')
MtM.set_title('Tenure for Month to Month Customers')

One = sns.distplot(Telecom[Telecom['Contract']=='One year']['tenure'],hist=True, kde = False,\
                      color = 'red',\
                      hist_kws={'edgecolor':'black'},
                  ax=One)

One.set_ylabel('Number of Customers')
One.set_xlabel('Tenure (months)')
One.set_title('Tenure for One Year Customers')

Two = sns.distplot(Telecom[Telecom['Contract']=='Two year']['tenure'],hist=True, kde = False,\
                      color = 'green',\
                      hist_kws={'edgecolor':'black'},
                  ax=Two)

Two.set_ylabel('Number of Customers')
Two.set_xlabel('Tenure (months)')
Two.set_title('Tenure for Two Year Customers')

# Comments
# those with longer contracts stay with the company for longer time. Those in the month-to-month contracts 
# generally stop using the services after the first couple months

# --------------------------------------------------------------------------------------
#                            5. Outliers Detection
# --------------------------------------------------------------------------------------

#boxplot MonthlyCharges 
size = (5, 2)
fig, ax = plt.subplots(figsize=size)
sns.boxplot(Telecom["MonthlyCharges"], ax=ax)

#boxplot Total Charges
size = (5, 2)
fig, ax = plt.subplots(figsize=size)
sns.boxplot(Telecom["TotalCharges"], ax=ax)

#boxplot Tenure
size = (5, 2)
fig, ax = plt.subplots(figsize=size)
sns.boxplot(Telecom['tenure'], ax=ax)

# Comment

# Outliers are oberservations having values which are "extreme" if compared to the remaining observations.
# Outliers are usually not considered in statistical analysis since they may be a source of bias.
# One of the most useful tools for identifying outliers in numerical data is the Box_Whisker plot. Starting 
# from the left, the first line represnets the minimum, the left-hand side of the mox is the first quartile Q1, 
# the line in the middle of the box is the mean, the right-hand side is the third quartile Q3 and the last vertical
# line represents the maximum.
# Outliers can be detected as those x which :  x< Q1 -[(Q3-Q1) *1.5] or x> Q3 +[(Q3-Q1)]*1.5
# The distribution of Monthly Charges is almost even, and we cannot detect outliers, The same
# considerations apply to Tenure.
# Also for Total Charges, we did not spot outliers using the interquantile range methodology.

# --------------------------------------------------------------------------------------
#                                6. Correlation 
# --------------------------------------------------------------------------------------

# we first split our data into numerical and categorical variables
categorical = Telecom.drop(['tenure', 'MonthlyCharges', 'TotalCharges'], axis=1)
numerical = Telecom[['tenure', 'MonthlyCharges', 'TotalCharges']]
categorical.info()
numerical.info()

# /////////////////////

# Numerical variables

# we use a pairplot to look at correlation among numerical variables besides printing the 
# correlation values
import seaborn as sns
sns.pairplot(numerical) # pairplot
print(numerical.corr()) # correlation

# on the diagonal we can look at the distribution of each numerical variable (histogram)
# while the scatter plots on the upper and lower triangles represent the 
# correlation between pairs of variables.

# The pairplot featuring only the numerical variables regressed against
# each other and looking at their numerical correlation values, we can spot a very high
# correlation value between the variables 'tenure' and 'TotalCharges' (0.83), 
# also represented by a well-defined diagonal shadowed area in the plot: with the increase
# of 'TotalCharges', 'tenure' increases, too.

# /////////////////////

# Categorical Variables

# We used Cramér's V as a measure of association for the categorical variables

import scipy.stats as stats

l = categorical.columns 
cramers_v_result = []
pair = []
pairs = []

def cramers_v(confusion_matrix):
    chi2 = stats.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))

# applying the function to each pair of categorical variables 
for i in range(len(l)-1):
    for j in range(1,len(l)-i):
        cramers_v_result.append(cramers_v(
                pd.crosstab(categorical[categorical.columns[i]
        ], categorical[categorical.columns[i+j]]).as_matrix()))
        pairs.append([categorical.columns[i],categorical.columns[i+j]])
        pair.append(str(pairs[i][0]+' - '+pairs[i][1]))

# representing it into a dataframe
Cramer_V = pd.DataFrame({'Cramer V': cramers_v_result}, index = pair)
Cramer_V.head()

# selecting only the pairs featuring a value > 0.5
Cramer_V[Cramer_V['Cramer V'] > 0.5] # this suggests we may exclude 'gender' from our regression 
#                                      not to have issues of multicollinearity  

# Comment
# We used Cramér's V as a measure of association of our categorical variables. We, hence, 
# built a function computing Cramér's V coefficient for each pair of categorical variables
# and we focused our attention on the sole pairs of variables featuring a measure > 0.5 
# (since closer to complete association, represented by a value of 1). As it appears, these
# are all pairs including the variable ‘gender’. 

# /////////////////////

# Also, we experimented a series of pairplots to spot common patterns in both numerical and
# categorical variables.

# let's colour the plot to account for the categorical variables.
for i in range(len(categorical.columns)):
    sns.pairplot(Telecom, hue = categorical.columns[i], diag_kind = 'kde',
             plot_kws = {'alpha': 0.9, 's': 40, 'edgecolor': 'k'},
             size = 2)


# We plotted the pairplot with numerical variables as many times as the number of categorical
# variables and we coloured it to highlight how each categorical attribute is distributed
# within the sample.

# Here are our considerations:
# 1. the 'gender' looks randomly distributed within the sample, since no gender-specific
#    pattern characterizes the numerical variables distribution.
# 2. the 'SeniorCitizen' attributes, instead, features a different distribution of 'MonthlyCharges'
#    and 'TotalCharges' depending on being or not senior: the senior have a less right-skewed
#    distribution for 'TotalCharges', and they have a left-skewed distribution for 'MonthlyCharges'
# 3. With respect to the attribute 'partner', it is spottable a partner-specific distribution
#    when looking at the variables 'tenure' and 'TotalCharges' (those with no partners have a 
#    right-skewed distribution for both of the attributes vs the ones who do have a partner
#    have a 'tenure' distribution almost specular to the former one, and it's less right-skewed
#    with respect to the attribute 'TotalCharges')
# 4. Customers with and with no 'dependents' do not seem to have a specific distribution
#    depending on their categorization, apart from their distribution when looking at the 
#    variable 'tenure', where those with no dependent are mainly concentrated in the part with 
#    lower tenure
# 5. The customers having 'PhoneService' seem to pay very low or very high 'MonthlyCharges',
#    while those who do not have it seem to pay a level of 'Monthly Charges' close to 
#    $50.
# 6. With regards to the 'MultipleLines' attribute, leaving apart the 'No phone service' 
#    sub-category which reflects what we have just said at point 5., we can notice almost
#    specular distributions of those with and with no MultipleLines when looking at the 'tenure'
#    chart (those who do have them feature higher levels of tenure); the ones with MultipleLines
#    also seem to have higher levels of Monthly charges compared with the ones with no MultipleLines
#    but that are also present in the right-side of the chart; the onses with no MultipleLines
#    also feature a more right-skewed curve with respect to the variable 'TotalCharges'.
# 7. When looking at the 'InternetService' cateogirzation, it is possible to spot higher levels
#    of both 'TotalCharges' and 'MonthlyCharges' for those who have the 'Fiber optic'.
# 8. Those who have 'OnlineSecurity' feature higher levels of 'TotalCharges'. What is more, those
#    with Online Security feature higher levels of tenure (curves almost specular in the 
#    'tenure' plot of 'Yes' and 'No' Online Service)
# 9. The same reasoning of point 8. is valid also for the variable 'OnlineBackup'
# 10. The same reasoning of point 8. is valid also for the variable 'DeviceProtection'
# 11. The same reasoning of point 8. is valid also for the variable 'TechSupport'
# 12. The same reasoning of point 8. is valid also for the variable 'StreamingTV'
# 13. The same reasoning of point 8. is valid also for the variable 'StreamingMovies'
# 14. With respect to the variable 'Contract', we can notice a higher concentration of customers
#     with 'month-to-month' contracts in correspondence with lower levels of tenure vis à vis the 
#     ones with 'Two year' contracts who are mainly concentrated in correspondence of higher level
#    of tenure, and the one with 'one year' contracts who present different levels of tenure, not too
#    high nor too low. While those with 'month-to-month' contracts are more likely to pay lower
#    'TotalCharges', they end up paying higher 'MonthlyCharges' when compared to the ones with
#    'Two year' contracts
# 15. Those with 'PaperlessBilling' tend to pay higher 'MontlyCharges' than the ones without it
# 16. With respect to 'PaymentMethod', we can see that customers paying with 'Credit Card' and 
#     'Bank Transfer' (noth automatic payments) have the same feature the same patterns when
#     considering all the three numerical variables distribution. The same can be said for 
#     customers paying with 'Electronic check' and 'Mailed check' in correspondence with the 'tenure'
#     distribution. On the other hand, with respect to the 'MonthlyCharges' distribution, those paying 
#     with Electronic check have a left-skewed distribution vis à vis the ones paying with Mailed check;
#     and the former also feature a more right-skewed 'TotalCharges' distribution
# 17. As for the 'Churn' attribute (our main variable of interest), those who churn present
#     lower levels of 'tenure', lower levels of 'TotalCharges' (more righ-skewed curve) but higher 
#     levels of 'MonthlyCharges'


########################################################################################
#                              MODELING THE CHURN BEHAVIOUR
########################################################################################

# --------------------------------------------------------------------------------------
#                                1. Logistic regression 
# --------------------------------------------------------------------------------------

#                                  Adjusting the data

Telecom.columns

for i in range(Telecom.shape[1]):
    print(pd.Series(Telecom.values[:,i]).unique())

# We decided to substitute the values 'No phone service' and 'No internet service' with 'No'
# in order not to have redundant information:
Telecom.replace(['No phone service','No internet service'], 'No', regex=True,inplace=True)

# checking it worked
for i in range(Telecom.shape[1]):
    print(pd.Series(Telecom.values[:,i]).unique())

# converting from categorical to numerical
Telecom['gender'].replace(to_replace='Male', value=1, inplace=True)
Telecom['gender'].replace(to_replace='Female', value=0, inplace=True)

# Let's also convert 'True'/'False' cells into 1s and 0s:
Telecom.info() 

# to be converted
Yes_No = ['Partner','SeniorCitizen','Dependents','PhoneService','MultipleLines','OnlineSecurity','OnlineBackup',
          'DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling','Churn']
for i in Yes_No:
    Telecom[i].replace(to_replace='Yes', value=1, inplace=True)
    Telecom[i].replace(to_replace='No', value=0, inplace=True)

Telecom.info(), Telecom.head()

# /////////////////////

#                                   Getting Dummies 

Telecom_with_dummies = pd.get_dummies(Telecom)
Telecom_with_dummies.columns
Telecom_with_dummies.info()

# /////////////////////

#                           Regressors Selection - 1 step

# Our dependent variable
y = Telecom_with_dummies['Churn']
Telecom_with_dummies_no_Churn = Telecom_with_dummies.drop('Churn', axis=1)


# Our independent variables
X = Telecom_with_dummies_no_Churn[['SeniorCitizen', 'Partner', 
        'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
       'PaperlessBilling', 'InternetService_DSL', 'MonthlyCharges',
       'InternetService_Fiber optic', 'Contract_Month-to-month',
       'Contract_Two year', 'PaymentMethod_Bank transfer (automatic)',
       'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']]

# we decided to drop the following columns:
# 0. 'Churn' because it's our dependent variable
# 1. 'gender' since, as it shown in the bivariate analysis with 'Churn', churning or not
#    is not affected by the gender itself
# 2. 'TotalCharges' since, having to choose between it and 'tenure' for their high 
#    correlation value (), we picked the one more significant in the bivariate analysis
#    with the 'Churn' variable
# 3. dummy 'InternetService_No' since it's just what remains after accounting for
#    'InternetService_DSL' and 'InternetService_Fiber optic' (if we include all three
#     there would be an issue with the matrix invertibility for the beta computation)
# 4. dummy 'Contract_One year' for the same reason of point 3.
# 5. dummy 'PaymentMethod_Credit card (automatic)' for the same reason of point 3.

# /////////////////////

#                            Variance Inflation Factor (VIF)

from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

X = add_constant(X)


pd.Series([variance_inflation_factor(X.values, i) 
               for i in range(X.shape[1])], 
              index=X.columns)

# If we accept only VIF values < 5 in order to be sure that there is no multicollinearity,
# we should drop all the regressors featuring a value above the 5.
# Since 'tenure' and 'MonthlyCharges' feature very high VIF (rispectively 7.572195
# and 10.779738), we decide to drop 'MonthlyCharges', since 'tenure' is more significant
# for the 'Churn' variable (as shown in the bivariate analysis) 

#                           Regressors Selection - 2 step

X.drop('MonthlyCharges', axis=1, inplace=True)

# VIF
pd.Series([variance_inflation_factor(X.values, i) 
               for i in range(X.shape[1])], 
              index=X.columns) # we like them since VIF < 5

# /////////////////////

#                                   Running the Logit
  
# splitting the data
from sklearn.model_selection import train_test_split

train_X, test_X = train_test_split(X, test_size=0.3, random_state=0)
train_y, test_y = train_test_split(y, test_size=0.3, random_state=0)

train_X.shape, test_X.shape
train_y.shape, test_y.shape

# running the reg
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm

logreg = LogisticRegression()
logreg.fit(train_X,train_y)
accuracy_lr = logreg.score(train_X,train_y)
print("Logistic Regression accuracy is :",accuracy_lr) # 0.8061763510767981

logit = sm.Logit(train_y, train_X)
result = logit.fit()
result.summary2()       

# Comment

# Logistic regression is a non-linear probability model used to explain the relationship between one
# dependent binary variable and one or more nominal, ordinal, interval or ratio-level independent variables.  
# The coefficients in the output of the logistic regression are given in units of log odds. 
# Therefore, the coefficients indicate the amount of change expected in the log odds when there is a one unit
# change in the independent variable.
# a) The variables Senior Citizen has a p-value of 0.0012 and a coefficient of 0.3327, which
#    means that if SeniorCitizen=1, the log odds of churning increase by 33.27%, all else being equal.
#    To recover the odds, we need to compute : e^0.3327= 1.39. This means that, if SeniorCitizen=1, 
#    the odds increase by 1.39
#    The same procedure is to be applied to all of the variables of the logit model, thus we will focus on the
#    regressors which we deem to be more relevant to the analysis.
# b) Tenure has a p-value of 0.00 and a coefficient of -0.0362, meaning that an increase in tenure by one 
#    month decreases the log odds of churning by 3.62%
# c) Phone Service has a p-value of 0.0017 and a coefficient of -0.4763, so that if PhoneService= 1 the log 
#    odds of churning decrease by 47.63%.
# d) Paperless Billing has a p-value of 0.00 and a coefficient of 0.4566, meaning that 
#    if Paperless Billing=1, the log odds of churning increase by 45.66%.

# --------------------------------------------------------------------------------------
#                                2. Model Evaluation 
# --------------------------------------------------------------------------------------

#                       Receiver operating characteristic - ROC

test_scores_reg = logreg.predict_proba(test_X)
test_scores_reg

import scikitplot as skplt
skplt.metrics.plot_roc_curve(test_y, test_scores_reg)

# Comments
# ROC curve is a performance measurement for classification problem at various thresholds settings.
# ROC is a probability curve. It tells the accuracy of the test.
# it is plotted with True Positive Rate (sensitivity) on y-axis and False Positive Rate on the x-axis (1-specifity).
# The closer the curve follows the left-hand border and then the top border of the ROC space,
# better the model is at predicting 0s as 0s and 1s as 1s.

# For detecting the accuracy of the model we have to look at the area below the curve.
# An area of 1 represents a perfect test; an area of .5 represents a worthless test.
# As we can see from the graph our model is pretty-good one having an area of 0.84

# /////////////////////

#                               Confusion Matrix

skplt.metrics.plot_confusion_matrix(test_y, result.predict(test_X) > 0.5)

# Comments
# the Confusion Matrix it is a performance measurement for machine learning classification problem
# where output can be two or more classes. It is a table with 4 different
# combinations of predicted and actual values: 
# - on the upper-left side we have the True negative
# - on the upper-right side we have the False positive (type I error)
# - on the lower-left side we have the False negative (type II error)
# - on the lower-right side we have the True positive
# As it appears from the our matrix the model misclassifies the data only in the 20% of the cases.

# /////////////////////

#                               Bootstrapping for higher accuracy

def bootstrap_replicate(data, function):
    bs_sample = np.random.choice(data, len(data))
    return function(bs_sample)

bootstrap_replicate(result.predict(test_X), np.mean)

bs_results = np.empty(10000)

for i in range(10000):
    bs_results[i] = bootstrap_replicate(result.predict(test_X), np.mean)

# plotting
plt.hist(bs_results, bins = 30, normed=True)
plt.xlabel("Mean of predicted Churn")
plt.ylabel("Empirical Probability Density Function")
plt.show()

mean_value = bs_results.mean()
mean_value
conf_interval = np.percentile(bs_results, [2.5, 97.5])
conf_interval 


# By bootstrapping we can make the prediction even more accurate and compute the confidence 
# intervals which give us an idea of how our predicted values distribute around the mean 
# value of 0.2627

########################################################################################
#                                  PCA: not an option
########################################################################################

# We could not implement PCA analysis as this is performed on numerical variables
# Our dataset is composed of mixed tyes of variables so that PCA is not a suitable option

########################################################################################
#                                    BUSINESS CASE
########################################################################################

#                                     Lift Chart

pred = np.array([1-result.predict(test_X), result.predict(test_X)])
pred.T.shape

skplt.metrics.plot_lift_curve(test_y, pred.T)

# Comment
# Lift is a measure of the effectiveness of a predictive model calculated 
# as the ratio between the results obtained with and without the predictive model.

# /////////////////////

#                                Cumulative Gain Chart

skplt.metrics.plot_cumulative_gain(test_y, pred.T)

# Comment 
# The cumulative gains chart shows the percentage of the overall number of 
# cases in a given category "gained" by targeting a percentage of the total number of cases.
# In our case, the x axes represents the bins in which the population has been divided,
# sorted by desceding probabiliy of default, the y-axes represents the cumulative 
# percentage of churning customers and the diangonal curve represents the baseline curve. 
# We can see that by selecting 20% of the cases, we would expect to "gain" approximately 50% of 
# all of the cases that actually churn. 
# The farther above the baseline a curve lies, the greater the gain.

# /////////////////////

#                                     Our Solution

# Given:
# ✓ Cost for each single contact: 5 euros 
# ✓ Expected Revenues for each retained customer: 25 euros
# ✓ Expected Retention rate obtained through the Commercial Campaign: 25% (consider the 
# number of people who really churned by target size, we’re hypothesizing that 1 out of 4 
# of them would not have abandoned the Company if contacted by the campaign).

# Companies aim to make profit, or at least, gain the break-even point.
# The break-even point is a point in time (or in number of units sold) when forecasted revenue
# exactly equals the estimated total costs; where loss ends, and profit begins to accumulate. 
# This is the point at which a business, product, or project becomes financially viable.

# Revenues depends on how many people we will expect to retain with our campaign:
# Revenues = r * n_c * g * Rr

# where:
# r = revenues per customer
# n_c = number churners
# g = gain (cumulative gain corresponding to the % customers contacted)
# Rr = retention rate

# Cost depends on how many people we need to contact with our campaign:
# Costs = % * n * c

# where:
# % = percentage of customers contacted
# n = number of customers (sample size)
# c = cost per customer


# in order to have a break-even point we must satifsy the following equation:

# r * n_c * g * Rr = % * n * c 

# which is to say:

# % / g = (r * n_c * Rr) / (n * c)

# since:

r = 25
n_c = y.sum()
Rr = 0.25
n = X.shape[0]
c = 5

# we can compute % / g as:

(r * n_c * Rr) / (n * c) # 0.332231228668942

# since base on our cumulative gain plot the values of % and g whose ratio give 1/3 correspond
# to a % customers to contact of barely 8%, we take this as a required number of customers to be contacted to
# achieve the break-even point.
