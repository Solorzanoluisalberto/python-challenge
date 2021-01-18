# main PyPoll file
import csv
from numpy import mean
import statistics
Votes_cast = []
County = []
Candidate = []
Votes_x_candidates = []
Unique_Candidate = []
Election_results = []

def Count_Candidate_votes(Candidatos): #Function that counts the votes for each Candidate
    #print(candidatos)
    Vote_count = 0
    for indice in range(0, len(Candidate)):
        if Candidatos == Candidate[indice]:
            Vote_count = Vote_count + 1
        #print(candidatod + " funcion")
    Percent_votes = "{:.3%}".format(Vote_count / len(Votes_cast)) # ("${:}".format((Vote_count / len(Votes_cast))*100)
    Cadena = Candidatos + ':  ' + str(Percent_votes) + ' (' + str(Vote_count) +')'
    Votes_x_candidates[Unique_Candidate.index(Candidatos)] = Vote_count
    #print(Votes_x_candidates)
    #print(Unique_Candidate)
    return(Cadena)

def Results_Screen_output(Election_results, Winner_Name, Total_Votes): #== function that prints data on screen
    #winner_index = Votes_x_candidates.index(max(Votes_x_candidates))
    #Winner_Name = Unique_Candidate[winner_index]
    #Winner_total_votes = Votes_x_candidates[winner_index]
    #Total_Votes = len(Votes_cast)
    print("Election Results")
    print("-------------------------")
    print("Total Votes:  " + str(Total_Votes))
    print("-------------------------")
    for f  in range(0, len(Election_results)):
        print(Election_results[f])
    print("-------------------------")
    print("Winner:  " + Winner_Name )
    print("-------------------------")

def Results_txt_output(Election_results, Winner_Name, Total_Votes):
    PyPoll_txt = open("Analysis/PyPoll_Results.txt","w")  # I create file to write the following content
    PyPoll_txt.write("Election Results \n")
    PyPoll_txt.write("-------------------------\n")
    PyPoll_txt.write("Total Votes:  " + str(Total_Votes) + " \n")
    PyPoll_txt.write("-------------------------\n")
    for f  in range(0, len(Election_results)):
        PyPoll_txt.write(Election_results[f] + " \n")
    PyPoll_txt.write("-------------------------\n")
    PyPoll_txt.write("Winner:  " + Winner_Name + " \n")
    PyPoll_txt.write("-------------------------\n")

#Vote_count = 0
# main program open file and operate
with open('Resources/election_data1.csv') as file:
    data_reader = csv.DictReader(file, delimiter=',')
    for row in data_reader:
    # suma = suma + int(row['Profit/Losses'])
        Votes_cast.append(int(row['Voter ID'])) # assign value to a list
        County.append(row['County']) # assign value to a list
        Candidate.append(row['Candidate']) # assign value to a list

Unique_Candidate = list(set(Candidate)) # convert set in to a list of values
Votes_x_candidates = list(set(Candidate)) #list(set(Candidate))

for Aspirant in Unique_Candidate: # do for each Aspirant in a list Unique_Candidate
    #print(Aspirant)
    Result = Count_Candidate_votes(Aspirant)
    Election_results.append(Result)
    #print(res)
print(Votes_x_candidates)
#print(max(Votes_x_candidates))
Winner_index = Votes_x_candidates.index(max(Votes_x_candidates))
winner_Name = Unique_Candidate[Winner_index]
Total_Votes = len(Votes_cast)
print(winner_Name)
Results_Screen_output(Election_results, winner_Name, Total_Votes) # calling subroutine to print to screen
Results_txt_output(Election_results, winner_Name, Total_Votes) # calling subroutine to print to txt file


