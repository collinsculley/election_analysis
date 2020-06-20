#The data we need to retrieve
#1 Total number of votes cast
#2 Complete list of candidates who received votes
#3 Percentage of votes each candidate won
#4 Total number of votes each candidate won
#5 Winner of the election based on popular vote

# Adding dependencies
import csv
import os

# Assign variable for the file to load and path
file_to_load = os.path.join("Week3", "election_analysis", "Resources", "election_results.csv")

# Create filename variable to a path to file
file_to_save = os.path.join("Week3", "election_analysis", "Analysis", "election_analysis.txt")

# Opening election results, read file
with open(file_to_load) as election_data:

    # Read file object with reader function
    file_reader = csv.reader(election_data)

    # Print header row
    headers = next(file_reader)
    print(headers)
