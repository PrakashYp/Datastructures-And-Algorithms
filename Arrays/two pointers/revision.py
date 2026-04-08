def rearrangeArray(nums):
    ans_list = [0] * len(nums)
    pos = 0
    neg = 1

    for i in range(len(nums)):
        if nums[i]>0:
            ans_list[pos] = nums[i]
            pos += 2
        elif nums[i]<0:
            ans_list[neg] = nums[i]
            neg += 2
        
    return ans_list


def removeDuplicates(nums):
    k=1
    for num in nums:
        if num > nums[k-1]:
            nums[k] = num
            k+=1
    return nums

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))