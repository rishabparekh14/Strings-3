#Time Complexity :- O(n)
#Space Complexity :- O(n)

class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        num = 0
        lastSign = '+'
        stack = []
        calc = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + (ord(s[i])- ord('0'))
            if (s[i].isdigit() is not True and s[i]!=' ') or i == len(s)-1:
                if lastSign == '+':
                    stack.append(num)
                elif lastSign == '-':
                    stack.append(-num)
                elif lastSign == '*':
                    calc = stack.pop() * num
                    stack.append(calc)
                elif lastSign == '/':
                    curr = stack.pop()
                    if curr < 0:
                        calc = int(curr/ num)
                    else:
                        calc = curr// num
                    stack.append(calc)
                calc = 0
                num = 0
                lastSign = s[i]
        
        for i in range(len(stack)):
            calc += stack[i]
        return calc


        
#ANother Appraoch more optimised :
#Time Complexity :- O(n)
#Space Complexity :- O(1)

class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        num, calc, tail = 0, 0, 0
        lastSign = '+'
        for i in range(len(s)):        
            if s[i].isdigit():
                num = num * 10 + (ord(s[i]) - ord('0'))
            if (s[i].isdigit() is not True and s[i]!=' ') or i == len(s)-1:
                if lastSign == '+':
                    calc = calc + num
                    tail = +num
                elif lastSign == '-':
                    calc = calc - num
                    tail = -num
                elif lastSign == '*':
                    calc = calc - tail + (tail * num)
                    tail = tail * num
                elif lastSign == '/':
                    if tail < 0:
                        calc = calc - tail + (int(tail / num))
                        tail = int(tail / num)
                    else:
                        calc = calc - tail + (tail // num)
                        tail = tail // num
                    
                num = 0
                lastSign = s[i]
        return calc


        