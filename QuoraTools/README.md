# QuoraTools
Some python scripts to play with Quora. I created them because I needed some text to experiment with Word2Vec. This is only for educational and research kind of purpose and here are three scripts that I created to get answers from Quora.

 - **get_answer_url.py**: This script takes URL of a question and get links of all the answers posted under it. It saves those permalinks of answers in a text file "`q_links.txt`" which it creates in the same working directory.
 - **get_answer_text.py**: This script reads the "`q_links.txt`" file created by the earlier script. It goes through all the answer links that it finds in the file and retrieves the answer text. It saves all the retrieved answers as text in a CSV file, "`answers.csv`".
 - **api.py**: This is a simple microservice that you can run locally or simply put it on a PaaS product like Heroku. It returns the answer data as a JSON response whose URL you supply as a URL parameter. The syntax for making a call is: `curl http://127.0.0.1:5000/ans/?url=AnswerURL`.
 

## Dependencies:
To use all these scripts, you need to have following dependencies setup along with Python3. Install them via `pip install` or `conda install` if you are using Anaconda distribution.
 - **BeautifulSoup**
 - **Demjson**
 - **Selenium**
 - **Flask**
