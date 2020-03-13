import demjson
import json
import requests
from bs4 import BeautifulSoup
import time
import csv
import sys

f = open("q_links.txt","r")
f1= open("answers.csv","w")
wr = csv.writer(f1)

start_time = time.time()

headers = {
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.quora.com/',
    'authority': 'www.quora.com'
}

wr.writerow(['index', 'url', 'ans_text'])

for i, url in enumerate(f):
   s=""
   sys.stdout.write("-.....Adding %sth answer in CSV.\r" % (i+1))
   b=requests.get(url, headers=headers)
   soup = BeautifulSoup(b.text, "html.parser").find_all("script")[9]

   line = next(line[line.find('{'):] for line in soup.text.splitlines() if '.results' in line).strip(';')
   d= demjson.decode(line)
   j = json.loads(list(d.values())[0])
   sections = json.loads(j['data']['answer']['content'])['sections']

   for section in sections:
      s+=section['spans'][0]['text']
   wr.writerow([i, url, s])

print(f"Added {i+1} answers in {time.time() - start_time} seconds ---")