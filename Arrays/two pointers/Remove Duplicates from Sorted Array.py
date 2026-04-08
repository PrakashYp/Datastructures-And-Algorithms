def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    k=0
    left=1
    for i in range(len(nums)):
        if nums[i]> nums[left-1]:
            nums[left] = nums[i]
            left+=1
        
    print(left)
    return nums
nums = [1,1,2]

print(removeDuplicates(nums))



