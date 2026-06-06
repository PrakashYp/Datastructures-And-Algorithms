def maximumUniqueSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left = 0
    count = set()
    count.add(nums[left])
    maximum_sum = 0
    current_sum = nums[left]
    
    for right in range(1,len(nums)):
       


        while nums[right] in count:
            sub=count.remove(nums[left])
            current_sum -= nums[left]
            left+=1
        count.add(nums[right])
        current_sum += nums[right]
        maximum_sum = max(maximum_sum,current_sum)
       

    return maximum_sum


nums = [5,2,1,2,5,2,1,2,5]

print(nums[:])
# print(maximumUniqueSubarray(nums))
