# Election Analysis with PyPoll

## Overview of Election Analysis
The purpose of this analysis was to analyze voting data to audit the results of a congressional election. Using python to churn through thousands of ballots, we are able to quickly confirm the outcome of the election as well as key supplimentary data like voter turnout by county, percentage share of votes per candidate.  

## Election-Audit Results 
[Link to the summary output of the PyPoll Program](https://github.com/matthewprice-github/election-analysis/blob/main/election_analysis.txt)
- Total number of votes cast in the congressional election: 369,711
- Voting Turnout by County: 
  - Jefferson County: 38,855 (10.5%) 
  - Denver County: 306,055 (82.8%) -- LARGEST TURNOUT 
  - Arapahoe County: 24,801 (6.7%) 
- Election Results by Candidate: 
  - Charles Casper Stockham: 85,213 (23.0%) 
  - Diana DeGette: 272,892 (72.8%) -- WINNER 
  - Raymon Anthony Doane 11,606 (3.1%) 


##  Election-Audit Summary 
The script used in this analysis is very versitile. There are only a few changes required to apply this program at a much higher scale. While this audit only had three counties and 3 candidates, if the dataset input contained a higher number of counties and/or candidates, the PyPoll program achieve the same analysis with no edits to main code (assuming the CSV input file has the same name!).

However, say we wanted to run this program for multiple different election seats. If the voter data had a column that indentified which seat the vote was cast for, we only need to make a few edits to the main body of the code to run this same analysis for ALL of those election seats. First we make an index list to differentiate which election seat the voting data pertains to. Then we run a FOR loop through the data outside of our other loops, adding new unique election seat values to our index list. Once we have our index list completed, we can run our analsis for each election listed in that index using our existing code, and create summaries for all of them. 
