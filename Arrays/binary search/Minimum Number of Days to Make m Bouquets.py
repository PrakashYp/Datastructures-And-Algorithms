def minDays(bloomDay, m, k):
    """
    :type bloomDay: List[int]
    :type m: int
    :type k: int
    :rtype: int
    """
    count = m * k
    if count > len(bloomDay):
        return -1
    def can_finish(day):

        consecutives = 0
        bouquets = 0

        for flower in bloomDay:

            if flower <= day:
                consecutives += 1
                if consecutives == k:
                    bouquets += 1
                    consecutives = 0
            else:
                consecutives = 0


        return bouquets >= m

    low = min(bloomDay)
    high = max(bloomDay)

    while low <= high:
        day = low + (high-low) // 2
        if can_finish(day):
            high = day - 1
        else:
            low = day + 1


    return low 





        
bloomDay =[1,10,3,10,2]    
m = 3
k = 1   
print(minDays(bloomDay,m,k))