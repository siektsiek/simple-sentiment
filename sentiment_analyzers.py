import os

class SentimentAnalyzers(object):
    """
    Predicting the sentiment polarity (good/bad) score of a list of tokens
    """
    def __init__(self):
        self.pos_words = self._get_words_list("POS_WORD_LIST")
        self.neg_words = self._get_words_list("NEG_WORD_LIST")

    def score(self, tokens):
        score = 0
        for word in tokens:
            if word in self.pos_words:
                score += 1

            elif word in self.neg_words:
                score -= 1

        return score

    def _get_words_list(self, path):
        words_path = os.environ.get(path)

        words = []

        with open(words_path) as f:
            for line in f:
                p = words.append(line.strip())

        return words
