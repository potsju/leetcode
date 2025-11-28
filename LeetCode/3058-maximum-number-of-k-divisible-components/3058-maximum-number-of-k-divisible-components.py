from collections import defaultdict
from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        ans = 0

        def dfs(node):
            nonlocal ans
            visited.add(node)
            total = values[node]

            for nei in adj[node]:
                if nei not in visited:
                    total += dfs(nei)

            if total % k == 0:
                ans += 1
                return 0  # this component gets cut

            return total

        dfs(0)
        return ans
