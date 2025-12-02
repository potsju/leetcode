class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        hmap = defaultdict(set)
        for key,value in points:
            hmap[value].add(key)
        arr = []
        print(hmap)
        size=0
        if len(hmap) < 2:
            return 0

        for key,value in hmap.items():
            if (int(len(value) * (len(value)-1)/ 2)) != 0:    
                arr.append(int(len(value) * (len(value)- 1) /2))
        ans=0
        total = sum(arr)
        for x in arr:
            total -=x
            ans += x * total

        return ans % (pow(10,9) + 7)
    
        