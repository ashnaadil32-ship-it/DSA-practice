class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append("")
            
            elif ch == ')':
                temp = stack.pop()[::-1]

                if stack:
                    stack[-1] += temp
                else:
                    stack.append(temp)
            
            else:
                if stack:
                    stack[-1] += ch
                else:
                    stack.append(ch)

        return stack[0]