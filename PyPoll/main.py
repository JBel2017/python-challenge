import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
#initialize variables
voter_id = []
candidates =[]
khan = 0
Li = 0
Otooley = 0
Correy = 0
x = 0
#open and read in file
with open(csvpath) as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    #count number of votes
    for x in csvreader:
        voter_id.append(x[0])
        num_votes = str(len(voter_id))
        candidates.append(x[2])
   #count candidate votes
    khan = candidates.count("Khan")
    Li = candidates.count("Li")
    Otooley = candidates.count("O'Tooley")
    Correy = candidates.count("Correy")
#perform calculations
    k = (khan/len(voter_id) )*100
    k2 = round(k,3)
    l= (Li/len(voter_id) )*100
    l2 = round(l,3)
    o = (Otooley/len(voter_id) )*100
    o2= round(o,3)
    c = (Correy/len(voter_id) )*100
    c2 = round(c,3)
    #Print output
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {num_votes}')
    print("-----------------------")
    print("Khan: " + str(k2) + "%   ("   + str(khan) + ")")
    print("Correy: " + str(c2) + "%   ("   + str(Correy) + ")")
    print("Li: " + str(l2) + "%   ("   + str(Li) + ")")
    print("O'tooley: " + str(o2) + "%   ("   + str(Otooley) + ")")