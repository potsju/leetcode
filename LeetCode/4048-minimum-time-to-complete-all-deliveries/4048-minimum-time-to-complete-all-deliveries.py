class Solution(object):
    def minimumTime(self, d, r):
        low = 0
        temp = (d[0] + d[1]) * max(r[0], r[1])
        high = max(100, temp)
        while low <= high:
            mid = (low + high) // 2
            x1 = mid - mid // r[0]
            x2 = mid - mid // r[1]
            gcdd = self.gcd(r[0], r[1])
            x = (r[0] // gcdd) * r[1]
            x3 = mid - (mid // r[0] + mid // r[1] - mid // x)
            if x1 >= d[0] and x2 >= d[1] and x1 + x2 - x3 >= d[0] + d[1]:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a