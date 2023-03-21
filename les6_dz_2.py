from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    my_dict = Counter()
    for i in file:
       my_dict[i.split()[0]] +=1

    ip, count = my_dict.most_common(1)[0][0], my_dict.most_common(1)[0][1]
    print(f'Spammer: {ip}\nCount: {count}')