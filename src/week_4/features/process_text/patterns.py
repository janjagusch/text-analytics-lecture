from re import compile


_ABBREVIATION_DICT = {
    'u.s': 'united states',
    't.v': 'television',
    'u.s.a': 'united states of america',
    'a.g': 'attorney general',
    'dr': 'doctor',
    'sen': 'senator',
    'v.p': 'vice president',
    'rep': 'republican',
    'u.k': 'united kingdom',
    'gen': 'general'
}

_CONTRACTION_DICT = {
    "ain't": "is not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'd've": "I would have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'm": "I am",
    "I've": "I have",
    "i'd": "i would",
    "i'd've": "i would have",
    "i'll": "i will",
    "i'll've": "i will have",
    "i'm": "i am",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you would",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have"
}

_SENTENCE_TOKEN_PATTERN = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<![A-Z]\.)(?<=\.|\?|\!)\s'

_WORD_TOKEN_PATTERN = r'\w+'

_STEMMING_PATTERN = 'ing$|s$|ed$'

_SPECIAL_CHARACTERS = ['$', '&', '*', '%', '(', ')', '~', '-', '—', '"', "'", ',', ':', ';', '“', '”']

_END_CHARACTERS = ['?', '!']

_HYPERLINK_PATTERN = r'https?:\/\/[^\s]+'

_APOSTROPHE_PATTERN = r'’'

_WHITESPACE_PATTERN = r'\s+'

_NUMBER_PATTERN = r'[^\s]*\d+[^\s]*'


def get_abbreviation_dict():
    """Returns abbreviation dict."""

    return _ABBREVIATION_DICT


def get_number_pattern():
    """Returns number pattern."""

    return compile('{}'.format(_NUMBER_PATTERN))


def get_whitespace_pattern():
    """Returns whitespace pattern."""

    return compile('{}'.format(_WHITESPACE_PATTERN))


def get_apostrophe_pattern():
    """Returns apostrophe pattern."""

    pattern = compile('[{}]'.format(_APOSTROPHE_PATTERN))
    return pattern


def get_hyperlink_pattern():
    """Returns hyperlink pattern."""

    hyperlink_pattern = compile('{}'.format(_HYPERLINK_PATTERN))
    return hyperlink_pattern


def get_contraction_dict():
    """Returns CONTRACTION DICT"""
    return _CONTRACTION_DICT


def get_sentence_token_pattern():
    """Returns SENTENCE TOKEN PATTERN"""
    return _SENTENCE_TOKEN_PATTERN


def get_word_token_pattern():
    """Returns WORD TOKEN PATTERN"""
    return _WORD_TOKEN_PATTERN


def get_special_characters_pattern():
    """
    Retrieves regular expression pattern from SPECIAL CHARACTERS.
    Returns:
        A regular expression object with the special characters pattern.
    """
    # Adds literal to each special character
    special_characters_string = ['\\' + character for character in _SPECIAL_CHARACTERS]
    # Converts list to regular expression pattern
    special_characters_pattern = compile('[{}]'.format(''.join(special_characters_string)))
    return special_characters_pattern


def get_end_characters_pattern():
    """
    Retrieves regular expression pattern from END CHARACTERS.
    Returns:
        A regular expression object with the end characters pattern.
    """
    # Adds literal to each character
    sentence_ending_characters_literal = ['\\' + character for character in _END_CHARACTERS]
    sentence_ending_characters_pattern = compile('[{}]+'.format(''.join(sentence_ending_characters_literal)))
    return sentence_ending_characters_pattern


def get_stemming_pattern():
    """Returns stemming pattern."""
    return _STEMMING_PATTERN
