
# Import dependencies
import csv
import os

# Add variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter - assigning variables
total_votes = 0

# Step 1. Initialize candidate option and candiate votes: list and dictionary
candidate_options  = []
candidate_votes = {}

# County options and county votes
county_names = []
county_votes = {}

# Track the winning candidate (name), vote count and percentage
winning_candidate  = ""
winning_count = 0
winning_percentage =  0

# Challenges track the largest county voter turnout (name) and its percentage
largest_county_turnout = ""
largest_county_votes = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # print(reader)

    # Read the header
    header = next(reader)
    # print(header)

    # For each row in the csv file
    for row in reader:
        # Add to the total votes count
        total_votes = total_votes + 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # Get the county name from each row
        county_name = row[1]

        # If the candicte doesn't match any existing candidate add it into the the list
        if candidate_name not in candidate_options:
            # Adding the candicate name to the candiadte list
            candidate_options.append(candidate_name)
            # Add begin tracking that candidate voter count
            candidate_votes [candidate_name] = 0
        # Add a vote to that candidate count
        candidate_votes[candidate_name] += 1

        if county_name not in county_names:
            
            # Add it to the  list if in the running
            county_names.append(county_name)

            # Tracking that candidate voter count
            county_votes[county_name] = 0
        county_votes[county_name] += 1

# Save the results to text file
with open(file_to_save, "w")as txt_file:
    # Print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"\n-------------------\n"
        f"Total Votes: {total_votes:,}"
        f"\n--------------------\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    # Save the final county votes count to the text file
    for county in county_votes:
        # Retrieve vote count and percentage
        county_vote = county_votes[county]
        county_percent = int(county_vote) / int(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
        )  
        print(county_results, end="")
        txt_file.write(county_results)

        # Determine winning votes and candidate
        if(county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county
    # Print the county with the largest turnout
    largest_county_turnout = (
        f"\n-----------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------------\n"
    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    for candidate in candidate_votes:
        # Retrieve vote count and percentages
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,}\n"
        )

        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage and candidate
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)