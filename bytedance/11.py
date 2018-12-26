# 暴力方法求解
# 
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         maxn =-99999
#         recordstart=0
#         recordend = 0
#         length = len(prices)
#         for start in range(length):
#             for end in range(start,length):
                 
#                 if prices[end]-prices[start]>maxn:
#                     maxn =prices[end]-prices[start]
#                     recordend=end
#                     recordstart=start
        
#         if maxn<0:
#             maxn=0

#         # print(maxn,recordend,recordstart)
#         return maxn  
class Solution(object):
    def maxProfit(self, prices):
        currentprice =0
        for i in prices:
            
            
            
        

if __name__=='__main__':
    sl=Solution()
    prices=[7,1,5,9,6,4]
    sl.maxProfit(prices)