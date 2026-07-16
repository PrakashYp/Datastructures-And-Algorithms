def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def can_split(max_sum):

    
        subarrays = 1
        remaining = max_sum
        for num in nums:
            if remaining < num:
                subarrays += 1
                remaining = max_sum
            remaining -= num        
        if subarrays > k:
            return False

        return True
    
    low = max(nums)
    high = sum(nums)

    while low <= high:
        mid = low + (high - low) // 2

        if can_split(mid):
            high = mid - 1
        else:
            low = mid + 1
    
    return low




nums = [7,2,5,10,8]
k = 2
print(splitArray(nums,k))











