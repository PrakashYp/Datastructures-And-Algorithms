def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    low = 0
    high = x - 1 
    if x == 0 or x == 1:
        return x
    elif x == 2:
        return 1
    else:


        while low<=high:
            mid = low + (high - low) // 2
            value = mid * mid
            low_value = low * low
            high_value = high * high

            if value == x:
                return mid
            elif low_value > x < high_value:
                return low - 1

            elif value >= x:
                high = mid
            else:
                low = mid + 1



print(mySqrt(8))


