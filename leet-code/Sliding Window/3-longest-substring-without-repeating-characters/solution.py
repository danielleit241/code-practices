class Solution:
    # Time Complexity: O(N^2)
    # Space Complexity: O(M) where M is the size of the character set 
    def lengthOfLongestSubstring_BruteForce(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            res = max(res, j - i)
        return res
    

    # Time Complexity: O(N)
    # Space Complexity: O(M) where M is the size of the character set
    def lengthOfLongestSubstring_Set(self, s: str) -> int:
        seen = set()
        left, right, res = 0, 0, 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res
    

    # Time Complexity: O(N)
    # Space Complexity: O(M) where M is the size of the character set
    def lengthOfLongestSubstring_Hashmap(self, s: str) -> int:
        mp = {}
        left, res = 0, 0
        for right in range(len(s)):
            if s[right] in mp:
                left = max(left, mp[s[right]] + 1)
            mp[s[right]] = right
            res = max(res, right - left + 1)
        return res