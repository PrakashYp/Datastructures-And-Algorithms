
def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    frequency_sum={}
    
    for i in range(len(nums)):
        sub = target-nums[i]
        if sub in frequency_sum:
            return [frequency_sum[sub],i]
        
        frequency_sum[nums[i]]=i

    return frequency_sum

nums = [2,7,11,15]
target = 9
        

print(twoSum(nums,target))

