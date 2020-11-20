from sentiment_analyzers import SentimentAnalyzers

class TestSentimentAnalyzers(object):
    """
    Unit test for sentiment analyzers module
    """

    def test_seniment_polarity_of_all_positive_tokens_should_be_positive(self):
        input = ['good', 'happy', 'wonderful']
        sa = SentimentAnalyzers()
        score = sa.score(input)
        assert score == 3

    def test_seniment_polarity_of_all_negative_tokens_should_be_positive(self):
        input = ['pathetic', 'horrible', 'bad']
        sa = SentimentAnalyzers()
        score = sa.score(input)
        assert score == -3

    def test_seniment_polarity_of_all_neutral_tokens_should_be_positive(self):
        input = ['pathetic', 'horrible', 'bad', 'good', 'nice', 'positive']
        sa = SentimentAnalyzers()
        score = sa.score(input)
        assert score == 0