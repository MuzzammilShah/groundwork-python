# bounce.py
#
# Exercise 1.5

height = 100
bounce_height = 0.6
max_bounces = 10

for i in range(max_bounces):

    new_height = height * bounce_height
    print(round(new_height))

    height = new_height
    i += 1