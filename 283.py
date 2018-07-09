class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag=0
        result=[]
        for i in nums:
            if i==0:
                flag=flag+1
            else:
                result.append(i)
        
        for j in range(flag):
            result.append(0)
        return result
                
            
        

if __name__=='__main__':
    sl = Solution()
    a= [0,1,0,3,12]
    print(sl.moveZeroes(a))
    