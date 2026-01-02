class Solution:
    def largestRectangleArea_BruteForce(self, heights: list[int]) -> int:
        n = len(heights)
        res = 0
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                res = max(res, min_height * (j - i + 1))
        return res

    def largestRectangleArea_Stack(self, heights: list[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)

        n = len(heights)
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            res = max(res, height * width)
        
        return res
            
    def largestRectangleArea_Optimize(self, heights: list[int]) -> int:
        stack = []
        heights.append(0)
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)

        return res         