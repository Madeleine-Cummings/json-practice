#!/usr/bin/python3

import json
import csv
import requests

url = 'https://raw.githubusercontent.com/uvasds-systems/DS2022/main/labs/data/schacon.repos.json'

response = requests.get(url)
data = response.json()

with open('chacon.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    count = 0
    for d in data:
        count = count + 1
        writer.writerow([d['name'], d['html_url'], d['updated_at'], d['visibility']])
        if count == 5:
            break

