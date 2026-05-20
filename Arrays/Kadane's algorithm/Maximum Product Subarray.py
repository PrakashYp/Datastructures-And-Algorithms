def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_min = nums[0]
    current_max = nums[0]
    result = nums[0]
    for i in range(1,len(nums)):
        temp_max = max(nums[i],nums[i]*current_max,nums[i]*current_min)
        temp_min = min(nums[i],nums[i]*current_max,nums[i]*current_min)
        current_max = temp_max
        current_min = temp_min

        result = max(result,current_max)

    return result



print(maxProduct([2, 3, -2, 4]))




