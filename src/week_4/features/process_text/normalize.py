from week_4.features.process_text.patterns import get_contraction_dict, get_special_characters_pattern,\
    get_end_characters_pattern, get_hyperlink_pattern, get_apostrophe_pattern, get_whitespace_pattern, get_number_pattern, \
    get_abbreviation_dict
from week_4.features.process_text.correct_spelling import correct_word
from week_4.features.process_text.tokenize import is_tokenized, merge_tokens, word_tokenize
from re import IGNORECASE, DOTALL, sub, compile
from nltk.corpus import stopwords


def expand_abbreviations(text):
    """Expands contractions in text."""

    # If text is empty, return None.
    if not text: return None
    # If texts is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text
    # If last character is not space, add space.
    try:
        if normalized_text[-1] != ' ':
            normalized_text += ' '
    except IndexError:
        print(1)
    # Creates abbreviations pattern.
    abbreviations_pattern = compile('({})'.format(r'\.?\s|'.join(get_abbreviation_dict().keys())), flags=IGNORECASE | DOTALL)

    def expand_match(abbreviation):
        """Expands matched contraction."""

        # Retrieves matched contraction from string.
        match = abbreviation.group(0)
        # If last character is space, remove space.
        if match[-1] == " ":
            match = match[:-1]
            remove_space = True
        else:
            remove_space = False
        # If last character is dot, remove dot.
        if match[-1] == r'.':
            match = match[:-1]
        # Find expanded contraction in dictionary, based on contraction key.
        expanded_contraction = get_abbreviation_dict().get(match.lower())
        if not expanded_contraction:
            return abbreviation.group(0)
        if remove_space:
            expanded_contraction += " "
        # Add first character to expanded contraction.
        return expanded_contraction

    # Replaces contractions with expanded contractions in text.
    normalized_text = abbreviations_pattern.sub(expand_match, normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If text was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)

    # Return expanded text.
    return normalized_text


def remove_numbers(text):
    """Remove numbers from text."""

    # If text is empty, return None.
    if not text: return None
    # If texts is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text
    # Remove all tailing white spaces.
    normalized_text = normalized_text.strip()
    # Replace all special characters with spaces.
    normalized_text = sub(get_number_pattern(), r' ', normalized_text)
    # Then remove multiple adjacent spaces.
    normalized_text = sub(' +', ' ', normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If text was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)
    # Return normalized text.
    return normalized_text


def _get_single_match(match):
    """Returns single match of multiple match."""

    word = match.group()
    return word[0]


def replace_multiple_stopwords(text):
    """Replaces multiple stopwords with single stopwords."""

    # If text is empty, return None.
    if not text: return None
    # If texts is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text
    # Replaces apostrophe pattern with '.
    normalized_text = sub('[.!?]+', _get_single_match, normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)
    # Return normalized text.
    return normalized_text


def replace_whitespaces(text):
    """Replaces all whitespaces with one space."""

    # If text is empty, return None.
    if not text: return None
    # If texts is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text
    # Replaces all whitespaces with ' '.
    normalized_text = sub(get_whitespace_pattern(), ' ', normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)
    # Return normalized text.
    return normalized_text


def replace_apostrophes(text):
    """Replaces apostrophe pattern with '."""

    # If text is empty, return None.
    if not text: return None
    # If texts is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text
    # Replaces apostrophe pattern with '.
    normalized_text = sub(get_apostrophe_pattern(), "'", normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)
    # Return normalized text.
    return normalized_text


def expand_contractions(text):
    """Expands contractions in text."""

    # If text is empty, return None.
    if not text: return None
    # If texts is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text

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
    normalized_text = contractions_pattern.sub(expand_match, normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If text was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)

    # Return expanded text.
    return normalized_text


def convert_case(text, to_lower=True):
    """Converts text to defined case."""

    # If text is empty, return None.
    if not text: return None
    # If texts is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text

    # If to lower, convert to lower case. Else, convert to upper case.
    if to_lower:
        normalized_text = normalized_text.lower()
    else:
        normalized_text = normalized_text.upper()

    # If text was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)

    # Return normalized text.
    return normalized_text


def remove_special_characters(text):
    """Removes special characters from text."""

    # If text is empty, return None.
    if not text: return None
    # If texts is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text
    # Retrieve special characters pattern.
    special_characters_pattern = get_special_characters_pattern()
    # Remove all tailing white spaces.
    normalized_text = normalized_text.strip()
    # Replace all special characters with spaces.
    normalized_text = sub(special_characters_pattern, r' ', normalized_text)
    # Then remove multiple adjacent spaces.
    normalized_text = sub(' +', ' ', normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If text was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)
    # Return normalized text.
    return normalized_text


def remove_end_characters(text):
    """Removes end characters from word token list."""

    # If text is empty, return None.
    if not text: return None
    # If text is not tokenize, tokenize text.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text
    normalized_text += ' '
    # Replace stopwords with spaces.
    normalized_text = sub(get_end_characters_pattern(), r' ', normalized_text)
    # Then remove multiple adjacent spaces.
    normalized_text = sub(' +', ' ', normalized_text)
    # Then strip text.
    normalized_text = normalized_text.strip()
    if normalized_text[-1] == r'.':
        normalized_text = normalized_text[:-1]
    # If text was tokenized, then re-tokenize.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)
    # Return normalized text.
    return normalized_text


def remove_stopwords(text):
    """Remove stopwords from word token list"""

    # If text is empty, return None.
    if not text: return None
    # If text is not tokenize, tokenize text.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = text
    else:
        was_tokenized = False
        normalized_text = word_tokenize(text, 'whitespace')
    # Create stopwords list.
    stop_set = set(stopwords.words('english'))
    stop_set.update(['amp'])
    # Filter stopwords from text.
    normalized_text = [token for token in normalized_text if token not in stop_set]
    # If text was not tokenize, merge tokens.
    if not was_tokenized:
        normalized_text = merge_tokens(normalized_text)
    # Return normalized text.
    return normalized_text


def remove_hyperlinks(text):
    """Remove hyperlinks from text."""

    # If text is empty, return None.
    if not text: return None
    # If is tokenized, merge tokens.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = merge_tokens(text)
    else:
        was_tokenized = False
        normalized_text = text
    # Replace hyperlinks with space.
    normalized_text = sub(get_hyperlink_pattern(), r' ', normalized_text)
    # Then remove multiple adjacent spaces.
    normalized_text = sub(' +', ' ', normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If text was tokenized, re-tokenize text.
    if was_tokenized:
        normalized_text = word_tokenize(normalized_text)
    # Return normalized text.
    return normalized_text


def correct_spelling(text):
    """Correct spelling."""

    # If text is empty, return None.
    if not text: return None
    # If is not tokenized, tokenize text.
    if is_tokenized(text):
        was_tokenized = True
        normalized_text = text
    else:
        was_tokenized = False
        normalized_text = was_tokenized(text, 'whitespace')
    # Correct words.
    normalized_text = [correct_word(word) for word in normalized_text]
    # If was tokenized, merge text.
    if not was_tokenized:
        normalized_text = merge_tokens(normalized_text)
    # Return normalized text.
    return normalized_text
