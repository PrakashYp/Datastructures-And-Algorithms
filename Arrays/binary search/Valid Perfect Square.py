def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    left = 1
    right = num-1

    while left<=right:
        mid = left + (right-left) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
            
    return False
        



print(isPerfectSquare(168))