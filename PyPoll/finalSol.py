import os
import csv
total_vote = 0
candidate_Dict = {}

percentageCount_Dict = {}

file_to_output = "PyPollResults.txt"
with open('../Resources/election_data.csv', 'r') as csv_file: # if we use with open , then file will automatically close after performing the work
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        #print(row)
        total_vote = total_vote + 1
        candidate = row[2]
        # dictionary Work
        if candidate in candidate_Dict:
            candidate_Dict[candidate] = candidate_Dict[candidate] + 1
        else:
            candidate_Dict[candidate] = 1
            
        # calculate percentage step.
        # how can we iterate the dictionary elements.
        
            #print(f"{}: {}%    ({})",key,value,candidate_Dict[key]) #syntax for printing.
            
   


   
    
    #print("winner : {}".format(winner))
    
with open(file_to_output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_vote}\n"
        f"-------------------------\n")
    print(election_results)
    txt_file.write(election_results)
    
    winner  = "" 
    maximumValue = -1
    for key,value in candidate_Dict.items():
        if value > maximumValue:
            winner = key
            maximumValue = value
        percentageCount_Dict[key] = candidate_Dict[key]/total_vote * 100
     # travers the percentageCount_Dict
    
    for key,value in percentageCount_Dict.items():
#         print("{} {:.3f}% {}".format(key,value,candidate_Dict[key]))  
        voter_output = f"{key}: {value:.3f}% ({candidate_Dict[key]})\n"
        print(voter_output)
        txt_file.write(election_results)
        
    print(f"winner : {winner}")   
    txt_file.write(f"winner : {winner}")
    
    
