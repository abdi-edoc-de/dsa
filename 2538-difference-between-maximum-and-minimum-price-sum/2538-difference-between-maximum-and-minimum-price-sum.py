class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph , msg, result = defaultdict(list), {}, 0
        for frm, to in edges:
            graph[frm].append(to)
            graph[to].append(frm)
        def bot_up(cur = 0, par = -1):
            nonlocal result
            res = 0
            for nei in graph[cur]:
                if nei != par:
                    msg[nei, cur] = bot_up(nei, cur)
                    res = max(res, msg[nei, cur])
                    result = max(result,res)
            return res + price[cur]
        def top_dwn(cur=0, par=-1):
            nonlocal result
            arr = [msg[k, cur] for k in graph[cur] ]
            arr.append(0)
            max_val = max(arr)
            ind = arr.index(max_val)
            arr[ind] = 0
            sec_max = max(arr)
            for i, nei in enumerate(graph[cur]):
                if nei != par:
                    if i == ind:
                        msg[cur, nei] = sec_max + price[cur]
                    else:
                        msg[cur,nei] = max_val + price[cur]
                    result = max(result, msg[cur,nei])
                    top_dwn(nei, cur)
        bot_up()
        top_dwn()
        return result
                    
                    
            