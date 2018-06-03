class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lstplus=[]
        lstminus=[]
        for i in range(100000):
            lstplus.append(0)
            lstminus.append(0)

        for i in nums:
            if i>=0:
                lstplus[i]=lstplus[i]+1
            else:
                
                lstminus[-i]=lstminus[-i]+1
                
        for i in range(100000):
            if  lstplus[i]==1:
                return i
            if   lstminus[i]==1:
                
                return -i
        
                
        

        

if __name__=='__main__':
    sl =Solution()
    print(sl.singleNumber([-1]))