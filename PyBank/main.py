# Import Modules 
import os
import csv
# Set path for the CSV file
csvpath = '/Users/admin/git_repos/python-challenge/PyBank/Resources/budget_data.csv'
#csvpath =os.path.join("..","Resources","budget_data.csv") relative path was not working 

#Open and read the csv file 
with open(csvpath) as csvfile:

	csvreader = csv.reader(csvfile,delimiter=',')

	#Read the header row 

	csv_header = next(csvreader)

	print(csv_header)




#set variables

	total_months = 0 
	net_total_profit_losses = 0 
	greatest_increase = 0
	greatest_decrease = 0
	previous = 0 

# create a for loop  to count months and find net profit and loss 
	for row in csvreader:  
		
		total_months += 1

		net_total_profit_losses += int(row[1])

		# average change 
		if row[0] == "Jan-10":
			start = int(row[1])
		if row[0] == "Feb-17":
			end = int(row[1])
			average_change = round((end - start)/(total_months-1),2)

		#  Greatest increase 
		if int(row[1])-previous > greatest_increase:
			greatest_increase = int(row[1])-previous
			time_increase = row[0]

		#  Greatest decrease 
		if int(row[1])-previous < greatest_decrease:
			greatest_decrease = int(row[1])-previous
			time_decrease = row[0]
		previous = int(row[1])

	#print financial analysis
	print('Financial Analysis')
	print('---------------------------')
	print(f'Total Months: {total_months}')
	print(f'Total: ${net_total_profit_losses}')
	print(f'Average Change: ${average_change}')
	print(f'Greatest Increase in Profits: {time_increase} ${greatest_increase}')
	print(f'Greatest Decrease in Profits: {time_decrease} ${greatest_decrease}')

#export txt file 
with open('/Users/admin/git_repos/python-challenge/PyBank/Analysis/financial_analysis.txt', 'w') as Analysis:
    Analysis.write(f'''Financial Analysis
----------------------------
Total Months: {str(total_months)}
Total: ${str(net_total_profit_losses)}
Average Change: ${str(average_change)}
Greatest Increase in Profits: {str(greatest_increase)}
Greatest Decrease in Profits: {str(greatest_decrease)}''')
