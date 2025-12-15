class Solution:

    # O(n^2) Time | O(1) Space
    def isAnagram_BruteForce(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_list = list(s)
        for char in t:
            if char in s_list:
                s_list.remove(char)
            else:
                return False
        return len(s_list) == 0

    # O(nlogn) Time | O(1) Space
    def isAnagram_Sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # O(n) Time | O(n) Space
    def isAnagram_HashMap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        for char_s, char_t in zip(s, t):
            char_count[char_s] = char_count.get(char_s, 0) + 1
            char_count[char_t] = char_count.get(char_t, 0) - 1

        for count in char_count.values():
            if count != 0:
                return False
        return True

    # O(n) Time | O(1) Space
    def isAnagram_Count(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1
        
        return all(c == 0 for c in count)

    def isAnagram_Set(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
            if i not in t:
                return False
        return True