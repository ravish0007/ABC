def isPalindrome(s):
    import string
    S = ''.join(i.lower() for i in s if i in string.ascii_letters + string.digits)
    
    i, j = 0, len(S) - 1
    
    while i < j:
        if S[i] != S[j]:
            return False
        i += 1
        j -= 1
    return True
