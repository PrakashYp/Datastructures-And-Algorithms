
def shipWithinDays(weights,days):
    def can_finish(capacity):
        weights = [1,2,3,4,5,6,7,8,9,10]
        days_count = 1
        remaining = capacity
        for package in weights:

            if package > remaining:
                remaining = capacity
                days_count += 1
            
            remaining -= package

        return days_count <= days


    low = max(weights)
    high = sum(weights)
    while low<= high:

        weight = low + (high - low) // 2

        if can_finish(weight):
            high = weight - 1
        else:
            low = weight + 1

    print(low,high)

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
shipWithinDays(weights,days)



# def can_finish(capacity,h):
#     weights = [1,2,3,4,5,6,7,8,9,10]
#     real_days =h
#     days = 1
#     remaining = capacity
#     for package in weights:

#         if package > remaining:
#             remaining = capacity
#             days += 1
        
#         remaining -= package

#     return days <= real_days







