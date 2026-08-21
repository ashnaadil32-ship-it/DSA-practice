class Solution:
    def decodeString(self, s: str) -> str:
        num = []
        string = []

        currnum = 0
        currstring = ""

        for ch in s:

            
            if ch.isdigit():
                currnum = currnum * 10 + int(ch)

            
            elif ch == '[':
                num.append(currnum)
                string.append(currstring)

                currnum = 0
                currstring = ""

            
            elif ch == ']':
                repeat = num.pop()
                prevstr = string.pop()

                currstring = prevstr + repeat * currstring

            
            else:
                currstring += ch

        return currstring