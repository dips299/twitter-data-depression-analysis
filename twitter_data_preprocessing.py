# -*- coding: utf-8 -*-

import json
import pandas as pd

import emoji

import re #regular expression
from textblob import TextBlob
import string
import preprocessor as p
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])

# Sad Emoticons
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])

#Emoji patterns
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
         "]+", flags=re.UNICODE)

#combine sad and happy emoticons
emoticons = emoticons_happy.union(emoticons_sad)

#mrhod clean_tweets()
def clean_tweets(tweet):
    
    #converting to lower case
    tweet = tweet.lower()

    #after tweepy preprocessing the colon left remain after removing mentions
    #or RT sign in the beginning of the tweet
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    #replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
    tweet = re.sub(r'[^a-zA-Z#]+',' ', tweet)
    
    #remove URLs
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    # remove the # in #hashtag
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet) 

    #remove emojis from tweet
    tweet = emoji_pattern.sub(r'', tweet)
    tweet = emoji.get_emoji_regexp().sub(u'', tweet)
    tweet = re.sub(emoji.get_emoji_regexp(), r"", tweet)

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)                       
    
    #filter using NLTK library append it to a string
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []   

    #looping through conditions
    for w in word_tokens:
        #check tokens against stop words , emoticons and punctuations
        if w not in stop_words and w not in string.punctuation or w in emoticons:
            filtered_tweet.append(w)
    
    return ' '.join(filtered_tweet)

ifile = open('Twitter_test_json.json', 'r')
tweet_list = []
all_data = []
i=0

for line in ifile:
    #print(line)
    i = i+1
    try:
        tweet = json.loads(line)
        tweet_list.append(tweet)
        
        t_id = tweet['id']
        t_lang = tweet['lang']
        t_text = tweet['text']
        t_user_id = tweet['user']['id']
        retweeted_status = tweet['retweeted_status']
        
        
        clean_text = p.clean(tweet['text'])

        #call clean_tweet method for extra preprocessing
        filtered_tweet=clean_tweets(clean_text)          
  
        #pass textBlob method for sentiment calculations
        blob = TextBlob(filtered_tweet)
        sentiments = blob.sentiment

        #seperate polarity and subjectivity in to two variables
        polarity = sentiments.polarity
        subjectivity = sentiments.subjectivity
        
        #using vader Analyser
        sentiment_analyser = analyser.polarity_scores(filtered_tweet)
        compound_score = sentiment_analyser['compound']
        
        if (sentiment_analyser['compound'] <= -0.05):
            compound_score_sentiment = 'Negative'    
            label = '1'
        if (sentiment_analyser['compound'] >= 0.05):
            compound_score_sentiment = 'Positive'
            label = '0'
        if ((sentiment_analyser['compound'] > -0.05) & (sentiment_analyser['compound'] < 0.05)):
            compound_score_sentiment = 'Neutral'
            label = ' '
        
        
        mentions = ", ".join([mention['screen_name'] for mention in tweet['entities']['user_mentions']]) 
        t_hashtags = ", ".join([hashtag_item['text'] for hashtag_item in tweet['entities']['hashtags']])
        
        if(t_lang == 'en'):
            all_data.append([t_id, t_lang, t_user_id, retweeted_status, mentions, t_hashtags, t_text, filtered_tweet, sentiments, polarity, subjectivity, sentiment_analyser, compound_score, compound_score_sentiment, label])

    except:
        continue


df = pd.DataFrame(all_data, columns=['Id','Language','User Id', 'Retweet Status', 'Mentions','Hashtags', 'Text', 'Filtered Text', 'Sentiment', 'Polarity', 'Subjectivity', 'Sentiment Analyser', 'Compound Score', 'Compound Score Sentiment', 'Label'])
df.to_csv('Twitter Data New.csv')



