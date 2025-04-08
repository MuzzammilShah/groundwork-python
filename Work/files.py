# files.py


# Exercise 1.26
# Uncomment these one by one to try them out

# with open('Data/portfolio.csv', 'rt') as f:
#     data = f.read()
#print(data)

# with open('Data/portfolio.csv', 'rt') as f:
#     for line in f:
#         print(line, end='')

# with open('Data/portfolio.csv', 'rt') as f:
#     headers = next(f)
#     for line in f:
#         print(line, end='')

# with open('Data/portfolio.csv', 'rt') as f:
#     headers = next(f).split(',')
#     print(headers)
#     for line in f:
#         row = line.split(',')
#         print(row)

# Exercise 1.28

# import gzip

# with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
#     for line in f:
#         print(line, end='')

# with gzip.open('Data/portfolio.csv.gz') as f:
#     for line in f:
#         print(line, end='')