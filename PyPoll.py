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

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Opening election results, read file
with open(file_to_load) as election_data:

    # Read file object with reader function
    file_reader = csv.reader(election_data)
    # Header row
    headers = next(file_reader)

    for row in file_reader:
        
        total_votes += 1

        candidate_name = row[2]
        
        # Exclude duplicates
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Set start at zero
            candidate_votes[candidate_name] = 0

        # Add vote to specific candidate total count
        candidate_votes[candidate_name] += 1
    
    # loop to iterate through candidate list to determine vote %
    for candidate in candidate_votes:
        
        # retrieve vote ct of candidate
        votes = candidate_votes[candidate]
        # calculate
        vote_percentage = float(votes) / float(total_votes) * 100
        # print candidate name & %
        #print(f"{candidate}: received {vote_percentage:.1f}% of the vote")

        #determine winning vote ct and name
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true, set winning_ct = votes AND winning_% = vote_%
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

        # print winning results
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    
    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")
    print(winning_candidate_summary)


# print/audits
#print(candidate_votes)
