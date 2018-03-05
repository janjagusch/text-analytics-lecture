from nltk import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer, RegexpTokenizer, TreebankWordTokenizer, WordPunctTokenizer, \
    WhitespaceTokenizer
from week_4.data.normalize_tweet.patterns import SENTENCE_TOKENS_PATTERN


sentence_tokenizer_default = sent_tokenize

sentence_tokenizer_punkt = PunktSentenceTokenizer.tokenize

sentence_tokenizer_regex = RegexpTokenizer(pattern=SENTENCE_TOKENS_PATTERN, gaps=True).tokenize


SENTENCE_TOKENIZER_DICT = {
    'default': sentence_tokenizer_default,
    'punkt': sentence_tokenizer_punkt,
    'regex': sentence_tokenizer_regex
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


word_tokenizer_default = word_tokenize

word_tokenizer_treebank = TreebankWordTokenizer.tokenize

word_tokenizer_regex = RegexpTokenizer(pattern=TOKEN_PATTERN, gaps=False).tokenize

word_tokenizer_punkt = WordPunctTokenizer.tokenize

word_tokenizer_whitespace = WhitespaceTokenizer.tokenize
