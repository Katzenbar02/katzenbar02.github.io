import random
 
def main():

    phrase = get_prepositional_phrase()
    print(f"{phrase}")

def get_determiner():
    # list of determiner
    determiner = ["The", "A", "An", "This", "That",
    "These", "Those", "My", "Your", "His",
    "Her", "Its", "Thier", "A few", "A little",
    "Many", "A lot of", "Some", "Many", "One",
    "Seven", "Ten"]

    return random.choice(determiner)

def get_noun():
    # list of all nouns
    noun = ["apple", "homework", "meat", "professor", "friend",
    "shoe", "broom", "hand", "men",
    "dogs", "girl", "cat", "woman", "bird",
    "children", "adults"]

    return random.choice(noun)

def get_verb():
    """Return a randomly chosen verb
    from this list of verbs:
    "witness", "obey", "hire", "identify", "award",
    "calm", "respect", "pray", "exhaust", "confess",
    "surprise", "steal", "insist", "notice", "feel",
    "point", "chat", "trust", "want", "listen",
    "kick", "recover", "attract", "forget", "select",
    "impress" 
    """

    # list of all verbs
    verb = ["witness", "obey", "hire", "identify", "award",
    "calm", "respect", "pray", "exhaust", "confess",
    "surprise", "steal", "insist", "notice", "feel",
    "point", "chat", "trust", "want", "listen",
    "kick", "recover", "attract", "forget", "select",
    "impress"]

    return random.choice(verb)

def get_preposition():
    # list of all prepositions
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

        