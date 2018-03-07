from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer, WordNetLemmatizer
from week_4.features.process_text.patterns import get_stemming_pattern

_stemming_porter = PorterStemmer().stem

_stemming_lancaster = LancasterStemmer().stem

_stemming_regex = RegexpStemmer(get_stemming_pattern()).stem

_stemming_snowball = SnowballStemmer('english').stem

_STEMMING_DICT = {
    'porter': _stemming_porter,
    'lancaster': _stemming_lancaster,
    'regex': _stemming_regex,
    'snowball': _stemming_snowball
}


def convert_word_stem(word_token_list, stemming_id='porter'):
    """Converts words to word stem"""
    stemming = _STEMMING_DICT.get(stemming_id)
    return [stemming(word_token) for word_token in word_token_list]
