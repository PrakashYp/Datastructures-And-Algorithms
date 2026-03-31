def hasDuplicate(nums):
    seen = set()
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
        else:
            return True
    return False


nums = [1, 2, 3, 4]

print(hasDuplicate(nums))


