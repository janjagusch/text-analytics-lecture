import unittest
from week_4.features.process_text.normalization import expand_contractions, convert_case, remove_special_characters, \
    remove_end_characters, remove_stopwords, correct_spelling
from week_4.features.process_text.tokenization import sentence_tokenize, word_tokenize
from week_4.features.process_text.stemming import convert_word_stem


class TestProcessTest(unittest.TestCase):

    def test_expand_contractions(self):
        text = "I've proven many times that I'm the smartest."
        processed_text = expand_contractions(text)
        self.assertEqual(processed_text, 'I have proven many times that I am the smartest.')

    def test_convert_case(self):
        text = 'I am the SMARTEST AND GREATEST president.'
        processed_text = convert_case(text)
        self.assertEqual(processed_text, 'i am the smartest and greatest president.')

    def test_remove_special_characters(self):
        text = 'As I said many times, we are not "ISIS" - and they know it.'
        processed_text = remove_special_characters(text)
        self.assertEqual(processed_text, 'As I said many times we are not ISIS and they know it.')

    def test_sentence_tokenize(self):
        text = 'We are America! We were great once. Can we make it great again?'
        processed_text = sentence_tokenize(text)
        self.assertEqual(processed_text, ['We are America!', 'We were great once.', 'Can we make it great again?'])

    def test_word_tokenize(self):
        text = 'Can we make the U.S. great again?'
        processed_text = word_tokenize(text)
        self.assertEqual(processed_text, ['Can', 'we', 'make', 'the', 'U.S.', 'great', 'again', '?'])

    def test_remove_end_characters(self):
        text = ['Can', 'we', 'make', 'the', 'U.S.', 'great', 'again', '?']
        processed_text = remove_end_characters(text)
        self.assertEqual(processed_text, ['Can', 'we', 'make', 'the', 'U.S.', 'great', 'again'])

    def test_remove_stop_words(self):
        text = ['I', 'am', 'going', 'to', 'make', 'the', 'U.S.', 'great', 'again']
        processed_text = remove_stopwords(text)
        self.assertEqual(processed_text, ['I', 'going', 'make', 'U.S.', 'great'])

    def test_correct_spelling(self):
        text = ['i', 'have', 'finaly', 'beaten', 'teh', 'cinese', 'goverment']
        processed_text = correct_spelling(text)
        self.assertEqual(processed_text, ['i', 'have', 'finally', 'beaten', 'the', 'chinese', 'government'])

    def test_convert_word_stem(self):
        text = ['i', 'am', 'laughing', 'at', 'the', 'countries', 'joking', 'about', 'my', 'presidency']
        processed_text = convert_word_stem(text)
        self.assertEqual(processed_text,
                         ['i', 'am', 'laugh', 'at', 'the', 'countri', 'joke', 'about', 'my', 'presid'])


if __name__ == '__main__':
    unittest.main()
