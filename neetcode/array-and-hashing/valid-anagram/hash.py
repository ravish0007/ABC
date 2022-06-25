def isAnagram(s, t):
        
    if len(s) != len(t):
        return False

    store = {}

    for char in s:
        store[char] =  store.get(char, 0) + 1

    for char in t:
        if char not in store:
            return False
        store[char] -= 1

    return sum(store.values()) == 0
            
