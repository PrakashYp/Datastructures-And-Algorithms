#Find All Anagrams in a String

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    left = 0
    p_len=len(p)
    required_hashmap = {}
    current_hashmap = {}
    indexs = []
    for i in range(len(p)):
        required_hashmap[p[i]] = required_hashmap.get(p[i],0)+1
    print(required_hashmap)

    for right in range(len(s)):
        current_hashmap[s[right]] = current_hashmap.get(s[right],0)+1
        print(current_hashmap)
        
        if current_hashmap == required_hashmap:
            indexs.append(left)
        if right-left +1 == p_len:
            
            current_hashmap[s[left]] -= 1
        
            if current_hashmap[s[left]] == 0:
                del current_hashmap[s[left]]
            left+=1
            
           
            

    return indexs

s =  "abab"
p = "ab"

print(findAnagrams(s,p))


