import re

def email_parse(email_address):
    if re.findall('\.ru$', email_address) == [] or re.findall('\\b@', email_address) == []:
        print(ValueError)
        print('Адрес не валиден')
    else:
        user_name = re.findall('^\w+', email_address)
        user_name = str(user_name).strip("[]'")
        domain = re.findall('\w{1,}.ru$', email_address)
        domain = str(domain).strip("[]'")
        print({'user_name': user_name, 'domain': domain})


email_parse('ilman@mail.ru')
email_parse('ilmanmail.ru')
email_parse('ilman@mailru')
