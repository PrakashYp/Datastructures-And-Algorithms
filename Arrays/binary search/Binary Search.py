def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums)-1

    while left<=right:
        mid = left+(right-left) // 2
        print(mid)

        if nums[mid] == target:
            return mid
        elif nums[mid]> target :
            right = mid - 1
        elif nums[mid] < target :
            left = mid + 1

    return -1 

nums = [5,7,7,8,8,10]
target = 8

print(search(nums,target))

