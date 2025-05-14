class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        from collections import Counter

        # Initial frequency count of each letter in the string
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Precompute transition mapping: how each character expands
        transitions = [[] for _ in range(26)]
        for i in range(26):
            count = nums[i]
            transitions[i] = [(i + j + 1) % 26 for j in range(count)]

        # Fast exponentiation over transformation
        def multiply(freq):
            new_freq = [0] * 26
            for i in range(26):
                for target in transitions[i]:
                    new_freq[target] = (new_freq[target] + freq[i]) % MOD
            return new_freq

        def fast_power(freq, t):
            while t > 0:
                if t % 2 == 1:
                    freq = multiply(freq)
                transitions[:] = [ [c for src in group for c in transitions[src]] for group in transitions ]
                t //= 2
            return freq

        final_freq = fast_power(freq, t)
        return sum(final_freq) % MOD
