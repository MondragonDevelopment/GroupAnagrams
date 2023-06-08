from collections import defaultdict
strings = ["eat","tea","tan","ate","nat","bat"]

# O(m*n*26) Time | O(N) I think
def groupAnagrams(strs):
    dictionary = defaultdict(list)
    for word in strs:
        count = [0] * 26  # This array contains 26 zeroes (one for each letter)
        for c in word:
            count[ord(c) - ord("a")] += 1  # Reseting ascii values
        dictionary[tuple(count)].append(word)
    return dictionary.values()

print(groupAnagrams(strings))