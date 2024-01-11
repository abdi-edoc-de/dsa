class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    # def canMakePaliQueries(s, queries):
        # Initialize prefix sum array
        counts = [[0]*26]
        for i in range(len(s)):
            # Copy previous counts
            count = counts[i][:]
            # Increment count of current character
            count[ord(s[i]) - ord('a')] += 1
            # Append count to prefix sum array
            counts.append(count)
        results = []
        for left, right, k in queries:
            # Calculate character counts for substring
            count = [c2 - c1 for c1, c2 in zip(counts[left], counts[right+1])]
            # Calculate number of odd counts
            odd_count = sum(c % 2 for c in count)
            # Check if palindrome can be formed
            results.append(odd_count // 2 <= k)
        return results