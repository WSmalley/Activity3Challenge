import os
import csv

votescount = 0
c1 = 0
d1 = 0
a1 = 0



csv_path = os.path.join("/Users/willsmalley/Downloads/Starter_Code/PyPoll/Resources/election_data.csv")

with open(csv_path, 'r') as csvfile:
    csvreader =csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        votes = row[0]
        candidates = row[2]
        votescount += 1

        if candidates == "Charles Casper Stockham":
            c1 += 1
            percentcharles = (int(c1)/int(369711))*100

        if candidates == "Diana DeGette":
            d1 += 1
            percentdiana = (int(d1)/int(369711))*100

        if candidates == "Raymon Anthony Doane":
            a1 += 1
            percentantman = (int(a1)/int(369711))*100

    if percentdiana > (percentantman and percentcharles):
        print("Winner = Diana DeGette")
    if percentcharles > (percentantman and percentdiana):
        print("Winner = Charles Casper Stockham")
    if percentantman > (percentdiana and percentcharles):
        print("Winner = Raymon Anthony the ANTMAN Doane")


print(f'total votes: {votescount}')
print(f'Percent for Charles Casper Stockham:{percentcharles}% ({c1})')
print(f'Percent for Diana Degetee:{percentdiana}% ({d1})')
print(f'Percent for Raymon Anthony Doane:{percentantman}% ({a1})')

