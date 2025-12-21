import re

class Solution:
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    def isPalindrome_Deque(self, s: str) -> bool:
        from collections import deque
        dp = deque()
        for i in range(len(s)):
            if s[i].isalnum():
               dp.append(s[i].lower()) 

        while len(dp) > 1:
            if dp.popleft() != dp.pop():
                return False
        return True

    #Time Complexity: O(n)
    #Space Complexity: O(n)
    def isPalindrome_ReverseString(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        return s == s[::-1]

    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def isPalindrome_TwoPointer(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def isPalindrome_OptimizeTwoPointer(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            else: 
                left += 1
                right -= 1
        return True