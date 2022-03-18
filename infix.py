def infix_to_postfix(expression): 
    ops     = set(['+', '-', '*', '/', '(', ')', '^']) 
    pri     = {'+':1, '-':1, '*':2, '/':2, '^':3}  
    stack   = []; ans     = "";
    for ch in expression:
        if ch not in ops: ans+= ch
        elif ch=='(': stack.append('(')
        elif ch==')':
            while stack and stack[-1]!= '(': ans+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and pri[ch]<=pri[stack[-1]]: ans+=stack.pop()
            stack.append(ch)
    while stack: ans+=stack.pop()
    return ans
    
expression = input()
print(infix_to_postfix(expression))