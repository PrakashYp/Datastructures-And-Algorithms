def search(nums, target):
    Target_Index = -1
    low = 0 
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low ) // 2
        if nums[mid] == target:
            return mid
        elif nums[low] < target:
            low = mid + 1
        else:
            high = mid - 1

        

    return Target_Index



nums = [4,5,6,7,0,1,2]
target = 5

print(search(nums,target))


        