def maxDistance(position, m):
    """
    :type position: List[int]
    :type m: int
    :rtype: int
    """


    pass



def gives_minimum(mid):
    positions = [1,2,3,4,7]
    m = 3
    count= 1
    minimum_count = positions[0]

    for position in positions:
        if count == m:
            minimum_count =   min((minimum_count - position),minimum_count)

        count += 1

    
    return abs(minimum_count - 1)

print(gives_minimum(3))




