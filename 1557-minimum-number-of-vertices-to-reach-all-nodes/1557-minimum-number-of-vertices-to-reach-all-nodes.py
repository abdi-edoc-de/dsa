class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inbound = defaultdict(int)
        for frm, to in edges:
            inbound[to] += 1
            inbound[frm] += 0
        return [key for key, value in inbound.items() if value == 0]
    