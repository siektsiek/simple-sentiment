from tokenizers import SimpleTokenizer
import pytest

class TestTokenizers(object):
    """
    Unit tests for Tokenizer module
    """
    @pytest.mark.parametrize("input, expected", [
        ("foo bar baz"  , ['foo','bar','baz'])  ,
        ("foo baz"      , ['foo', 'baz'])       ,
        (""             , [])                   ,
        ("123 432"      , ["123","432"])        ,
    ])
    def test_tokenizer_splits_string_tokens_on_whitespace(self, input, expected):
        input_string = "foo bar baz"
        tokenizer = SimpleTokenizer()
        tokens = tokenizer.tokenize(input)
        assert expected == tokens

    @pytest.mark.parametrize("input, expected", [
        ("FOOBAZ"   , ['foobaz'])           ,
        ("fOo BAZ"  , ['foo', 'baz'])       ,
    ])
    def test_tokenizer_splits_string_case_sensitive_tokens_on_whitespace(self, input, expected):
        tokenizer = SimpleTokenizer()
        tokens = tokenizer.tokenize(input)
        assert tokens == expected

    @pytest.mark.parametrize("input, expected", [
        ("!!#@$#$%$#%"  , [])       ,
        ("Store?"       , ['store']),
    ])
    def test_tokenizer_removes_non_alphannumeric_chars(self, input, expected):
        tokenizer = SimpleTokenizer()
        tokens = tokenizer.tokenize(input)
        assert tokens == expected

    @pytest.mark.parametrize("input, expected", [
        ("A Foo that bar and for BAZ", ['foo', 'bar', 'baz']),
        ("a and the he where to go"  , []),
    ])
    def test_tokenizer_removes_stop_words(self, input, expected):
        tokenizer = SimpleTokenizer()
        tokens = tokenizer.tokenize(input)
        assert tokens == expected
