def maxDistance(position, m):
    """
    :type position: List[int]
    :type m: int
    :rtype: int
    """
        
    position.sort()
    def gives_minimum(mid):

        balls_placed = 1
        last_placed_ball = position[0]

        for basket in position[1:]:
            if basket - last_placed_ball >= mid:
                balls_placed += 1 
                last_placed_ball =basket
                
        return balls_placed >= m

    low = 1
    high = max(position)

    while low <= high:
        mid = low +(high - low) // 2

        if gives_minimum(mid):
            low = mid + 1 
        else:
            high = mid -1 


    return low - 1



