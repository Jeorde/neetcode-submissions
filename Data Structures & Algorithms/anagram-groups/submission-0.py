class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        
        for word in range(len(strs)):
            count = [0] * 26
            for letter in strs[word]:
                index = ord(letter) - ord("a")
                count[index] += 1
            

            key = tuple(count)
            if key not in group:
                group[key] = []
            group[key].append(strs[word])
        return list(group.values())