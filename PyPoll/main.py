import os
import csv

csvfiles = ['1','2']
voters = []
voteCount = []
candidates = []
candidateList = []

for file in csvfiles:
    election_data_CSV = os.path.join('election_data_' + file + '.csv')
   
    with open(election_data_CSV,'r', newline="") as datafile:
        csvreader = csv.reader(datafile, delimiter=",")
        
        next(csvreader, None)

        for row in csvreader:
            voters.append(str(row[0]))
            candidates.append(str(row[2]))
            candidateList = set(candidates)

totalVotes = len(voters)

print('\nElection Results\n' + '-'*25 + '\nTotal Votes: ' + str(totalVotes) +'\n'+ '-'*25)

for name in candidateList:
    candidate_votes = 0
    for l in candidates:
        if l == name:
            candidate_votes = candidate_votes + 1

    percent_totalVotes = float((candidate_votes / totalVotes)*100)
    print('\n'+ str(name) + ': ' + str(percent_totalVotes) + '% (' + str(candidate_votes) +')')



