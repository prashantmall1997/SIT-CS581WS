# Author: Prashant Mall
# Assignment 7 of CS581 (Spring 2022)
# This program will analyze the CSV file Pew_Survey and show insightful data

# Run in terminal to install the required package:
# pip install matplotlib
# pip install pandas
# To run program from terminal window: python3 Mall.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Import CSV file in Data Frame
df = pd.read_csv("Pew_Survey.csv")


###########
# Select one column form df
useSocialMedia = df["snsint2"]
socialUse = ["Yes", "No"]
socialUseStats = [useSocialMedia.value_counts()[1], useSocialMedia.value_counts(
)[2]]
# Mke Pie Chart
plt.pie(socialUseStats, labels=socialUse, autopct='%1.1f%%', explode=(0.1, 0),
        shadow=True, startangle=0)
plt.title('% of people on Social Media')
# Show plot
plt.show()

############

# Creaate sub frame with social app used heading
socialMedia = df[["web1a", "web1b", "web1c", "web1d", "web1e",
                  "web1f", "web1g", "web1h", "web1i"]]
socialMediaNames = ['Twitter', 'Instagram', 'Facebook', 'Snapchat',
                    'YouTube', 'WhatsApp', 'Pinterest', 'LinkedIn', 'Reddit']
activeUsers = []

for (columnName, columnData) in socialMedia.iteritems():
    activeUsers.append(columnData.value_counts()[1])

# print(socialMediaNames)
# print(activeUsers)

data = {"Social Media Platform": socialMediaNames, "Active Users": activeUsers}
data = pd.DataFrame(data=data)

# Plot the bargraph
data.plot.bar(x="Social Media Platform", y="Active Users", rot=70,
              title="Number of active users on different Social Media")
# Show plot
plt.show(block=True)

#################

# Analysis on how many times the social app is checked
socialMedia = df[["sns2a", "sns2b", "sns2c", "sns2d", "sns2e"]]
socialMediaNames = ['Twitter', 'Instagram', 'Facebook', 'Snapchat',
                    'YouTube']

severalTimesDay = []
aboutOnceDay = []
fewTimesWeek = []
fewWeeks = []
lessOften = []

# Looping through to identify the value 
for (columnName, columnData) in socialMedia.iteritems():
    if (1 in columnData):
        severalTimesDay.append(columnData.value_counts()[1])
    else:
        severalTimesDay.append(0)
    if (2 in columnData):
        aboutOnceDay.append(columnData.value_counts()[2])
    else:
        aboutOnceDay.append(0)
    if (3 in columnData):
        fewTimesWeek.append(columnData.value_counts()[3])
    else:
        fewTimesWeek.append(0)
    if (4 in columnData):
        fewWeeks.append(columnData.value_counts()[4])
    else:
        fewWeeks.append(0)
    if (5 in columnData):
        lessOften.append(columnData.value_counts()[5])
    else:
        lessOften.append(0)

# print(severalTimesDay)

data = {"Social Media Platform": socialMediaNames,
        "Several Times/Day": severalTimesDay, "About Once/Day": aboutOnceDay, "Few Times/Week": fewTimesWeek, "Every Few Weeks": fewWeeks, "Less Often": lessOften}
data = pd.DataFrame(data=data)

# Plot Graph

# plotting graph
data.plot(x="Social Media Platform", y=["Several Times/Day",
          "About Once/Day", "Few Times/Week", "Every Few Weeks", "Less Often"], kind="bar")
plt.show(block=True)

##########################

# Pie chart on how the population is distributed 
region = df[["snsint2", "cregion"]]
region = region[region.snsint2 == 1]
region = region.drop('snsint2', 1)
regionNames = ["Northeast", "Midwest", "South", "West"]
regionDistribution = []

for (columnName, columnData) in region.iteritems():
    regionDistribution.append(columnData.value_counts()[1])
    regionDistribution.append(columnData.value_counts()[2])
    regionDistribution.append(columnData.value_counts()[3])
    regionDistribution.append(columnData.value_counts()[4])

plt.pie(regionDistribution, labels=regionNames, autopct='%1.1f%%', explode=(0.01, 0.01, 0.01, 0.01),
        shadow=True, startangle=0)
plt.title('% of people on Social Media - Region Wise')
plt.show()

###################################

party = df[["snsint2", "party"]]
party = party[party.snsint2 == 1]
party = party.drop('snsint2', 1)
partyNames = ["Republican", "Democrat", "Independent",
              "No preference", "Other party", "Don't know", "Refused"]
partyDistribution = []

for (columnName, columnData) in party.iteritems():
    if (1 in columnData):
        partyDistribution.append(columnData.value_counts()[1])
    else:
        partyDistribution.append(0)
    if (2 in columnData):
        partyDistribution.append(columnData.value_counts()[2])
    else:
        partyDistribution.append(0)
    if (3 in columnData):
        partyDistribution.append(columnData.value_counts()[3])
    else:
        partyDistribution.append(0)
    if (4 in columnData):
        partyDistribution.append(columnData.value_counts()[4])
    else:
        partyDistribution.append(0)
    if (5 in columnData):
        partyDistribution.append(columnData.value_counts()[5])
    else:
        partyDistribution.append(0)
    if (8 in columnData):
        partyDistribution.append(columnData.value_counts()[8])
    else:
        partyDistribution.append(0)
    if (9 in columnData):
        partyDistribution.append(columnData.value_counts()[9])
    else:
        partyDistribution.append(0)
# print(partyDistribution)
plt.pie(partyDistribution, labels=partyNames,
        autopct='%1.1f%%', shadow=True, startangle=0)
plt.title('% of online people consider their political party')
plt.show()

######

partyInclination = df[["snsint2", "partyln"]]
partyNames = ['Republican', 'Democrat']

partyInclination = partyInclination[partyInclination.snsint2 == 1]
partyInclination = partyInclination.drop('snsint2', 1)

userInclination = []

for (columnName, columnData) in partyInclination.iteritems():
    if (1 in columnData):
        userInclination.append(columnData.value_counts()[1])
    else:
        userInclination.append(0)
    if (2 in columnData):
        userInclination.append(columnData.value_counts()[2])
    else:
        userInclination.append(0)

print(userInclination)

# plotting graph

data = {"Party Name": partyNames, "Users Inclination": userInclination}
data = pd.DataFrame(data=data)

data.plot.bar(x="Party Name", y="Users Inclination", rot=70,
              title="User lean towards Republican and Democratic")

plt.show(block=True)

#####################

education = df[["educ2"]]
print(education)