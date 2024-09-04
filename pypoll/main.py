import os
import csv
poll_csv = os.path.join('.','Resources','election_data.csv')
with open(poll_csv, 'r') as csvfile:
    folder_name = "Analyses"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Define the file path within the folder
    file_path = os.path.join(folder_name, "output.txt")
    f = open(file_path, 'w')
    
    
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

    # write percentages and votes to file
    f.writelines("Election Results\n")
    f.writelines("------------------------\n")
    f.writelines(f"Total votes: {total}\n")
    f.writelines("------------------------\n")
    f.writelines(f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})\n")
    f.writelines(f"Diana DeGette: {diana_percentage}% ({diana_votes})\n")
    f.writelines(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})\n")

    # finding and writing the winner to our file
    winner_votes = max(charles_votes,diana_votes,raymon_votes)
    if winner_votes == charles_votes:
        f.writelines("Winner: Charles Casper Stockham\n ")
    elif winner_votes == diana_votes:
        f.writelines("Winner: Diana DeGette\n")
    else:
        f.writelines("Winner: Raymon Anthony Doane\n")
    f.writelines("------------------------\n")


f.close()


