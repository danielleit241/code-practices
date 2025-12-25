class Solution:
    def characterReplacement_BruteForce(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            max_freq = 0
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                if j - i + 1 - max_freq <= k:
                    res = max(res, j - i + 1)
                else:
                    break
        return res

    def characterReplacement_HashMap(self, s: str, k: int) -> int:
        count = {}
        left, max_freq, res = 0, 0, 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            while right - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res

    def characterReplacement_Array(self, s: str, k: int) -> int:
        count = [0] * 26
        left, max_freq, res = 0, 0, 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])

            while right - left + 1 - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res