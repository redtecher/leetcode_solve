class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        n5=0
        n10=0
        
        for i in range(n+1):
            if i==0:
                continue
            if i%5 == 0 and i%10!=0:
                n5=n5+1
                continue
            if i%10 == 0 :
                n10 = n10+1
                continue

        #print(n2,n5,n10)
        return n5+n10
       
            
        

if __name__=='__main__':
    sl =Solution()
    print(sl.trailingZeroes(100))