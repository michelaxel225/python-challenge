#Import the modules 
import os 
import csv 

# path for the csv file 
csvpath  = '/Users/admin/git_repos/python-challenge/PyPoll/Resources/election_data.csv'


#define variables 

total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0
per_charles = 0
per_diana = 0
per_raymon = 0
#open and read the csv file 
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for rows in csvreader:
        #find the total number of votes 
        total_votes += 1
        #find the number of votes for each candidate 
        if rows[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif rows[2] == "Diana DeGette":
            diana_votes += 1
        elif rows[2] == "Raymon Anthony Doane":
            raymon_votes += 1
        #vote percentage for each caandidate 
        per_charles = (charles_votes/total_votes) * 100
        per_diana = (diana_votes/total_votes) * 100
        per_raymon = (raymon_votes/total_votes) * 100
        #Who is the winner 
    if per_charles > per_diana and per_diana > per_raymon:
        winner = "Charles Casper Stockham"
    elif per_diana > per_charles and per_diana > per_raymon:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
    print(f'''Election Results
-------------------------
Total Votes: {str(total_votes)}
-------------------------
Charles Casper Stockham: {str(per_charles)}% ({str(charles_votes)})
Diana DeGette: {str(per_diana)}% ({str(diana_votes)})
Raymon Anthony Doane: {str(per_raymon)}% ({str(raymon_votes)})
-------------------------
Winner: {winner}
-------------------------''')

election_result_txt='/Users/admin/git_repos/python-challenge/PyPoll/Analysis/Analysis.txt'
with open(election_result_txt, 'w') as txtfile:
		txtfile.write(f'Election Results\n---------------------------\n\tTotal Votes: {total_votes}\n---------------------------\n"Charles Casper Stockham": {per_charles}% ({charles_votes})\n"Diana DeGette": {per_diana}% ({diana_votes})\n\t"Raymon Anthony Doane": {per_raymon}% ({raymon_votes})\n---------------------------\n\tWinner: {winner}\n---------------------------')

