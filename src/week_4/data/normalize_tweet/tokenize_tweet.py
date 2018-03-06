from nltk import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer, RegexpTokenizer, TreebankWordTokenizer, WordPunctTokenizer, \
    WhitespaceTokenizer
from week_4.data.normalize_tweet.patterns import SENTENCE_TOKENS_PATTERN, TOKEN_PATTERN


_sentence_tokenizer_default = sent_tokenize

_sentence_tokenizer_punkt = PunktSentenceTokenizer.tokenize

_sentence_tokenizer_regex = RegexpTokenizer(pattern=SENTENCE_TOKENS_PATTERN, gaps=True).tokenize

SENTENCE_TOKENIZER_DICT = {
    'default': _sentence_tokenizer_default,
    'punkt': _sentence_tokenizer_punkt,
    'regex': _sentence_tokenizer_regex
}


def _sentence_tokenize(sentence, sentence_tokenizer_id):
    """
    Tokenizes a sentence, based on a given tokenizer.
    Args:
        sentence: A string, describing a sentence.
        sentence_tokenizer_id: A tokenizer key, taken from SENTENCE_TOKENIZER_DICT.
    Returns:
        A tokenized sentence.
    """
    sentence_tokenizer = SENTENCE_TOKENIZER_DICT.get(sentence_tokenizer_id)
    return sentence_tokenizer(sentence)


def sentence_tokenize_tweet(tweet, sentence_tokenizer_id='default'):
    """
    Applies sentence tokenization to tweet.
    Args:
        tweet: A tweet object.
        sentence_tokenizer_id: A sentence tokenizer id.
    """
    tweet.text_processed['text_sentence_tokenized'] = \
        _sentence_tokenize(tweet.text_processed['text_remove_special_characters'], sentence_tokenizer_id)


_word_tokenizer_default = word_tokenize

_word_tokenizer_treebank = TreebankWordTokenizer.tokenize

_word_tokenizer_regex = RegexpTokenizer(pattern=TOKEN_PATTERN, gaps=False).tokenize

_word_tokenizer_punkt = WordPunctTokenizer.tokenize

_word_tokenizer_whitespace = WhitespaceTokenizer.tokenize

WORD_TOKENIZER_DICT = {
    'default': _word_tokenizer_default,
    'treebank': _word_tokenizer_treebank,
    'regex': _word_tokenizer_regex,
    'punkt': _word_tokenizer_punkt,
    'whitespace': _word_tokenizer_whitespace
}


def _word_tokenize(sentence, word_tokenizer_id):
    """
    Word-tokenizes a given sentence, based on a defined tokenizer.
    Args:
        sentence: A string, corresponding to a sentence.
        word_tokenizer_id: A key from WORD_TOKENIZER_DICT
    Returns:
        A list of words, corresponding to the tokenized sentence.
    """
    word_tokenizer = WORD_TOKENIZER_DICT.get(word_tokenizer_id)
    return word_tokenizer(sentence)


def word_tokenize_tweet(tweet, word_tokenizer_id='default'):
    tweet.text_processed['text_word_tokenized'] = \
        [_word_tokenize(sentence, word_tokenizer_id) for sentence in tweet.text_processed['text_sentence_tokenized']]
