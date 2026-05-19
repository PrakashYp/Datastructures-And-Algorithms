def maxAbsoluteSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    min_sum = 0 
    max_sum = 0
    current_max = 0
    current_min = 0
    abs_max = 0

    for i in range(len(nums)):
        current_max = max(current_max+nums[i],nums[i])
        max_sum  = max(current_max,max_sum)

        current_min = min(nums[i]+current_min,nums[i])
        min_sum = min(current_min,min_sum)

    abs_max = max(abs(min_sum),max_sum,abs_max)

    return abs_max

nums =  [2,-5,1,-4,3,-2]

print(maxAbsoluteSum(nums))

