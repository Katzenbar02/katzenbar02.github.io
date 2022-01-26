from sentences import get_determiner, \
    get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest

def test_get_determiner():

    assert get_determiner("Those; ") == "Those"


def test_get_noun():

    assert get_noun("meat;") == "meat"


def test_get_verb():

    assert get_verb("obey; ") == "obey"

def test_get_preposition():

    assert get_preposition("under; ") == "under"

def test_get_prepositional_phrase():

    assert get_prepositional_phrase("Those meat obey under those meat") == "Those meat obey under those meat"

pytest.main(["-v", "--tb=line", "-rN", __file__])