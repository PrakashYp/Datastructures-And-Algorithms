# def rearrangeArray(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """

#     positive_sign=0
#     for i in range(len(nums)):
#         if nums[i]<0:
#             positive_sign+=1
#             swap = nums[positive_sign]
#             nums[positive_sign]=nums[i]
#             nums[i]=swap
#             positive_sign+=1
    
#     return nums


# def rearrangeArray(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     ans_list = [0] * len(nums)

#     pos = 0
#     neg = 1

#     for i in range(len(nums)):
#         if nums[i]>0:
#             ans_list[pos] = nums[i]
#             pos+=2
#         else:    
#             ans_list[neg] = nums[i]
#             neg+=2

#     return ans_list


def rearrangeArray(nums):
    pos = 0
    neg = 1
    ans_list=[0]*len(nums)
    for num in nums:
        if num>0:
            ans_list[pos]=num
            pos+=2
        else:
            ans_list[neg]=num
            neg+=2

    return ans_list








nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
print(rearrangeArray(nums))

