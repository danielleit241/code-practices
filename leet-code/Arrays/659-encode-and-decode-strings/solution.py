class Solution:
    #Time Complexity: O(N)
    #Space Complexity: O(N)
    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s;    
        return res

    #Time Complexity: O(N)
    #Space Complexity: O(N)
    def decode(self, s: str) -> list[str]:
        if not s:
            return []
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res
    

solution = Solution()
print(solution.encode(["we","say",":","yes","!@#$%^&*()"]))
print(solution.decode("2#we3#say1#:3#yes10#!@#$%^&*()"))