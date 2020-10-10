from stack import Stack

def bracketMatching(string):
    s = Stack()
    correctlyFormatted = True 
    index = 0
    while index < len(string) and correctlyFormatted:
        char = string[index]
        index += 1
        if char != "(" and char != ")":
            pass
        else:
            if char == "(":
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