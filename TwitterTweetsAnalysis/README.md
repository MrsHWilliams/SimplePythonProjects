Here is a simple experiment that I conducted while I was learning data science. I streamed live tweets from Twitter during Delhi elections and feed those tweets to a Word2Vec model and they showed some pretty good insights.
I downloaded around 100k tweets in Hindi and English Languages and created 
a model for tweets in both languages.

Here are the steps involved:

Step 1: Downloaded Tweets using Tweepy (*tweets.py*) file does that and saves those tweets in a CSV file.

Step 2: Import the downloaded CSV as a Pandas dataframe, clean the tweets (removing special characters, extra spaces, emojis, etc..) and save the cleaned tweets in a MySQL database. The file "*pandas to mysql.ipynb*" does that.

Step 3: Created 2 Word2Vec models for English and Hindi tweets. They are saved in "*word2vec-english-tweets.ipynb*" and "*word2vec-hindi-tweets.ipynb*" files.
