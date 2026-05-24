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

        # no_delete_sum = max(prev_no_delete+arr[i],arr[i])
        # one_delete_sum = max(prev_one_delete,prev_no_delete+arr[i])

#         ans = max(ans, no_del, one_del)


#     return ans


# arr = [1,-2,0,3]

# print(maximumSum(arr))



def maximumSum(arr):
    one_delete_sum = 0
    total_delete_sum = arr[0]
    ans = arr[0]
    for i in range(1,len(arr)):
        prev_total_delete_sum = total_delete_sum
        prev_one_delete_sum = one_delete_sum

        total_delete_sum = max(arr[i],prev_total_delete_sum+arr[i])
        one_delete_sum = max(prev_one_delete_sum+arr[i],prev_total_delete_sum)

        ans = max(one_delete_sum,total_delete_sum,ans)
    return ans


    


arr = [-1,-1,-1,-1]
print(maximumSum(arr))




























