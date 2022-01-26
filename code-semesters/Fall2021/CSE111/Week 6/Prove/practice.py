import random

get_noun_s = ["job ","litter ", "bank "]
get_noun_p = ["jobs ","litters ", "banks "]
get_determiner_s = ["The ","A ", "One "]
get_determiner_p = ["Some ","Those ", "Ten "]
get_verb = ["ran","plundered", "spits"]

determiner = random.choice(get_determiner_s)

if determiner == "Those " or "Some " or "Ten ":
    noun = random.choice(get_noun_p)
else:
    noun = random.choice(get_noun_s)

verb = random.choice(get_verb)

print(f"{determiner} {noun} {verb}")
