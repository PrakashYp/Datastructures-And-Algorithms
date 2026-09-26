import math
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    low = 0 
    high = len(matrix) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            print("Entered")
            return mid
        if matrix[mid][0] >= target:
            high = mid - 1
        else:
            low = mid + 1 

  
    def check_func(nums,target):
        low = 0
        high = len(nums) - 1
        if nums[low]<=target<=nums[high]:
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] > target:
                    high = mid - 1 
                else :
                    low = mid + 1


        return False

        
# print(check_func([1,3,5,7],2))

matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]
         ]



print(math.ceil(1/7))
print(math.ceil(2/7))
print(math.ceil(3/7))
print(math.ceil(9/7))
