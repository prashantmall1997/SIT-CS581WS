# Author: Prashant Mall
# Assignment 4 of CS581 (Spring 2022)
# This program will process graph data and analyze results

# Run in terminal - "pip install networkx" to install the required package
# To run program from terminal window: python3 Mall.py
# Please make sure to have the CSV files in the same path before you run the program

# Import Time to show time taken to run program 
import time
start_time = time.time()
# Import module to read CSV files
import csv
from operator import neg
# Import NetworkX module - DS for Graphs
# To install, run in terminal - "pip install networkx"
import networkx

# Set initial value to required variables
totalEdges = 0
trust = 0
distrust = 0
triangles = []
numberOfTriangles = 0

# Read CSV file
tryAgain = True
while tryAgain:
    try:
        csvName = input("Enter Exact CSV File Name (Example - 'test.csv'): ")
        file = open(csvName)
        tryAgain = False
    except FileNotFoundError:
        print("Wrong file name or file does not exsist. Please check and enter again.")
# file = open("epinions0.csv")
csvreader = csv.reader(file)

# Copy rows from CSV to a Python array
rows = []
for row in csvreader:
    rows.append(row)

# Graph Data
graph = networkx.Graph()
for row in rows:
    totalEdges = totalEdges + 1
    nodeA = int(row[0])
    nodeB = int(row[1])
    relation = int(row[2])
    # print(nodeA,nodeB,relation)
    graph.add_edge(nodeA, nodeB, relation=relation)

    if (relation == 1):
        trust = trust + 1
    elif (relation == -1):
        distrust = distrust + 1

# Calculate Triangles
for possibleTriangles in networkx.enumerate_all_cliques(graph):
    if len(possibleTriangles) == 3:
        numberOfTriangles = numberOfTriangles + 1
        triangles.append(possibleTriangles)

# Expected Probability Distribution*
positiveProbability = trust/totalEdges
negativeProbability = 1 - positiveProbability

expectedPercentTTT = positiveProbability * \
    positiveProbability*positiveProbability*100
expectedPercentTTD = positiveProbability * \
    positiveProbability*negativeProbability*100*3
expectedPercentTDD = positiveProbability * \
    negativeProbability*negativeProbability*100*3
expectedPercentDDD = negativeProbability * \
    negativeProbability*negativeProbability*100

expectedNumberTTT = expectedPercentTTT*numberOfTriangles*0.01
expectedNumberTTD = expectedPercentTTD*numberOfTriangles*0.01
expectedNumberTDD = expectedPercentTDD*numberOfTriangles*0.01
expectedNumberDDD = expectedPercentDDD*numberOfTriangles*0.01

totalExpectedPercentage = expectedPercentTTT + \
    expectedPercentTTD+expectedPercentTDD+expectedPercentDDD
totalExpectedNumber = expectedNumberTTT + \
    expectedNumberTTD+expectedNumberTDD+expectedNumberDDD

# Actual Probability Distribution*
actualNumberTTT = 0
actualNumberTTD = 0
actualNumberTDD = 0
actualNumberDDD = 0

for triangle in triangles:
    nodeOne = triangle[0]
    nodeTwo = triangle[1]
    nodeThree = triangle[2]

    firstEdge = graph[nodeOne][nodeTwo]["relation"]
    secondEdge = graph[nodeOne][nodeThree]["relation"]
    thirdEdge = graph[nodeTwo][nodeThree]["relation"]
    overallRelationScore = firstEdge + secondEdge + thirdEdge

    if (overallRelationScore == 3):
        actualNumberTTT = actualNumberTTT + 1
    elif (overallRelationScore == 1):
        actualNumberTTD = actualNumberTTD + 1
    elif(overallRelationScore == -1):
        actualNumberTDD = actualNumberTDD + 1
    elif(overallRelationScore == -3):
        actualNumberDDD = actualNumberDDD + 1

actualPercentageTTT = actualNumberTTT/numberOfTriangles*100
actualPercentageTTD = actualNumberTTD/numberOfTriangles*100
actualPercentageTDD = actualNumberTDD/numberOfTriangles*100
actualPercentageDDD = actualNumberDDD/numberOfTriangles*100

totalActualPercentage = actualPercentageTTT + \
    actualPercentageTTD+actualPercentageTDD+actualPercentageDDD
totalactualNumber = actualNumberTTT + \
    actualNumberTTD + actualNumberTDD + actualNumberDDD

print("*** START ***")
print("\n")
print("RESULTS FOR FILE: " + csvName)
print("\n")
print("Triangles " + str(numberOfTriangles))
print("TTT: " + str(actualNumberTTT) +
      "\t\t\t" + "Edges used: " + str(totalEdges))
print("TTD: " + str(actualNumberTTD) + "\t\t\t" + "Trust Edges: " + str(trust) +
      "\t\t\t" + "Probability %: " + str(round(positiveProbability*100, 2)))
print("TTT: " + str(actualNumberTDD) + "\t\t\t" + "Distrust Edges: " +
      str(distrust) + "\t\t" + "Probability %: " +
      str(round(negativeProbability*100, 2)))
print("DDD: " + str(actualNumberDDD) +
      "\t\t\t" + "Total: " + str(trust+distrust) + "\t\t\t\t\t" + str((round(positiveProbability*100, 2)) + (round(negativeProbability*100, 2))))

print("\n")
print("Expected Distribution")
print("\t\tPercentage\tNumber")
print("TTT: " + "\t\t" + str(round(expectedPercentTTT, 2)) +
      "\t\t" + str(round(expectedNumberTTT, 2)))
print("TTD: " + "\t\t" + str(round(expectedPercentTTD, 2)) +
      "\t\t" + str(round(expectedNumberTTD, 2)))
print("TDD: " + "\t\t" + str(round(expectedPercentTDD, 2)) +
      "\t\t" + str(round(expectedNumberTDD, 2)))
print("DDD: " + "\t\t" + str(round(expectedPercentDDD, 2)) +
      "\t\t" + str(round(expectedNumberDDD, 2)))
print("Total: " + "\t\t" + str(round(totalExpectedPercentage, 2)) +
      "\t\t" + str(round(totalExpectedNumber, 2)))

print("\n")
print("Actual Distribution")
print("\t\tPercentage\tNumber")
print("TTT: " + "\t\t" + str(round(actualPercentageTTT, 2)) +
      "\t\t" + str(round(actualNumberTTT, 2)))
print("TTD: " + "\t\t" + str(round(actualPercentageTTD, 2)) +
      "\t\t" + str(round(actualNumberTTD, 2)))
print("TDD: " + "\t\t" + str(round(actualPercentageTDD, 2)) +
      "\t\t" + str(round(actualNumberTDD, 2)))
print("DDD: " + "\t\t" + str(round(actualPercentageDDD, 2)) +
      "\t\t" + str(round(actualNumberDDD, 2)))
print("Total: " + "\t\t" + str(round(totalActualPercentage, 2)) +
      "\t\t" + str(round(totalactualNumber, 2)))

print("\n")
print("*** END ***")
print("%s Seconds taken to execute code!" % (time.time() - start_time))
