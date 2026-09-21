
# def shipWithinDays(weights,days):
#     def can_finish(capacity):
#         ship_capacity = capacity 
#         day = 0
#         for package in weights:
#             if ship_capacity< package:
#                 day+= 1
#                 ship_capacity = capacity
#             ship_capacity -= package

#         return day <= days

#     left = 1
#     right = sum(weights)

#     while left<= right:
#         capacity = left +(right - left) // 2
#         if can_finish(capacity):
#             right = capacity - 1
#         else:
#             left = capacity + 1

#     return left







def can_finish(capacity,days):
    weights = [1,2,3,4,5,6,7,8,9,10]
    day = 0
    ship_capacity = capacity
    for package in weights:

        if ship_capacity < package:
            day+= 1
            ship_capacity = capacity

        ship_capacity -= package

    return day<= days


print(can_finish(10,5))




