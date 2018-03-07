from nltk import pos_tag, word_tokenize
from nltk.chunk import ne_chunk
from nltk.tree import Tree

sentence = 'The brown fox is quick and he is jumping over the lazy dog'
tokens = word_tokenize(sentence)
tagged_sent = pos_tag(tokens, tagset='universal')
chunks = ne_chunk(tagged_sent, binary=True)

print(tagged_sent)
print(chunks)