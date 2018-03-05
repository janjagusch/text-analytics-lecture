from re import search
from week_4.utils.convert import convert_string_to_date


def filter_by_term(tweet_set, term):
    """
    Filters week_3.tweet set by search term.

    Args:
        tweet_set: Set of week_3.tweet objects.
        term: String, describing search term.

    Returns:
        Filtered set of week_3.tweet objects.
    """
    return [tweet for tweet in tweet_set if search(term.lower(), tweet.text.lower())]


def filter_by_date(tweet_set, start_date, end_date):
    """
    Filters week_3.tweet set by start and end date
    Args:
        tweet_set: Set of week_3.tweet objects.
        start_date: Minimum created_at date
        end_date: Maximum created_at date

    Returns:
        Filtered set of week_3.tweet objects.
    """
    return [tweet for tweet in tweet_set if _is_tweet_in_date_range(tweet,
                                                                    convert_string_to_date(start_date),
                                                                    convert_string_to_date(end_date))]


def _is_tweet_in_date_range(tweet, start_date, end_date):
    """
    Checks if week_3.tweet is contained in date range.
    Args:
        tweet: A week_3.tweet object.
        start_date: Minimum created_at date (format: '%Y/%m/%d')
        end_date: Maximum created_at date. (format: '%Y/%m/%d')
    Returns:
        A boolean, corresponding to whether the week_3.tweet in contained in the date range.
    Notes:
        Help on the datetime format: https://docs.python.org/2/library/time.html
    """
    return start_date <= tweet.created_at <= end_date
