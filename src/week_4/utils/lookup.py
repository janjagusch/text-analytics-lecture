def get_tweet_by_tweet_id(tweet_set, tweet_id):
    """
    Retrieves tweet, based on unique tweet id.
    Args:
        tweet_set: A set of tweets.
        tweet_id: A unique tweet id.

    Returns:
        A tweet with the defined tweet id.
    """
    for tweet in tweet_set:
        if tweet.tweet_id == tweet_id:
            return tweet
