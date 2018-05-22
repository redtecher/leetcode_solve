class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        lst = []
        if x>0:
            flag =1
        else:
            flag =-1
            x=-x

        while x!= 0:
            newnum=x%10
            x=x//10
            lst.append(newnum)
        
        length =len(lst)-1
        lt =range(length+1)
        
        result =0
        for i in lt:
        
            result = result+lst[i]*(10**(length-i))

        result = result*flag
        if result>2147483647 or result<-2147483648:
            
            return 0 
        return result
        

            
            
            
                
        
            
        





if __name__ == "__main__":

    sl = Solution()
    print(sl.reverse(1534236469))
    