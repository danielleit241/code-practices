class Solution:
    def dailyTemperatures_BruteForce(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        return res

    def dailyTemperatures_Stack(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                colder = stack.pop()
                res[colder] = i - colder
            stack.append(i)
        return res
    
solution = Solution()
print(solution.dailyTemperatures_BruteForce([73,74,75,71,69,72,76,73]))  # Output: [1,1,4,2,1,1,0,0]
print(solution.dailyTemperatures_BruteForce([30,40,50,60]))  # Output: [1,1,1,0]
print(solution.dailyTemperatures_BruteForce([30,60,90]))  # Output: [1,1,0]