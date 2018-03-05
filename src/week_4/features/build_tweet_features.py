from statistics import mean
from week_4.tweet.tweet import *
from collections import Counter
from re import split


def calculate_average_tweets_per_day(tweet_set):
    """
    Calculated the average number of tweets per day.
    Args:
        tweet_set: Set of week_3.tweet objects.

    Returns:
        Float value, corresponding to the average number of tweets.
    """
    # Calculate difference in days between maximum date and minimum date.
    min_date = min([tweet.created_at for tweet in tweet_set])
    max_date = max([tweet.created_at for tweet in tweet_set])
    delta_date = (max_date - min_date).days
    # Return average number of tweets per day.
    return len(tweet_set) / delta_date


def calculate_average_word_count(tweet_set):
    """"
    Calculates average number of words in set of tweets.

    Args:
        tweet_set: A set of tweets.
    Returns:
        The average number of words per week_3.tweet (float).
    """
    return mean([tweet.count_number_of_words() for tweet in tweet_set])


def calculate_average_popularity(tweet_set):
    """
    Calculates average popularity of week_3.tweet set.

    Args:
        tweet_set: A set of week_3.tweet objects.
    Returns:
        A float corresponding to the average popularity.
    """
    return mean([tweet.calculate_popularity() for tweet in tweet_set])


def get_most_popular_tweets(tweet_set, most_popular=10):
    """
    Retrieves most popular tweets from week_3.tweet set.
    Args:
        tweet_set: Set of week_3.tweet objects.
        most_popular: Number of tweets to be retrieved, default is 10.

    Returns:
        A list of week_3.tweet objects.
    """
    # Sort tweets based on popularity
    sorted_tweets = sorted(tweet_set, key=Tweet.calculate_popularity)
    # Return most popular tweets
    return sorted_tweets[-most_popular:]


def get_top_mentions(tweet_set, top_mentions=10):
    """
    Returns the top mentions (@...) and the count from the week_3.tweet set.

    Args:
        tweet_set: A set of week_3.tweet objects.
        top_mentions: Maximum number of mentions to return (default: 10)

    Returns:
        A list of tuples.
    """
    mentions = list()
    for tweet in tweet_set:
        text_cleaned = tweet.text.lower()
        for word in text_cleaned.split():
            # Removes attached characters from word.
            word_cleaned = split('[:.,!?()]', word)[0]
            if '@' in word_cleaned:
                mentions.append(word_cleaned)
    mentions_count = Counter(mentions)
    return mentions_count.most_common(top_mentions)

