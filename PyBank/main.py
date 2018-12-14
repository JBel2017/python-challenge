import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
line =[]
profit_list = []
month_list = []
with open(csvpath) as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',')
    file_to_output = os.path.join("analysis", "budget_analysis.txt")
    
    next(csvreader)
       #count number of rows
    #sum_count = sum(1 for row in csvreader)
    #calculated number of months and summed the totals
      
    for row in csvreader:
       
          
          profit_list.append(int(row[1]))
          month_list.append(row[0])
          sum_total = sum(profit_list)
          row_count = len(profit_list)
          total = str(sum_total)
          #row_count = len(list(csvreader))
    #print(new_list)
       #print (sum(new_list))
    
    #calculated Average change             
    n=0
    i=0
    loss= []
    num = 0
    for x in range(len(profit_list)-1):
      
        loss.append(profit_list[n+1] - profit_list[n])
        n = n + 1
   
    average_change = round(((sum(loss))/row_count),3)   
    
    #calculate greatest Increase in Profits
    
    max_val = max(profit_list)
    month_max_val = month_list[profit_list.index(max_val)]
    
    m= str(max_val)

    #calculate greates decrease in profits
    min_val = min(profit_list)
    month_min_val = month_list[profit_list.index(min_val)]
    row = str(row_count)
    a = str(average_change)
    #output_path = os.path.join("..", "output", "new.csv")             
    m2= str(min_val) 

    # Initialize csv.writer
    #csvwriter = csv.writer('new_file.csv', 'w'))

    # Write the first row (column headers)
   # csvwriter.writerow(["Financial Analysis"])

    # Write the second row
    #csvwriter.writerow(['-----------------------------'])
    #csvwriter.writerow(['Total Months: ' + str(row_count)])
    #csvwriter.writerow(['Total: $' + str(sum_total)])
    #csvwriter.writerow(['Average Change: ' + str(average_change)])  
    #csvwriter.writerow(['Greatest Increase in Profits: ' + str(month_max_val) + " " + str(max_val)])
    #csvwriter.writerow(['Greatest Decrease in Profits: ' + str(month_min_val) + " " + str(min_val)])
    output ={}
    
    output ={
    'Financial Analysis',
            
   'Total Months: '+ row ,
             
    'Total: $' + total,
    'Average Change: ' + a,
    'Greatest Increase in Profits: ' + month_max_val + m,
    'Greatest Decrease in Profits: ' + month_min_val + m2 }
    
    with open(file_to_output, "w") as txt_file:
        txt_file.write(str(output))
    print("Financial Analysis")
    print("-----------------------------")

    print(f'Total Months: {row_count}')
    print("Total: $" + str(sum_total))
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {month_max_val} {max_val}')
    print(f'Greatest Decrease in Profits: {month_min_val} {min_val}')
   
    