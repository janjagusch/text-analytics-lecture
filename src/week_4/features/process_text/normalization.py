from week_4.features.process_text.patterns import get_contraction_dict, get_special_characters_pattern,\
    get_end_characters_pattern
from re import IGNORECASE, DOTALL, sub, match, compile
from nltk.corpus import stopwords
from week_4.features.process_text.correct_spelling import correct_word


def expand_contractions(text):
    """Expands contractions in text."""
    # Creates contractions pattern.
    contractions_pattern = compile('({})'.format('|'.join(get_contraction_dict().keys())), flags=IGNORECASE | DOTALL)

    def expand_match(contraction):
        """Expands matched contraction."""
        # Retrieves matched contraction from string.
        match = contraction.group(0)
        # Stores first character for case sensitivity.
        first_char = match[0]
        # Find expanded contraction in dictionary, based on contraction key.
        expanded_contraction = get_contraction_dict().get(match)
        # If the contraction could not be found, try again with lower case.
        if not expanded_contraction:
            expanded_contraction = get_contraction_dict().get(match.lower())
        # Add first character to expanded contraction.
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    # Replaces contractions with expanded contractions in text.
    expanded_text = contractions_pattern.sub(expand_match, text)
    return expanded_text


def convert_case(text):
    """Converts text to lower case."""
    return text.lower()


def remove_special_characters(text):
    """Removes special characters from text."""

    # Retrieve special characters pattern.
    special_characters_pattern = get_special_characters_pattern()
    # Remove all tailing white spaces.
    text = text.strip()
    # Replace all special characters with spaces.
    filtered_text = sub(special_characters_pattern, r' ', text)
    # Then remove multiple adjacent spaces.
    filtered_text = sub(' +', ' ', filtered_text)
    return filtered_text


def remove_end_characters(word_token_list):
    """Removes end characters from word token list."""
    return [word_token for word_token in word_token_list
            if not match(get_end_characters_pattern(), word_token)]


def remove_stopwords(word_token_list):
    """Remove stopwords from word token list"""
    stopword_list = stopwords.words('english')
    return [word_token for word_token in word_token_list if word_token not in stopword_list]


def correct_spelling(word_token_list):
    """Correct spelling."""
    return [correct_word(word) for word in word_token_list]
