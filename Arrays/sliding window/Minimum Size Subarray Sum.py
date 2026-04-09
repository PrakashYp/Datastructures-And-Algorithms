#Minimum Size Subarray Sum


#My Logic for this problem
# def minSubArrayLen(target, nums):
#     """
#     :type target: int
#     :type nums: List[int]
#     :rtype: int
#     """
#     min_len  = float('inf')
#     sum_total = 0
#     left = 0
#     for right in range(len(nums)):
#         sum_total+=nums[right]
#         if sum_total >= target:
#             min_len = min(min_len,right-left+1)
#         print(sum_total)
#         while sum_total >= target:
#             sum_total-=nums[left]
#             left+=1
#             if sum_total>= target:
#                 min_len = min(min_len,right-left+1)
        
        
#     if min_len >= float('inf') :
#         return 0
#     return min_len 






def minSubArrayLen(target, nums):
    min_len = float('inf')
    sum_total = 0
    left = 0

    for right in range(len(nums)):
        sum_total += nums[right]

        while sum_total >= target:
            min_len = min(min_len, right - left + 1)
            sum_total -= nums[left]
            left += 1

    if min_len == float('inf'):
        return 0

    return min_len

target = 6
nums =[10,2,3]
print(minSubArrayLen(target,nums))



        