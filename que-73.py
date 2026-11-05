# Que-73
# a= [12, -1, -7, 8, -15, 30, 16, 28]
# K = 3 
# from collections import deque
# def first_negative_in_window(arr, k):
#     q = deque()  
#     result = []    
#     for i in range(k):
#         if arr[i] < 0:
#             q.append(i)            
#     result.append(arr[q[0]] if q else 0)        
#     for i in range(k, len(arr)):
#         if q and q[0] <= i - k:
#             q.popleft()            
#         if arr[i] < 0:
#             q.append(i)            
#         result.append(arr[q[0]] if q else 0)
#     return result
# print(first_negative_in_window(a, K))
