class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:k],nums[k:]=nums[-k:],nums[:-k]
        
'''
lst = [1,2,3,4,5,6,7]
print(lst.__dir__)
k=3
lst = lst[-3:]+lst[:-3]
print(lst.__dir__)

lst[:k],lst[k:]=lst[-k:],lst[:-k]
print(lst.__dir__)


开始时候  我使用的nums = nums[-k:]+nums[:-k] 赋值  但是 一直通过不了  而且无法改变nums
最后写了 上方代码  分析发现  如果直接改变数组再重新赋值的话  原来的nums的地址发生改变
只有对数组元素赋值才能对源数组改变 
'''       

        


if __name__ == '__main__':
    sl =Solution()
    print(sl.rotate([1],0))
    
