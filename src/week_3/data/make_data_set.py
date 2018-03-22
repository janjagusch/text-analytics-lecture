from json import loads
from os.path import join
from week_3.tweet.tweet import create_tweet_from_dict
from utils.utils import get_data_path


def make_tweet_set(filename):
    """
    Creates set of tweets from week_3.data/raw/trump_tweets.json.
    Returns:
        Set of week_3.tweet objects.
    """

    # Create relative file path to raw file.
    file_path = get_data_path(join('raw', filename))

    # Open connection and read .json file.
    with open(file_path, encoding="utf8") as f:
        tweet_dict_list = loads(f.read())

    # Create set and week_3.tweet objects.
    tweet_set = set()
    for tweet_dict in tweet_dict_list:
        tweet = create_tweet_from_dict(tweet_dict)
        tweet_set.add(tweet)

    return tweet_set
