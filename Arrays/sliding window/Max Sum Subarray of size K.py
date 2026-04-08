#Max Sum Subarray of size K
def maxSum(nums,k):
    max_sum = sum(nums[:k])
    total = 0
    for i in range(k,len(nums)):
        total =(max_sum - nums[i-k]) + nums[i]
        max_sum = max(max_sum,total)
        
        
    return max_sum


nums =  [100, 200, 300, 400]
k = 1
print(maxSum(nums,k))