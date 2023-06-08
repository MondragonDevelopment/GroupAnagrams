from collections import defaultdict
strings = ["eat","tea","tan","ate","nat","bat"]

# O(m*n*26) Time | O(N) I think
def groupAnagrams(strs):
    dictionary = {}
    for word in strs:  # This array contains 26 zeroes (one for each letter)
        sWord = "".join(sorted(word))
        if sWord in dictionary:
            dictionary[sWord].append(word)
        else:
            dictionary[sWord] = [word]
    return list(dictionary.values())

print(groupAnagrams(strings))