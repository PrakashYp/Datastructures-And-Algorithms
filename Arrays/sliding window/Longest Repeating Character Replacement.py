#Longest Repeating Character Replacement


def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

    freq = {}
    left = 0
    longest_len = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                del freq[s[left]]
            left+=1
        longest_len = max(longest_len,right-left+1)

    return longest_len



freq = {'A':2,'B':4,'C':2}


s = "aabacbebebe"
k = 3
print(characterReplacement(s,k))


        



