
# open the data file 

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)
    
    #for row in file_reader: 
     #   print(row)


# write down the names of the candidates 

# add a vote count for each candidate 

# get the total votes for each candidate 

# get the total votes cast for the election 