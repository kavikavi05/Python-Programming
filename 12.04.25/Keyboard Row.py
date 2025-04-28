class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")
        res = []
        for i in words:
            lword = set(i.lower())  # set string to lower case
# if a word is made from a particular row then it'll be a subset of that row fs.
            if lword.issubset(r1) or lword.issubset(r2) or lword.issubset(r3):
                res.append(i)
        return res
