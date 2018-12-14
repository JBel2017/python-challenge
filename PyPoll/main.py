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
    file_to_output = os.path.join("analysis", "election_data.txt")
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
    k2 = str(round(k,4))
    k3=str(khan)
    l= (Li/len(voter_id) )*100
    l2 = str(round(l,4))
    l3= str(Li)
    o = (Otooley/len(voter_id) )*100
    o2= str(round(o,4))
    o3 = str(Otooley)
    c = (Correy/len(voter_id) )*100
    c2 = str(round(c,4))
    c3 = str(Correy)
    #find the winner
    winner = []
    winner = [k, l, o, c]
    
    win= max(winner)
    if win == winner[0]:
        w = "Khan"
    elif win == winner[1]:
        w = "Li"
    elif win == winner[2]:
        w = "O'Tooley"
    else:
        w = "Correy"
    
    output ={}
    
    output ={'Election Results',
            
    'Total Votes: ' + num_votes,
             
    'Khan: ' + k3 + '% ' + k3,
    'Correy: '+ c2 + '% ' + c3,
    'Li: ' + l2 + '% '+ l3,
    'OTooley: ' + o2 + '% ' + o3}
    
    with open(file_to_output, "w") as txt_file:
       txt_file.write(str(output))
       
    #Print output
    print("Election Results")
    print("-----------------------")
    print(f'Total Votes: {num_votes}')
    print("-----------------------")
    print(f'Khan: {k2} % ({k3}) ')
    print(f'Correy: {c2} % ({c3}) ')
    print(f'Li: {l2} % ({l3}) ')
    print(f'OTooley: {o2} % ({o3}) ')
    print("-----------------------")
    print(f'Winner: {w}')
    