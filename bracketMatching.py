from stack import Stack

def bracketMatching(string):
    s = Stack()
    correctlyFormatted = True 
    index = 0
    
    # parse the brackets string
    while index < len(string) and correctlyFormatted:
        char = string[index]
        index += 1
        
        # check if the character matches any of the brackets
        if char not in "({[" and char not in "]})":
            pass
        else:
            if char in "({[":
                s.push(char)
            else:
                if s.isEmpty():
                    correctlyFormatted = False 
                else:
                    s.pop()
    
    if correctlyFormatted and s.isEmpty():
        return True
    else:
        return False
