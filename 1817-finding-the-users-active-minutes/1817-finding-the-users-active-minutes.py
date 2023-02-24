class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users , result = defaultdict(set), [0] * k
        for i, time in logs:
            users[i].add(time)
        for _, times in users.items():
            result[len(times)-1] += 1
        return result