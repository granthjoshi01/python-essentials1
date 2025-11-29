class Solution:
    def closestNumber(self, n, m):
        # q stores floor value of division
        q = n // m
        
        #calculate the numbers that are closest to n
        closest1 = q * m
        closest2 = (q + 1) * m
        
        #calculate these numbers absolute distance from n
        dist1 = abs(n - closest1)
        dist2 = abs(n - closest2)
        
        #compare these distances 
        if  dist1 < dist2:
             return closest1
        elif dist1 > dist2:
            return closest2
        else:  
            #compare these numbers
            if abs(closest1) > abs(closest2):
                return closest1
            else:
                return closest2