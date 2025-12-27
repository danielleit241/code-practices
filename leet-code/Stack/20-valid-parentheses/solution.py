class Solution:
    # Time complexity: O(N^2)
    # Space complexity: O(1)
    def isValid_BruteForce(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s: #O(N)
            s = s.replace('()', '') #O(N)
            s = s.replace('[]', '') 
            s = s.replace('{}', '')

        return s == ''

    # Time complexity: O(N)
    # Space complexity: O(N)
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in openToClose:
                if not stack or stack.pop() != openToClose[c]:
                    return False
            else:
                stack.append(c)

        return not stack
