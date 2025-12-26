class Solution:
    # Time Complexity: O(N^2 * M)
    # Space Complexity: O(M)
    def minWindow_BruteForce(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        map_t = {}
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1

        need = len(map_t)
        min_len = float('inf')
        min_start = 0
        for i in range(len(s)):
            window = {}
            matched = 0
            for j in range(i, len(s)):
                c = s[j]
                window[c] = window.get(c, 0) + 1

                if c in map_t and window[c] == map_t[c]:
                    matched += 1

                if matched == need:
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        min_start = i
                    break
        
        return "" if min_len == float('inf') else s[min_start:min_len + min_start]

    # Time Complexity: O(N)
    # Space Complexity: O(M)
    def minWindow_SlidingWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        map_t = {}
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1
        need = len(map_t)

        left, matched, min_start = 0, 0, 0
        min_len = float('inf')
        window = {}

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in map_t and window[c] == map_t[c]:
                matched += 1

            while matched == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                c_left = s[left]
                if c_left in map_t and window[c_left] == map_t[c_left]:
                    matched -= 1

                window[c_left] -= 1
                left += 1
        
        return "" if min_len == float('inf') else s[min_start:min_len + min_start] 

