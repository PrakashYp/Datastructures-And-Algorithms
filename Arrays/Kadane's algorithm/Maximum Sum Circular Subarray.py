def maxSubarraySumCircular(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    global_sum = nums[0]
    global_min = nums[0]
    ans = nums[0]
    current_sum = global_sum
    current_min = global_min
    total_sum = nums[0]
    for i in range(1,len(nums)):
        total_sum+=nums[i]
        
        current_sum = max(current_sum+nums[i],nums[i])
        global_sum = max(current_sum,global_sum)

        current_min = min(current_min+nums[i],nums[i])
        global_min = min(current_min,global_min)
       
    ans = max(total_sum-global_min,global_sum)
        
    if ans == 0:
        return global_sum

    return ans


nums =   [-3,-2,-3]
print(maxSubarraySumCircular(nums))