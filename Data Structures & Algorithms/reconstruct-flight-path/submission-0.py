class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()
        for fro, to in tickets: 
            adj[fro].append(to)
        res = ["JFK"]
        def dfs(src): 
            if len(res) == len(tickets) + 1: 
                return True
            if src not in adj: 
                return False
            temp = list(adj[src])

            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res



