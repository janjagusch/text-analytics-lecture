from json import loads
from os.path import join, exists
from os import makedirs
from week_4.tweet.tweet import create_tweet_from_dict
from utils.utils import get_data_path
from pickle import dump


def make_tweet_set():
    """
    Creates set of tweets from data/01_raw/trump_tweets.json.
    Returns:
        Set of tweet objects.
    """

    # Create relative file path to 01_raw file.
    file_path = get_data_path('01_raw/trump_tweets.json')
    # Open connection and read .json file.
    with open(file_path, encoding="utf8") as f:
        tweet_dict_list = loads(f.read())
    # Create set and tweet objects.
    tweet_set = set()
    for tweet_dict in tweet_dict_list:
        tweet = create_tweet_from_dict(tweet_dict)
        tweet_set.add(tweet)
    # Return tweet set.
    return tweet_set


def write_tweets_cleaned(tweets_cleaned):
    """Writes cleaned tweet set into datasets/processed/trump_tweets.pkl."""

    # Get file path to 02_cleaned.
    file_path_ext = get_data_path('02_cleaned')
    # If file path does not exist, create file path.
    if not exists(file_path_ext):
        makedirs(file_path_ext)
    # Write file into file path.
    with open(join(file_path_ext, 'trump_tweets.pkl'), 'wb') as f:
        dump(tweets_cleaned, f)
