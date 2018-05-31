#二分查找,逐步逼近

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        start = 0
        end =length-1
        
        while numbers[start]+numbers[end]!=target:
            if numbers[start]+numbers[end]>target:
                end = end-1
            else:
                start = start+1

        return([start+1,end+1])
    
            
        
        




if __name__ == "__main__":
    sl = Solution()
    print(sl.twoSum([3,24,50,79,88,150,345],200))