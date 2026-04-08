# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     count = 0
#     left = 0
#     for i in range(0,len(nums)):
#         if nums[i-1]==nums[i]:
#             count +=1
#             if count<3:
#                 left = count
#     print(count,left)

def removeDuplicates(nums):
    write = 2

    for i in range(2,len(nums)):
        if nums[i] != nums[write]:
            nums[write] = nums[i]
            write += 1

    return write,nums





nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

    



