class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n==1:
            return True
        if n==2:
            return True
        if n==3:
            return False
        
            
        p = n
        result = []

        while p !=0:
            getbit = p%2
            result.append(getbit)
            p=p//2

        #print(result)
        flag=0
        for i in range(len(result)):
            if i==0 or i==len(result)-1:
                continue
            #print(result[i],result[i-1],result[i+1])
            if result[i]!=result[i-1] and  result[i]!=result[i+1]:
                flag =0
            else:
                flag=1
                break
        
        if flag==0:
            return True
        else:
            return False
            
        

            
        
        

if __name__=='__main__':
    sl =Solution()
    print(sl.hasAlternatingBits(3))
