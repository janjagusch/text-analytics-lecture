from data.make_data_set import make_tweet_set
from data.filter_data_set import filter_by_term, filter_by_date
from features.build_tweet_features import calculate_average_tweets_per_day, calculate_average_popularity, \
    calculate_average_word_count, get_most_popular_tweets, get_top_mentions
from utils.format import format_tweets_table, format_mentions_table


def main():
    trump_tweet_set = make_tweet_set("trump_tweets.json")

    # Print basic averages
    print("Averages:")
    # Average tweets per day
    avg_tpd = calculate_average_tweets_per_day(trump_tweet_set)
    print("In average, Trump posts {:.2f} tweets per day.".format(avg_tpd))
    # Average words per tweet
    avg_wpt = calculate_average_word_count(trump_tweet_set)
    print("In average, Trump tweets {:.2f} words.".format(avg_wpt))
    # Average popularity per tweet
    avg_ppt = calculate_average_popularity(trump_tweet_set)
    print("In average, Trump's tweets have a popularity of {:.2f}.".format(avg_ppt))

    print()

    # Print term-filtered averages
    print("Term-Filtered Averages:")
    # Average tweets per day, term-filtered
    avg_tpd_tf = calculate_average_tweets_per_day(filter_by_term(trump_tweet_set, 'Fake News'))
    print("In average, Trump posts {:.2f} tweets about 'Fake News' per day.".format(avg_tpd_tf))
    # Average word per tweet, term-filtered
    avg_wpt_tf = calculate_average_word_count(filter_by_term(trump_tweet_set, 'China'))
    print("In average, Trump tweets {:.2f} words about 'China'.".format(avg_wpt_tf))
    # Average popularity per tweet, term-filtered
    avg_ppt_tf = calculate_average_popularity(filter_by_term(trump_tweet_set, 'CNN'))
    print("In average, Trump's posts about 'CNN' have a popularity of {:.2f}.".format(avg_ppt_tf))

    print()

    # Print date-filtered averages
    print("Date-Filtered Averages")
    # Average tweets per day, date-filtered
    avg_tpd_df = calculate_average_tweets_per_day(filter_by_date(trump_tweet_set, '2016/01/01', '2016/12/31'))
    print("In 2016, Trump posted {:.2f} tweets per day.".format(avg_tpd_df))
    # Average words per tweet, date-filtered
    avg_wpt_df = calculate_average_word_count(filter_by_date(trump_tweet_set, '2013/01/01', '2015/12/31'))
    print("From 2013 to 2015, Trump tweeted {:.2f} words in average.".format(avg_wpt_df))
    # Average popularity per tweet, date-filtered
    avg_ppt_df = calculate_average_popularity(filter_by_date(trump_tweet_set, '2014/01/01', '2014/12/31'))
    print("In 2014, Trump's posts had an average popularity of {:.2f}".format(avg_ppt_df))

    print()

    # Print top mentions
    print("Top Mentions:")
    tm = get_top_mentions(trump_tweet_set)
    print(format_mentions_table(tm))

    print()

    # Print term-filtered top mentions:
    print("Top Mentions for 'Fake News':")
    tm_tf = get_top_mentions(filter_by_term(trump_tweet_set, 'Fake News'), top_mentions=5)
    print(format_mentions_table(tm_tf))

    print()

    # Print date-filtered mentions:
    print("Top Mention in 2016-2017:")
    tm_df = get_top_mentions(filter_by_date(trump_tweet_set, '2016/01/01', '2017/12/31'), top_mentions=5)
    print(format_mentions_table(tm_df))

    print()

    # Print most popular tweets
    print("Most Popular Tweets:")
    mpt = get_most_popular_tweets(trump_tweet_set)
    print(format_tweets_table(mpt))

    print()

    # Print term-filtered most popular tweets
    print("Most Popular Tweets for 'Clinton':")
    mpt_tf = get_most_popular_tweets(filter_by_term(trump_tweet_set, 'Clinton'), most_popular=5)
    print(format_tweets_table(mpt_tf))

    print()

    # Print date-filtered most popular tweets
    print("Most Popular Tweets in 2015")
    mpt_df = get_most_popular_tweets(filter_by_date(trump_tweet_set, '2015/01/01', '2015/12/31'), most_popular=5)
    print(format_tweets_table(mpt_df))

if __name__ == "__main__":
    main()
