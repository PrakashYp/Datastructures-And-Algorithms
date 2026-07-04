def findInMountainArray(target, mountainArr):
    """
    :type target: integer
    :type mountain_arr: MountainArray
    :rtype: integer
    """

    def find_peak(mountainArr):
        low = 0 
        high = len(mountainArr) - 1

        while low < high:
            mid = low + (high-low) // 2

            if mountainArr[mid]<mountainArr[mid + 1]:
                low = mid + 1 
            else :
                high = mid - 1
        return low
    
    def left_occurence(target,mountainArr,peak):
        low = 0
        high = peak

        while low <= high:
            mid = low + (high - low) // 2
            if mountainArr[mid] == target:
                return mid
            elif mountainArr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def right_occurence(target,mountainArr,peak):
        low = peak + 1
        high = len(mountainArr) - 1
        while low <= high:
            mid = low +(high - low)//2
            if mountainArr[mid] == target:
                return mid
            elif mountainArr[mid] < target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1 
    
    peak = find_peak(mountainArr)

    ans = left_occurence(target,mountainArr,peak)
    if ans != -1:
        return ans
    return right_occurence(target,mountainArr,peak)



print(findInMountainArray(3,[1,2,3,4,5,3,1]))
            



