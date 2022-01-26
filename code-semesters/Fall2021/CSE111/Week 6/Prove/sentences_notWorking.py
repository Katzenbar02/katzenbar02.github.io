import random
from typing import NoReturn
 
def main():

    phrase = get_prepositional_phrase()
    print(f"{phrase}")

def get_determiner():
    """Return a randomly chosen determiner"""

    # list of determiner
    determiner_singular = ["The", "A", "An", "This", "That",
    "My", "Your", "His","Her", "Its",
    "Thier", "A little",
    "One",]
    determiner_plural = ["The",
    "These", "Those", "My", "Your", "His",
    "Her", "Its", "Thier", "A few",
    "Many", "A lot of", "Some", "Many",
    "Seven", "Ten"]

    determiner = [determiner_singular,determiner_plural]

    return random.choice(determiner)

def get_noun():
    """Return a randomly chosen noun"""

    # list of all nouns
    singular = ["apple", "homework", "meat", "professor", "friend",
    "shoe", "hand", "man"
    "dog", "girl", "cat", "woman", "bird",
    "child", "adult"]
    plural = ["apples", "homework", "meat", "professors", "friends",
    "shoes", "hands", "men"
    "dogs", "girls", "cats", "women", "birds",
    "children", "adults"]

    determiner = get_determiner()

    if determiner == ["The", "A", "An", "This", "That","My", "Your", "His","Her", "Its","Thier", "A little","One"]:
        noun = singular
    else:
        noun = plural
    

    return random.choice(noun)

def get_verb():
    """Return a randomly chosen verb"""

    # list of all verbs
    verb_past = ["witnessed", "obeyed", "hired", "identified", "awarded",
    "calmed", "respected", "prayed", "exhausted", "confessed",
    "surprised", "stole", "insisted", "noticed", "felt",
    "pointed", "chatted", "trusted", "wanted", "listened",
    "kicked", "recovered", "attracted", "forgot", "selected",
    "impressed"]
    verb_present = ["witness", "obey", "hire", "identify", "award",
    "calm", "respect", "pray", "exhaust", "confess",
    "surprise", "steal", "insist", "notice", "feel",
    "point", "chat", "trust", "want", "listen",
    "kick", "recover", "attract", "forget", "select",
    "impress"]
    verb_future = ["witness", "obey", "hire", "identified", "awarded",
    "calmed", "respected", "prayed", "exhausted", "confessed",
    "surprised", "stole", "insisted", "noticed", "felt",
    "pointed", "chatted", "trusted", "wanted", "listened",
    "kicked", "recovered", "attracted", "forgot", "selected",
    "impressed"]
    
    verb = [verb_past,verb_present,verb_future]

    return random.choice(verb)

def get_preposition():
    """Return: a randomly chosen preposition."""

    # list of all prepostions
    preposition = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    return random.choice(preposition)

def get_prepositional_phrase():
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
    quantity: an integer that determines if the
    determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """


    determiner = get_determiner()
    determiner2 = get_determiner()
    noun = get_noun()
    noun2 = get_noun()
    verb = get_verb()
    preposition = get_preposition()

    prepositional_phrase = (f"{determiner} {noun} {verb} {preposition} {determiner2.lower()} {noun2}")

    return prepositional_phrase

main()

        