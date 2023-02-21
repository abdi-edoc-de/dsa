class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inbound = defaultdict(int)
        result = set()
        for frm, to in edges:
            inbound[to] += 1
            inbound[frm] += 0
            if inbound[frm] == 0:
                result.add(frm)
            if to in result:
                result.remove(to)
        return result    