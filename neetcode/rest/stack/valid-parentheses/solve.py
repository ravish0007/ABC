def isValid(s):
    
    s = list(s)
    stack = []
    
    match  = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    for char in s:
        if char in'([{':
            stack.append(char)
            
        elif len(stack) == 0:
            return False
        
        elif char != match[stack.pop()]:
            return False
     
    return len(stack) == 0 
