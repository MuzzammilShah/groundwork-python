# pcost.py
#
# Exercise 1.27

totalcost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        totalcost += nshares * price

print('Total cost= ', totalcost)