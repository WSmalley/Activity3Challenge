
import os
import csv

#count months

monthscount = 0
plcount = 0


csv_path = os.path.join("/Users/willsmalley/Downloads/Starter_Code/PyBank/Resources/budget_data.csv")

with open(csv_path, 'r') as csvfile:
    csvreader =csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        months = row[0]
        profitloss = int(row[1])

        monthscount += 1            #month total
        plcount += int(row[1])      #p&l calculation

print(f'total months: {monthscount}')
print(f'profit&loss: {plcount}')


#Find monthly trends/average

total_changes = 0
monthchanges = 0
previous_profit_loss = None
maxchange = 0
minchange = 0

csv_path = os.path.join('/Users/willsmalley/Downloads/Starter_Code/PyBank/Resources/budget_data.csv')

with open(csv_path, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        profit_loss = int(row['Profit/Losses'])


        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            total_changes += change
            monthchanges += 1

##Find highest & lowest monthly totals
            if change > maxchange:
                maxchange = change
            if change < minchange:
                minchange = change

        previous_profit_loss = profit_loss

# Calculate the average change
if monthchanges > 0:
    average_change = total_changes / monthchanges


print(f"Total Change in Profit/Losses: {total_changes}")
print(f"Average Change in Profit/Losses: {average_change}")
print(f"Max Change in Profit/Losses: {maxchange} on {str(months)}")
print(f"Min Change in Profit/Losses: {minchange} on {str(months)}")


#Find highest & lowest monthly totals










