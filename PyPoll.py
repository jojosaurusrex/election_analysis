#data we need to retrieve
#Total number of votes cast
    #count the number of rows minus the header
#A complete list of candidates who received votes
    #Fund all candidate options
        #identify all the different options
    #form a list with the info above
#Total number of votes each candidate received
    #add up all of the votes for each canidate
#Percentage of votes each candidate won
    #count of votes for canidateA,B,C / total votes *100
#The winner of the election based on popular vote

#add our dependencies
import os
import csv
#from turtle import clear

#declaring the csv file and since this script is in the same folder they are considered on the same level so no path directory needed
#Example of path directory: Resources\election_results.csv This means it is down a level
#Another example if it was up two level and in a different folder: ..\..\classfolder

#file_to_load = 'election_results.csv'
#^ used when opening and closing csv and the with open function

#open the selection results and read the file
#election_data = open(file_to_load,'r')

#with open function allows you to not have to close the file at the end of your code
#with open(file_to_load,'r') as election_data: #'r' is needed when using open/close & with open
 #   print(election_data)

#Straight from 3.4.2
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("test","election_analysis","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("test","election_analysis","analysis","election_analysis.txt")

#intiialize total vote counter
total_votes = 0 #why place it here
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 24

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:

        candidate_name = row[2]
        total_votes += 1

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0 
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


    # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes) / float(total_votes))*100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(candidate_results)
        
         #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")

    print(winning_candidate_summary)

    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary) 


    

#Output was suppose to be: <open file 'Resources/election_results.csv', mode 'r' at 0x10479c780>
#Output I have at this step: <_io.TextIOWrapper name='election_results.csv' mode='r' encoding='cp1252'>
# Not sure why, maybe cuz mine isn't in a folder idk

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis","election_analysis.txt") #this is an example to make sure it was working

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World") #used when outfile is a varaible that is using the open function

#Example 3.4.2/3
#
# Unsure if i needed file_to load w/in this ex. I know i needed the imports tho
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis","election_analysis.txt") #this is an example to make sure it was working
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
#    txt_file.write("Counties in the Election \n")
#    txt_file.write("--------------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")
#
# End of Ex. 3.4.2/3




# Close the file
#outfile.close()

#close File
#election_data.close()

# Using panda instead of for loops look for other options