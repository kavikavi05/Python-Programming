class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            
            for length in range(1, 4):
                if start + length > len(s): 
                    break
                
                segment = s[start:start + length]
                
                if (segment[0] == "0" and len(segment) > 1) or int(segment) > 255:
                    continue
                
                backtrack(start + length, path + [segment])
        
        result = []
        backtrack(0, [])
        return result
