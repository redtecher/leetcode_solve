class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        Zlst = []
        for i in range(1000):
            #print(i,Zlst)
            if i==0:
                Zlst.append(0)
                continue
            if i==1:
                Zlst.append(0)
                continue
            flag=0
            for j in range(i):
                #print(i,j)
                if j==0 or j==1:
                    continue
                if i%j==0:
                    flag=1
                    #print('there is a',i,j)
                
            if flag==0:
                Zlst.append(1)
            else:
                Zlst.append(0)
        #print(Zlst)
        count=0
        for i in range(n):
            count = count + Zlst[i]
        return count
                   
                
            
            
        


if __name__=='__main__':
    sl =Solution()
    print(sl.countPrimes(11))
