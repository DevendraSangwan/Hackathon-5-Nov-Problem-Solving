# Que-78
# a = [1, 2, 3, 4]
# def product_except_self(nums):
#     length = len(nums)
#     ans = [1] * length
#     left = 1
#     for i in range(length):
#         ans[i] = left
#         left *= nums[i]
#     right = 1
#     for i in range(length - 1, -1, -1):
#         ans[i] *= right
#         right *= nums[i]
#     return ans

# ans = product_except_self(a)
# print(ans)
