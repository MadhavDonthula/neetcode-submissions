class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        overall_hash = defaultdict(list)
        for st in strs:
            check = [0] * 26 
            for c in st: 
                check[ord(c) - ord("a")] += 1
            overall_hash[tuple(check)].append(st)
        
        return list(overall_hash.values())
                


