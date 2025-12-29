class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def evalRPN_BruteForce(self, tokens: list[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    operator = tokens[i]
                    left = int(tokens[i - 2])
                    right = int(tokens[i - 1])
                    if operator == '+':
                        result = left + right
                    elif operator == '-':
                        result = left - right
                    elif operator == '*':
                        result = left * right
                    else:
                        result = int(left / right)
                    
                    tokens = tokens[:i - 2] + [str(result)] + tokens[i + 1:]
                    break
        return int(tokens[0])

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def evalRPN_Recursion(self, tokens: list[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            
            right = dfs()
            left = dfs()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            else:
                return int(left / right)
        
        return dfs()

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def evalRPN_Stack(self, tokens: list[str]) -> int:
        numStack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                numStack.append(int(token))
            else:
                num2 = numStack.pop()
                num1 = numStack.pop()
                if token == '+':
                    numStack.append(num1 + num2)
                elif token == '-':
                    numStack.append(num1 - num2)
                elif token == '*':
                    numStack.append(num1 * num2)
                else:
                    numStack.append(int(num1 / num2))

        return numStack[-1]   