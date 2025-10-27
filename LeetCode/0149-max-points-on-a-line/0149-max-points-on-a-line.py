class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        len_points = len(points) 
        if len_points == 1: return 1
        elif len_points == 2: return 2
        else:
            ans = 0
            # get all combination of length 2 from points
            for i in list(combinations(points,2)):
                count = 0
                for j in points:
                    x1,y1  = i[0][0], i[0][1]
                    x2, y2 = i[1][0], i[1][1]
                    x3, y3 = j[0], j[1]
                    if (y3 - y2) * (x2 - x1) == (x3 - x2) * (y2 - y1):
                        count += 1
                ans = max(ans, count)
            return ans