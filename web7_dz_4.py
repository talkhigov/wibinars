import os

dir = 'lessons'
files = os.listdir(dir)
result = {}
j = 1
q = 1
x = 1
a = 1
for i in files:
    size = os.stat(f'{dir}/{i}').st_size
    if size < 100:
        result['100'] = q
        q+=1
    elif size > 100 and size < 1000:
        result['1000'] = j
        j+=1
    elif size > 1000 and size < 10000:
        result['10000'] = x
        x+=1
    elif size > 10000 and size < 1_000_00:
        result['100000'] = a
        a+=1

print(result)


