def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low = 0 
    high = len(nums) - 1


    while low < high:
        mid = low + (high - low ) // 2
        if nums[mid+1] > nums[mid]:
            low = mid + 1
        elif nums[mid] > nums[mid+1]: 
            high = mid 
        

    return high

nums = [1,2,3,1]
print(findPeakElement(nums))

