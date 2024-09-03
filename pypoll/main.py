import os
import csv
poll_csv = os.path.join('.','Resources','election_data.csv')
with open(poll_csv, 'r') as csvfile:
    # defining variables
    csvreader = csv.reader(csvfile)
    total = -1
    charles_votes = 0
    diana_votes = 0
    raymon_votes = 0

    # counting votes
    for row in csvreader:
        total += 1
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes += 1
            
    # calculating percentages
    charles_percentage = round(charles_votes/total *100,3)
    diana_percentage =round(diana_votes/total * 100 ,3)
    raymon_percentage = round(raymon_votes/total * 100 ,3)

    # print percentages and votes
    print("Election Results")
    print("------------------------")
    print(f"Total votes: {total}")
    print("------------------------")
    print(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})")
    print(f"Diana DeGette: {diana_percentage}% ({diana_votes})")
    print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})")

    # finding and printing the winner
    winner_votes = max(charles_votes,diana_votes,raymon_votes)
    if winner_votes == charles_votes:
        print("Winner: Charles Casper Stockham ")
    elif winner_votes == diana_votes:
        print("Winner: Diana DeGette")
    else:
        print("Winner: Raymon Anthony Doane")
    print("------------------------")
