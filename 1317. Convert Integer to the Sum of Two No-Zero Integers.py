class Solution(object): 
    def getNoZeroIntegers(self, n): 
        return next([i, n - i] for i in range(1, n) if '0' not in str(i) and '0' not in str(n - i))