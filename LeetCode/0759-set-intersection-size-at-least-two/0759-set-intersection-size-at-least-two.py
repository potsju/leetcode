class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        interval = sorted(intervals, key=lambda x: (x[1], -x[0]))
        a = -1 
        b = -1
        total = 0
        for i in range(len(interval)):
            l, r = interval[i]

            # Case 1: no selected points inside [l, r]
            if b < l:
                total += 2
                a = r - 1
                b = r

            # Case 2: only one selected point inside
            elif a < l <= b:
                total += 1
                a = b
                b = r

            # Case 3: already have 2 points inside → add nothing
            else:
                pass

        return total
