def longestOnes(nums, k):
    left = 0
    max_ones = 0
    zero_fre = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_fre += 1
        
        while zero_fre > k:
            
            
            if nums[left] == 0:
                zero_fre -= 1
            left += 1
        max_ones = max(max_ones, right-left+1)
        

    return max_ones



nums = [1,1,1,0,0,0,1,1,1,1,0]

k = 2

print(longestOnes(nums,k))
