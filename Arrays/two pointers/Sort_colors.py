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
            continue
        current += 1
    return nums

nums = [2,0,1]
print(sortColors(nums))

# def sort_colors(nums):
#     red_count = 0
#     white_count = 0
#     blue_count = 0
#     for num in nums:
#         if num == 0:
#             red_count+=1
#         if num == 1:
#             white_count+=1
#         if num == 2:
#             blue_count+=1

#     print(red_count,white_count,blue_count)
    
#     for i in range(len(nums)):
#         if red_count>0:
#             nums[i] = 0
#             red_count-=1
       
#         elif white_count > 0:
#             nums[i] = 1
#             white_count -= 1
            
#         elif blue_count > 0:
#             nums[i] = 2
#             blue_count -= 1


#     return nums


# nums = [2,0,2,1,1,0]
# print(sort_colors(nums))


