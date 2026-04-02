# Check if a string is palindrome or not.

s = "abba"

def check_palindrom(string):
    right=len(string)-1
    for i in range(len(string)):
        if string[i] != string[right]:
            return False

        right-=1

    return True


print(check_palindrom(s))




