class Solution:
    def racecar(self, target: int) -> int:
        heap = [(0,0,1),(0,0,-1)]
        visited = set()
        while heap:
            step, pos, speed = heappop(heap)
            if pos < 0:
                continue
            if (pos,speed) in visited:
                continue
            visited.add((pos,speed))
            if pos == target:
                return step
            heappush(heap,(step+1,pos+speed,speed*2))
            if speed <= 0:
                heappush(heap,(step+1, pos,1))
            else:
                heappush(heap,(step+1, pos,-1))