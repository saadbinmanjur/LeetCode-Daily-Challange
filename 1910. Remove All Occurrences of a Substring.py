class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:                # Keep removing while part exists in s
            s = s.replace(part, "", 1)  # Remove the first occurrence of part
        return s