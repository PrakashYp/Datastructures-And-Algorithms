#Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s):
        unique_char = set()
        left=0
        max_len = 0
        for right in range(len(s)):
            while s[right] in unique_char:
                    unique_char.remove(s[left])
                    left+=1
                    
            unique_char.add(s[right])
            max_len = max(max_len,right-left+1)
            print(unique_char)
        return max_len


s = "abcabcbb"

print(lengthOfLongestSubstring(s))
