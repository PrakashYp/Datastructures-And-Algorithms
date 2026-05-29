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



nums =  [10,20,-30,-1,40]

print(maxSubArray(nums))


