import pytest
from utils.strings import reverse_words

class TestReverseWords:
    def test_basic(self):
        assert reverse_words("hello world foo") == "foo world hello"

    def test_single_word(self):
        assert reverse_words("hello") == "hello"

    def test_empty_string(self):
        assert reverse_words("") == ""

    def test_two_words(self):
        assert reverse_words("good morning") == "morning good"
