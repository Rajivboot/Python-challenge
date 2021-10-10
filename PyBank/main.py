import csv
import os

# open relative path to data file
csvpath = os.path.join('Resources', 'budget_data.csv').replace("\\", "/")

with open(csvpath) as csvfile:
    
    reader = csv.reader(csvfile)
    # skip first line bc it has column titles
    next(csvfile)

    # This part counts the total months
    totalMonths = 0
    for row in reader:
        # looping 0+1"
        totalMonths = totalMonths + 1

    
    # reset the file so we read from the first row again and skip the header line
    csvfile.seek(0)
    next(csvfile)

    # This for-loop will add the dollar amount in each row of the CSV
    totalDollars = 0
    for row in reader:
        totalDollars = totalDollars + int(row[1])

    # reset the file so we read from the first row again and skip the header line
    csvfile.seek(0)
    next(csvfile)


    # This part will calculate the average change between months
    monthlyChangesList = []
    lastMonth = None
    for row in reader:
        thisMonth = row
        # only calculate difference starting with the second row. 
        if (lastMonth is not None):
            difference = int(thisMonth[1]) - int(lastMonth[1])
            monthlyChangesList.append([thisMonth[0], difference])
        # set lastMonth equal to the $ from thisMonth so that it's accurate for the next iteration of the for-loop
        lastMonth = thisMonth
    # At this point, monthlyChangesList is fully populated with the difference between each month.
    # To get the average, now need to add all the differences and divide by the total number of entries in monthlyChangesList
    diffTotal = 0
    # reset the file so we read from the first row again and skip the header line
    csvfile.seek(0)
    next(csvfile)
    # Calculate total and avg
    for row in monthlyChangesList:
        # Same as diffTotal = diffTotal + int(row[1])
        diffTotal += int(row[1])
    averageChange = diffTotal / len(monthlyChangesList)
    # round to 2 decimals
    averageChange = round(averageChange, 2)

    # reset the file so we read from the first row again and skip the header line
    csvfile.seek(0)
    next(csvfile)

    
    # Find a greater increase as we iterate through monthlyChangesList, then we will replace greatestInc
    greatestInc = monthlyChangesList[0]
    for monthlyChange in monthlyChangesList:
        if (monthlyChange[1] > greatestInc[1]):
            greatestInc = monthlyChange

    # reset the file so we read from the first row again and skip the header line
    csvfile.seek(0)
    next(csvfile)

    # This part will calculate teh greatest decrease in profits.
    greatestDec = monthlyChangesList[0]
    for monthlyChange in monthlyChangesList:
        if (monthlyChange[1] < greatestDec[1]):
            greatestDec = monthlyChange

    # Write report to text file and console. Use the variables we calculated previously.
    # Use textFile.write() to write to the text file.
    # Use print() to write to the console.
    if os.path.exists("analysis/analysis.txt"):
        os.remove("analysis/analysis.txt")
    textFile = open("analysis/analysis.txt","a")
    textFile.write("Financial Analysis\n")
    textFile.write("----------------------------\n")
    textFile.write("Total Months: " + str(totalMonths) + "\n")
    textFile.write("Total: $" + str(totalDollars) + "\n")
    textFile.write("Average Change: $" + str(averageChange) + "\n")
    textFile.write("Greatest Increase in Profits: " + str(greatestInc[0]) + " ($" + str(greatestInc[1]) + ")" + "\n")
    textFile.write("Greatest Decrease in Profits: " + str(greatestDec[0]) + " ($" + str(greatestDec[1]) + ")" + "\n")

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(totalMonths))
    print("Total: $" + str(totalDollars))
    print("Average Change: $" + str(averageChange))
    print("Greatest Increase in Profits: " + str(greatestInc[0]) + " ($" + str(greatestInc[1]) + ")")
    print("Greatest Decrease in Profits: " + str(greatestDec[0]) + " ($" + str(greatestDec[1]) + ")")

