class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        w = set(wordList)

        if beginWord != endWord and endWord not in w:
            return 0
        
        q = deque()
        q.append((beginWord, 1))
        l = list(set("".join(wordList)))
        v = {beginWord}

        len_g = len(beginWord)

        while q:
            g, n = q.popleft()


            if g == endWord:
                return n

            for i in range(len_g):
                for c in l:
                    if g[i] != c:
                        m = g[:i]+c+g[i+1:]
                        if m in w and m not in v:
                            q.append((m, n+1))
                            v.add(m)
        
        return 0
