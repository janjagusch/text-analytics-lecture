from json import loads
from os.path import join, dirname
from os import pardir
from week_4.tweet.tweet import create_tweet_from_dict


def make_tweet_set(filename):
    """
    Creates set of tweets from data/raw/trump_tweets.json.
    Returns:
        Set of tweet objects.
    """

    # Create relative file path to raw file.
    file_path = join(dirname(__file__), pardir, pardir, pardir, "data", "raw", filename)

    # Open connection and read .json file.
    with open(file_path, encoding="utf8") as f:
        tweet_dict_list = loads(f.read())

    # Create set and tweet objects.
    tweet_set = set()
    for tweet_dict in tweet_dict_list:
        tweet = create_tweet_from_dict(tweet_dict)
        tweet_set.add(tweet)

    return tweet_set


def _get_data_path(sub_path):
    file_path = join(dirname(__file__), pardir, pardir, pardir, "data", sub_path)
    return file_path


def load_big_txt():
    file_path = _get_data_path('raw/big.txt')
    return open(file_path).read()




