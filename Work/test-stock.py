import stock

# s = stock.Stock('GOOG', 100, 490.10)

# print(s.cost())
# print(s.shares)
# print(s.sell(25))
# print(s.shares)
# print(s.cost())

import fileparse

with open('Data/portfolio.csv') as lines:
    portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
print(portfolio)
print(sum([s.cost() for s in portfolio]))