class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:k],nums[k:]=nums[-k:],nums[:-k]
        
        

        


if __name__ == '__main__':
    sl =Solution()
    print(sl.rotate([1],0))
    
