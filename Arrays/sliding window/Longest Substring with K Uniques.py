#Longest Substring with K Uniques

# def longestSubstring(s,k):
#     count_hashset = set()
#     char = []
#     left = 0
#     first_char = s[left]
#     longest_len = 0

#     for right in range(len(s)):
#         count_hashset.add(s[right])
#         char.append(s[right])
#         longest_len = max(longest_len,right-left+1)
#         while len(count_hashset) > k and first_char in char:
#             char.pop(left)
#             left+=1
            
#         first_char=s[left]
#     if longest_len != 0:
#         return longest_len
#     return len(char)




def longestSubstring(s,k):
    freq = {}
    left = 0
    longest_len = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+1
        while len(freq) > k:
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                del freq[s[left]]
            left+=1
        
        longest_len = max(longest_len,right-left+1)

    return longest_len
s =  "aabacbebebe"
k = 3
print(longestSubstring(s,k))


