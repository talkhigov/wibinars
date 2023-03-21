import pprint

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    content = ((i.split()[0], i.split()[5][1:], i.split()[6]) for i in file)
    pprint.pprint(list(content))