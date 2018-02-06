import os
import csv

# List of file numbers
csvfiles = ['1', '2']

# Initialize lists
date = []
revenue = []

# Loop through each file
for file in csvfiles:

    # Grab budget CSV
    budgetCSV = os.path.join('budget_data_' + file + '.csv')
    outputTXT = os.path.join('financial_analysis_results_'+ file + '.txt')

    # Delete contents in lists to start empty
    del date[:]
    del revenue[:]

    # Open current budget CSV
    with open(budgetCSV, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip headers
        next(csvreader, None)
        
        # Append data 
        for row in csvreader:
            date.append(str(row[0]))
            revenue.append(int(row[1]))
        
        # Calculate results
        countMonths = len(date)
        sumRevenue = sum(revenue)
        avgRevenue = int(sumRevenue / countMonths)
        maxRevenue = max(revenue)
        maxDate = date[revenue.index(maxRevenue)]
        minRevenue = min(revenue)
        minDate = date[revenue.index(minRevenue)]

    # Define ouput results in order to print and write to text file
    outputResults = ('\nFinancial Analysis ' + file + '\n' +
                    '-'*25 + 
                    '\nTotal Months: ' + str(countMonths) +
                    '\nTotal Revenue: $' + str(sumRevenue) +
                    '\nAverage Revenue Change: $' + str(avgRevenue) +
                    '\nGreatest Increase in Revenue: ' + str(maxDate) + ' ($' + str(maxRevenue) + ')' +
                    '\nGreatest Decrease in Revenue: ' + str(minDate) + ' ($' + str(minRevenue) + ')')
    
    # Print results in terminal
    print(outputResults)

    # Write results into text file
    with open(outputTXT, 'w', newline="") as txtfile:
        txtfile.write(outputResults)

        
