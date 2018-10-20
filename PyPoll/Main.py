import csv

import csv

total_vote = 0
candidate_Dict = {}

percentageCount_Dict = {}

#os.path.join('..', 'Resources', 'election_data.csv')
with open('election_data.csv', 'r') as csv_file: # if we use with open , then file will automatically close after performing the work
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
            
    print("total Votes {}".format(total_vote))
    winner  = "" 
    maximumValue = -1
    for key,value in candidate_Dict.items():
        if value > maximumValue:
            winner = key
            maximumValue = value
        percentageCount_Dict[key] = candidate_Dict[key]/total_vote * 100


    # travers the percentageCount_Dict
    for key,value in percentageCount_Dict.items():
        print("{} {:.3f}% {}".format(key,value,candidate_Dict[key]))  
    #print(f"winner : {}",winner)
    print("winner : {}".format(winner))