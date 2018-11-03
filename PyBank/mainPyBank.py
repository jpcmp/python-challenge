import csv

with open('budget_data.csv', newline='') as csvfile:
    csvfile.readline()
    data = list(csv.reader(csvfile))
    totmonths = len(data)
    pnl=0
    avgpnl=0
    for i in range(len(data)):
        pnl+= int(data[i][1])
    for i in range(len(data)-1):
        avgpnl += (int(data[i+1][1])-int(data[i][1]))
        avgpnlf=avgpnl/(len(data)-1)
    vmin = int(data[1][1])
    vmax = int(data[1][1])
    for i in range(len(data)-1):
        if int(data[i+1][1]) < vmin : 
            vmin = int(data[i+1][1])
            datemin = data[i+1][0]
        elif int(data[i+1][1]) > vmax : 
            vmax = int(data[i+1][1])
            datemax = data[i+1][0]
        
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totmonths}")
print(f"Total: {'${:,.2f}'.format(pnl)}")
print(f"Average Change: {'${:,.2f}'.format(avgpnlf)}")
print(f"Greatest Increase in Profits: {datemax} ({'${:,.2f}'.format(vmax)})")
print(f"Greatest Decrease in Profits: {datemin} ({'${:,.2f}'.format(vmin)})")

with open("Analysis_Results.csv", "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Total Months:", totmonths])
    writer.writerow(["Total:", pnl])
    writer.writerow(["Average Change:", avgpnlf])
    writer.writerow(["Greatest Increase in Profits:", datemax, vmax])
    writer.writerow(["Greatest Decrease in Profits:", datemin, vmin])