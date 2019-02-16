class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # if m==1 or n==1:
        #     return 1
        # else:
        #     return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)

        # C(N-1,M+N-2)
        lowsum=1
        upsum=1
        
        for i in range(m,m+n-1):
            # print(i)
            upsum = upsum*i
        for j in range(1,n):
            # print(j)
            lowsum=lowsum*j
        # print(upsum,lowsum)
        result = upsum//lowsum
        return result


        

if __name__=='__main__':
    sl=Solution()
    
    print(sl.uniquePaths(7,3))