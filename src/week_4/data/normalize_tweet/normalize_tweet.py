from week_4.data.normalize_tweet.patterns import CONTRACTION_MAP, get_special_characters_pattern
from re import compile, IGNORECASE, DOTALL, sub, escape


def _expand_contractions(sentence):
    """
    Expands contractions in sentence.
    Args:
        sentence: A string that represents a sentence.

    Returns:
        A string that represents a sentence with expanded contractions.
    """

    # Creates contractions pattern.
    contractions_pattern = compile('({})'.format('|'.join(CONTRACTION_MAP.keys())), flags=IGNORECASE | DOTALL)

    def expand_match(contraction):
        """
        Expands matched contraction.
        Args:
            contraction: A contraction.

        Returns:
            An expanded contraction.
        """

        # Retrieves matched contraction from string.
        match = contraction.group(0)
        # Stores first character for case sensitivity.
        first_char = match[0]
        # Find expanded contraction in dictionary, based on contraction key.
        expanded_contraction = CONTRACTION_MAP.get(match)
        # If the contraction could not be found, try again with lower case.
        if not expanded_contraction:
            expanded_contraction = CONTRACTION_MAP.get(match.lower())
        # Add first character to expanded contraction.
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    # Replaces contractions with expanded contractions in text.
    expanded_sentence = contractions_pattern.sub(expand_match, sentence)
    return expanded_sentence


def expand_tweet(tweet):
    """
    Expands raw text of tweet.

    Converts contracted words into expanded version and adds expanded text to dictionary.
    Args:
        tweet: A tweet object.
    """
    tweet.text_processed['text_expanded'] = _expand_contractions(tweet.text_raw)


def lower_case_tweet(tweet):
    """
    Converts tweet to lower case convention.
    Args:
        tweet: A tweet object.
    """
    tweet.text_processed['text_lower_case'] = tweet.text_processed['text_expanded'].lower()


def _remove_special_characters(sentence):
    """
    Removes special characters from sentence.
    Args:
        sentence:

    Returns:
        Sentence without special characters.
    """
    # Retrieve special characters pattern.
    special_characters_pattern = get_special_characters_pattern()
    # Remove all tailing white spaces.
    sentence = sentence.strip()
    # Replace all special characters with spaces.
    filtered_sentence = sub(special_characters_pattern, r' ', sentence)
    # Then remove multiple adjacent spaces.
    filtered_sentence = sub(' +', ' ', filtered_sentence)
    return filtered_sentence


def remove_special_characters_tweet(tweet):
    """
    Removes special characters from tweet.
    Args:
        tweet: A tweet object.
    """
    tweet.text_processed['text_remove_special_characters'] = \
        _remove_special_characters(tweet.text_processed['text_lower_case'])
