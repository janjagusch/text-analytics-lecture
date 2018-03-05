import unittest
from week_4.data.make_data_set import make_tweet_set
from week_4.data.normalize_tweet.normalize_tweet import expand_tweet, lower_case_tweet, remove_special_characters_tweet
from week_4.utils.lookup import get_tweet_by_tweet_id
from week_4.data.normalize_tweet.tokenize_tweet import sentence_tokenize_tweet


class TestNormalizeTweet(unittest.TestCase):
    def setUp(self):
        self.trump_tweet_set = make_tweet_set('trump_tweets.json')

    def test_expand_tweet(self):
        test_tweet = get_tweet_by_tweet_id(self.trump_tweet_set, '745693029089034240')
        expand_tweet(test_tweet)
        self.assertEqual(test_tweet.text_processed['text_expanded'],
                         'Hillary says things cannot change. I say they have to change. '
                         'It is a choice between Americanism and her corrupt globalism. #Imwithyou')

    def test_lower_case_tweet(self):
        test_tweet = get_tweet_by_tweet_id(self.trump_tweet_set, '745693029089034240')
        expand_tweet(test_tweet)
        lower_case_tweet(test_tweet)
        self.assertEqual(test_tweet.text_processed['text_lower_case'],
                         'hillary says things cannot change. i say they have to change. '
                         'it is a choice between americanism and her corrupt globalism. #imwithyou')

    def test_remove_special_characters_tweet(self):
        test_tweet = get_tweet_by_tweet_id(self.trump_tweet_set, '495380307911385088')
        expand_tweet(test_tweet)
        lower_case_tweet(test_tweet)
        remove_special_characters_tweet(test_tweet)
        self.assertEqual(test_tweet.text_processed['text_remove_special_characters'],
                         'just as i have been predicting for years iraq will fall to the people that hate the u.s. '
                         'the most just outside of baghdad. keep the oil ')

    def test_tokenize_tweet(self):
        test_tweet = get_tweet_by_tweet_id(self.trump_tweet_set, '495380307911385088')
        expand_tweet(test_tweet)
        lower_case_tweet(test_tweet)
        remove_special_characters_tweet(test_tweet)
        sentence_tokenize_tweet(test_tweet)
        self.assertEqual(test_tweet.text_processed['text_sentence_tokenized'][0],
                         'just as i have been predicting for years iraq will fall'
                         ' to the people that hate the u.s. the most just outside of baghdad.')
        self.assertEqual(test_tweet.text_processed['text_sentence_tokenized'][1], 'keep the oil')


if __name__ == '__main__':
    unittest.main()
