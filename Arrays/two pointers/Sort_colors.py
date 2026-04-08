def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    red_pointer = 0
    current = 0
    blue_pointer = len(nums)-1

    while current <= blue_pointer:
        
        if nums[current] == 0:
            swap = nums[red_pointer]          
            nums[red_pointer] =  nums[current]
            nums[current] = swap
            red_pointer += 1
            current+=1
        elif nums[current] == 2:
            swap = nums[blue_pointer]          
            nums[blue_pointer] =  nums[current]
            nums[current] = swap
            blue_pointer-=1
        
        current+=1
    return nums

nums = [2,0,1]
print(sortColors(nums))