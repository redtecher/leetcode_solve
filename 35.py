class Solution:
    def searchInsert(self, nums, target):
        length = len(nums)
        if nums[-1]<target:
            return length
        if nums[0]>target:
            return 0
        for i in range(length):

            if nums[i]==target:
                return i
            elif nums[i]<target and nums[i+1]>target:
                return i+1

if __name__ =='__main__':
    sl = Solution()
    print(sl.searchInsert([1,3,5,6], 7))




        