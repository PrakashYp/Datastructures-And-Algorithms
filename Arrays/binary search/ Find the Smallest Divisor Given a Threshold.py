def smallestDivisor(nums, threshold):
    """
    :type nums: List[int]
    :type threshold: int
    :rtype: int
    """
    def calculate_sum(divisor):
        total = 0 
        for num in nums:
            total += (num + divisor - 1) // divisor
        return total

    low = 1
    high = max(nums)

    while low <= high:
        divisor = low + (high - low) // 2
        if calculate_sum(divisor) > threshold:
            low = divisor + 1
        else:
            high = divisor - 1

    return low

nums =  [44,22,33,11,1]
threshold = 5

print(smallestDivisor(nums,threshold))

