import json
import os
from tweet.tweet import create_tweet_from_dict


def make_tweet_set(filename):
    """
    Creates set of tweets from data/raw/trump_tweets.json.
    Returns:
        Set of tweet objects.
    """

    # Create relative file path to raw file.
    file_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "data", "raw", filename)

    # Open connection and read .json file.
    with open(file_path, encoding="utf8") as f:
        trump_dict_list = json.loads(f.read())

    # Create set and tweet objects.
    trump_tweet_set = set()
    for trump_dict in trump_dict_list:
        trump_tweet = create_tweet_from_dict(trump_dict)
        trump_tweet_set.add(trump_tweet)

    return trump_tweet_set
