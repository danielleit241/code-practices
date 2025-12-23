class Solution:
    def groupAnagrams_BruteForce(self, strs: list[str]) -> list[list[str]]:
        anagrams = []
        visited = [False] * len(strs)
        for i in range(len(strs)):
            if visited[i]:
                continue
            group = [strs[i]]
            for j in range(i + 1, len(strs)):
                if(sorted(group[0]) == sorted(strs[j]) and not visited[j]):
                    group.append(strs[j])
                    visited[j] = True
            anagrams.append(group)
            visited[i] = True
        return anagrams
    
    def groupAnagrams_HashMap_Count(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)] = anagrams.get(tuple(count), []) + [s]
        return list(anagrams.values())
    
    def groupAnagrams_HashMap(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return list(anagrams.values())

solution = Solution()
print(solution.groupAnagrams_HashMap(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams_HashMap([""]))