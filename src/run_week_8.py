from week_7.data.io import load_tweets
from utils.utils import get_data_path
import os.path
import pickle

tweets = load_tweets()

# Merge sentence lists.
for tweet in tweets:
    text_concat = list()
    if tweet.text_cleaned is not None:
        for sentence in tweet.text_cleaned:
            text_concat.extend(sentence)
        tweet.text_cleaned = text_concat

russia_tweets = [t for t in tweets if t.text_cleaned is not None and 'russia' in t.text_cleaned and len(t.text_cleaned) > 10]
china_tweets = [t for t in tweets if t.text_cleaned is not None and 'china' in t.text_cleaned and len(t.text_cleaned) > 10]
mexico_tweets = [t for t in tweets if t.text_cleaned is not None and 'mexico' in t.text_cleaned and len(t.text_cleaned) > 10]

country_tweets = russia_tweets + china_tweets + mexico_tweets

file_path = os.path.join(os.path.dirname(__file__), os.path.pardir, 'notebooks', 'week_8')
file_name = 'country_tweets.pkl'

with open(os.path.join(file_path, file_name), 'wb') as f:
    pickle.dump(country_tweets, f)
