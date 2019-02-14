class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for i in range(len(nums)):
            for j in range(len(output)):
                output.append(output[j]+[nums[i]])
        return output
        
        

if __name__=='__main__':
    sl=Solution()
    nums=[1,2,3]
    print(sl.subsets(nums))