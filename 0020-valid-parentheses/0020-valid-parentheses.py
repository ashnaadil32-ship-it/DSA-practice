class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
               ')': '(',
               ']': '[',
               '}': '{'
               }
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
               stack.append(ch)
            else:
               if stack == []:
                  return False
               else:   
                  last = stack.pop()    
                  if last != pair[ch]:
                     return False

        return len(stack) == 0


                     