#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import demjson
import json
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello welcome to the root of the Quora Answer Downloader API."

@app.route('/ans/', methods=['GET'])
def get_ans_text():
   
   if request.args.get('url') == None:
   
      return "Please make the request correctly"
   
   else:
             
      url = request.args.get('url') 
      headers = {
         'accept-encoding': 'gzip, deflate, br',
         'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
         'accept': '*/*',
         'referer': 'https://www.quora.com/',
                  }
      b=requests.get(url, headers=headers)
      soup = BeautifulSoup(b.text, "html.parser").find_all("script")[9]

      line = next(line[line.find('{'):] for line in soup.text.splitlines() if '.results' in line).strip(';')
      d = demjson.decode(line)
      j = json.loads(list(d.values())[0])
   
      return jsonify(json.loads(j['data']['answer']['content'])['sections'])
    
if __name__ == '__main__':
    app.run(debug=True)