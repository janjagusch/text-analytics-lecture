import unittest
from week_4.features.process_text.normalize import expand_contractions, convert_case, remove_special_characters, \
    remove_end_characters, remove_stopwords, correct_spelling, remove_hyperlinks, replace_apostrophes, \
    replace_whitespaces, replace_multiple_stopwords, remove_numbers, expand_abbreviations
from week_4.features.process_text.tokenize import sentence_tokenize, word_tokenize
from week_4.features.process_text.stemming import convert_word_stem, lemmatize_text
from week_4.features.process_text.clean import clean_text

class TestProcessTest(unittest.TestCase):


    def test_lemmatize_text(self):
        text = 'The dog is funny. The dog is jumping over the brown fox.'
        processed_text = lemmatize_text(text)
        solution = ""


    def test_expand_abbreviations(self):
        text = "U.K. U.S. U.S.A. sen. v.p can."
        processed_text = expand_abbreviations(text)
        solution = 'united kingdom united states united states of america senator vice president can.'
        self.assertEqual(processed_text, solution)


    def test_remove_numbers(self):
        text = "I have 100 dollars at least 5 times"
        processed_text = remove_numbers(text)
        solution = "I have dollars at least times"
        self.assertEqual(processed_text, solution)


    def test_replace_multiple_stopwords(self):
        text = "This is a test!!! I hope this works..."
        processed_text = replace_multiple_stopwords(text)
        solution = "This is a test! I hope this works."
        self.assertEqual(processed_text, solution)


    def test_replace_whitespaces(self):
        text = """This
        is
        
        a
        
        
        test"""
        processed_text = replace_whitespaces(text)
        solution = "This is a test"
        self.assertEqual(processed_text, solution)


    def test_replace_apostrophe(self):
        text = "It’s the wrong apostrophe."
        processed_text = replace_apostrophes(text)
        solution = "It's the wrong apostrophe."
        self.assertEqual(processed_text, solution)


    def test_clean(self):
        text = "I've proven MANY times - at least 5 or 6 times - that I'm the smartest president! I am the strongest president!"
        cleaned_text = clean_text(text, tokenize=True)


    def test_remove_hyperlinks(self):
        text = "Look at my code https://regex101.com/ it is awesome"
        normalized_text = remove_hyperlinks(text)
        solution = 'Look at my code it is awesome'
        self.assertEqual(normalized_text, solution)


    def test_expand_contractions(self):
        text = "I've proven many times that I'm the smartest"
        processed_text = expand_contractions(text)
        solution = 'I have proven many times that I am the smartest'
        self.assertEqual(processed_text, solution)
        text = word_tokenize(text, 'whitespace')
        processed_text = expand_contractions(text)
        solution = solution.split()
        self.assertEqual(processed_text, solution)


    def test_convert_case(self):
        text = 'I am the SMARTEST AND GREATEST president'
        processed_text = convert_case(text)
        solution = 'i am the smartest and greatest president'
        self.assertEqual(processed_text, solution)
        text = word_tokenize(text, 'whitespace')
        processed_text = convert_case(text)
        solution = solution.split()
        self.assertEqual(processed_text, solution)


    def test_remove_special_characters(self):
        text = 'As I said many times, we are not "ISIS" - and they know it'
        processed_text = remove_special_characters(text)
        solution = 'As I said many times we are not ISIS and they know it'
        self.assertEqual(processed_text, solution)
        # text = word_tokenize(text)
        # processed_text = remove_special_characters(text)
        # solution = solution.split()
        # self.assertEqual(processed_text, solution)


    def test_sentence_tokenize(self):
        text = 'We are America! We were great once. Can we make it great again?'
        processed_text = sentence_tokenize(text)
        self.assertEqual(processed_text, ['We are America!', 'We were great once.', 'Can we make it great again?'])


    def test_word_tokenize(self):
        text = 'Can we make the U.S. great again?'
        processed_text = word_tokenize(text)
        self.assertEqual(processed_text, ['Can', 'we', 'make', 'the', 'U.S.', 'great', 'again', '?'])


    def test_remove_end_characters(self):
        text = ['Can', 'we', 'make', 'the', 'U.S.', 'great', 'again', '.']
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
