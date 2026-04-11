def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """
    fruit_basket = {}
    max_fruits = 0
    left = 0 

    for right in range(len(fruits)):
        fruit_basket[fruits[right]]=fruit_basket.get(fruits[right],0)+1

        while len(fruit_basket)>2:
            fruit_basket[fruits[left]] -= 1            
            if fruit_basket[fruits[left]] == 0:
                del fruit_basket[fruits[left]]
               
            left+=1

        print(fruit_basket)
        max_fruits = max(max_fruits,right-left+1)

    return max_fruits


fruits =  [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruit(fruits))







