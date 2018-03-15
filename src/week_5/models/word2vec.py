import multiprocessing
from gensim.models import Doc2Vec


def build_bow_model(tweet_set):
    """
    Compute Bag of Words (BOW) features.
    Args:
        tweet_set: Set of week_3.tweet objects.

    Returns:
        Doc2Vec model build with bag of words vocabulary.
    """
    # Count the number of available cores (useful for distributed computing)
    cores = multiprocessing.cpu_count()

    dbow = Doc2Vec(dm=0, size=100, negative=5, min_count=2, workers=cores, alpha=0.065, min_alpha=0.065)
    dbow.build_vocab([x for x in [tweet.text_raw for tweet in tweet_set]])

    return dbow