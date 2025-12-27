class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        numy=0
        for c in customers:
            if c == "Y":
                numy+=1
        arr= [numy]
        penalty=0
        for i in range(0,len(customers)):
            if customers[i] == "N":
                penalty+=1
                arr.append(numy + penalty)
       
            elif customers[i] == "Y":
                numy-=1
                arr.append(numy + penalty)
            
        return arr.index(min(arr))
            

