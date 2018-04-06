from week_4.data.io import make_tweet_set, write_tweets_cleaned
from week_4.features.process_tweet.clean_tweet import clean_tweet
from tqdm import tqdm

def main():
    # Load data into session.
    tweets = make_tweet_set()
    # Remove retweets.
    tweets = set(tweet for tweet in tweets if not tweet.is_retweet)
    # Clean tweets.
    for tweet in tqdm(tweets): clean_tweet(tweet)
    # Write as .pkl file.
    write_tweets_cleaned(tweets)


if __name__ == '__main__':
    main()