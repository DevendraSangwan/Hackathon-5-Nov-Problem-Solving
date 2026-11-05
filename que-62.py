# Que-62
# a= [-1, 0, 1, 2, -1, -4]
# ans=[]
# a.sort()
# first=a[-1]
# second=a[-1]
# for i in range(len(a)-2):
#     if i>0 and a[i]==a[i-1]:
#         continue
#     left=i+1
#     right=len(a)-1
#     while left<right:
#         sum=a[i]+a[left]+a[right]
#         if sum==0:
#             ans.append([a[i],a[left],a[right]])
#             while left<right and a[left]==a[left+1]:
#                 left+=1
#             while left<right and a[right]==a[right-1]:
#                 right-=1
#             left+=1
#             right-=1
#         elif sum<0:
#             left+=1
#         else:
#             right-=1
# print(ans)
