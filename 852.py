class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        for i in range(length):
            
            if i==0 :
                if  A[i]>A[i+1]:
                    return 0
                else:
                    continue
            if i==length-1 and A[i]>=A[i-1]:
                return length-1
                
            if A[i]>=A[i-1] and A[i]>=A[i+1]:
                return i


if __name__=='__main__':
    sl = Solution()
    A=[0,1,2,3]
    print(sl.peakIndexInMountainArray(A))
    

