import re

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')


with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    logs = file.read()
    remote_addr = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\ ', logs)
    request_datetime = re.findall('\d{2}/\w{1,3}/2015[:0-9]+\s\+0000', logs)
    request_type = re.findall('GET', logs)
    requested_resource = re.findall('/downloads/\w+', logs)
    response_code = re.findall('\ \d{3}\ ', logs)
    response_size = re.findall('\ \d+\ "', logs)
        

# print(re.findall('^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', raw))
# print(re.findall('\d{2}/\w{1,3}/2015[:0-9]+\s\+0000', raw))
# print(re.findall('/downloads/\w+', raw))
# print(re.finditer('GET', raw))
# print(re.findall('\ \d{3}\ ', raw))
# x = re.findall('\ \d+\ "', raw)
# x = str(x).strip("[]'").strip().strip('"')
# print(x)
