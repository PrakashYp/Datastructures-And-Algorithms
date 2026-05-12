def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    window_sum = nums[0]

    for i in range(1,len(nums)):        
        window_sum = max(window_sum+nums[i],nums[i])
        max_sum = max(window_sum,max_sum)


    print(window_sum)

    return max_sum



nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(nums))


