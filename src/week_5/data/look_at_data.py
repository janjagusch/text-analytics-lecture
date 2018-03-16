from sklearn.datasets import fetch_20newsgroups
from os.path import join, dirname


def load_dataset(train_test_all):
    
    # data_home = '/Users/pelejaf/Documents/workspace/textmining/text-analytics-lecture/src/week_5/data/'

    categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

    # The selection of categories is optional. If empty we will obtain samples from all categories
    # subset can be: train, test or all
    dataset = fetch_20newsgroups(subset=train_test_all, categories=categories, shuffle=True, random_state=42, download_if_missing=True)

    # dataset = fetch_20newsgroups(subset=train_test_all, categories=categories, shuffle=True, random_state=42,
    #                              download_if_missing=False)
    # dataset = fetch_20newsgroups(subset=train_test_all, categories=categories, shuffle=True, random_state=42,
    #                              data_home=data_home, download_if_missing=False)
    return dataset


def target_classes(dataset):
    # Classes in the dataset
    return dataset.target_names


def nr_samples(dataset):
    # Number of training samples:
    return len(dataset.data)


def sample_content(dataset, sample_pos):
    sample_pos -= 1  # Why -1? Because the vector starts counting at position 0

    return dataset.data[sample_pos]


def sample_class_pos(dataset, sample_pos):
    class_pos = dataset.target[sample_pos]

    return class_pos


def sample_class(dataset, class_pos):
    return dataset.target_names[class_pos]


def sample_filename(dataset, sample_pos):
    return dataset.filenames[sample_pos]

