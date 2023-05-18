# PyPoll Python Assignment

# Dependencies
import os
import csv

# Files to load
csvpath = os.path.join("..", "Resources", "election_data.csv")  

# Read the cvs and create a list
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)

 # Lists to store data
    total_vote = 0
    cand_list = {}

# Look through the values and add them to the empty list 
    for row in csv_reader:
        total_vote += 1
        name = row[2]
        if name in cand_list:
            cand_list[name] += 1
        else:
            cand_list[name] = 1

cand_list["Charles Casper Stockham Votes"] = round((cand_list["Charles Casper Stockham"]/total_vote) * 100, 3)
cand_list["Diana DeGette Votes"] = round((cand_list["Diana DeGette"]/total_vote) * 100, 3)
cand_list["Raymon Anthony Doane Votes"] = round((cand_list["Raymon Anthony Doane"]/total_vote) * 100, 3)

cand_winner = max(cand_list, key=cand_list.get)

# Output
print("Election Results")
print("--------------------------")
print("Total Vote: " + str(total_vote))
print("--------------------------")
print("Charles Casper Stockham: " + str(cand_list["Charles Casper Stockham Votes"]) + "% " + str(cand_list["Charles Casper Stockham"])) 
print("Diana DeGette: " + str(cand_list["Diana DeGette Votes"]) + "% " + str(cand_list["Diana DeGette"]))
print("Raymon Anthony Doane: " + str(cand_list["Raymon Anthony Doane Votes"]) + "% " + str(cand_list["Raymon Anthony Doane"]))
print("--------------------------")
print("Winner: " + str(cand_winner))
print("--------------------------")

# Export the analysis to text file
output = os.path.join("..", "analysis", "output.txt")
with open(output, "w") as txt_file:
    txt_file.write("Election Results" + "\n")
    txt_file.write("--------------------------" + "\n")
    txt_file.write("Total Vote: " + str(total_vote) + "\n")
    txt_file.write("--------------------------" + "\n")
    txt_file.write("Charles Casper Stockham: " + str(cand_list["Charles Casper Stockham Votes"]) + "% " + str(cand_list["Charles Casper Stockham"]) + "\n") 
    txt_file.write("Diana DeGette: " + str(cand_list["Diana DeGette Votes"]) + "% " + str(cand_list["Diana DeGette"]) + "\n")
    txt_file.write("Raymon Anthony Doane: " + str(cand_list["Raymon Anthony Doane Votes"]) + "% " + str(cand_list["Raymon Anthony Doane"]) + "\n")
    txt_file.write("--------------------------" + "\n")
    txt_file.write("Winner: " + str(cand_winner) + "\n")
    txt_file.write("--------------------------" + "\n")

