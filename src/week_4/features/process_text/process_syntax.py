from nltk.parse.stanford import StanfordDependencyParser, StanfordParser


path_to_jar = 'C://Users//Jan//Documents//stanford-corenlp-full-2018-02-27//stanford-corenlp-3.9.1.jar'
path_to_models_jar = 'C://Users//Jan//Documents//stanford-corenlp-full-2018-02-27//stanford-corenlp-3.9.1-models.jar'

dep_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
parser = StanfordParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

sentence = ['i', 'am', 'a', 'smart', 'business', 'man', 'and', 'can', 'lead', 'much', 'better', 'than', 'the', 'old', 'lazy', 'presidents']

# print(list(parser.raw_parse("the quick brown fox jumps over the lazy dog")))
# print([parse.tree() for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")])

# result = list(dep_parser.parse(sentence))
# result[0].draw()

result = list(dep_parser.parse(sentence))
dep_tree = [parse.tree() for parse in result][0]
dep_tree.draw()