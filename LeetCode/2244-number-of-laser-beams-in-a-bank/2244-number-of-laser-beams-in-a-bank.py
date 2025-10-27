class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        arr = []
        for i in range(len(bank)):
            cur = 0
            for j in range(len(bank[0])):
                if bank[i][j] == "1":
                    cur += 1
            arr.append(cur)
        print(arr)
        ans = 1
        if len(arr) == 1:
            return 0
        newarr= []
        for i in range(len(arr)):
            if arr[i] != 0:
                newarr.append(arr[i])
        ans =0
        for i in range(1,len(newarr)):
            ans += newarr[i] * newarr[i-1]
        return ans
