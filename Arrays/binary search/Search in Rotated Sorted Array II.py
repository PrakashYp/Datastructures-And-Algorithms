def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    low = 0
    high = len(nums) - 1

    while low<=high:
        mid = low + (high-low) // 2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[high]:
            high -= 1
        elif nums[mid] <= nums[high]:
            if nums[mid] < target < nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[mid] < target < nums[high]:
                low = mid + 1 
            else:
                high = mid - 1 
    return False



nums=[1,0,1,1,1]
target = 0
print(search(nums,target))




    


