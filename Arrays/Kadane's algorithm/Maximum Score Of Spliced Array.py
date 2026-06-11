def maximumsSplicedArray(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    total_nums1 = sum(nums1)
    total_nums2 = sum(nums2)
    def kadane(nums):
        total_max = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i]+current_sum,nums[i])
            total_max = max(current_sum,total_max)

        return total_max
    

    gain_nums1 = []
    gain_nums2 = []
    for i in range(len(nums1)):
        gain_nums1.append(nums2[i]-nums1[i])
        gain_nums2.append(nums1[i]-nums2[i])

    max_nums1 = kadane(gain_nums1)+total_nums1 
    max_nums2 = kadane(gain_nums2)+total_nums2

    return max(max_nums1,max_nums2)
    
    print(gain_nums1)
    print(gain_nums2)
    









# def kadane(nums):
#     total_max = nums[0]
#     current_sum = nums[0]
#     for i in range(1,len(nums)):
#         current_sum = max(nums[i]+current_sum,nums[i])
#         total_max = max(current_sum,total_max)

#     return total_max





nums1 =  [20,40,20,70,30]
nums2 = [50,20,50,40,20]

print(maximumsSplicedArray(nums1,nums2))
