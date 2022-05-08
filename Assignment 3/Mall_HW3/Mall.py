# Author: Prashant Pramodkumar Mall
# The following program takes user input for a search term and number of search results and then searches YouTube for top-rated videos in Mumbai geographical location for 2022
# To run from terminal window: python3 mall.py

from googleapiclient.discovery import build
import copy #Will be used to create true copies of variables and not copies with same reference
import csv #Will write result to CSV file 

# YouTube API key
API_KEY = "AIzaSyB4UvkJoNN_O-Fa7Vm9m1JFwqEYN_g9L1c"

API_NAME = "youtube"
API_VERSION = "v3"

youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)

# User input for search term and number of search results to show
searchTerm = input("Enter your search term: ")
searchMax = input("Enter the max number of results you want: ")

# Parameters for the API
requestData = youtube.search().list(
    q=searchTerm,
    location="19.0760,72.8777",  # This is my home city, Mumbai (India) :)
    locationRadius="10km",
    type="video",
    part="id, snippet",
    maxResults=searchMax,
    order="rating",
    publishedAfter="2022-01-01T00:00:00Z",
)

# Data received from the API
responseData = requestData.execute()

# Table headers and data variables defined for analysis
analysisOne = ["Video Id", "Views",
               "Likes", "Comments", "Duration", "Title"]
analysisOneData = []

analysisTwo = ["Like %", "Views", "Likes", "Title"]
analysisTwoData = []

analysisThree = ["Views", "Comments", "Title"]
analysisThreeData = []

# Fetch statistics and content detail from the videoId 
for count, video in enumerate(responseData.get("items", [])):
    videoData = youtube.videos().list(
        id=video["id"]["videoId"], part="statistics").execute()
    videoContent = youtube.videos().list(
        id=video["id"]["videoId"], part="contentDetails").execute()

    if "viewCount" in videoData["items"][0]["statistics"]:
        views = int(videoData["items"][0]["statistics"]["viewCount"])
    else:
        views = 0

    if "likeCount" in videoData["items"][0]["statistics"]:
        likes = int(videoData["items"][0]["statistics"]["likeCount"])
    else:
        likes = 0

    if "commentCount" in videoData["items"][0]["statistics"]:
        comments = int(videoData["items"][0]["statistics"]["commentCount"])
    else:
        comments = 0

    analysisOneData.append([video["id"]["videoId"], f'{views:,}', f'{likes:,}', f'{comments:,}',
                           videoContent["items"][0]["contentDetails"]["duration"][2:], video["snippet"]["title"]])

# Printing of first table in console
format_row_one = "{:<15}" * (len(analysisOne) + 1)
print(format_row_one.format("", *analysisOne))
for count, row in enumerate(analysisOneData):
    print(format_row_one.format(count+1, *row))

# Citation - https://www.geeksforgeeks.org/writing-csv-files-in-python/
# writing to csv file 
with open("Mall.csv", 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(analysisOne) 
    # writing the data rows 
    csvwriter.writerows(analysisOneData)

print("\n\n")
analysisTwoData = copy.deepcopy(analysisOneData)
for count, row in enumerate(analysisTwoData):
    if int(row[1]) != 0:
        likePercentage = (int(row[2])/int(row[1]))*100
    else:
        likePercentage = 0

    analysisTwoData[count].insert(0, format(likePercentage, ".3f"))
    del analysisTwoData[count][1]
    del analysisTwoData[count][3]
    del analysisTwoData[count][3]

analysisTwoData = sorted(
    analysisTwoData, key=lambda x: float(x[0]), reverse=True)

# Printing of second table in console
format_row_two = "{:<15}" * (5)
print(format_row_two.format("", *analysisTwo))
for i in range(5):
    if i < len(analysisTwoData):
        analysisTwoData[i][0] = analysisTwoData[i][0]+"%"
        print(format_row_two.format(i+1, *analysisTwoData[i]))
    else:
        print(format_row_two.format(i+1, "-", "-", "-", "-",))

print("\n\n")
analysisThreeData = copy.deepcopy(analysisOneData)
for count, row in enumerate(analysisThreeData):
    del analysisThreeData[count][0]
    del analysisThreeData[count][1]
    del analysisThreeData[count][2]

analysisThreeData = sorted(
    analysisThreeData, key=lambda x: int(x[1]), reverse=True)

# Printing of third table in console
format_row_three = "{:<15}" * (4)
print(format_row_three.format("", *analysisThree))
for i in range(5):
    if i < len(analysisThreeData):
        print(format_row_three.format(i+1, *analysisThreeData[i]))
    else:
        print(format_row_three.format(i+1, "-", "-", "-", "-",))
