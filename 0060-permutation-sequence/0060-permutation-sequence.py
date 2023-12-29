class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of numbers from 1 to n
        nums = list(range(1, n + 1))
        k -= 1  # Convert k to 0-based index

        # Initialize variables for the result and factorial
        result = []
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        # Generate the kth permutation
        for i in range(n, 0, -1):
            index = k // factorial[i - 1]
            result.append(str(nums.pop(index)))
            k %= factorial[i - 1]

        return ''.join(result)

# Example usage:
# solution = Solution()
# print(solution.getPermutation(3, 3))  # Output: "213"
# print(solution.getPermutation(4, 9))  # Output: "2314"
# print(solution.getPermutation(3, 1))  # Output: "123"
