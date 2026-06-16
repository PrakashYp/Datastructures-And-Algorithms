def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    low = 1
    high = num-1

    while low<=high:
        mid = low + (high-low) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            low = mid + 1
        else:
            high = mid - 1
            
    return False
        



print(isPerfectSquare(168))