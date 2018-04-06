from week_4.features.process_text.normalize import expand_contractions, convert_case, remove_special_characters, \
    remove_end_characters, remove_stopwords


def expand_tweet(tweet, input_text_id='01_raw'):
    """Expands contractions in tweet."""
    input_text = tweet.get_text_element(input_text_id)
    tweet.text_processed['expand'] = expand_contractions(input_text)


def convert_case_tweet(tweet, input_text_id='expand'):
    """Converts tweet to case convention."""
    input_text = tweet.get_text_element(input_text_id)
    tweet.text_processed['convert_case'] = convert_case(input_text)


def remove_special_characters_tweet(tweet, input_text_id='convert_case'):
    """Removes special characters from tweet."""
    input_text = tweet.get_text_element(input_text_id)
    tweet.text_processed['remove_special_characters'] = remove_special_characters(input_text)


def remove_end_characters_tweet(tweet, input_text_id='word_tokenized'):
    """Removes end characters from tweet."""
    input_text = tweet.get_text_element(input_text_id)
    tweet.text_processed['remove_end_characters'] = \
        [remove_end_characters(word_token_list) for word_token_list in input_text]


def remove_stopwords_tweet(tweet, input_text_id='remove_end_characters'):
    """Removes stopwords from tweet."""
    input_text = tweet.get_text_element(input_text_id)
    tweet.text_processed['remove_stopwords'] = [remove_stopwords(word_token_list) for word_token_list in input_text]


