# def minDays(bloomDay, m, k):
#     """
#     :type bloomDay: List[int]
#     :type m: int
#     :type k: int
#     :rtype: int
#     """
#     count = m*k
#     if count > len(bloomDay):
#         return -1 

#     def can_bloom(days):
#         bloom_count = 0 
#         flower = 0 
#         for day in bloomDay:
#             if (days-day) >= 0:
#                 bloom_count += 1
#             if bloom_count == k:
#                 flower += 1
#                 bloom_count = 0 
#         return flower == m



     




def can_bloom(days):
    bloomDay =[7,7,7,7,12,7,7] 
    m = 2
    k = 3 
    bloom_count = 0 
    flower = 0 
    for day in bloomDay:
        if (days-day) >= 0:
            bloom_count += 1
        if bloom_count == k:
            flower += 1
            bloom_count = 0
    print(flower)
    return flower >= m
        
 
print(can_bloom(7))