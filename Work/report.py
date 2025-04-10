# report.py
#
# Exercise 2.4

import csv

# def portfolio_list(filename):

#     portfolio = []

#     with open(filename, 'rt') as f:

#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             portfolio.append((row[0], int(row[1]), float(row[2])))

#     return portfolio

# def main():
#     listp = portfolio_list('Data/portfolio.csv')
#     for item in listp:
#         print(item)

# if __name__ == '__main__':
#     main ()

def portfolio_dict(filename):

    portfolio = {}

    with open(filename, 'rt') as f:

        rows = csv.reader(f)
        headers = next(rows)
        # for i, row in enumerate(rows):
        #     portfolio[i] = {
        #         'name': row[0],
        #         'shares': row[1],
        #         'price': row[2]
        #     }
        for row in rows:
            portfolio[row[0]] = {
                'shares': int(row[1]),
                'price': float(row[2])
            }

    return portfolio

def main():
    listp = portfolio_dict('Data/portfolio.csv')
    print(listp)

if __name__ == '__main__':
    main ()