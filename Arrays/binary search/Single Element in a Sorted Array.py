def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    low = 0 
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if mid % 2 == 1:
            mid -=1
        
        if nums[mid] == nums[mid+1]:
            low = mid + 2
        else:
            high = mid - 1

    return nums[low] 
            
        

nums = [1,1,2]

print(singleNonDuplicate(nums))

