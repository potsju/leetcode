class Solution(object):
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        k -= 1  # 0-index
        res = []

        for i in range(n, 0, -1):
            idx = k // fact[i - 1]
            res.append(nums[idx])
            nums.pop(idx)
            k %= fact[i - 1]

        return "".join(res)
