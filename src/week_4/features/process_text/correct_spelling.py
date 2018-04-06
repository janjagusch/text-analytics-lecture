from re import findall, sub
from collections import Counter
import nltk.corpus

# Taken from https://norvig.com/spell-correct.html


def _words(text):
    return findall(r'\w+', text.lower())

_BIG_TEXT = '\n'.join([nltk.corpus.gutenberg.raw(file_id) for file_id in nltk.corpus.gutenberg.fileids()])

_WORD_DICT = Counter(_words(_BIG_TEXT))


def _prob(word, n=sum(_WORD_DICT.values())):
    """"Probability of `word`."""
    return _WORD_DICT[word] / n


def _candidates(word):
    """"Generate possible spelling corrections for word."""
    return _known([word]) or _known(_edits1(word)) or _known(_edits2(word)) or [word]


def _known(words):
    """The subset of `words` that appear in the dictionary of WORDS."""
    return set(w for w in words if w in _WORD_DICT)


def _edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def _edits2(word):
    """All edits that are two edits away from `word`."""
    return (e2 for e1 in _edits1(word) for e2 in _edits1(e1))


def correct_word(word):
    """Most probable spelling correction for word."""
    return max(_candidates(word), key=_WORD_DICT.get)


def _correct_match(match):
    word = match.group()

    def case_of(text):
        """
        Return the case-function appropriate
        for text: upper, lower, title, or just str.:
            """
        return (str.upper if text.isupper() else
                str.lower if text.islower() else
                str.title if text.istitle() else
                str)

    return case_of(word)(correct_word(word.lower()))


def correct_text(text):
    """Correct all the words within a text, returning the corrected text."""
    return sub('[a-zA-Z]+', _correct_match, text)
