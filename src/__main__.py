from data.make_data_set import make_tweet_set
from data.filter_data_set import *
from features.tweet_analyzer import *
from utils.format import *


def main():
    trump_tweet_set = make_tweet_set("trump_tweets.json")

    # Print basic averages
    print("Averages:")
    print("In average, Trump posts {} tweets per day.".format(round(calculate_average_tweets_per_day(trump_tweet_set))))
    print("In average, Trump tweets {} words.".format(round(calculate_average_word_count(trump_tweet_set))))
    print("In average, Trump's tweets have a popularity of {}."
          .format(int(round(calculate_average_popularity(trump_tweet_set), -3))))

    print()

    # Print term-filtered averages
    print("Term-Filtered Averages:")
    print("In average, Trump posts {} tweets about 'Fake News' per day."
          .format(round(calculate_average_tweets_per_day(filter_by_term(trump_tweet_set, 'Fake News')), 2)))
    print("In average, Trump tweets {} words about 'China'."
          .format(round(calculate_average_word_count(filter_by_term(trump_tweet_set, 'China')))))
    print("In average, Trump's posts about 'CNN' have a popularity of {}."
          .format(int(round(calculate_average_popularity(filter_by_term(trump_tweet_set, 'CNN')), -3))))

    print()

    # Print date-filtered averages
    print("Date-Filtered Averages")
    print("In 2016, Trump posted {} tweets per day."
          .format(round(calculate_average_tweets_per_day(filter_by_date(trump_tweet_set, "2016/01/01", "2016/12/31")))))
    print("From 2013 to 2015, Trump tweeted {} words in average."
          .format(round(calculate_average_word_count(filter_by_date(trump_tweet_set, "2013/01/01", "2015/12/31")))))
    print("In 2014, Trump's posts had an average popularity of {}"
          .format(int(round(calculate_average_popularity(filter_by_date(trump_tweet_set, "2015/01/01", "2015/12/31")
                                                         ), -3))))

    print()

    # Print top mentions
    print("Top Mentions:")
    print(format_mentions_table(get_top_mentions(trump_tweet_set)))

    print()

    # Print term-filtered top mentions:
    print("Top Mentions for 'Fake News':")
    print(format_mentions_table(get_top_mentions(filter_by_term(trump_tweet_set, 'Fake News'), top_mentions=5)))

    print()

    # Print date-filtered mentions:
    print("Top Mention in 2016-2017:")
    print(format_mentions_table(get_top_mentions(filter_by_date(trump_tweet_set, "2016/01/01", "2017/12/31"))))
    print()

    # Print most popular tweets
    print("Most Popular Tweets:")
    print(format_tweets_table(get_most_popular_tweets(trump_tweet_set)))

    print()

    # Print term-filtered most popular tweets
    print("Most Popular Tweets for 'Clinton':")
    print(format_tweets_table(get_most_popular_tweets(filter_by_term(trump_tweet_set, 'Clinton'), most_popular=5)))

    print()

    # Print date-filtered most popular tweets
    print("Most Popular Tweets in 2015")
    print(format_tweets_table(get_most_popular_tweets(filter_by_date(trump_tweet_set, "2015/01/01", "2015/12/31"),
                                                      most_popular=5)))

if __name__ == "__main__":
    main()
