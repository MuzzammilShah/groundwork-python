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

    # portfolio = {}
    portfolio = []

    with open(filename, 'rt') as f:

        rows = csv.reader(f)
        headers = next(rows)
        # for i, row in enumerate(rows):
        #     portfolio[i] = {
        #         'name': row[0],
        #         'shares': row[1],
        #         'price': row[2]
        #     }
        # for row in rows:
        #     portfolio[row[0]] = {
        #         'shares': int(row[1]),
        #         'price': float(row[2])
        #     }
        # for row in rows:
        #     stock = {
        #         'name': row[0],
        #         'shares': int(row[1]),
        #         'prices': float(row[2])
        #     }
        #     portfolio.append(stock)
        for row in rows:
            stock = (
                row[0],
                int(row[1]),
                float(row[2])
            )
            portfolio.append(stock)

    return portfolio

def main():
    listp = portfolio_dict('Data/portfolio.csv')
    # print(listp)
    headers = ('Name', 'Shares', 'Price')
    print('%10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in listp:
        # print('%10s %10d %10.2f %10.2f' % row)
        print(f'{row[0]:>10s} {row[1]:10d} ${row[2]:>10.2f}')

if __name__ == '__main__':
    main ()