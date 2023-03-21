class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        self.memory[0] = (n, -1, 0)
        self.n = n
    def allocate(self, size: int, mID: int) -> int:
        ind = 0
        while ind < self.n:
            local_size, id, _ = self.memory[ind]
            if id != -1 or local_size < size:
                ind += local_size 
            else:
                left_size = local_size - size
                self.memory[ind] = (size, mID, ind)
                if left_size == 0: return ind
                self.memory[ind+size] = (left_size, -1, ind+size)
                return ind
        return -1
    def free(self, mID: int) -> int:
        num_memory_unit_freed = 0
        for i in range(self.n-1, -1,-1):
            if self.memory[i] == 0: continue
            if self.memory[i][1] == mID:
                freed_size, _, ind = self.memory[i]
                num_memory_unit_freed += freed_size
                self.memory[i] = (freed_size, -1, ind)
            if self.memory[i][1] == -1:
                freed_size, _, ind = self.memory[i]
                if ind + freed_size < self.n and self.memory[ind+freed_size][1] == -1:
                    val = freed_size
                    freed_size += self.memory[ind+freed_size][0]
                    self.memory[ind+val] = 0
                self.memory[i] = (freed_size, -1, i)
            
        return num_memory_unit_freed
    
'''
["Allocator","free","free","free","free","free","allocate","allocate","allocate","free","free","free","allocate","allocate","free","free","free","allocate","allocate","free","allocate","allocate","allocate","free","free","free","free","free","free","free","allocate","free","allocate","free","allocate","allocate","free","allocate","allocate","free","free","allocate","free","free","allocate","allocate","allocate","free","allocate","allocate","free","free","allocate","allocate","allocate","free","allocate","allocate","free","free","free","allocate","free","free","free","free","allocate","allocate","allocate","free","allocate","free","free","allocate","free","allocate","free","free"]
[[100],[27],[12],[53],[61],[80],[21,78],[81,40],[50,76],[40],[76],[63],[25,100],[96,12],[92],[92],[84],[19,71],[22,90],[60],[42,79],[26,41],[59,33],[79],[58],[97],[92],[97],[92],[40],[52,74],[40],[53,17],[17],[36,32],[51,13],[41],[5,87],[44,66],[71],[53],[74,14],[78],[14],[32,54],[45,28],[84,47],[16],[100,78],[5,99],[33],[100],[62,79],[31,32],[85,81],[78],[34,45],[47,7],[7],[84],[6],[35,55],[94],[87],[20],[87],[96,60],[40,66],[28,96],[28],[25,2],[100],[96],[19,35],[16],[92,42],[80],[79]]
'''       
        

'''
    [(10,-1), 0, 0, 0, 0, 0, 0, 0, 0, 0]
    [(1,1), (9,-1), 0, 0, 0, 0, 0, 0, 0, 0]
    [(1,1), (1,2), (8, -1), 0, 0, 0, 0, 0, 0, 0]
    [(1,1), (1,2), (1,3), (7,-1), 0, 0, 0, 0, 0, 0]
    [(1,1), (1,-1), (1,3), (7,-1), 0, 0, 0, 0, 0, 0]
    [(1,1), (1,-1), (1,3), (3,4), (4,-1), 0, 0, 0, 0, 0]
    [(1,1), (1,1), (1,3), (3,4), (4,-1), 0, 0, 0, 0, 0]
    [(2,-1), 0, (1,3), (3,4), (4,-1), 0, 0, 0, 0, 0]
    [(2,-1), 0, (1,3), (3,4), 0, 0, (4,-1), 0, 0, 0]
    [(2,-1), 0, (1,3), (3,4), (4,-1), 0, 0, 0, 0, 0]
    
["Allocator","allocate","allocate","allocate","free","free","free","allocate","allocate","allocate","free","allocate","free"]
[[10],[1,1],[1,2],[1,3],[1],[2],[3],[3,4],[1,1],[1,1],[1],[10,2],[7]]
'''
# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)