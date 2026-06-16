def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def left_occurence(nums,target):
        left = 0 
        right = len(nums) - 1
        ans = -1

        while left<= right:
            mid = left+(right-left) // 2

            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    





    def right_occurence(nums,target):
        left = 0 
        right = len(nums) - 1
        ans = -1

        while left<= right:
            mid = left+(right-left) // 2

            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    

    left = left_occurence(nums,target)
    right = right_occurence(nums,target)

    return right - left + 1



nums = [1, 1, 2, 2, 2, 2, 3]
target = 2
        
print(searchRange(nums,target))

