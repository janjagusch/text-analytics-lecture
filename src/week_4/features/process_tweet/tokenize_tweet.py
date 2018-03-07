from week_4.features.process_text.tokenization import sentence_tokenize, word_tokenize


def sentence_tokenize_tweet(tweet, tokenizer_id='default', input_text_id='remove_special_characters'):
    """Sentence-tokenizes tweet, based on tokenizer id."""
    input_text = tweet.get_text_element(input_text_id)
    tweet.text_processed['sentence_tokenize'] = sentence_tokenize(input_text, tokenizer_id)


def word_tokenize_tweet(tweet, tokenizer_id='default', input_text_id='sentence_tokenize'):
    """Word-tokenizes tweet, based on tokenizer id."""
    input_text = tweet.get_text_element(input_text_id)
    tweet.text_processed['text_word_tokenized'] = \
        [word_tokenize(sentence, tokenizer_id) for sentence in input_text]
