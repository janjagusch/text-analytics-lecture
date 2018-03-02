from data.make_data_set import make_tweet_set
from data.filter_data_set import *
from features.build_tweet_features import *
from utils.format import *


def main():
    trump_tweet_set = make_tweet_set("trump_tweets.json")

    # Print basic averages
    print("Averages:")
    # TODO: Calculate average tweet per day.
    avg_tweet = 0
    print("In average, Trump posts {} tweets per day.".format(round(avg_tweet)))
    # TODO: Calculate average words per tweet.
    avg_words = 0
    print("In average, Trump tweets {} words.".format(round(avg_words)))
    # TODO: Calculate average popularity.
    avg_pop = 0
    print("In average, Trump's tweets have a popularity of {}.".format(int(round(avg_pop))))

    print()

    # Print term-filtered averages
    print("Term-Filtered Averages:")
    # TODO: Calculate average tweets per day that contain 'Fake News'.
    avg_tweet_tf = 0
    print("In average, Trump posts {} tweets about 'Fake News' per day.".format(round(avg_tweet_tf)))
    # TODO: Calculate average words per tweet about 'China'.
    avg_words_tf = 0
    print("In average, Trump tweets {} words about 'China'."
          .format(round(avg_words_tf)))
    # TODO: Calculate average popularity of tweets about 'CNN'.
    avg_pop_tf = 0
    print("In average, Trump's posts about 'CNN' have a popularity of {}.".format(round(avg_pop_tf)))

    print()

    # Print date-filtered averages
    print("Date-Filtered Averages")
    # TODO: Calculate average number of tweets per day in 2016.
    avg_tweet_df = 0
    print("In 2016, Trump posted {} tweets per day.".format(round(avg_tweet_df)))
    # TODO: Calculate average number of tweets from 2013 to 2015.
    avg_words_df = 0
    print("From 2013 to 2015, Trump tweeted {} words in average.".format(round(avg_words_df)))
    # TODO: Calculate average popularity of tweets in 2014.
    avg_pop_df = 0
    print("In 2014, Trump's posts had an average popularity of {}".format(round(avg_pop_df)))

    print()

    # Print top mentions
    print("Top Mentions:")
    # TODO: Calculate top 10 mentions.
    top_mentions = None
    print(format_mentions_table(top_mentions))

    print()

    # Print term-filtered top mentions:
    print("Top Mentions for 'Fake News':")
    # TODO: Calculate top 5 mentions where the tweet contains 'Fake News'.
    top_mentions_tf = None
    print(format_mentions_table(top_mentions_tf))

    print()

    # Print date-filtered mentions:
    print("Top Mention in 2016-2017:")
    # TODO: Calculate top 10 mentions from 2016 to 2017.
    top_mentions_df = None
    print(format_mentions_table(top_mentions_df))

    print()

    # Print most popular tweets
    print("Most Popular Tweets:")
    # TODO: Calculate 10 most popular tweets.
    popular_tweets = list()
    print(format_tweets_table(popular_tweets))

    print()

    # Print term-filtered most popular tweets
    print("Most Popular Tweets for 'Clinton':")
    # TODO: Calculate 5 most popular tweet that contain 'Clinton'.
    popular_tweets_tf = list()
    print(format_tweets_table(popular_tweets_tf))

    print()

    # Print date-filtered most popular tweets
    print("Most Popular Tweets in 2016")
    # TODO: Calculate 5 most popular tweets in 2016.
    popular_tweets_df = list()
    print(format_tweets_table(popular_tweets_df))

if __name__ == "__main__":
    main()
