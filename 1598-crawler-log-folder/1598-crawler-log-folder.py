class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log[:-1] == '..':
                if stack:
                    stack.pop()
            elif log[:-1] == '.':
                continue
            else:
                stack.append(log)
        return len(stack)

                