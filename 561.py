class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        length = len(nums)
        result = 0
        for i in range(length):
            if i%2==0:
                result = result+nums[i]
        print(result)
        return result
                
        



if __name__=='__main__':

    sl = Solution()
    nums=[1,4,3,2]
    sl.arrayPairSum(nums)