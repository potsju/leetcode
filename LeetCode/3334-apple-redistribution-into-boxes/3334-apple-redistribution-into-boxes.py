class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        capacity.sort(reverse = True)
        total = sum(apple)
        print(apple)
        print(capacity)
        print(total)
        iterations = 0
        for c in capacity:
            if total - c > 0:
                total -=c
                iterations+=1
            else:
                return iterations+1
        return iterations