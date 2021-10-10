import csv
import os

# open relative path to data file
csvpath = os.path.join('Resources','election_data.csv').replace("\\", "/")

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    # skip first line bc it has column titles
    next(csvfile)


    # This for-loop will gather candidate data and count totalVoters
    totalVoters = 0
    candidateNames = []
    candidateVotes = []
    for row in reader:
        totalVoters += 1
        if (row[2] not in candidateNames):
            candidateNames.append(row[2])
            candidateVotes.append(0)
        else:
            index = candidateNames.index(row[2])
            candidateVotes[index] += 1

    maxVotes = 0
    for votes in candidateVotes:
        if (votes > maxVotes):
            maxVotes = votes
    winnerIndex = candidateVotes.index(maxVotes)
    winnerName = candidateNames[winnerIndex]

    candidatePercent = []
    for votes in candidateVotes:
        index = candidateVotes.index(votes)
        candidatePercent.append(round(votes/totalVoters * 100, 3))


    # Write report to text file and console. Use the variables calculated previously.
    # Use textFile.write() to write to the text file.
    # Use print() to write to the console.
    if os.path.exists("analysis/analysis.txt"):
        os.remove("analysis/analysis.txt")
    textFile = open("analysis/analysis.txt","a")
    textFile.write("Election Results\n")
    textFile.write("-------------------------\n")
    textFile.write("Total Votes: " + str(totalVoters) + "\n")
    textFile.write("-------------------------\n")
    for i in range(len(candidateNames)):
        textFile.write(candidateNames[i] + ": " + str(candidatePercent[i]) + "% (" + str(candidateVotes[i]) + ")\n")
    textFile.write("-------------------------\n")
    textFile.write("Winner: " + winnerName + "\n")
    textFile.write("-------------------------\n")

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(totalVoters) + "")
    print("-------------------------")
    for i in range(len(candidateNames)):
        print(candidateNames[i] + ": " + str(candidatePercent[i]) + "% (" + str(candidateVotes[i]) + ")")
    print("-------------------------")
    print("Winner: " + winnerName)
    print("-------------------------")


