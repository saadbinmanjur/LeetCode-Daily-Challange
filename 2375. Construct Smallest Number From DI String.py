class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))  # Push the next available number onto the stack
            
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())  # Pop all elements from stack to maintain order
        
        return "".join(result)