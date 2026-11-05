# Que-75
# a=[16, 17, 4, 3, 5, 2]
# def find_leaders(arr):
#     size = len(arr)
#     if size == 0:
#         return []        
#     max_from_right = arr[size - 1]
#     leaders = [max_from_right]    
#     for i in range(size - 2, -1, -1):
#         if arr[i] >= max_from_right:
#             max_from_right = arr[i]
#             leaders.append(max_from_right)            
#     leaders.reverse()
#     return leaders

# ans = find_leaders(a)
# print(ans)
