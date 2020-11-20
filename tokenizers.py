import re
import os

class SimpleTokenizer(object):
    """
    Handles the tokenization of strings => list of token strings
    """

    def __init__(self):
        self.stopwords = self._get_stopwords()
        pass

    def tokenize(self, sentence):
        """
        Splits string text on whitespace, remove non-alphanumeric characters
        :param sentence:
        :return:
        """
        lower_sent = sentence.lower()
        cleand_sent = re.sub(r"[^a-zA-Z0-9 ]", '', lower_sent)
        return [word for word in cleand_sent.split() if word not in self.stopwords]

    def _get_stopwords(self):
        stopwords_path = os.environ.get("STOPWORDS_LIST")
        print(stopwords_path)
        stopwords = []
        with open(stopwords_path, encoding='UTF-8') as f:
            for line in f:
                stopwords.append(line.strip())
        return stopwords
