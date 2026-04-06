def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ''
    right = len(height)-1
    left=0
    max_water = 0
    while left<right:
        width = right - left
        if height[left] <= height[right]:
            max_water = max(max_water,width*height[left])
            left+=1
        else:
            max_water = max(max_water,width*height[right])
            right-=1
            
        
    return max_water
        

height = [1,8,6,2,5,4,8,3,7]


print(maxArea(height))