from collections import defaultdict
strings = ["eat","tea","tan","ate","nat","bat"]

# O(m*n*26) Time | O(N) I think
def groupAnagrams(strs):
    dictionary = {}
    for word in strs:  # This array contains 26 zeroes (one for each letter)
        sWord = "".join(sorted(word)) # This is very weird, but you have to add "".join() in order to make sWord a string lmao
        if sWord in dictionary:
            dictionary[sWord].append(word)
        else:
            dictionary[sWord] = [word] # This right-side brackets are needed for the dictionary to know that we are dealing with a list, not a string
    return list(dictionary.values())

print(groupAnagrams(strings))