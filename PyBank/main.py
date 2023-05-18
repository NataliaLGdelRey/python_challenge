# PyBank Python Assignment

# Dependencies
import os
import csv 

# Files to load
file = os.path.join('..', 'Resources', 'budget_data.csv')

# Read the cvs and create a list
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    # Lists to store data
    month_count = []
    profit = []
    change_profit = []
    
                      
    # Look through the values and add them to the empty list 
    for row in csvreader:
        # The net total amount of "Profit/Losses" over the entire period
        month_count.append(row[0])

         # The changes in "Profit/Losses" over the entire period,
        profit.append(int(row[1]))
        
        # Average of those changes
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
# The greatest increase in profits (date and amount) over the entire period
increase = max(change_profit)

# The greatest decrease in profits (date and amount) over the entire period
decrease = min(change_profit)

#using the index, 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

# Output
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      

# Export the analysis to text file
output = os.path.join("..", "analysis", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")