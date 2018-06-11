lst = [1,2,3,4,5,6,7]
print(lst.__dir__)
k=3
lst = lst[-3:]+lst[:-3]
print(lst.__dir__)

lst[:k],lst[k:]=lst[-k:],lst[:-k]
print(lst.__dir__)