from datetime import datetime


def _clean_tween_date_string(date_string):
    """
    Cleans week_3.tweet date string.
    Args:
        date_string: A week_3.tweet date string.

    Returns:
        A cleaned week_3.tweet date string in format
    """
    date_list = date_string.split()
    year = date_list[5]
    month = date_list[1]
    day = date_list[2]
    time = date_list[3]

    return year + " " + month + " " + day + " " + time


def convert_tweet_string_to_date(date_string):
    """
    Converts week_3.data in string format to date object:

    Args:
        date_string: Date in string format (e.g. 'Sat Dec 30 22:42:09 +0000 2017')

    Returns:
        Date object (e.g. '2017-12-30 22:42:09')
    """

    # Extract information from string
    date_string_formatted = _clean_tween_date_string(date_string)

    # Return datetime object
    return datetime.strptime(date_string_formatted, '%Y %b %d %H:%M:%S')


def convert_string_to_date(date_string):
    """
    Converts date string to date object.
    Args:
        date_string: A date string in format '%Y/%m/%d'

    Returns:
        A date object.
    Notes:
        Help on the datetime format: https://docs.python.org/2/library/time.html
    """
    return datetime.strptime(date_string, '%Y/%m/%d')
