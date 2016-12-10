import pytest

import solution001 as solution


def test():
    assert solution.abbreviations("word") == "word"
    assert solution.abbreviations("localization") == "l10n"
    assert solution.abbreviations("internationalization") == "i18n"
    assert solution.abbreviations("pneumonoultramicroscopicsilicovolcanoconiosis") == "p43s"
