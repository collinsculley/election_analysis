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
county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

winning_county = ""
largest_county = 0

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

    # jump back to start of file and skip header row
    start = election_data.seek(1)
    headers = next(file_reader)

    # challenge loop
    for row in file_reader:
        #county_votes += 1
        county_name = row[1]

        # Exclude dupes
        if county_name not in county_options:
            county_options.append(county_name)
            # Set zero
            county_votes[county_name] = 0
        # Add vote to specific county
        county_votes[county_name] += 1


with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"--------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------\n")
    print(election_results, end="")
    # Save final vote ct to txt file
    txt_file.write(election_results)

    # loop to iterate through candidate list to determine vote %
    for candidate in candidate_votes:
        
        # retrieve vote ct of candidate
        votes = candidate_votes[candidate]
        # calculate
        vote_percentage = float(votes) / float(total_votes) * 100

        # determine winning vote ct and name
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true, set winning_ct = votes AND winning_% = vote_%
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    # loop to itertate through counties
    for county in county_votes:
        
        # retrieval and calculation
        cvotes = county_votes[county]
        cvote_percentage = float(cvotes) / float(total_votes) * 100

        #testing for largest
        if (cvotes > largest_county):
            largest_county = cvotes
            winning_county = county
        
        county_results = (f"{county}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results)
        txt_file.write(county_results)
    
    largest_county_summary = (
        f"--------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------")
    print(largest_county_summary)
    txt_file.write(largest_county_summary)
