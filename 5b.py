import re

pattern = re.compile(r'(\+\d{12}|[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,})')

with open('example.txt', 'r') as f:
    text = f.read()   
    matches = pattern.findall(text)
    for match in matches:
        print(match)
