from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)


        for word in strs:
            mapping = defaultdict(int)

            for c in word:
                mapping[c] += 1

            mapping = tuple(sorted(mapping.items()))

            res[mapping].append(word)

        
        return list(res.values())
