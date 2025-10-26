class Solution(object):
    def countStableSubarrays(self, A):
        count = defaultdict(Counter)
        res = pre = 0
        for i, a in enumerate(A):
            res += count[a][pre - a]
            pre += a
            count[a][pre] += 1
            if a == 0 and i > 0 and A[i - 1] == 0:
                res -= 1
        return res