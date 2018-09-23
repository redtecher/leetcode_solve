class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while(i<len(nums)-1):
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
            else:
                i=i+1

        return len(nums)
            
        

if __name__ == "__main__":
    sl =Solution()
    sl.removeDuplicates([0,0,1,1,1,2,2,3,3,4])