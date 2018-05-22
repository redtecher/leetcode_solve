class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)): 
            a = target-nums[i]
            if a in nums:
                y=nums.index(target-nums[i])

                if i==y :
                    continue
                else :


                    result.append(i)
                    result.append(y)
                    break

        
        return result


if __name__=='__main__':
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums,target))
    
                    
                    
                    
        