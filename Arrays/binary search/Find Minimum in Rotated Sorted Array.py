def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    min_value = float('inf')
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid]>= nums[high]:
            low = mid + 1 
        elif nums[mid] <= nums[high]:
            high = mid - 1
        min_value = min(min_value,nums[mid])
        
    return min_value


nums = [3,1,2]

print(findMin(nums))



