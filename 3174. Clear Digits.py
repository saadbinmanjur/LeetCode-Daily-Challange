class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char.isdigit():
                if stack:  # Remove the closest left letter
                    stack.pop()
            else:
                stack.append(char)  # Push letters to stack

        return "".join(stack)