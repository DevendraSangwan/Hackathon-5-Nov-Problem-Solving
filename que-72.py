# que-72
# a = [2, 1, 5, 1, 3, 2]
# K = 3
# def max_sum_subarray(arr, K):
#     if len(arr) < K:
#         return 0    
#     window_sum = sum(arr[:K])
#     max_sum = window_sum    
#     for i in range(len(arr) - K):
#         window_sum = window_sum - arr[i] + arr[i + K]
#         max_sum = max(max_sum, window_sum)
#     return max_sum

# print(max_sum_subarray(a, K))
