from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            
            mapping = defaultdict(int)

            for c in word:
                mapping[c] += 1

            key = tuple(sorted(mapping.items()))

            anagrams[key].append(word)

        return list(anagrams.values())
