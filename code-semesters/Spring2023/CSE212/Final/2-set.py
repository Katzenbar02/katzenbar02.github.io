def are_anagrams(string1, string2):
    set1 = set(string1.lower())
    set2 = set(string2.lower())
    return set1 == set2

# Example usage
word1 = "listen"
word2 = "silent"
result = are_anagrams(word1, word2)
print(result)  # Output: True
