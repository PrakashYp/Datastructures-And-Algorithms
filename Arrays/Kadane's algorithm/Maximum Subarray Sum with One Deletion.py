# def maximumSum(arr):
#     """
#     :type arr: List[int]
#     :rtype: int
#     """
#     no_del = arr[0]
#     one_del = 0
#     ans = arr[0]

#     for i in range(1, len(arr)):
#         prev_no_del = no_del
#         prev_one_del = one_del

#         no_del = max(arr[i], prev_no_del + arr[i])

#         one_del = max(prev_no_del,prev_one_del + arr[i])

#         ans = max(ans, no_del, one_del)


#     return ans


# arr = [1,-2,0,3]

# print(maximumSum(arr))



def maximumSum(arr):
    one_delete_sum = 0
    total_sum = arr[0]
    ans = 0
    for i in range(1,len(arr)):
        prev_delete_sum = total_sum
        prev_one_delete_sum = one_delete_sum
        one_delete_sum = max(prev_delete_sum,prev_one_delete_sum+arr[i])
        total_sum = max(prev_delete_sum+arr[i],arr[i])

        ans = max(one_delete_sum,ans,total_sum)




    return ans



arr = [1,-2,0,3]

print(maximumSum(arr))




























