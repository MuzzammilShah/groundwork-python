# pcost.py
#
# Exercise 1.27

# def total():
#     totalcost = 0.0

#     with open('Data/portfolio.csv', 'rt') as f:
#         headers = next(f).split(',')
#         for line in f:
#             row = line.split(',')
#             nshares = int(row[1])
#             price = float(row[2])
#             totalcost += nshares * price

#     return(totalcost)

# tc = total()
# print('Total cost= ', tc)

# Exercise 1.32

import csv

def total():

    totalcost = 0.0
    f = open('Data/portfolio.csv')
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        nshares = int(row[1])
        price = float(row[2])
        totalcost += nshares * price

    return totalcost

tc = total()
print('Total cost= ', tc)