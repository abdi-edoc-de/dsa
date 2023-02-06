class DetectSquares:
    def __init__(self):
        self.x_dict = defaultdict(set)
        self.y_dict = defaultdict(set)
        self.counts = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_dict[x].add(y)
        self.y_dict[y].add(x)
        self.counts[(x, y)] += 1
        

    def count(self, point: List[int]) -> int:
        x_dict = self.x_dict
        y_dict = self.y_dict
        counts = self.counts
        
        x, y = point
        res = 0
        
        if x not in x_dict or y not in y_dict:
            return 0
        
        for cand_x in y_dict[y]:

            if cand_x == x:
                continue
            
            length = x - cand_x
            
            cand_y = y - length
            multiplier = counts[(cand_x, y)]
            if cand_y in x_dict[cand_x] and cand_y in x_dict[x]:
                multiplier *= counts[(cand_x, cand_y)]
                multiplier *= counts[(x, cand_y)]
                res += multiplier 
            
            cand_y = y + length
            multiplier = counts[(cand_x, y)]
            
            if cand_y in x_dict[cand_x] and cand_y in x_dict[x]:
                multiplier *= counts[(cand_x, cand_y)]
                multiplier *= counts[(x, cand_y)]
                res += multiplier 
                
        return res