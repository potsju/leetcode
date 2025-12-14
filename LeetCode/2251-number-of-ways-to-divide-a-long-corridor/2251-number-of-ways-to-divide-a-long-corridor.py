class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        a= 0
        numberofs=0
        numberofP=0
        for c in corridor:
            if c == "S":
                numberofs +=1
        if numberofs == 2:
            return 1
        elif numberofs < 2:
            return 0
        elif numberofs % 2 != 0:
            return 0
        DURR = (numberofs / 2) -1
        numseat = 0
        numplant=0
        arr = []
        first = True
        for c in corridor:
            if c == "P" and numseat ==2:
                numplant+=1
            elif c == "S" and numseat == 2 and len(arr) < DURR:
                arr.append(numplant+1)
                numplant = 0
                numseat= 1
                continue
            if c == "S":
                numseat+=1
        mult=1
        print(arr)
        for a in arr:
            mult *=a
        return mult % (pow(10,9) + 7)