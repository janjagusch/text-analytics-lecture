from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer, WordNetLemmatizer
from week_4.features.process_text.patterns import get_stemming_pattern
from nltk import pos_tag
from nltk.corpus import wordnet
from week_4.features.process_text.tokenize import is_tokenized, merge_tokens, word_tokenize

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



# Annotate text tokens with POS tags
def pos_tag_text(text):
    def convert_tags(pos_tag):
        if pos_tag.startswith('J'):
            return wordnet.ADJ
        elif pos_tag.startswith('V'):
            return wordnet.VERB
        elif pos_tag.startswith('N'):
            return wordnet.NOUN
        elif pos_tag.startswith('R'):
            return wordnet.ADV
        else:
            return None

    tagged_text = pos_tag(text)
    tagged_lower_text = [(word.lower(), convert_tags(pos_tag)) for word, pos_tag in tagged_text]
    return tagged_lower_text


# lemmatize text based on POS tags
def lemmatize_text(text):
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = text
    else:
        normalized_text = word_tokenize(text, 'whitespace')
        was_tokenized = False

    pos_tagged_text = pos_tag_text(normalized_text)
    lemmatized_text = [WordNetLemmatizer().lemmatize(word, pos_tag) if pos_tag else word
                         for word, pos_tag in pos_tagged_text]
    if not was_tokenized:
        lemmatized_text = merge_tokens(lemmatized_text)
    return lemmatized_text