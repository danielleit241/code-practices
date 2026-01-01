class Solution:
    # Time Complexity: O(N log N)
    # Space Complexity: O(N)
    def carFleet_Stack(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = []
        for p, s in cars:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    
    # Time Complexity: O(N log N)
    # Space Complexity: O(n)
    def carFleet_Iteration(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = 1
        prevTime = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            currTime = (target - cars[i][0]) / cars[i][1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime

        return fleets

solution = Solution()
print(solution.carFleet_Stack(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3
print(solution.carFleet_Iteration(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 3