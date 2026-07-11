def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """

    def can_finish(speed):
        hours = 0 
        
        for pile in piles:
            hours += pile // speed

            if pile % speed != 0:
                hours += 1
            
        return hours <= h
    
    low = 1
    high = max(piles)

    while low <= high:
        speed = low + (high - low) // 2

        if can_finish(speed):
            high = speed - 1
        else:
            low = speed + 1
    return low


piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles,h))




    



