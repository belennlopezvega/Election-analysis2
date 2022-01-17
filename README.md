# Election Analysis

## Overview of Election Audit

The purpose of this election audit analysis is to present the following information to the election commission: the voter turnout for each county, the percentage of votes from each county out of the total, and the county with the highest turnout. Below are the results along with an overview of the methods used to obtain the results, and how they can be used for future elections. 

## Election Audit Results

The following bullet points show and overview of the election audit results.

* There were a total of 369,711 votes cast in this congressional election.
* Below is a breakdown of thenumber of votes and the percentage of total votes each county had in the precinct:
  * Jefferson County - 38,855 votes which amounts to 10.5% of the total votes in the precinct. 
  * Denver County - 306,055 votes which amounts to 82.8% of the total votes in the precinct. 
  * Jefferson County - 24,801 votes which amounts to 6.7% of the total votes in the precinct. 
* Denver County had the largest number of votes. 
* Below is a breakdown of the number of votes followed by the percentage of total votes each candidate received: 
  * Charles Casper Stockham - 85,213 number of votes, 23.0% of total votes.
  * Diana DeGette - 272,892 number of votes, 73.8% of total votes.
  * Raymon Anthony Doane - 11,606 number of votes, 3.1% of total votes.
* The winner of the election is Diana DeGette with an strong 272,892 number of votes which totaled to 73.8% of the total votes.

## Election Audit Summary

The script written for this analysis can be useful for future elections and use as it's easy to read and variables are adequately assigned with the absence of magic numbers. In the below picture, variables were assigned for things we kept track of for this election. For this election counties, candidates and votes were tracked and it's likely that those same things will be tracked for coming elections. If there's another category to be kept track of for the future, such as the lowest county turnout, then that's an easy variable to add. Much like the the `largest_county_votes = 0` you would instead use `lowest_county_votes = 0` along with `largest_county_turnout =""`, and add a for loop similar to the Largest County Turnout code later on in the code. 

![This is an image](https://github.com/belennlopezvega/Election-analysis2/blob/main/Assigning%20variables.png)

The script is also user-friendly when it comes to the actual code tracking the above stated variables. The picture below is the portion of the script used to track the winning candidate. As seen, there are no actual names of candidates. We used a for loop to track individual candidates, their votes and percentages. Then used an if statement and logical operator to get the name of the individual with the most votes and finally printed the results using f-strings. For future use, there would be almost no need to change the code if the intent is to track the winning candidate and their votes and percentages. 

![This is an image](https://github.com/belennlopezvega/Election-analysis2/blob/main/Candidate%20for%20loop%20and%20result%20code.png)

Overall, this code can be helpful and save a lot of time for any future election as it's easy for anyone else to read per the pseudocode, and can be easily adjusted if there are other categories to track or remove. 
