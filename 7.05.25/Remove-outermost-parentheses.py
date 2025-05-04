class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        queue = []
        i = 0
        final = []
        answer = []

        while i <= len(s)-1:
            if (s[i] == '(') and len(queue) == 0:
                queue.append(s[i])
            elif len(queue) > 0 and (s[i] == '('):
                final.append(s[i])
                queue.append(s[i])
            elif (s[i] == ')'):
                queue.pop()
                if len(queue) > 0:
                    final.append(s[i])


                

            i = i+1            

        return "".join(final)        
