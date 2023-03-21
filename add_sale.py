import sys

command = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as file:
    sum = command
    file.write(sum + '\n')