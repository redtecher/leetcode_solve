# class Solution(object):
#     def maxCount(self, m, n, ops):
#         """
#         :type m: int
#         :type n: int
#         :type ops: List[List[int]]
#         :rtype: int
#         """
#         initial =[]
#         single = []
#         for i in range(n):
#             for j in range(m):
#                 single.append(0)
#             initial.append(single)
#             single=[]
#         for op in ops:
#             for j in range(0,op[1]):
#                 for i in range(0,op[0]):
#                     initial[j][i]=initial[j][i]+1
#         maxm = -1
#         for row in initial:
#             for num in row:
#                 if num >maxm:
#                     maxm=num
#                     record=1
#                     continue
#                 if num ==maxm:
#                     record=record+1
        
#         return record
# 
# 
#       不能用暴力求解 注意40000的规模            
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        x=[]
        y=[]
        if ops ==[]:
            return m*n
        for op in ops:
            x.append(op[0])
            y.append(op[1])
        
        return min(x)*min(y)
                           

        

if __name__=='__main__':
    sl=Solution()
    # ops = [[2,2],[3,3]]
    ops=[]
    print(sl.maxCount(3,3,ops))