import csv

with open('budget_data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
    
    totmonths = len(data)-1
    pnl=0
    avgpnl=0
    for i in range(len(data)-1):
        pnl+= int(data[i+1][1])
    for i in range(len(data)-2):
        avgpnl += (int(data[i+2][1])-int(data[i+1][1]))
        avgpnlf=avgpnl/(len(data)-2)
    min = int(data[1][1])
    max = int(data[1][1])
    for i in range(len(data)-2):
        if int(data[i+2][1]) < min : 
            min = int(data[i+2][1])
            datemin = data[i+2][0]
        elif int(data[i+2][1]) > max : 
            max = int(data[i+2][1])
            datemax = data[i+2][0]
        
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totmonths}")
print(f"Total: {'${:,.2f}'.format(pnl)}")
print(f"Average Change: {'${:,.2f}'.format(avgpnlf)}")
print(f"Greatest Increase in Profits: {datemax} ({'${:,.2f}'.format(max)})")
print(f"Greatest Decrease in Profits: {datemin} ({'${:,.2f}'.format(min)})")

