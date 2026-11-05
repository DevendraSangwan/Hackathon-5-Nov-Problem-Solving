# que-76
# a = [100, 4, 200, 1, 3, 2]
# def longest_sequence(nums):
#     if not nums:
#         return 0
#     nums.sort()
#     longest = 1
#     current_streak = 1
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             continue
#         if nums[i] == nums[i-1] + 1:
#             current_streak += 1
#         else:
#             if current_streak > longest:
#                 longest = current_streak
#             current_streak = 1
#     if current_streak > longest:
#         longest = current_streak
#     return longest

# ans = longest_sequence(a)
# print(ans)
