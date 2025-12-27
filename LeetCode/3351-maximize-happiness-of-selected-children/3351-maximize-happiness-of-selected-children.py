class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse = True)
        sum =0
        iter=0
        print(happiness)
        while iter < k:
            if iter >1:
                if happiness[iter] - (iter) <=0:
                    break
            sum += happiness[iter]
            if iter>= 1:
                sum -= (iter)
            iter+=1
        return sum