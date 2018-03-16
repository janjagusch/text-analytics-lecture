import os
import pickle
import tarfile
import codecs

from sklearn.datasets.base import load_files


def create_pkz(target_dir, source_dir):
    """
    Used to create pkz file - this allows to work with this data in offline mode (pkz is as a zipped pickle)
    Args:
        source_dir: Location of the .tar.gz file
        target_dir: Location to save pkz file

    """

    DOWNLOADED_NAME = "20news-bydate.tar.gz"
    CACHE_NAME = "20news-bydate.pkz"
    TRAIN_FOLDER = "20news-bydate-train"
    TEST_FOLDER = "20news-bydate-test"

    cache_path = os.path.join(target_dir, CACHE_NAME)

    train_path = os.path.join(target_dir, TRAIN_FOLDER)
    test_path = os.path.join(target_dir, TEST_FOLDER)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    tarfile.open(source_dir+DOWNLOADED_NAME, "r:gz").extractall(path=target_dir)

    # Store a zipped pickle
    cache = dict(train=load_files(train_path, encoding='latin1'),
                 test=load_files(test_path, encoding='latin1'))
    compressed_content = codecs.encode(pickle.dumps(cache), 'zlib_codec')
    with open(cache_path, 'wb') as f:
        f.write(compressed_content)
